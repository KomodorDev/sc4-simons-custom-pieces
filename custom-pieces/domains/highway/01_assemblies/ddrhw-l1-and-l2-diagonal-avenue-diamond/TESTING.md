---
title: "Testing: DD RHW-4 \u2014 Compact Diagonal Avenue Diamond"
summary: "Inspect this assembly\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Compact Diagonal Avenue Diamond

<!-- ASSEMBLY TESTING LAYOUT: 1 -->

[Assembly overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This assembly contains two opposing elevated highway decks, two avenue directions, four ramps, and two at-grade ramp junctions. Inspect the [placement guide](README.md). Saved-resource checks concern encoded traffic paths, actual indexed model triangles, exclusive construction-tile ownership, proper rotations, and menu resources. Human game observations are separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Human game checks use only 0° CCW; supported construction states and software rotation checks remain separate.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `external-1` | road / 1 / primary | out | [-8.0, -115.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `external-2` | road / 1 / primary | in | [-8.0, -115.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `external-3` | road / 1 / primary | out | [-8.0, -108.8, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `external-4` | road / 1 / primary | in | [-8.0, -108.8, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `external-5` | road / 1 / primary | in | [8.0, -19.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `external-6` | road / 1 / primary | in | [8.0, -12.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `external-7` | road / 1 / primary | out | [12.8, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `external-8` | road / 1 / primary | in | [18.237287, -56.0, 3.985684]; [-0.050695312326797345, -0.9987141659694672]; 0.338519187 | `path-interface-6eb8fd83ff52449caa68` |
| `external-9` | road / 1 / primary | out | [18.237287, -56.0, 3.985684]; [-0.05054654119578982, -0.998721706569524]; 0.338466957 | `path-interface-e962113498b0059e6dc4` |
| `external-10` | road / 1 / primary | out | [19.2, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `external-11` | road / 1 / primary | in | [56.0, -86.601434, 1.817631]; [0.8334622813545903, 0.5525763526963506]; -0.386266857 | `path-interface-95072b0547417ef03720` |
| `external-12` | road / 1 / primary | out | [56.0, -86.601434, 1.817631]; [0.8334517358574574, 0.5525922583570921]; -0.386288559 | `path-interface-05773366e00caa251eba` |
| `external-13` | road / 1 / primary | in | [56.0, -18.237287, 3.985684]; [-0.998721706569524, -0.05054654119578982]; -0.338466957 | `path-interface-3f53148c09905eadd6a6` |
| `external-14` | road / 1 / primary | out | [56.0, -18.237287, 3.985684]; [-0.9987141659694672, -0.050695312326797345]; -0.338519187 | `path-interface-33a5949b637b213eb160` |
| `external-15` | road / 1 / primary | in | [86.601434, -56.0, 1.817631]; [0.5525922583570921, 0.8334517358574574]; 0.386288559 | `path-interface-ddaedacaddd065c037d8` |
| `external-16` | road / 1 / primary | out | [86.601434, -56.0, 1.817631]; [0.5525763526963506, 0.8334622813545903]; 0.386266857 | `path-interface-5015313eb0038d7c0221` |
| `external-17` | road / 1 / primary | out | [88.0, -99.2, 0.0]; [0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `external-18` | road / 1 / primary | out | [88.0, -92.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `external-19` | road / 1 / primary | in | [92.8, -88.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `external-20` | road / 1 / primary | in | [99.2, -88.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `external-21` | road / 1 / primary | in | [108.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `external-22` | road / 1 / primary | out | [108.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `external-23` | road / 1 / primary | in | [115.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `external-24` | road / 1 / primary | out | [115.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `external-25` | pedestrian / 2 / primary | in | [8.0, -23.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `external-26` | pedestrian / 2 / primary | out | [23.3, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `external-27` | pedestrian / 2 / primary | out | [88.0, -103.3, 0.0]; [0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `external-28` | pedestrian / 2 / primary | in | [103.3, -88.0, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `external-11` → `external-10` | primary |
| road | `external-11` → `external-17` | primary |
| road | `external-11` → `external-9` | primary |
| road | `external-13` → `external-10` | primary |
| road | `external-13` → `external-16` | primary |
| road | `external-13` → `external-17` | primary |
| road | `external-15` → `external-24` | primary |
| road | `external-19` → `external-7` | primary |
| road | `external-20` → `external-10` | primary |
| road | `external-20` → `external-16` | primary |
| road | `external-20` → `external-9` | primary |
| road | `external-21` → `external-14` | primary |
| road | `external-21` → `external-3` | primary |
| road | `external-23` → `external-1` | primary |
| pedestrian | `external-25` → `external-27` | primary |
| pedestrian | `external-28` → `external-26` | primary |
| road | `external-2` → `external-12` | primary |
| road | `external-2` → `external-24` | primary |
| road | `external-4` → `external-22` | primary |
| road | `external-5` → `external-16` | primary |
| road | `external-5` → `external-17` | primary |
| road | `external-5` → `external-9` | primary |
| road | `external-6` → `external-18` | primary |
| road | `external-8` → `external-3` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `external-2` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-2` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-4` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-5` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-6` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-8` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-11` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-13` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-15` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-19` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-20` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-21` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| road / `external-23` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-25` | pedestrian / `external-26` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-1` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-3` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-7` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-9` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-10` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-12` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-14` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-16` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-17` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-18` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-22` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | road / `external-24` | not reachable in the saved placed encoded-route graph |
| pedestrian / `external-28` | pedestrian / `external-27` | not reachable in the saved placed encoded-route graph |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact native NAM 50 right-hand-traffic archives recorded in `config/profiles/nam50-rhd.jsonc`. Prepare Python with the [repository setup guide](../../../../docs/BUILD_AND_INSTALL.md#31-python-setup-for-a-checkout-or-source-zip). Build into `custom-pieces/dist/`; keep personal Plugins settings under ignored `custom-pieces/local/`. For a later human game test, use a disposable flat city and install through the [shared installation guide](../../../../docs/BUILD_AND_INSTALL.md). This work has not installed the candidate.

## 3. Software checks

Run the following commands from the repository root. Building reads your own supported native inputs and creates game archives (DAT files). Verification reopens their saved resources. The menu command creates a separate candidate with one component-cycle button.

```sh
python3 -B custom-pieces/scp.py build --set ddrhw-compact-diagonal-diamond --output custom-pieces/dist/ddrhw-compact-diagonal-diamond
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-compact-diagonal-diamond
python3 -B custom-pieces/domains/highway/tools/verify_compact_assembly.py --build custom-pieces/dist/ddrhw-compact-diagonal-diamond --output custom-pieces/local/highway-assembly-check.json
python3 -B custom-pieces/scp.py assembly-menu --source custom-pieces/dist/ddrhw-compact-diagonal-diamond --output custom-pieces/dist/ddrhw-compact-diagonal-diamond-menu --domain highway --layout compact-diagonal-diamond
python3 -B custom-pieces/scp.py docs-check --assembly ddrhw-l1-and-l2-diagonal-avenue-diamond
python3 -B tools/run_tests.py
```

To regenerate the six actual-model assembly views into a review folder, run `python3 -B custom-pieces/domains/highway/tools/render_compact_assembly.py --build custom-pieces/dist/ddrhw-compact-diagonal-diamond --output-dir custom-pieces/local/highway-assembly-views`. It uses the private Plugins setting for native textures. Review the staged images before promoting their unchanged bytes into `previews/`; preserve [the original schematic render evidence](evidence/render.json).

The independent pavement verifier reads saved PATH segments and indexed S3D triangles. It checks continuous pavement support, encoded slopes, declared empty shoulder cells, authored atlas pixels, and intersections with a 2.5 m-wide, 3.8 m-high car corridor through all four rotations. This is a triangle-face test, rather than a complete solid or swept-vehicle proof. The earlier [schematic source](design.jsonc), [geometry check](evidence/geometry-check.json), and [schematic render report](evidence/render.json) retain their original source-only scope.

## 4. Game checks

No game observations have been supplied. In a disposable city, place every component in each supported rotation, then supply real traffic demand on all four arms. Observe every generated journey separately with Route Query and visible vehicles. Check pedestrians through both surface junctions, vehicles on the steep grades, barrier openings, stopping and junction conflicts, shadows, demolition, replacement, and save/reload. Record exact observations through the [shared testing procedure](../../../../docs/TESTING.md); software checks cannot tick those cases.

## 5. Results and known issues

The final normal build passes its saved-resource checks for 574 resources in 15 DAT files. The [independent assembly check](evidence/compiled-assembly-check.json) verifies 17 placements, 41 construction tiles, 162 saved PATH fragments, 158 directed lane seams, 20 native external lane and pedestrian channels, and all twelve required arm movements. Eight are transfers between the highway and avenue, and four are through movements. The saved path’s maximum grades are approximately 33.8474% lower and 38.6269% upper.

The [pier contact proof](evidence/pier-contact-proof.json) verifies six 0.8 m-square columns, 48 pavement-plane corner contacts, and 14,232 segment-to-column checks, with a minimum conservative car-corridor clearance of approximately 1.578 m. The assembly’s pavement seams have 360 collar samples; their maximum sampled height difference is approximately 1.641 mm. These results describe the exact saved candidate and do not establish structural engineering or human game operation. The [compiled validation record](evidence/compiled-validation.json) preserves the exact test history: the portable matrix ran 1,428 tests with 81 explicit skips. One documentation-link failure was corrected, then all 20 CLI tests and all 26 installer bundle tests passed, and the portable documentation check passed. Of the skips, 69 lack private or audited native inputs, and twelve lack protected or historical saved-build captures. The current highway candidate was separately compiled and checked against the actual pinned native archives.

The thirteen modules have current intrinsic traffic records; full physical connector cards for graded modules remain unsupported pending review. The standalone native crossing has six checked boundary cards.

The 40% slope limit is an experimental authoring bound chosen for the requested compact footprint. Traffic-signal timing, vehicle animation on steep grades, terrain behaviour and actual game operation remain unverified. Six authored concrete pier surfaces meet the pavement planes outside the measured car corridors; no structural engineering claim follows from these visual model contacts. Surface turns have intentional conflicts and require game inspection. Native model overhangs are retained. Building, installing, publishing, and human observations are separate actions.

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Human game checks are required only at 0° CCW. Supported construction orientations and software rotation checks retain their separate scope; these human cases do not establish observations at the other orientations.

Current totals: unverified: 236, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/checks/manual-tests.json --observation custom-pieces/domains/highway/01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-0184d6b917d00cb763b7">[ ] unverified</a> | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-0184d6b917d00cb763b7"></a>

**General: unverified** — `software_resources-0184d6b917d00cb763b7`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-0184d6b917d00cb763b7">[ ] unverified</a> | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-0184d6b917d00cb763b7"></a>

**General: unverified** — `software_connectivity-0184d6b917d00cb763b7`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-d3cfcd278fba6b54f7d5">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-d3cfcd278fba6b54f7d5"></a>

**0° CCW: unverified** — `in_game_render-d3cfcd278fba6b54f7d5`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-d3cfcd278fba6b54f7d5">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-d3cfcd278fba6b54f7d5"></a>

**0° CCW: unverified** — `in_game_placement-d3cfcd278fba6b54f7d5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-d3cfcd278fba6b54f7d5">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-d3cfcd278fba6b54f7d5"></a>

**0° CCW: unverified** — `in_game_demolition-d3cfcd278fba6b54f7d5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-d3cfcd278fba6b54f7d5">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-d3cfcd278fba6b54f7d5"></a>

**0° CCW: unverified** — `in_game_save_reload-d3cfcd278fba6b54f7d5`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 22 cases; unverified: 22</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: external-11>external-10; entry: external-11; exit: external-10 | — | <a href="#case-in_game_route_query-9296729bebf2c3f3fb46">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-11>external-17; entry: external-11; exit: external-17 | — | <a href="#case-in_game_route_query-257d9e5bdc50e2e7b9c5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-11>external-9; entry: external-11; exit: external-9 | — | <a href="#case-in_game_route_query-932bc7280c32821b5dab">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-10; entry: external-13; exit: external-10 | — | <a href="#case-in_game_route_query-ee2ed307014e8f7e0e79">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-16; entry: external-13; exit: external-16 | — | <a href="#case-in_game_route_query-e3e49a033f129337e669">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-13>external-17; entry: external-13; exit: external-17 | — | <a href="#case-in_game_route_query-76b417b84fb3a7a4a9d9">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-15>external-24; entry: external-15; exit: external-24 | — | <a href="#case-in_game_route_query-70ed31100bcf26b733f4">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-19>external-7; entry: external-19; exit: external-7 | — | <a href="#case-in_game_route_query-3cab14d2e6b444135d65">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-20>external-10; entry: external-20; exit: external-10 | — | <a href="#case-in_game_route_query-fc8c478f194311e35bcb">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-20>external-16; entry: external-20; exit: external-16 | — | <a href="#case-in_game_route_query-d3aab79642082859df76">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-20>external-9; entry: external-20; exit: external-9 | — | <a href="#case-in_game_route_query-fea5efcd066b8ed5c834">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-21>external-14; entry: external-21; exit: external-14 | — | <a href="#case-in_game_route_query-f22cb77727203659750e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-21>external-3; entry: external-21; exit: external-3 | — | <a href="#case-in_game_route_query-1162ff08e9e1357957d7">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-23>external-1; entry: external-23; exit: external-1 | — | <a href="#case-in_game_route_query-bd8eadad195c0b827ec0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-12; entry: external-2; exit: external-12 | — | <a href="#case-in_game_route_query-974cf8e01db8405eb52e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-2>external-24; entry: external-2; exit: external-24 | — | <a href="#case-in_game_route_query-28c8b93fac96cdf0b66e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-4>external-22; entry: external-4; exit: external-22 | — | <a href="#case-in_game_route_query-1df3119d36e204c67cf5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-16; entry: external-5; exit: external-16 | — | <a href="#case-in_game_route_query-1cdad7ff3e37487006bf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-17; entry: external-5; exit: external-17 | — | <a href="#case-in_game_route_query-dfd1c70413139ed686d0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9 | — | <a href="#case-in_game_route_query-0301aed91499dadd0fc9">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-6>external-18; entry: external-6; exit: external-18 | — | <a href="#case-in_game_route_query-df262dcc800ee048eb60">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: external-8>external-3; entry: external-8; exit: external-3 | — | <a href="#case-in_game_route_query-a2a9348540dac7ed1b06">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: external-11>external-10; entry: external-11; exit: external-10</summary>

<a id="case-in_game_route_query-9296729bebf2c3f3fb46"></a>

**0° CCW: unverified** — `in_game_route_query-9296729bebf2c3f3fb46`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-11>external-10; entry: external-11; exit: external-10.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-11>external-17; entry: external-11; exit: external-17</summary>

<a id="case-in_game_route_query-257d9e5bdc50e2e7b9c5"></a>

**0° CCW: unverified** — `in_game_route_query-257d9e5bdc50e2e7b9c5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-11>external-17; entry: external-11; exit: external-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-11>external-9; entry: external-11; exit: external-9</summary>

<a id="case-in_game_route_query-932bc7280c32821b5dab"></a>

**0° CCW: unverified** — `in_game_route_query-932bc7280c32821b5dab`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-11>external-9; entry: external-11; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-10; entry: external-13; exit: external-10</summary>

<a id="case-in_game_route_query-ee2ed307014e8f7e0e79"></a>

**0° CCW: unverified** — `in_game_route_query-ee2ed307014e8f7e0e79`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-10; entry: external-13; exit: external-10.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-16; entry: external-13; exit: external-16</summary>

<a id="case-in_game_route_query-e3e49a033f129337e669"></a>

**0° CCW: unverified** — `in_game_route_query-e3e49a033f129337e669`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-16; entry: external-13; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-13>external-17; entry: external-13; exit: external-17</summary>

<a id="case-in_game_route_query-76b417b84fb3a7a4a9d9"></a>

**0° CCW: unverified** — `in_game_route_query-76b417b84fb3a7a4a9d9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-13>external-17; entry: external-13; exit: external-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-15>external-24; entry: external-15; exit: external-24</summary>

<a id="case-in_game_route_query-70ed31100bcf26b733f4"></a>

**0° CCW: unverified** — `in_game_route_query-70ed31100bcf26b733f4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-15>external-24; entry: external-15; exit: external-24.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-19>external-7; entry: external-19; exit: external-7</summary>

<a id="case-in_game_route_query-3cab14d2e6b444135d65"></a>

**0° CCW: unverified** — `in_game_route_query-3cab14d2e6b444135d65`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-19>external-7; entry: external-19; exit: external-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-20>external-10; entry: external-20; exit: external-10</summary>

<a id="case-in_game_route_query-fc8c478f194311e35bcb"></a>

**0° CCW: unverified** — `in_game_route_query-fc8c478f194311e35bcb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-20>external-10; entry: external-20; exit: external-10.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-20>external-16; entry: external-20; exit: external-16</summary>

<a id="case-in_game_route_query-d3aab79642082859df76"></a>

**0° CCW: unverified** — `in_game_route_query-d3aab79642082859df76`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-20>external-16; entry: external-20; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-20>external-9; entry: external-20; exit: external-9</summary>

<a id="case-in_game_route_query-fea5efcd066b8ed5c834"></a>

**0° CCW: unverified** — `in_game_route_query-fea5efcd066b8ed5c834`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-20>external-9; entry: external-20; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-21>external-14; entry: external-21; exit: external-14</summary>

<a id="case-in_game_route_query-f22cb77727203659750e"></a>

**0° CCW: unverified** — `in_game_route_query-f22cb77727203659750e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-21>external-14; entry: external-21; exit: external-14.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-21>external-3; entry: external-21; exit: external-3</summary>

<a id="case-in_game_route_query-1162ff08e9e1357957d7"></a>

**0° CCW: unverified** — `in_game_route_query-1162ff08e9e1357957d7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-21>external-3; entry: external-21; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-23>external-1; entry: external-23; exit: external-1</summary>

<a id="case-in_game_route_query-bd8eadad195c0b827ec0"></a>

**0° CCW: unverified** — `in_game_route_query-bd8eadad195c0b827ec0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-23>external-1; entry: external-23; exit: external-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-12; entry: external-2; exit: external-12</summary>

<a id="case-in_game_route_query-974cf8e01db8405eb52e"></a>

**0° CCW: unverified** — `in_game_route_query-974cf8e01db8405eb52e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-12; entry: external-2; exit: external-12.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-2>external-24; entry: external-2; exit: external-24</summary>

<a id="case-in_game_route_query-28c8b93fac96cdf0b66e"></a>

**0° CCW: unverified** — `in_game_route_query-28c8b93fac96cdf0b66e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-2>external-24; entry: external-2; exit: external-24.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-4>external-22; entry: external-4; exit: external-22</summary>

<a id="case-in_game_route_query-1df3119d36e204c67cf5"></a>

**0° CCW: unverified** — `in_game_route_query-1df3119d36e204c67cf5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-4>external-22; entry: external-4; exit: external-22.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-16; entry: external-5; exit: external-16</summary>

<a id="case-in_game_route_query-1cdad7ff3e37487006bf"></a>

**0° CCW: unverified** — `in_game_route_query-1cdad7ff3e37487006bf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-16; entry: external-5; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-17; entry: external-5; exit: external-17</summary>

<a id="case-in_game_route_query-dfd1c70413139ed686d0"></a>

**0° CCW: unverified** — `in_game_route_query-dfd1c70413139ed686d0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-17; entry: external-5; exit: external-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9</summary>

<a id="case-in_game_route_query-0301aed91499dadd0fc9"></a>

**0° CCW: unverified** — `in_game_route_query-0301aed91499dadd0fc9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-6>external-18; entry: external-6; exit: external-18</summary>

<a id="case-in_game_route_query-df262dcc800ee048eb60"></a>

**0° CCW: unverified** — `in_game_route_query-df262dcc800ee048eb60`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-6>external-18; entry: external-6; exit: external-18.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: external-8>external-3; entry: external-8; exit: external-3</summary>

<a id="case-in_game_route_query-a2a9348540dac7ed1b06"></a>

**0° CCW: unverified** — `in_game_route_query-a2a9348540dac7ed1b06`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: external-8>external-3; entry: external-8; exit: external-3.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 22 cases; unverified: 22</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: external-11>external-10; entry: external-11; exit: external-10 | — | <a href="#case-in_game_visible_travel-9296729bebf2c3f3fb46">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-11>external-17; entry: external-11; exit: external-17 | — | <a href="#case-in_game_visible_travel-257d9e5bdc50e2e7b9c5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-11>external-9; entry: external-11; exit: external-9 | — | <a href="#case-in_game_visible_travel-932bc7280c32821b5dab">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-10; entry: external-13; exit: external-10 | — | <a href="#case-in_game_visible_travel-ee2ed307014e8f7e0e79">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-16; entry: external-13; exit: external-16 | — | <a href="#case-in_game_visible_travel-e3e49a033f129337e669">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-13>external-17; entry: external-13; exit: external-17 | — | <a href="#case-in_game_visible_travel-76b417b84fb3a7a4a9d9">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-15>external-24; entry: external-15; exit: external-24 | — | <a href="#case-in_game_visible_travel-70ed31100bcf26b733f4">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-19>external-7; entry: external-19; exit: external-7 | — | <a href="#case-in_game_visible_travel-3cab14d2e6b444135d65">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-20>external-10; entry: external-20; exit: external-10 | — | <a href="#case-in_game_visible_travel-fc8c478f194311e35bcb">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-20>external-16; entry: external-20; exit: external-16 | — | <a href="#case-in_game_visible_travel-d3aab79642082859df76">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-20>external-9; entry: external-20; exit: external-9 | — | <a href="#case-in_game_visible_travel-fea5efcd066b8ed5c834">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-21>external-14; entry: external-21; exit: external-14 | — | <a href="#case-in_game_visible_travel-f22cb77727203659750e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-21>external-3; entry: external-21; exit: external-3 | — | <a href="#case-in_game_visible_travel-1162ff08e9e1357957d7">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-23>external-1; entry: external-23; exit: external-1 | — | <a href="#case-in_game_visible_travel-bd8eadad195c0b827ec0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-12; entry: external-2; exit: external-12 | — | <a href="#case-in_game_visible_travel-974cf8e01db8405eb52e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-2>external-24; entry: external-2; exit: external-24 | — | <a href="#case-in_game_visible_travel-28c8b93fac96cdf0b66e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-4>external-22; entry: external-4; exit: external-22 | — | <a href="#case-in_game_visible_travel-1df3119d36e204c67cf5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-16; entry: external-5; exit: external-16 | — | <a href="#case-in_game_visible_travel-1cdad7ff3e37487006bf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-17; entry: external-5; exit: external-17 | — | <a href="#case-in_game_visible_travel-dfd1c70413139ed686d0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9 | — | <a href="#case-in_game_visible_travel-0301aed91499dadd0fc9">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-6>external-18; entry: external-6; exit: external-18 | — | <a href="#case-in_game_visible_travel-df262dcc800ee048eb60">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: external-8>external-3; entry: external-8; exit: external-3 | — | <a href="#case-in_game_visible_travel-a2a9348540dac7ed1b06">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-11>external-10; entry: external-11; exit: external-10</summary>

<a id="case-in_game_visible_travel-9296729bebf2c3f3fb46"></a>

**0° CCW: unverified** — `in_game_visible_travel-9296729bebf2c3f3fb46`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-11>external-10; entry: external-11; exit: external-10.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-11>external-17; entry: external-11; exit: external-17</summary>

<a id="case-in_game_visible_travel-257d9e5bdc50e2e7b9c5"></a>

**0° CCW: unverified** — `in_game_visible_travel-257d9e5bdc50e2e7b9c5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-11>external-17; entry: external-11; exit: external-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-11>external-9; entry: external-11; exit: external-9</summary>

<a id="case-in_game_visible_travel-932bc7280c32821b5dab"></a>

**0° CCW: unverified** — `in_game_visible_travel-932bc7280c32821b5dab`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-11>external-9; entry: external-11; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-10; entry: external-13; exit: external-10</summary>

<a id="case-in_game_visible_travel-ee2ed307014e8f7e0e79"></a>

**0° CCW: unverified** — `in_game_visible_travel-ee2ed307014e8f7e0e79`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-10; entry: external-13; exit: external-10.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-16; entry: external-13; exit: external-16</summary>

<a id="case-in_game_visible_travel-e3e49a033f129337e669"></a>

**0° CCW: unverified** — `in_game_visible_travel-e3e49a033f129337e669`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-16; entry: external-13; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-13>external-17; entry: external-13; exit: external-17</summary>

<a id="case-in_game_visible_travel-76b417b84fb3a7a4a9d9"></a>

**0° CCW: unverified** — `in_game_visible_travel-76b417b84fb3a7a4a9d9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-13>external-17; entry: external-13; exit: external-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-15>external-24; entry: external-15; exit: external-24</summary>

<a id="case-in_game_visible_travel-70ed31100bcf26b733f4"></a>

**0° CCW: unverified** — `in_game_visible_travel-70ed31100bcf26b733f4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-15>external-24; entry: external-15; exit: external-24.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-19>external-7; entry: external-19; exit: external-7</summary>

<a id="case-in_game_visible_travel-3cab14d2e6b444135d65"></a>

**0° CCW: unverified** — `in_game_visible_travel-3cab14d2e6b444135d65`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-19>external-7; entry: external-19; exit: external-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-20>external-10; entry: external-20; exit: external-10</summary>

<a id="case-in_game_visible_travel-fc8c478f194311e35bcb"></a>

**0° CCW: unverified** — `in_game_visible_travel-fc8c478f194311e35bcb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-20>external-10; entry: external-20; exit: external-10.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-20>external-16; entry: external-20; exit: external-16</summary>

<a id="case-in_game_visible_travel-d3aab79642082859df76"></a>

**0° CCW: unverified** — `in_game_visible_travel-d3aab79642082859df76`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-20>external-16; entry: external-20; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-20>external-9; entry: external-20; exit: external-9</summary>

<a id="case-in_game_visible_travel-fea5efcd066b8ed5c834"></a>

**0° CCW: unverified** — `in_game_visible_travel-fea5efcd066b8ed5c834`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-20>external-9; entry: external-20; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-21>external-14; entry: external-21; exit: external-14</summary>

<a id="case-in_game_visible_travel-f22cb77727203659750e"></a>

**0° CCW: unverified** — `in_game_visible_travel-f22cb77727203659750e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-21>external-14; entry: external-21; exit: external-14.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-21>external-3; entry: external-21; exit: external-3</summary>

<a id="case-in_game_visible_travel-1162ff08e9e1357957d7"></a>

**0° CCW: unverified** — `in_game_visible_travel-1162ff08e9e1357957d7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-21>external-3; entry: external-21; exit: external-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-23>external-1; entry: external-23; exit: external-1</summary>

<a id="case-in_game_visible_travel-bd8eadad195c0b827ec0"></a>

**0° CCW: unverified** — `in_game_visible_travel-bd8eadad195c0b827ec0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-23>external-1; entry: external-23; exit: external-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-12; entry: external-2; exit: external-12</summary>

<a id="case-in_game_visible_travel-974cf8e01db8405eb52e"></a>

**0° CCW: unverified** — `in_game_visible_travel-974cf8e01db8405eb52e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-12; entry: external-2; exit: external-12.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-2>external-24; entry: external-2; exit: external-24</summary>

<a id="case-in_game_visible_travel-28c8b93fac96cdf0b66e"></a>

**0° CCW: unverified** — `in_game_visible_travel-28c8b93fac96cdf0b66e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-2>external-24; entry: external-2; exit: external-24.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-4>external-22; entry: external-4; exit: external-22</summary>

<a id="case-in_game_visible_travel-1df3119d36e204c67cf5"></a>

**0° CCW: unverified** — `in_game_visible_travel-1df3119d36e204c67cf5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-4>external-22; entry: external-4; exit: external-22.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-16; entry: external-5; exit: external-16</summary>

<a id="case-in_game_visible_travel-1cdad7ff3e37487006bf"></a>

**0° CCW: unverified** — `in_game_visible_travel-1cdad7ff3e37487006bf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-16; entry: external-5; exit: external-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-17; entry: external-5; exit: external-17</summary>

<a id="case-in_game_visible_travel-dfd1c70413139ed686d0"></a>

**0° CCW: unverified** — `in_game_visible_travel-dfd1c70413139ed686d0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-17; entry: external-5; exit: external-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9</summary>

<a id="case-in_game_visible_travel-0301aed91499dadd0fc9"></a>

**0° CCW: unverified** — `in_game_visible_travel-0301aed91499dadd0fc9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-5>external-9; entry: external-5; exit: external-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-6>external-18; entry: external-6; exit: external-18</summary>

<a id="case-in_game_visible_travel-df262dcc800ee048eb60"></a>

**0° CCW: unverified** — `in_game_visible_travel-df262dcc800ee048eb60`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-6>external-18; entry: external-6; exit: external-18.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: external-8>external-3; entry: external-8; exit: external-3</summary>

<a id="case-in_game_visible_travel-a2a9348540dac7ed1b06"></a>

**0° CCW: unverified** — `in_game_visible_travel-a2a9348540dac7ed1b06`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: external-8>external-3; entry: external-8; exit: external-3.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: external-25>external-27; entry: external-25; exit: external-27 | — | <a href="#case-in_game_route_query-18c90edeeaf629b04fc8">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: external-28>external-26; entry: external-28; exit: external-26 | — | <a href="#case-in_game_route_query-25efc5d185a1bc2353cf">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: external-25>external-27; entry: external-25; exit: external-27</summary>

<a id="case-in_game_route_query-18c90edeeaf629b04fc8"></a>

**0° CCW: unverified** — `in_game_route_query-18c90edeeaf629b04fc8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: external-25>external-27; entry: external-25; exit: external-27.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: external-28>external-26; entry: external-28; exit: external-26</summary>

<a id="case-in_game_route_query-25efc5d185a1bc2353cf"></a>

**0° CCW: unverified** — `in_game_route_query-25efc5d185a1bc2353cf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: external-28>external-26; entry: external-28; exit: external-26.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: external-25>external-27; entry: external-25; exit: external-27 | — | <a href="#case-in_game_visible_travel-18c90edeeaf629b04fc8">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: external-28>external-26; entry: external-28; exit: external-26 | — | <a href="#case-in_game_visible_travel-25efc5d185a1bc2353cf">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: external-25>external-27; entry: external-25; exit: external-27</summary>

<a id="case-in_game_visible_travel-18c90edeeaf629b04fc8"></a>

**0° CCW: unverified** — `in_game_visible_travel-18c90edeeaf629b04fc8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: external-25>external-27; entry: external-25; exit: external-27.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: external-28>external-26; entry: external-28; exit: external-26</summary>

<a id="case-in_game_visible_travel-25efc5d185a1bc2353cf"></a>

**0° CCW: unverified** — `in_game_visible_travel-25efc5d185a1bc2353cf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: external-28>external-26; entry: external-28; exit: external-26.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 122 cases; unverified: 122</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4df5253325d3a5a962f5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ddb4a78290312195656f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b0d9ea504f5838993d64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f62a7f5591195f1c5a27">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-92beb85de3919a9f9e38">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-140ee7e98e4d06df1dc0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3075f5cb376e2f3f3613">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-03009dd2ec284829b8ac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-da553f758322c6fc383d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f0a9e434b62af55b7fdc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e3f26b8bfed582a472bc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f27e177f3bed406e3c3c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f2a81135215123b6227a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-600a06c657e4ef3e84d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2b811d8d836f123cbdcc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-04a8aa36cf7687a2a4d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e7c7bd2654b640b3137f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-65313dd337171d04c96d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2cff6e39a14ce8d71b7f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8b72d941bc5dec677316">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-efc2006f482a4aa3e6f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-614d4acdee2b148f4a12">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7a96dc89bf152f9e8bc0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-09136b99468fea2ee46b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5f983faebd94d30d9f06">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f871b890263dda3e604a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5738e475c8093b427958">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9e934b61a5ef78888ea5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ac0d6981f57946608577">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-78192997b1c56fd76763">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f2702d2408f51ed64baa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c5e5229b98fc4fd7d276">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-851dcd531963126d90ae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-15a3c1721c004d0fc4b3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-66021f827b123db47514">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b19325bb983939793add">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-fd3e8683ebc19b6b9a6d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ff38f9cccda68adf36c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-90dece1964246b145aba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d669bf759b00a9d0ac18">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0c3ddd47bc15a226d828">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-83d13ce8ea2b622fb346">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-15b58c190897431cef08">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0b0ad20bc311fa680b60">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b747b785b9817d690348">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ced437801ac9647acebc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a72d5000ed876e3ea24d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-857d17c963342eda4b0a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ad80df5b27bdfec0fc4f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-88e754e3fb5dabf80136">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e4b1549edb3fb70ec24c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0d718437096ef0970881">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-860ff11898ce9da9dd60">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3e6be5243156fd77aece">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-463f09851127e2d811fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f8f91f40f0e65f9343a2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f1f4321e731d9b8ef6df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1f648c8cad4fb8757c89">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6c861fd9e0dee9bf6d4d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ba4fa05f863466f2e287">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-475fad3310778d09dd72">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-210d47233ae064107780">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-925e696c29bf2b6dc1c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8f0c6eda05a095b919df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2291b13f6fa48e39e6ac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-56faa1ed18b908959dca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-314c1990d32c0e69c644">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-eed5161ba0708c788179">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a5f860391a8b8d37c50b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6479b6d7e96ec837c6e2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7c5b3bdf80fe1096d696">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2fe324b9ddfea7efd735">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-cb152456b8963fd35e67">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-39cc6c6371f04ead37c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8710d4a3a76557f4279f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-464802d2ab1d6d8740bc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-02e67baeee7acfa73fa6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d1aa2d95bfe64701a475">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-95285a06cc6fcddc23db">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-541c778b1a2441cd5614">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-35f7b77ac23427409b1b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a9f0f3169576f6775dd7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c03443588a77b3e6efe9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-bf1a72424564bd98ebd5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8940b0d1a0316ba98418">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-01c8a5896f607907051f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e7458bea672ba47c09ee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9eab3c7f548921c19fba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e3023adddb0790809919">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a921f12e4e0ad6156602">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-35dd1dae5436761f82c6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7bb29e47dc3a96e59ffd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-54bf54259a58b7dbb2e6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f20e0f1efc871f074049">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ffbc7d9711d70aef117f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1829af5e4dd96cb98f21">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a6e4104ab82c6e0c1438">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d51cde0d74d53a61c38a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7718304bcd7f34c3d698">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a7bf2ca2da7646a639ac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-52657eb2e132d7e0d910">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7b736c36ea0fb4e2cf2d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-61ac0ba65d0cea959dbe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-98a7809e3ce9e8e47ab8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3c9c27e42be6927a2364">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-03f32f7eed125cbf9caf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-49eb78690921dffc69df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-923db78cf7f1b3ac2cb5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b25759d12d55b8527b11">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-60ff2f7df4aefa98cc3c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b9d3cffe91f2f428e7c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-40cafadaaf3d6071f69e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e95edb44257f027b52a4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6ffa77491e556eeb9089">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d2fa5981bd45d00a57f8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1a882ab74d010c1418a4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-49c33fea073aabf481f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e601b69fa3d61fd4454b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-edbec1da311eb6a141b9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-2d8e40171cb395950d36">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a4d2841751bb5d074416">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-182e77dd9bb0910cabc6">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4df5253325d3a5a962f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4df5253325d3a5a962f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ddb4a78290312195656f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ddb4a78290312195656f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b0d9ea504f5838993d64"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0d9ea504f5838993d64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f62a7f5591195f1c5a27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f62a7f5591195f1c5a27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-92beb85de3919a9f9e38"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-92beb85de3919a9f9e38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-140ee7e98e4d06df1dc0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-140ee7e98e4d06df1dc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3075f5cb376e2f3f3613"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3075f5cb376e2f3f3613`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-03009dd2ec284829b8ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-03009dd2ec284829b8ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-da553f758322c6fc383d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-da553f758322c6fc383d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f0a9e434b62af55b7fdc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f0a9e434b62af55b7fdc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e3f26b8bfed582a472bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3f26b8bfed582a472bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f27e177f3bed406e3c3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f27e177f3bed406e3c3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f2a81135215123b6227a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2a81135215123b6227a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-600a06c657e4ef3e84d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-600a06c657e4ef3e84d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2b811d8d836f123cbdcc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2b811d8d836f123cbdcc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-04a8aa36cf7687a2a4d9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-04a8aa36cf7687a2a4d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e7c7bd2654b640b3137f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7c7bd2654b640b3137f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-65313dd337171d04c96d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-65313dd337171d04c96d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2cff6e39a14ce8d71b7f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2cff6e39a14ce8d71b7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8b72d941bc5dec677316"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8b72d941bc5dec677316`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-efc2006f482a4aa3e6f7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-efc2006f482a4aa3e6f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-614d4acdee2b148f4a12"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-614d4acdee2b148f4a12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7a96dc89bf152f9e8bc0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7a96dc89bf152f9e8bc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-09136b99468fea2ee46b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-09136b99468fea2ee46b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5f983faebd94d30d9f06"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5f983faebd94d30d9f06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f871b890263dda3e604a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f871b890263dda3e604a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5738e475c8093b427958"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5738e475c8093b427958`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9e934b61a5ef78888ea5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9e934b61a5ef78888ea5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ac0d6981f57946608577"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac0d6981f57946608577`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-78192997b1c56fd76763"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-78192997b1c56fd76763`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f2702d2408f51ed64baa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2702d2408f51ed64baa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c5e5229b98fc4fd7d276"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5e5229b98fc4fd7d276`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-851dcd531963126d90ae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-851dcd531963126d90ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-15a3c1721c004d0fc4b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-15a3c1721c004d0fc4b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-66021f827b123db47514"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-66021f827b123db47514`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b19325bb983939793add"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b19325bb983939793add`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-fd3e8683ebc19b6b9a6d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fd3e8683ebc19b6b9a6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ff38f9cccda68adf36c7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ff38f9cccda68adf36c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-90dece1964246b145aba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-90dece1964246b145aba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d669bf759b00a9d0ac18"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d669bf759b00a9d0ac18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0c3ddd47bc15a226d828"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0c3ddd47bc15a226d828`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-83d13ce8ea2b622fb346"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-83d13ce8ea2b622fb346`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-15b58c190897431cef08"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-15b58c190897431cef08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0b0ad20bc311fa680b60"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0b0ad20bc311fa680b60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b747b785b9817d690348"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b747b785b9817d690348`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ced437801ac9647acebc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ced437801ac9647acebc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a72d5000ed876e3ea24d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a72d5000ed876e3ea24d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-857d17c963342eda4b0a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-857d17c963342eda4b0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ad80df5b27bdfec0fc4f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad80df5b27bdfec0fc4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-88e754e3fb5dabf80136"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-88e754e3fb5dabf80136`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e4b1549edb3fb70ec24c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e4b1549edb3fb70ec24c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0d718437096ef0970881"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0d718437096ef0970881`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-860ff11898ce9da9dd60"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-860ff11898ce9da9dd60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3e6be5243156fd77aece"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e6be5243156fd77aece`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-463f09851127e2d811fd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-463f09851127e2d811fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f8f91f40f0e65f9343a2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f8f91f40f0e65f9343a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f1f4321e731d9b8ef6df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f1f4321e731d9b8ef6df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1f648c8cad4fb8757c89"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f648c8cad4fb8757c89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6c861fd9e0dee9bf6d4d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c861fd9e0dee9bf6d4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ba4fa05f863466f2e287"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ba4fa05f863466f2e287`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-475fad3310778d09dd72"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-475fad3310778d09dd72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-210d47233ae064107780"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-210d47233ae064107780`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-925e696c29bf2b6dc1c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-925e696c29bf2b6dc1c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8f0c6eda05a095b919df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8f0c6eda05a095b919df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2291b13f6fa48e39e6ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2291b13f6fa48e39e6ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-56faa1ed18b908959dca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-56faa1ed18b908959dca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-314c1990d32c0e69c644"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-314c1990d32c0e69c644`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-eed5161ba0708c788179"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eed5161ba0708c788179`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a5f860391a8b8d37c50b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a5f860391a8b8d37c50b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6479b6d7e96ec837c6e2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6479b6d7e96ec837c6e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7c5b3bdf80fe1096d696"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c5b3bdf80fe1096d696`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2fe324b9ddfea7efd735"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2fe324b9ddfea7efd735`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-cb152456b8963fd35e67"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb152456b8963fd35e67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-39cc6c6371f04ead37c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-39cc6c6371f04ead37c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8710d4a3a76557f4279f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8710d4a3a76557f4279f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-464802d2ab1d6d8740bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-464802d2ab1d6d8740bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-02e67baeee7acfa73fa6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-02e67baeee7acfa73fa6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d1aa2d95bfe64701a475"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d1aa2d95bfe64701a475`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-95285a06cc6fcddc23db"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-95285a06cc6fcddc23db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-541c778b1a2441cd5614"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-541c778b1a2441cd5614`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-35f7b77ac23427409b1b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35f7b77ac23427409b1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a9f0f3169576f6775dd7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a9f0f3169576f6775dd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c03443588a77b3e6efe9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c03443588a77b3e6efe9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-bf1a72424564bd98ebd5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bf1a72424564bd98ebd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8940b0d1a0316ba98418"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8940b0d1a0316ba98418`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-01c8a5896f607907051f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01c8a5896f607907051f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e7458bea672ba47c09ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7458bea672ba47c09ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9eab3c7f548921c19fba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9eab3c7f548921c19fba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e3023adddb0790809919"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3023adddb0790809919`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a921f12e4e0ad6156602"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a921f12e4e0ad6156602`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-35dd1dae5436761f82c6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35dd1dae5436761f82c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7bb29e47dc3a96e59ffd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7bb29e47dc3a96e59ffd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-54bf54259a58b7dbb2e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-54bf54259a58b7dbb2e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f20e0f1efc871f074049"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f20e0f1efc871f074049`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ffbc7d9711d70aef117f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ffbc7d9711d70aef117f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1829af5e4dd96cb98f21"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1829af5e4dd96cb98f21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a6e4104ab82c6e0c1438"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a6e4104ab82c6e0c1438`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d51cde0d74d53a61c38a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d51cde0d74d53a61c38a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7718304bcd7f34c3d698"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7718304bcd7f34c3d698`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a7bf2ca2da7646a639ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a7bf2ca2da7646a639ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-52657eb2e132d7e0d910"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-52657eb2e132d7e0d910`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7b736c36ea0fb4e2cf2d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7b736c36ea0fb4e2cf2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-1; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-61ac0ba65d0cea959dbe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-61ac0ba65d0cea959dbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-98a7809e3ce9e8e47ab8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-98a7809e3ce9e8e47ab8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3c9c27e42be6927a2364"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3c9c27e42be6927a2364`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-03f32f7eed125cbf9caf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-03f32f7eed125cbf9caf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-49eb78690921dffc69df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-49eb78690921dffc69df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-923db78cf7f1b3ac2cb5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-923db78cf7f1b3ac2cb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b25759d12d55b8527b11"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b25759d12d55b8527b11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-60ff2f7df4aefa98cc3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-60ff2f7df4aefa98cc3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b9d3cffe91f2f428e7c7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b9d3cffe91f2f428e7c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-40cafadaaf3d6071f69e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-40cafadaaf3d6071f69e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-3; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e95edb44257f027b52a4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e95edb44257f027b52a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-7; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6ffa77491e556eeb9089"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ffa77491e556eeb9089`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-9; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d2fa5981bd45d00a57f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d2fa5981bd45d00a57f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-10; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1a882ab74d010c1418a4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a882ab74d010c1418a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-12; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-49c33fea073aabf481f6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-49c33fea073aabf481f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-14; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e601b69fa3d61fd4454b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e601b69fa3d61fd4454b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-16; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-edbec1da311eb6a141b9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-edbec1da311eb6a141b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-17; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-2d8e40171cb395950d36"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2d8e40171cb395950d36`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-18; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a4d2841751bb5d074416"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a4d2841751bb5d074416`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-22; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-182e77dd9bb0910cabc6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-182e77dd9bb0910cabc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-24; from service: road; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-2; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-87e0dd3e5e2054b62908">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-2; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b997856d4974b4aacba0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-395bbedf567034065771">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-4; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-53b120961c7b574add1e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-da2abd8c5c7acbe746d0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-5; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-c3cbf04fcaa73c4a52c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e87814212f1092b28d6c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-6; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b6ba0ff84ac11f1d6253">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-405d3715673a5f89c831">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-8; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-d9c4271a32f8ec77d734">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6efd32dc20e84f524c3f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-11; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-129d02cc36472760df88">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7430b5287a0cfb07b839">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-13; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-551159d17dbe8556f41f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8e94394de4462b5c8987">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-15; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ad7d90b45313e3320d83">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ff4820bd8dd214ad18ec">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-19; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1217492298f1e90bc8c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5df7e6b5bdcc50930bc1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-20; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1725c3f048e50099c822">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-bc40f4b94c225c70f7f0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-21; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-7a3e0cdbe6604be203b7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-953e71d6cf12b23395dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-23; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-11229623f40912ed6664">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-87e0dd3e5e2054b62908"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-87e0dd3e5e2054b62908`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-2; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b997856d4974b4aacba0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b997856d4974b4aacba0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-2; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-395bbedf567034065771"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-395bbedf567034065771`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-4; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-53b120961c7b574add1e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-53b120961c7b574add1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-4; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-da2abd8c5c7acbe746d0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-da2abd8c5c7acbe746d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-5; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-c3cbf04fcaa73c4a52c7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c3cbf04fcaa73c4a52c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-5; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e87814212f1092b28d6c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e87814212f1092b28d6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-6; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b6ba0ff84ac11f1d6253"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b6ba0ff84ac11f1d6253`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-6; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-405d3715673a5f89c831"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-405d3715673a5f89c831`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-8; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-d9c4271a32f8ec77d734"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d9c4271a32f8ec77d734`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-8; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6efd32dc20e84f524c3f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6efd32dc20e84f524c3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-11; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-129d02cc36472760df88"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-129d02cc36472760df88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-11; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7430b5287a0cfb07b839"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7430b5287a0cfb07b839`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-13; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-551159d17dbe8556f41f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-551159d17dbe8556f41f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-13; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8e94394de4462b5c8987"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8e94394de4462b5c8987`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-15; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ad7d90b45313e3320d83"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad7d90b45313e3320d83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-15; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ff4820bd8dd214ad18ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ff4820bd8dd214ad18ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-19; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1217492298f1e90bc8c7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1217492298f1e90bc8c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-19; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5df7e6b5bdcc50930bc1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5df7e6b5bdcc50930bc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-20; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1725c3f048e50099c822"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1725c3f048e50099c822`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-20; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-bc40f4b94c225c70f7f0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bc40f4b94c225c70f7f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-21; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-7a3e0cdbe6604be203b7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7a3e0cdbe6604be203b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-21; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-953e71d6cf12b23395dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-953e71d6cf12b23395dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-26; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-23; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-11229623f40912ed6664"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-11229623f40912ed6664`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-23; to port: external-27; from service: road; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 24 cases; unverified: 24</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-25; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3e6737a7f6d335c37ee8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-68d79a68ea534750a467">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-9c8d897667393a31e27c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-258e2cd48a5ca7a1353f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5cceb0093dd7d42daa19">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-12; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-5d5911c0f9dda0bfc49a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b2200976a881db7c0cf5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-59ba5fe8c9e76a7a38f3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-17; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-edb71f0cd321fc48467f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-18; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-1d2d4edaa3a3b07f8be5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-22; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-f66ada2c8ce2d4f3dd78">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-25; to port: external-24; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-8df8c14bf6642a378150">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-50e831d3346a5b3b7db0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-0e46f17159a1ee8b1ac6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-b8716799e62b01834cf0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-4a1137bb644c74af045a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-89b967aded19fdaa9dae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-12; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-aa3bb1e181da39602898">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3f725b6b4ec537300357">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-e0f69d46521546dacd0a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-17; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-a0c34bdf2b07da08df09">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-18; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-984253c770898cd7be73">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-22; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-3f54302fc9238221f7ea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-24; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-32381af14c143c79a81a">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3e6737a7f6d335c37ee8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e6737a7f6d335c37ee8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-68d79a68ea534750a467"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-68d79a68ea534750a467`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-9c8d897667393a31e27c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9c8d897667393a31e27c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-258e2cd48a5ca7a1353f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-258e2cd48a5ca7a1353f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5cceb0093dd7d42daa19"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5cceb0093dd7d42daa19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-12; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-5d5911c0f9dda0bfc49a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5d5911c0f9dda0bfc49a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-12; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b2200976a881db7c0cf5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b2200976a881db7c0cf5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-59ba5fe8c9e76a7a38f3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-59ba5fe8c9e76a7a38f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-17; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-edb71f0cd321fc48467f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-edb71f0cd321fc48467f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-17; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-18; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-1d2d4edaa3a3b07f8be5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1d2d4edaa3a3b07f8be5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-18; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-22; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-f66ada2c8ce2d4f3dd78"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f66ada2c8ce2d4f3dd78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-22; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-24; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-8df8c14bf6642a378150"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8df8c14bf6642a378150`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-24; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-50e831d3346a5b3b7db0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-50e831d3346a5b3b7db0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-1; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-0e46f17159a1ee8b1ac6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e46f17159a1ee8b1ac6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-3; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-b8716799e62b01834cf0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8716799e62b01834cf0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-7; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-4a1137bb644c74af045a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4a1137bb644c74af045a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-9; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-89b967aded19fdaa9dae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-89b967aded19fdaa9dae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-10; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-12; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-aa3bb1e181da39602898"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aa3bb1e181da39602898`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-12; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3f725b6b4ec537300357"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f725b6b4ec537300357`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-14; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-e0f69d46521546dacd0a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e0f69d46521546dacd0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-16; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-17; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-a0c34bdf2b07da08df09"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a0c34bdf2b07da08df09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-17; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-18; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-984253c770898cd7be73"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-984253c770898cd7be73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-18; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-22; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-3f54302fc9238221f7ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f54302fc9238221f7ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-22; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-24; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-32381af14c143c79a81a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32381af14c143c79a81a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-24; from service: pedestrian; to service: road; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Forbidden transfer**<br>from port: external-25; to port: external-26; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-6252c26e2e476116dedb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: external-28; to port: external-27; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph | — | <a href="#case-in_game_forbidden_transfer-ad4483fcabd42a9b6446">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: external-25; to port: external-26; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-6252c26e2e476116dedb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6252c26e2e476116dedb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-25; to port: external-26; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: external-28; to port: external-27; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph</summary>

<a id="case-in_game_forbidden_transfer-ad4483fcabd42a9b6446"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad4483fcabd42a9b6446`.

Confirm this undeclared transfer is unavailable.

Scope: from port: external-28; to port: external-27; from service: pedestrian; to service: pedestrian; basis: not reachable in the saved placed encoded-route graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 10 cases; unverified: 10</summary>

| Check / exact scope | General | 0° |
| --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-southeast | <a href="#case-preview_review-1078b138a2c094aa07cc">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-top | <a href="#case-preview_review-b02e7ddb83975dfa69a4">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-northwest | <a href="#case-preview_review-c4c07979aec5da50d199">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-southeast | <a href="#case-preview_review-bc702f29fdf636f1adbb">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-top | <a href="#case-preview_review-2f13a8f3bd777cd10246">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-northwest | <a href="#case-preview_review-41945dab4d14218575f2">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-profiles | <a href="#case-preview_review-ca10fd6f9f960a69288e">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-southeast | <a href="#case-preview_review-a27eb7d003ae1a9abb69">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-top | <a href="#case-preview_review-3fc1532c9931e2deb4e3">[ ] unverified</a> | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:tile-ownership | <a href="#case-preview_review-a7286a3bc6d0b50ac5e7">[ ] unverified</a> | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-southeast</summary>

<a id="case-preview_review-1078b138a2c094aa07cc"></a>

**General: unverified** — `preview_review-1078b138a2c094aa07cc`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-top</summary>

<a id="case-preview_review-b02e7ddb83975dfa69a4"></a>

**General: unverified** — `preview_review-b02e7ddb83975dfa69a4`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:clean-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-northwest</summary>

<a id="case-preview_review-c4c07979aec5da50d199"></a>

**General: unverified** — `preview_review-c4c07979aec5da50d199`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-southeast</summary>

<a id="case-preview_review-bc702f29fdf636f1adbb"></a>

**General: unverified** — `preview_review-bc702f29fdf636f1adbb`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-top</summary>

<a id="case-preview_review-2f13a8f3bd777cd10246"></a>

**General: unverified** — `preview_review-2f13a8f3bd777cd10246`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:named-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-northwest</summary>

<a id="case-preview_review-41945dab4d14218575f2"></a>

**General: unverified** — `preview_review-41945dab4d14218575f2`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-northwest.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-profiles</summary>

<a id="case-preview_review-ca10fd6f9f960a69288e"></a>

**General: unverified** — `preview_review-ca10fd6f9f960a69288e`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-profiles.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-southeast</summary>

<a id="case-preview_review-a27eb7d003ae1a9abb69"></a>

**General: unverified** — `preview_review-a27eb7d003ae1a9abb69`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-top</summary>

<a id="case-preview_review-3fc1532c9931e2deb4e3"></a>

**General: unverified** — `preview_review-3fc1532c9931e2deb4e3`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:schematic-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:tile-ownership</summary>

<a id="case-preview_review-a7286a3bc6d0b50ac5e7"></a>

**General: unverified** — `preview_review-a7286a3bc6d0b50ac5e7`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-diagonal-avenue-diamond:tile-ownership.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The earlier design was a source-only schematic with provisional 12 m-wide highway decks, 48 m lower curves, and 80 m upper curves. The measured native DD RHW-4 deck width is 16 m. The compiled experiment snaps the external paths to actual native tile-side lanes, producing approximately 50.04 m lower curves and 80.47 m upper curves. Its [schematic top](previews/schematic-top.png), [opposite angled view](previews/schematic-northwest.png), [profiles](previews/schematic-profiles.png), and [original validation summary](evidence/validation.json) remain historical prototype evidence; they are not tests of the new compiled pieces.
