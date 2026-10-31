---
title: "Testing: DD RHW-4 — L1/L2 over Avenue L0 — Diagonal 90° — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1/L2 over Avenue L0 — Diagonal 90° — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This record covers **ddrhw-parallel-crossing**, used once as **P01** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 3 occupied tiles in a 2 × 2 rectangle, the exact authored 0° reference at X4, Y5, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

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
| `channel-12-out` | road / 1 / primary | out | [-8.0, -12.8, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-02-in` | road / 1 / primary | in | [-8.0, -12.8, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-03-in` | road / 1 / primary | in | [-8.0, -3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-04-in` | road / 1 / primary | in | [-8.0, 3.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-13-out` | road / 1 / primary | out | [-3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-05-in` | road / 1 / primary | in | [0.970563, -24.0, 0.131713]; [0.7071067811865519, 0.7071067811865431]; -0.183235324 | `path-interface-e3cc651d01db26df1e9d` |
| `channel-14-out` | road / 1 / primary | out | [3.2, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-15-out` | road / 1 / primary | out | [8.0, -20.675154, 0.0]; [0.9835050748723825, -0.18088053433210963]; 0.0 | `path-interface-eb8edd053c1b618ae382` |
| `channel-16-out` | road / 1 / primary | out | [8.0, -19.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-17-out` | road / 1 / primary | out | [8.0, -12.8, 0.0]; [0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-06-in` | road / 1 / primary | in | [12.8, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-07-in` | road / 1 / primary | in | [12.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865475]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-18-out` | road / 1 / primary | out | [12.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-08-in` | road / 1 / primary | in | [19.2, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-09-in` | road / 1 / primary | in | [19.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-19-out` | road / 1 / primary | out | [19.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-10-in` | road / 1 / primary | in | [20.675154, -8.0, 0.0]; [-0.18088053433210963, 0.9835050748723825]; 0.0 | `path-interface-ab0dc819ba4c7fec9f5c` |
| `channel-20-out` | road / 1 / primary | out | [24.0, -0.970563, 0.131713]; [0.7071067811865431, 0.7071067811865519]; 0.183235324 | `path-interface-e362ca9b6cb3a77b1c9a` |
| `channel-21-in` | pedestrian / 2 / primary | in | [-8.0, -7.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `channel-23-out` | pedestrian / 2 / primary | out | [7.3, 8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `channel-24-out` | pedestrian / 2 / primary | out | [8.0, -23.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `channel-22-in` | pedestrian / 2 / primary | in | [23.3, -8.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-19-out` | primary |
| road | `channel-02-in` → `channel-18-out` | primary |
| road | `channel-03-in` → `channel-16-out` | primary |
| road | `channel-04-in` → `channel-17-out` | primary |
| road | `channel-05-in` → `channel-15-out` | primary |
| road | `channel-06-in` → `channel-13-out` | primary |
| road | `channel-07-in` → `channel-12-out` | primary |
| road | `channel-08-in` → `channel-14-out` | primary |
| road | `channel-09-in` → `channel-11-out` | primary |
| road | `channel-10-in` → `channel-20-out` | primary |
| pedestrian | `channel-21-in` → `channel-24-out` | primary |
| pedestrian | `channel-22-in` → `channel-23-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-21-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `channel-22-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X4, Y5), (X5, Y5), (X4, Y4)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-pedestrian-mouths-01
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-crossing --build dist/ddrhw-parallel-diamond-pedestrian-mouths-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-crossing
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

The current revision changes only the two ground terminals' visible asphalt width: each retains its 6 m grade join, narrows to 3.5 m over 3 m, and stays narrow through its R6 turn and Avenue joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from the grade join, after the 3 m taper is complete. The asphalt footprint reaches the pedestrian route earlier, while the taper is still narrowing; this is the actual driveway crossing. Traffic PATHs, permanent identifiers, construction ownership, and the other thirteen physical components retain their previous scope. Adaptive sidewalks are implemented for all three Avenue cells of this component. The game selects a native Avenue pavement appearance from the surrounding development; connecting another Avenue alone does not force a sidewalk to appear. The rotating highway or ramp model is attached above that native ground artwork, and the pedestrian PATHs are separate retained traffic data. The complete new assembly still needs its own game observations. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

## 4. Game checks

1. Select this exact component through the assembly button, match P01 at **X4, Y5**, and confirm that the occupied preview squares match **(X4, Y5), (X5, Y5), (X4, Y4)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and compare its pavement variant with the neighbouring Avenue. Connecting the Avenue alone does not select the developed pavement appearance. Inspect both narrow driveway crossings, then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH, and the crossing remains road asphalt. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-crossing** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. Its sparse 2 × 2 footprint has three occupied corners and an empty local [1,1] corner. That empty corner supplies a temporary placement handle, which the supported NAM DLL removes. It is not a fourth permanent road tile. The highway model stays straight; curved high departures belong to the separate ramp modules. This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

Adaptive pavement is implemented through native texture variants and correctly rotating model props, rather than a fixed sidewalk slab. Its visible appearance depends on the native development rules, and a sidewalk replacement mod needs its own compatibility check. The approximately 1.149 m clearance applies where the terminal asphalt and retained pedestrian centreline run beside one another; the actual driveway crossings are deliberately excluded. A measured route clearance does not establish visible walking, a continuous pavement strip, or a particular pedestrian-versus-car priority in the game.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/48 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/48 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 645, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-crossing/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-crossing/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-ac49012ca7f09ecbd5ff">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-ac49012ca7f09ecbd5ff"></a>

**General: unverified** — `software_resources-ac49012ca7f09ecbd5ff`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-ac49012ca7f09ecbd5ff">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-ac49012ca7f09ecbd5ff"></a>

**General: unverified** — `software_connectivity-ac49012ca7f09ecbd5ff`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-c36b058e6f1085b5f41e">[ ] unverified</a> | <a href="#case-in_game_render-9da9fc838fc7286f556f">[ ] unverified</a> | <a href="#case-in_game_render-0dc93709d566b97b81f8">[ ] unverified</a> | <a href="#case-in_game_render-0f17877912775a85d482">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-c36b058e6f1085b5f41e"></a>

**0° CCW: unverified** — `in_game_render-c36b058e6f1085b5f41e`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9da9fc838fc7286f556f"></a>

**90° CCW: unverified** — `in_game_render-9da9fc838fc7286f556f`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0dc93709d566b97b81f8"></a>

**180° CCW: unverified** — `in_game_render-0dc93709d566b97b81f8`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0f17877912775a85d482"></a>

**270° CCW: unverified** — `in_game_render-0f17877912775a85d482`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-c36b058e6f1085b5f41e">[ ] unverified</a> | <a href="#case-in_game_placement-9da9fc838fc7286f556f">[ ] unverified</a> | <a href="#case-in_game_placement-0dc93709d566b97b81f8">[ ] unverified</a> | <a href="#case-in_game_placement-0f17877912775a85d482">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-c36b058e6f1085b5f41e"></a>

**0° CCW: unverified** — `in_game_placement-c36b058e6f1085b5f41e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9da9fc838fc7286f556f"></a>

**90° CCW: unverified** — `in_game_placement-9da9fc838fc7286f556f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0dc93709d566b97b81f8"></a>

**180° CCW: unverified** — `in_game_placement-0dc93709d566b97b81f8`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0f17877912775a85d482"></a>

**270° CCW: unverified** — `in_game_placement-0f17877912775a85d482`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-c36b058e6f1085b5f41e">[ ] unverified</a> | <a href="#case-in_game_demolition-9da9fc838fc7286f556f">[ ] unverified</a> | <a href="#case-in_game_demolition-0dc93709d566b97b81f8">[ ] unverified</a> | <a href="#case-in_game_demolition-0f17877912775a85d482">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-c36b058e6f1085b5f41e"></a>

**0° CCW: unverified** — `in_game_demolition-c36b058e6f1085b5f41e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9da9fc838fc7286f556f"></a>

**90° CCW: unverified** — `in_game_demolition-9da9fc838fc7286f556f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0dc93709d566b97b81f8"></a>

**180° CCW: unverified** — `in_game_demolition-0dc93709d566b97b81f8`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0f17877912775a85d482"></a>

**270° CCW: unverified** — `in_game_demolition-0f17877912775a85d482`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-c36b058e6f1085b5f41e">[ ] unverified</a> | <a href="#case-in_game_save_reload-9da9fc838fc7286f556f">[ ] unverified</a> | <a href="#case-in_game_save_reload-0dc93709d566b97b81f8">[ ] unverified</a> | <a href="#case-in_game_save_reload-0f17877912775a85d482">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-c36b058e6f1085b5f41e"></a>

**0° CCW: unverified** — `in_game_save_reload-c36b058e6f1085b5f41e`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9da9fc838fc7286f556f"></a>

**90° CCW: unverified** — `in_game_save_reload-9da9fc838fc7286f556f`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0dc93709d566b97b81f8"></a>

**180° CCW: unverified** — `in_game_save_reload-0dc93709d566b97b81f8`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0f17877912775a85d482"></a>

**270° CCW: unverified** — `in_game_save_reload-0f17877912775a85d482`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-9c0ce3ac5085a861c837">[ ] unverified</a> | <a href="#case-in_game_route_query-e16239f2f04ad8bd1676">[ ] unverified</a> | <a href="#case-in_game_route_query-3601dd52281eafd8753e">[ ] unverified</a> | <a href="#case-in_game_route_query-3545fe71e86e3db127cf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-276dc328887ec5a73af7">[ ] unverified</a> | <a href="#case-in_game_route_query-6fe7f8af0d601713bd1f">[ ] unverified</a> | <a href="#case-in_game_route_query-06449c479e719feac9ac">[ ] unverified</a> | <a href="#case-in_game_route_query-e162bbba902e606e9c6e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-2836d996db6128e14724">[ ] unverified</a> | <a href="#case-in_game_route_query-003f28934bfea4faa137">[ ] unverified</a> | <a href="#case-in_game_route_query-5658af2d317281a1e794">[ ] unverified</a> | <a href="#case-in_game_route_query-c0755caaeef8ca82693e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-5135f97300d37145f205">[ ] unverified</a> | <a href="#case-in_game_route_query-9fb13003005aee830a95">[ ] unverified</a> | <a href="#case-in_game_route_query-407fa7dfcf6e0c2d4001">[ ] unverified</a> | <a href="#case-in_game_route_query-152f57b5643e43ab68e7">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out | — | <a href="#case-in_game_route_query-540a8b5c25e95596b096">[ ] unverified</a> | <a href="#case-in_game_route_query-d1e4100cbacc02f8f719">[ ] unverified</a> | <a href="#case-in_game_route_query-da0968a9d6b621bb20fa">[ ] unverified</a> | <a href="#case-in_game_route_query-71c72c3493ed587c21a6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-db6586bcbdd417580318">[ ] unverified</a> | <a href="#case-in_game_route_query-71a949aa13b7eaf20766">[ ] unverified</a> | <a href="#case-in_game_route_query-fd82126958fefc76cddd">[ ] unverified</a> | <a href="#case-in_game_route_query-8bc979cb4abe54ab4516">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-004a6f8a50eb9d0d84d1">[ ] unverified</a> | <a href="#case-in_game_route_query-5fb0fff4cafd70788e84">[ ] unverified</a> | <a href="#case-in_game_route_query-57bf5796a9b4b31b5347">[ ] unverified</a> | <a href="#case-in_game_route_query-09ca2f3cb653b3885d9a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-829f9ac3e99aecdac0bc">[ ] unverified</a> | <a href="#case-in_game_route_query-8b96ce7bd12bcdd91a74">[ ] unverified</a> | <a href="#case-in_game_route_query-80baef04cc7fd3cd4f26">[ ] unverified</a> | <a href="#case-in_game_route_query-e623d174d9a3a9a8007b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-4dc9f7b947d4b0a5af85">[ ] unverified</a> | <a href="#case-in_game_route_query-9161cadd6445bd6e8ef1">[ ] unverified</a> | <a href="#case-in_game_route_query-e415b82d84f9e81dd1b2">[ ] unverified</a> | <a href="#case-in_game_route_query-df33937c4dfbc78dc4e6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out | — | <a href="#case-in_game_route_query-4a11fd7029524ca99703">[ ] unverified</a> | <a href="#case-in_game_route_query-773e7842ad271fd2fa35">[ ] unverified</a> | <a href="#case-in_game_route_query-2b32b17f6ed1accee26c">[ ] unverified</a> | <a href="#case-in_game_route_query-65f864859b605b012fd9">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-9c0ce3ac5085a861c837"></a>

**0° CCW: unverified** — `in_game_route_query-9c0ce3ac5085a861c837`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-e16239f2f04ad8bd1676"></a>

**90° CCW: unverified** — `in_game_route_query-e16239f2f04ad8bd1676`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-3601dd52281eafd8753e"></a>

**180° CCW: unverified** — `in_game_route_query-3601dd52281eafd8753e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-3545fe71e86e3db127cf"></a>

**270° CCW: unverified** — `in_game_route_query-3545fe71e86e3db127cf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-276dc328887ec5a73af7"></a>

**0° CCW: unverified** — `in_game_route_query-276dc328887ec5a73af7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-6fe7f8af0d601713bd1f"></a>

**90° CCW: unverified** — `in_game_route_query-6fe7f8af0d601713bd1f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-06449c479e719feac9ac"></a>

**180° CCW: unverified** — `in_game_route_query-06449c479e719feac9ac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-e162bbba902e606e9c6e"></a>

**270° CCW: unverified** — `in_game_route_query-e162bbba902e606e9c6e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-2836d996db6128e14724"></a>

**0° CCW: unverified** — `in_game_route_query-2836d996db6128e14724`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-003f28934bfea4faa137"></a>

**90° CCW: unverified** — `in_game_route_query-003f28934bfea4faa137`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-5658af2d317281a1e794"></a>

**180° CCW: unverified** — `in_game_route_query-5658af2d317281a1e794`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-c0755caaeef8ca82693e"></a>

**270° CCW: unverified** — `in_game_route_query-c0755caaeef8ca82693e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-5135f97300d37145f205"></a>

**0° CCW: unverified** — `in_game_route_query-5135f97300d37145f205`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-9fb13003005aee830a95"></a>

**90° CCW: unverified** — `in_game_route_query-9fb13003005aee830a95`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-407fa7dfcf6e0c2d4001"></a>

**180° CCW: unverified** — `in_game_route_query-407fa7dfcf6e0c2d4001`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-152f57b5643e43ab68e7"></a>

**270° CCW: unverified** — `in_game_route_query-152f57b5643e43ab68e7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out</summary>

<a id="case-in_game_route_query-540a8b5c25e95596b096"></a>

**0° CCW: unverified** — `in_game_route_query-540a8b5c25e95596b096`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-d1e4100cbacc02f8f719"></a>

**90° CCW: unverified** — `in_game_route_query-d1e4100cbacc02f8f719`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-da0968a9d6b621bb20fa"></a>

**180° CCW: unverified** — `in_game_route_query-da0968a9d6b621bb20fa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-71c72c3493ed587c21a6"></a>

**270° CCW: unverified** — `in_game_route_query-71c72c3493ed587c21a6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-db6586bcbdd417580318"></a>

**0° CCW: unverified** — `in_game_route_query-db6586bcbdd417580318`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-71a949aa13b7eaf20766"></a>

**90° CCW: unverified** — `in_game_route_query-71a949aa13b7eaf20766`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-fd82126958fefc76cddd"></a>

**180° CCW: unverified** — `in_game_route_query-fd82126958fefc76cddd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-8bc979cb4abe54ab4516"></a>

**270° CCW: unverified** — `in_game_route_query-8bc979cb4abe54ab4516`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-004a6f8a50eb9d0d84d1"></a>

**0° CCW: unverified** — `in_game_route_query-004a6f8a50eb9d0d84d1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-5fb0fff4cafd70788e84"></a>

**90° CCW: unverified** — `in_game_route_query-5fb0fff4cafd70788e84`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-57bf5796a9b4b31b5347"></a>

**180° CCW: unverified** — `in_game_route_query-57bf5796a9b4b31b5347`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-09ca2f3cb653b3885d9a"></a>

**270° CCW: unverified** — `in_game_route_query-09ca2f3cb653b3885d9a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-829f9ac3e99aecdac0bc"></a>

**0° CCW: unverified** — `in_game_route_query-829f9ac3e99aecdac0bc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-8b96ce7bd12bcdd91a74"></a>

**90° CCW: unverified** — `in_game_route_query-8b96ce7bd12bcdd91a74`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-80baef04cc7fd3cd4f26"></a>

**180° CCW: unverified** — `in_game_route_query-80baef04cc7fd3cd4f26`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-e623d174d9a3a9a8007b"></a>

**270° CCW: unverified** — `in_game_route_query-e623d174d9a3a9a8007b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-4dc9f7b947d4b0a5af85"></a>

**0° CCW: unverified** — `in_game_route_query-4dc9f7b947d4b0a5af85`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-9161cadd6445bd6e8ef1"></a>

**90° CCW: unverified** — `in_game_route_query-9161cadd6445bd6e8ef1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-e415b82d84f9e81dd1b2"></a>

**180° CCW: unverified** — `in_game_route_query-e415b82d84f9e81dd1b2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-df33937c4dfbc78dc4e6"></a>

**270° CCW: unverified** — `in_game_route_query-df33937c4dfbc78dc4e6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out</summary>

<a id="case-in_game_route_query-4a11fd7029524ca99703"></a>

**0° CCW: unverified** — `in_game_route_query-4a11fd7029524ca99703`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-773e7842ad271fd2fa35"></a>

**90° CCW: unverified** — `in_game_route_query-773e7842ad271fd2fa35`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-2b32b17f6ed1accee26c"></a>

**180° CCW: unverified** — `in_game_route_query-2b32b17f6ed1accee26c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-65f864859b605b012fd9"></a>

**270° CCW: unverified** — `in_game_route_query-65f864859b605b012fd9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-9c0ce3ac5085a861c837">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e16239f2f04ad8bd1676">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3601dd52281eafd8753e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3545fe71e86e3db127cf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-276dc328887ec5a73af7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6fe7f8af0d601713bd1f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-06449c479e719feac9ac">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e162bbba902e606e9c6e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-2836d996db6128e14724">[ ] unverified</a> | <a href="#case-in_game_visible_travel-003f28934bfea4faa137">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5658af2d317281a1e794">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c0755caaeef8ca82693e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-5135f97300d37145f205">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9fb13003005aee830a95">[ ] unverified</a> | <a href="#case-in_game_visible_travel-407fa7dfcf6e0c2d4001">[ ] unverified</a> | <a href="#case-in_game_visible_travel-152f57b5643e43ab68e7">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out | — | <a href="#case-in_game_visible_travel-540a8b5c25e95596b096">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d1e4100cbacc02f8f719">[ ] unverified</a> | <a href="#case-in_game_visible_travel-da0968a9d6b621bb20fa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-71c72c3493ed587c21a6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-db6586bcbdd417580318">[ ] unverified</a> | <a href="#case-in_game_visible_travel-71a949aa13b7eaf20766">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fd82126958fefc76cddd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8bc979cb4abe54ab4516">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-004a6f8a50eb9d0d84d1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5fb0fff4cafd70788e84">[ ] unverified</a> | <a href="#case-in_game_visible_travel-57bf5796a9b4b31b5347">[ ] unverified</a> | <a href="#case-in_game_visible_travel-09ca2f3cb653b3885d9a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-829f9ac3e99aecdac0bc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8b96ce7bd12bcdd91a74">[ ] unverified</a> | <a href="#case-in_game_visible_travel-80baef04cc7fd3cd4f26">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e623d174d9a3a9a8007b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-4dc9f7b947d4b0a5af85">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9161cadd6445bd6e8ef1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e415b82d84f9e81dd1b2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-df33937c4dfbc78dc4e6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out | — | <a href="#case-in_game_visible_travel-4a11fd7029524ca99703">[ ] unverified</a> | <a href="#case-in_game_visible_travel-773e7842ad271fd2fa35">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2b32b17f6ed1accee26c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-65f864859b605b012fd9">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-9c0ce3ac5085a861c837"></a>

**0° CCW: unverified** — `in_game_visible_travel-9c0ce3ac5085a861c837`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-e16239f2f04ad8bd1676"></a>

**90° CCW: unverified** — `in_game_visible_travel-e16239f2f04ad8bd1676`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-3601dd52281eafd8753e"></a>

**180° CCW: unverified** — `in_game_visible_travel-3601dd52281eafd8753e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-3545fe71e86e3db127cf"></a>

**270° CCW: unverified** — `in_game_visible_travel-3545fe71e86e3db127cf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-276dc328887ec5a73af7"></a>

**0° CCW: unverified** — `in_game_visible_travel-276dc328887ec5a73af7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-6fe7f8af0d601713bd1f"></a>

**90° CCW: unverified** — `in_game_visible_travel-6fe7f8af0d601713bd1f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-06449c479e719feac9ac"></a>

**180° CCW: unverified** — `in_game_visible_travel-06449c479e719feac9ac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-e162bbba902e606e9c6e"></a>

**270° CCW: unverified** — `in_game_visible_travel-e162bbba902e606e9c6e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-2836d996db6128e14724"></a>

**0° CCW: unverified** — `in_game_visible_travel-2836d996db6128e14724`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-003f28934bfea4faa137"></a>

**90° CCW: unverified** — `in_game_visible_travel-003f28934bfea4faa137`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-5658af2d317281a1e794"></a>

**180° CCW: unverified** — `in_game_visible_travel-5658af2d317281a1e794`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-c0755caaeef8ca82693e"></a>

**270° CCW: unverified** — `in_game_visible_travel-c0755caaeef8ca82693e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-5135f97300d37145f205"></a>

**0° CCW: unverified** — `in_game_visible_travel-5135f97300d37145f205`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-9fb13003005aee830a95"></a>

**90° CCW: unverified** — `in_game_visible_travel-9fb13003005aee830a95`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-407fa7dfcf6e0c2d4001"></a>

**180° CCW: unverified** — `in_game_visible_travel-407fa7dfcf6e0c2d4001`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-152f57b5643e43ab68e7"></a>

**270° CCW: unverified** — `in_game_visible_travel-152f57b5643e43ab68e7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-17-out; entry: channel-04-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out</summary>

<a id="case-in_game_visible_travel-540a8b5c25e95596b096"></a>

**0° CCW: unverified** — `in_game_visible_travel-540a8b5c25e95596b096`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-d1e4100cbacc02f8f719"></a>

**90° CCW: unverified** — `in_game_visible_travel-d1e4100cbacc02f8f719`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-da0968a9d6b621bb20fa"></a>

**180° CCW: unverified** — `in_game_visible_travel-da0968a9d6b621bb20fa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-71c72c3493ed587c21a6"></a>

**270° CCW: unverified** — `in_game_visible_travel-71c72c3493ed587c21a6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-15-out; entry: channel-05-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-db6586bcbdd417580318"></a>

**0° CCW: unverified** — `in_game_visible_travel-db6586bcbdd417580318`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-71a949aa13b7eaf20766"></a>

**90° CCW: unverified** — `in_game_visible_travel-71a949aa13b7eaf20766`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-fd82126958fefc76cddd"></a>

**180° CCW: unverified** — `in_game_visible_travel-fd82126958fefc76cddd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-8bc979cb4abe54ab4516"></a>

**270° CCW: unverified** — `in_game_visible_travel-8bc979cb4abe54ab4516`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-13-out; entry: channel-06-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-004a6f8a50eb9d0d84d1"></a>

**0° CCW: unverified** — `in_game_visible_travel-004a6f8a50eb9d0d84d1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-5fb0fff4cafd70788e84"></a>

**90° CCW: unverified** — `in_game_visible_travel-5fb0fff4cafd70788e84`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-57bf5796a9b4b31b5347"></a>

**180° CCW: unverified** — `in_game_visible_travel-57bf5796a9b4b31b5347`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-09ca2f3cb653b3885d9a"></a>

**270° CCW: unverified** — `in_game_visible_travel-09ca2f3cb653b3885d9a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-12-out; entry: channel-07-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-829f9ac3e99aecdac0bc"></a>

**0° CCW: unverified** — `in_game_visible_travel-829f9ac3e99aecdac0bc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-8b96ce7bd12bcdd91a74"></a>

**90° CCW: unverified** — `in_game_visible_travel-8b96ce7bd12bcdd91a74`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-80baef04cc7fd3cd4f26"></a>

**180° CCW: unverified** — `in_game_visible_travel-80baef04cc7fd3cd4f26`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-e623d174d9a3a9a8007b"></a>

**270° CCW: unverified** — `in_game_visible_travel-e623d174d9a3a9a8007b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-14-out; entry: channel-08-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-4dc9f7b947d4b0a5af85"></a>

**0° CCW: unverified** — `in_game_visible_travel-4dc9f7b947d4b0a5af85`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-9161cadd6445bd6e8ef1"></a>

**90° CCW: unverified** — `in_game_visible_travel-9161cadd6445bd6e8ef1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-e415b82d84f9e81dd1b2"></a>

**180° CCW: unverified** — `in_game_visible_travel-e415b82d84f9e81dd1b2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-df33937c4dfbc78dc4e6"></a>

**270° CCW: unverified** — `in_game_visible_travel-df33937c4dfbc78dc4e6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-11-out; entry: channel-09-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out</summary>

<a id="case-in_game_visible_travel-4a11fd7029524ca99703"></a>

**0° CCW: unverified** — `in_game_visible_travel-4a11fd7029524ca99703`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-773e7842ad271fd2fa35"></a>

**90° CCW: unverified** — `in_game_visible_travel-773e7842ad271fd2fa35`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-2b32b17f6ed1accee26c"></a>

**180° CCW: unverified** — `in_game_visible_travel-2b32b17f6ed1accee26c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-65f864859b605b012fd9"></a>

**270° CCW: unverified** — `in_game_visible_travel-65f864859b605b012fd9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-20-out; entry: channel-10-in; exit: channel-20-out.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out | — | <a href="#case-in_game_route_query-51ed2712e3b38ee25e6c">[ ] unverified</a> | <a href="#case-in_game_route_query-63449fbddb584dca65d2">[ ] unverified</a> | <a href="#case-in_game_route_query-1449bc8a1ea6b38c3b63">[ ] unverified</a> | <a href="#case-in_game_route_query-7086c54fa2464c4c26c4">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out | — | <a href="#case-in_game_route_query-6ad6c4f14377e790fed5">[ ] unverified</a> | <a href="#case-in_game_route_query-da06eafbc7bcc95a1b92">[ ] unverified</a> | <a href="#case-in_game_route_query-343e192f3ab2d9fdb43b">[ ] unverified</a> | <a href="#case-in_game_route_query-c3147db2d36460165c81">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out</summary>

<a id="case-in_game_route_query-51ed2712e3b38ee25e6c"></a>

**0° CCW: unverified** — `in_game_route_query-51ed2712e3b38ee25e6c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-63449fbddb584dca65d2"></a>

**90° CCW: unverified** — `in_game_route_query-63449fbddb584dca65d2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-1449bc8a1ea6b38c3b63"></a>

**180° CCW: unverified** — `in_game_route_query-1449bc8a1ea6b38c3b63`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-7086c54fa2464c4c26c4"></a>

**270° CCW: unverified** — `in_game_route_query-7086c54fa2464c4c26c4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out</summary>

<a id="case-in_game_route_query-6ad6c4f14377e790fed5"></a>

**0° CCW: unverified** — `in_game_route_query-6ad6c4f14377e790fed5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-da06eafbc7bcc95a1b92"></a>

**90° CCW: unverified** — `in_game_route_query-da06eafbc7bcc95a1b92`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-343e192f3ab2d9fdb43b"></a>

**180° CCW: unverified** — `in_game_route_query-343e192f3ab2d9fdb43b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-c3147db2d36460165c81"></a>

**270° CCW: unverified** — `in_game_route_query-c3147db2d36460165c81`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out | — | <a href="#case-in_game_visible_travel-51ed2712e3b38ee25e6c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-63449fbddb584dca65d2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1449bc8a1ea6b38c3b63">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7086c54fa2464c4c26c4">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out | — | <a href="#case-in_game_visible_travel-6ad6c4f14377e790fed5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-da06eafbc7bcc95a1b92">[ ] unverified</a> | <a href="#case-in_game_visible_travel-343e192f3ab2d9fdb43b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c3147db2d36460165c81">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out</summary>

<a id="case-in_game_visible_travel-51ed2712e3b38ee25e6c"></a>

**0° CCW: unverified** — `in_game_visible_travel-51ed2712e3b38ee25e6c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-63449fbddb584dca65d2"></a>

**90° CCW: unverified** — `in_game_visible_travel-63449fbddb584dca65d2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-1449bc8a1ea6b38c3b63"></a>

**180° CCW: unverified** — `in_game_visible_travel-1449bc8a1ea6b38c3b63`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-7086c54fa2464c4c26c4"></a>

**270° CCW: unverified** — `in_game_visible_travel-7086c54fa2464c4c26c4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out</summary>

<a id="case-in_game_visible_travel-6ad6c4f14377e790fed5"></a>

**0° CCW: unverified** — `in_game_visible_travel-6ad6c4f14377e790fed5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-da06eafbc7bcc95a1b92"></a>

**90° CCW: unverified** — `in_game_visible_travel-da06eafbc7bcc95a1b92`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-343e192f3ab2d9fdb43b"></a>

**180° CCW: unverified** — `in_game_visible_travel-343e192f3ab2d9fdb43b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-c3147db2d36460165c81"></a>

**270° CCW: unverified** — `in_game_visible_travel-c3147db2d36460165c81`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 360 cases; unverified: 360</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1bd90a8ae90419a2ba3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f480a780803e3a91f84e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03368b3926e069afd837">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f51a0f63430eaafdb56">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a6860327a6f71b1039d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a9fc713b97106d1c2f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92c47bcc56a292110cb4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e953a207526e05769834">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3260bfc585119d14c085">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d97c59e3d6ed9ea0014">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc96d93ecfa56d1e29b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0cfdfb96156338a3919">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-05fa46f64ae8cd77e33c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5972b6316969a76b677">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3cdb47645108985c2c16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30a4010385f80a490edc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0bea3e8dc9edea2d5a07">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-929c90835545243128a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20ab86edcf8c47079e83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5b6505d30ebe5eda451">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-01408cdbd23ffbc9e15e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73499477edccabbcdb6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4172111b32c393591e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-694e972e5dfd02f3d39e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8771d1a0de9cb18d5b4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f850d321fdf044caf27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55c47bc62337b7c29b91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cbbe3b09575ce1df382">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aabc5d2f9ec020f679d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3037e909ddcb3355510b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d26d85f2425c186110aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f16eec8734a20600caa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5959c56e8e94addd2615">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-566d242806e76afe3274">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65dfed02b4d3fbf99145">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6236954d2175ee2eb77a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3201bde843483f4a7ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b2c85a5cb9bfff753e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce93182f2724f6bd91cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7e4cfc005ec4276c3c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0f6e569d86e179c9df4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f67a35f8b24f64839054">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51b5fedc8b90c66d384c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87fd689f2f117e414aac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7bccd8283407e0267c37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9659b8f9adab21938c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16fb38febda4147e583d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7c07a3964924fa48a4b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4e5073a86246050f04c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d5f38869be4d61ce304">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa3e53ab6a99e62dce51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5eb6a428d995a334fa68">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a64328c16f9028043ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03e67932df4ab61ba191">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f131bcc3795fe013c564">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8d32133a793ccad0b30">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8546b0f024513b8231e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc90bcbecd9487db81dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f78127bae3eaccbeefc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9edc3b6df850be89dceb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2c0c270d3008fb74448d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70d6ba56a71d7542c7fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27ea6d15f7f0e80ac780">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb6a198237c183bf5e8f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-11dc7ca5df5e434b90b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f46e5ca792b331f9d304">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfda55de1826169e1c3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c5095361f3116978832">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-164da9651996996779fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6f5e119fe0b739339eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9eb42e0db169e739b10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea4cc88417ccb13ed286">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f9a5c679fa5ccccc29ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf083dd48d47a479a397">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c930f9d5787fff859ec7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0af981c84817f7f7ef68">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cc0fef22f08cf4cb2529">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c5d224acba82e045111">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57fad74fb1f7b173f114">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a8fd6afe33b4437e13e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c61f1080fb1dac156372">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c907d783c492f6c6f786">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53ee6516c7abc7686ee3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6211070b72f593a625dd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-40ef635d10a73ba724d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65250d36876a42aaa33e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3ee3c15507f750e0bb8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf8d910151ae200c284b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a6cb57de8e84bbee0a4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7594055e53cda87a3ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-651256f06a21a1a2882d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cb3d348eda2a1ba69a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-35143634d8ced064ebb6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2a2f794858ab4c8808f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb518b057a43e15794bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bf2ff18845c7817f702">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e8e80706fc7890c45b18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d79f47d6fdeecb2d491">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9b11ff9aff95810514f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9979681041ba5c8c954">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b4ed8f3b9ce41182aad2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36372d037eef5f282a10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98a2e7ab535c78f25961">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0e582caf155e2d7c2e2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cae9e6dbb0bb509ff1a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-916fa33cce1509b05b0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-597e8d2715f8902d2e5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea9f86248ef999e3ed2a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0fc0fb1b87069b4f0531">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-369142be3d969a7f148e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78d91abb398ae6b2b551">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cceaa5d335e17a40638d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0a1fbaa353dc64eaf41b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea870c3f327952bdb00a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99a209897854264ff498">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f472f649bfb6726d7be">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b10e6a2df866076429bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61affff63a4532c0ca39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4e2a6af23f6924686d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18d3c8352b9a3fa69324">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2c5a6564a85444f518fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b1c695464970c2adfad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed01d61e1b0d2c492443">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1d872ebf9804ed3ec82">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9aae3519cf707f301ef9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82aaac8d1053731e2a36">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-775104c9a45ab62ba3f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b57f9af875e180dc51d3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-50f4ce62bace365d3c10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43c33d70c20720fca309">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0a2523dd9f468d1a00e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6973fd3c735f63edb871">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ebc15120885d58800b84">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23d07d77d8cc9a558fda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-494327096fb22b1c37d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-780798f17b712532a158">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-824c9324b7a399d78a38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a29329c28bca6a66c133">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd0abf393cab9ef167ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-903bbb92eeb64cde2ce4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-11d98b140ec45190438a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1e5bcd3b47b30d05e81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccb2b4283ad388320590">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9951de8a4c2547d113c0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-09bd24c0e1a9306d7800">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e8f517c671dd735387f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f78a0121afa083b6939a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afaad9af30b34ff38f28">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-85b8a711037da8ce006d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dca6e6b6d2ede18b4435">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60f98fd176440608718a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39c90a81a9bf18d8529b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4e4252b4dfc6338ad6ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee0f79e5bfe2d304c361">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b61972b16bed9022f9c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6e25bf5be265fbb91d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-73b91bbf456e046e0693">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74959d3378dd23e5739d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f8bbdcf2e3c2a079ee2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eafab442dbcef99a0619">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d7917c2a42043eb5205b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fed6e3ebbc0a6a5dcd50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b670444efcf68285c473">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afd232624ccd97b03b9d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b9c5191301ece65e01ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9600244e87bc5e3773b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c081db08eae98af0930f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b6523cd9c7ad99b89c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-080123257346c1b23f53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5f7c80716dc2d8bc5aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-854a15e035c0de2aa24a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba822810b69121cc1465">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f917640dba8c9f4d9aec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0b88fbf532db7b5e05b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a4d2fd16033208a299e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a8577970fa2a96c1b09">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b8ea2da307ff7b42cc5b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acb2b6aa59aa1ab94d1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20bf346e139d2002d002">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8d463e243ab5aad7520">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-250d11d142c844a89dee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40b3cbdb6712acd15f78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfffc287cd3181b053b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5654108685d9086e4a0f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-336baed47ed59616e057">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef31a0ecdef794d32bda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-975edf249c02520ba75c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e74f620a06b4f79d3f5c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-af087a283cc185cc27d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b976249e5c059472ee95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25bc6cae0adbd071684b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70ea92ae019917fb5e1e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-87e8605e174706f65100">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5af0cd44a412db4e6a3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3e569d712b092bec52b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e399195466804d052365">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-14e7e1066f3ff9f4c767">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df2963862e8e672fe380">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ee3e97bc731e15f3955">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4f7671c00488535b126">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f1820dcc0190bf33c411">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b24d80cf12f607a2fd59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c0c666b4428e9d94659">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ae2b46bb2614fed53a3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f52931bf337b9e4623f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e43cc677d0b823a0ae47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-280be923ea4067b2c1e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3cc2036b60b277076c2d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aa4f9c53bedd43e0e8b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1875b0a91eb9faeb6037">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5b375d451d9940676ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5b58a50a7dbe6ea2cd7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d65ea8bada569310a98c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c25d7da8ff99aa27437d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b03f12a9c228c79efa9f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4828eacaa328980aef02">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-328c7b05fbf844fb831e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df67e4e71bba5ed2b89b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76ff2adf2f12110ae4cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ad2dcc8049ba7b395b6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b0d86bde721de459d39b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-435f47b12a2417b8d9b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c07287bb1f37cf3ad642">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db4aef8ebe9e9f10459d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0111ca869446c1f8cfcf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-517d750b791f33fa276b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a2255a132621ad2e30a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-079cd663877148481a78">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3548f2dacf02693984bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-972e482569b4ee0656d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-101e1d04594c64756f90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0ed286e6714e06ae4e7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ad56cacafc9825886868">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-105a83b977fa0007ff77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58172c2fcbe2bb53a1f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bbec064e511cb97f882">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-71286a4da40b07c7f1e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a4796584a1ade076bcf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e9f1dc56322f6866a2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d9007d6becb3b911086">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-223c5b0c5bbbceaebbe5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a4d12f020664ab73f75">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea11ae9ae77e68f95291">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba65707ce800ff423f74">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b0c1ff6e3bc8cdf302c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0c86a3f0fd5b1497f98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a518750f3d8fe659d5c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42ee8d78952030fc6a1a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d878954c05c19ca1101d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7bbd349b7e94fbcd7431">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a5cf5826bd2df8f564a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d49dd91d9c1ef035c06">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ada9f0dfe1ddcf050827">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3627084cdb904cfc370">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8eebc43d37c76dbec47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98eecab0f5385fef2575">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fa42f67e7bd63c536096">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b316eb6c26e6d796f62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf6f4bd91360cf3e869d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb5bb06b20a246e2e4f9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b7d851ccc943001a8447">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fadfd4cd3b4b1b2b31b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5d5b6393be0228fc12f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8040499398acbfb4081">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-55e199ce74dcfed30084">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78c5d027e18b447d550d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fccb5da23b222afb2a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9e59f4d9e5987e135a6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-370b7746d56a249dc34a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1ba81a883c5ec48766c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a82212c26712b2b36957">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-265eb63ff988f066f9e9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6d2bbfaf81e500c582ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-207f7fafed6c5fdc3d5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e79c6017d0bd18529aa8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34a730332f91a037ae4f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2d1f607e406461d402a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-578a02be7f1ad5f9aedc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb74abb67f7dab57f944">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e3c9930a890624b4d13">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e758bd281c980e4958bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07d4a4b5884cc01a5d1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27c8ff955ead8a109cab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0f291230c0bcefe08f8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e87e4bd11e0eaecbc6f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b50b9aca89e5df68a59a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65a6053dd4a4433a6b26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10381e739b9fc8ae947d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-37a5cc03c9ebdbcf1a05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb162e301b3d94deb13f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b25e7342bdd39801eb9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55a9c70bd489317a774a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d9e09dc5450224473844">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8121aa1864d8f228ee91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f7230649556453f3c58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14b662db17cf32511ee9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4577915363ccd00957ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd2727ff987741d8cfba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f491fa919f373ec65971">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1df3c074001760acc18">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc7545d40ab394d96eea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed3f51b7b5afe5d692db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c6d7044dba5bbd36e5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0049256bf4dc1c12b02b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-002e497e194063aed971">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ee6ba10d6185b20b4b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-252a948f36dbfa25d45e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6332b357f122f28a0ee1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-23b7f6803752e61fc6f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc0fa6f4945662f8e9ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46caa30e862dcf667ae9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c924570059370f80629">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d7cddc9d634faa2055f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9c1d020a4a00887e06f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b8e5c5bff3bea7d5657">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37d8e246021c23b586aa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-524d4c6b6196b21596eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ecf7b299976d0db445c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-657c13af67e424ab495b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8afa089268e06d6f69e3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0a9facf0c0c1df29f4da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eafb52e6bb1d172f8c1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df836ee7a7fe43de2dbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37ebc84c402b13801c53">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e2f0c65d98b71787690">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8cf77d46ce18d90efa1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70ad169a70ea42d906d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-becfff8e71edc87f0840">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-310e2b671f933d78cc4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe4dc88bcc4573dbfa60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5a10a1536d7b95251d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e4ba8fc3d7e0fe792a3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41a400db768853a55b2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0a1ab131ff8a07fe513">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4128e11c6405ed99bf11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-125c069a552b168f6ce8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e8fd7e11ba1a6fa65cec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6abb3e5493d6debf5102">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4c49aecc9f71f7bc45b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-490cd3320c318223a115">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7601424e6f5b4dab86f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2a0fed177434a899f2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0005590fa5273f518f03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab5cc712344f02254a23">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a3354214cf9dc7081c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8f172b2c6b2c9ec70f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2ad111b1a6655abd0a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b55418e7a081dfaa8c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-051380956433ac67d676">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f5093cc297b11702423">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8090032aad75f8e07c12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd2e0f579e1285530d42">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d7398f830bbb48975eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d679a8ed1952ae2e0eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35ee57ef46df43e66619">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eda9d1ed6eb41a8390b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41c3a7610121866570c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63424c08c20cba9cdd22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b87abc4d4aa8c7390370">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5a7cb36e8eaf9b9065e">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1bd90a8ae90419a2ba3d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1bd90a8ae90419a2ba3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f480a780803e3a91f84e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f480a780803e3a91f84e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03368b3926e069afd837"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-03368b3926e069afd837`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f51a0f63430eaafdb56"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5f51a0f63430eaafdb56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a6860327a6f71b1039d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a6860327a6f71b1039d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a9fc713b97106d1c2f9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7a9fc713b97106d1c2f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92c47bcc56a292110cb4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-92c47bcc56a292110cb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e953a207526e05769834"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e953a207526e05769834`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3260bfc585119d14c085"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3260bfc585119d14c085`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d97c59e3d6ed9ea0014"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2d97c59e3d6ed9ea0014`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc96d93ecfa56d1e29b5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc96d93ecfa56d1e29b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0cfdfb96156338a3919"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b0cfdfb96156338a3919`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-05fa46f64ae8cd77e33c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-05fa46f64ae8cd77e33c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5972b6316969a76b677"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b5972b6316969a76b677`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3cdb47645108985c2c16"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3cdb47645108985c2c16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30a4010385f80a490edc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-30a4010385f80a490edc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0bea3e8dc9edea2d5a07"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0bea3e8dc9edea2d5a07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-929c90835545243128a0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-929c90835545243128a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20ab86edcf8c47079e83"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-20ab86edcf8c47079e83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5b6505d30ebe5eda451"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d5b6505d30ebe5eda451`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-01408cdbd23ffbc9e15e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01408cdbd23ffbc9e15e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73499477edccabbcdb6a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-73499477edccabbcdb6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4172111b32c393591e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f4172111b32c393591e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-694e972e5dfd02f3d39e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-694e972e5dfd02f3d39e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8771d1a0de9cb18d5b4d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8771d1a0de9cb18d5b4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f850d321fdf044caf27"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7f850d321fdf044caf27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55c47bc62337b7c29b91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-55c47bc62337b7c29b91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cbbe3b09575ce1df382"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9cbbe3b09575ce1df382`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aabc5d2f9ec020f679d4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aabc5d2f9ec020f679d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3037e909ddcb3355510b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3037e909ddcb3355510b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d26d85f2425c186110aa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d26d85f2425c186110aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f16eec8734a20600caa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8f16eec8734a20600caa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5959c56e8e94addd2615"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5959c56e8e94addd2615`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-566d242806e76afe3274"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-566d242806e76afe3274`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65dfed02b4d3fbf99145"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65dfed02b4d3fbf99145`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6236954d2175ee2eb77a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6236954d2175ee2eb77a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3201bde843483f4a7ff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3201bde843483f4a7ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b2c85a5cb9bfff753e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b2c85a5cb9bfff753e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce93182f2724f6bd91cc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ce93182f2724f6bd91cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7e4cfc005ec4276c3c7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c7e4cfc005ec4276c3c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0f6e569d86e179c9df4d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0f6e569d86e179c9df4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f67a35f8b24f64839054"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f67a35f8b24f64839054`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51b5fedc8b90c66d384c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-51b5fedc8b90c66d384c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87fd689f2f117e414aac"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-87fd689f2f117e414aac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7bccd8283407e0267c37"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7bccd8283407e0267c37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9659b8f9adab21938c5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c9659b8f9adab21938c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16fb38febda4147e583d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-16fb38febda4147e583d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7c07a3964924fa48a4b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e7c07a3964924fa48a4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4e5073a86246050f04c4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e5073a86246050f04c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d5f38869be4d61ce304"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8d5f38869be4d61ce304`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa3e53ab6a99e62dce51"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fa3e53ab6a99e62dce51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5eb6a428d995a334fa68"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5eb6a428d995a334fa68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a64328c16f9028043ad"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a64328c16f9028043ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03e67932df4ab61ba191"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-03e67932df4ab61ba191`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f131bcc3795fe013c564"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f131bcc3795fe013c564`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8d32133a793ccad0b30"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c8d32133a793ccad0b30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8546b0f024513b8231e7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8546b0f024513b8231e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc90bcbecd9487db81dc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fc90bcbecd9487db81dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f78127bae3eaccbeefc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4f78127bae3eaccbeefc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9edc3b6df850be89dceb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9edc3b6df850be89dceb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2c0c270d3008fb74448d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2c0c270d3008fb74448d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70d6ba56a71d7542c7fe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-70d6ba56a71d7542c7fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27ea6d15f7f0e80ac780"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-27ea6d15f7f0e80ac780`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb6a198237c183bf5e8f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bb6a198237c183bf5e8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-11dc7ca5df5e434b90b8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-11dc7ca5df5e434b90b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f46e5ca792b331f9d304"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f46e5ca792b331f9d304`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfda55de1826169e1c3e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dfda55de1826169e1c3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c5095361f3116978832"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c5095361f3116978832`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-164da9651996996779fa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-164da9651996996779fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6f5e119fe0b739339eb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f6f5e119fe0b739339eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9eb42e0db169e739b10"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f9eb42e0db169e739b10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea4cc88417ccb13ed286"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ea4cc88417ccb13ed286`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f9a5c679fa5ccccc29ab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f9a5c679fa5ccccc29ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf083dd48d47a479a397"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf083dd48d47a479a397`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c930f9d5787fff859ec7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c930f9d5787fff859ec7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0af981c84817f7f7ef68"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0af981c84817f7f7ef68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cc0fef22f08cf4cb2529"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cc0fef22f08cf4cb2529`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c5d224acba82e045111"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5c5d224acba82e045111`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57fad74fb1f7b173f114"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-57fad74fb1f7b173f114`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a8fd6afe33b4437e13e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2a8fd6afe33b4437e13e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c61f1080fb1dac156372"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c61f1080fb1dac156372`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c907d783c492f6c6f786"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c907d783c492f6c6f786`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53ee6516c7abc7686ee3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-53ee6516c7abc7686ee3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6211070b72f593a625dd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6211070b72f593a625dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-40ef635d10a73ba724d3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-40ef635d10a73ba724d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65250d36876a42aaa33e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-65250d36876a42aaa33e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3ee3c15507f750e0bb8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a3ee3c15507f750e0bb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf8d910151ae200c284b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bf8d910151ae200c284b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a6cb57de8e84bbee0a4e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a6cb57de8e84bbee0a4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7594055e53cda87a3ae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a7594055e53cda87a3ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-651256f06a21a1a2882d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-651256f06a21a1a2882d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cb3d348eda2a1ba69a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8cb3d348eda2a1ba69a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-35143634d8ced064ebb6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35143634d8ced064ebb6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d2a2f794858ab4c8808f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d2a2f794858ab4c8808f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb518b057a43e15794bb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eb518b057a43e15794bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bf2ff18845c7817f702"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8bf2ff18845c7817f702`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e8e80706fc7890c45b18"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e8e80706fc7890c45b18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d79f47d6fdeecb2d491"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d79f47d6fdeecb2d491`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9b11ff9aff95810514f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e9b11ff9aff95810514f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9979681041ba5c8c954"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e9979681041ba5c8c954`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b4ed8f3b9ce41182aad2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b4ed8f3b9ce41182aad2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36372d037eef5f282a10"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-36372d037eef5f282a10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98a2e7ab535c78f25961"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-98a2e7ab535c78f25961`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0e582caf155e2d7c2e2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e0e582caf155e2d7c2e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cae9e6dbb0bb509ff1a5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cae9e6dbb0bb509ff1a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-916fa33cce1509b05b0d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-916fa33cce1509b05b0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-597e8d2715f8902d2e5a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-597e8d2715f8902d2e5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea9f86248ef999e3ed2a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ea9f86248ef999e3ed2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0fc0fb1b87069b4f0531"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0fc0fb1b87069b4f0531`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-369142be3d969a7f148e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-369142be3d969a7f148e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78d91abb398ae6b2b551"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78d91abb398ae6b2b551`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cceaa5d335e17a40638d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cceaa5d335e17a40638d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0a1fbaa353dc64eaf41b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a1fbaa353dc64eaf41b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea870c3f327952bdb00a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ea870c3f327952bdb00a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99a209897854264ff498"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-99a209897854264ff498`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f472f649bfb6726d7be"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6f472f649bfb6726d7be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b10e6a2df866076429bf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b10e6a2df866076429bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61affff63a4532c0ca39"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-61affff63a4532c0ca39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4e2a6af23f6924686d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d4e2a6af23f6924686d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18d3c8352b9a3fa69324"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-18d3c8352b9a3fa69324`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2c5a6564a85444f518fa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2c5a6564a85444f518fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b1c695464970c2adfad"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0b1c695464970c2adfad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed01d61e1b0d2c492443"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed01d61e1b0d2c492443`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1d872ebf9804ed3ec82"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b1d872ebf9804ed3ec82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9aae3519cf707f301ef9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9aae3519cf707f301ef9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82aaac8d1053731e2a36"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-82aaac8d1053731e2a36`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-775104c9a45ab62ba3f2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-775104c9a45ab62ba3f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b57f9af875e180dc51d3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b57f9af875e180dc51d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-50f4ce62bace365d3c10"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-50f4ce62bace365d3c10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43c33d70c20720fca309"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-43c33d70c20720fca309`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0a2523dd9f468d1a00e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b0a2523dd9f468d1a00e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6973fd3c735f63edb871"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6973fd3c735f63edb871`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ebc15120885d58800b84"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ebc15120885d58800b84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23d07d77d8cc9a558fda"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-23d07d77d8cc9a558fda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-494327096fb22b1c37d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-494327096fb22b1c37d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-780798f17b712532a158"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-780798f17b712532a158`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-824c9324b7a399d78a38"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-824c9324b7a399d78a38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a29329c28bca6a66c133"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a29329c28bca6a66c133`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd0abf393cab9ef167ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cd0abf393cab9ef167ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-903bbb92eeb64cde2ce4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-903bbb92eeb64cde2ce4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-11d98b140ec45190438a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-11d98b140ec45190438a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1e5bcd3b47b30d05e81"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c1e5bcd3b47b30d05e81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccb2b4283ad388320590"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ccb2b4283ad388320590`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9951de8a4c2547d113c0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9951de8a4c2547d113c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-09bd24c0e1a9306d7800"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-09bd24c0e1a9306d7800`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e8f517c671dd735387f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6e8f517c671dd735387f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f78a0121afa083b6939a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f78a0121afa083b6939a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afaad9af30b34ff38f28"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afaad9af30b34ff38f28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-85b8a711037da8ce006d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-85b8a711037da8ce006d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dca6e6b6d2ede18b4435"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dca6e6b6d2ede18b4435`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60f98fd176440608718a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-60f98fd176440608718a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39c90a81a9bf18d8529b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39c90a81a9bf18d8529b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4e4252b4dfc6338ad6ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e4252b4dfc6338ad6ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee0f79e5bfe2d304c361"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ee0f79e5bfe2d304c361`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b61972b16bed9022f9c7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b61972b16bed9022f9c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6e25bf5be265fbb91d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e6e25bf5be265fbb91d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-73b91bbf456e046e0693"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-73b91bbf456e046e0693`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74959d3378dd23e5739d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74959d3378dd23e5739d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f8bbdcf2e3c2a079ee2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6f8bbdcf2e3c2a079ee2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eafab442dbcef99a0619"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eafab442dbcef99a0619`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d7917c2a42043eb5205b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d7917c2a42043eb5205b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fed6e3ebbc0a6a5dcd50"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fed6e3ebbc0a6a5dcd50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b670444efcf68285c473"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b670444efcf68285c473`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afd232624ccd97b03b9d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afd232624ccd97b03b9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b9c5191301ece65e01ab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b9c5191301ece65e01ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9600244e87bc5e3773b1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9600244e87bc5e3773b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c081db08eae98af0930f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c081db08eae98af0930f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b6523cd9c7ad99b89c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b6523cd9c7ad99b89c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-080123257346c1b23f53"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-080123257346c1b23f53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5f7c80716dc2d8bc5aa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e5f7c80716dc2d8bc5aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-854a15e035c0de2aa24a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-854a15e035c0de2aa24a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba822810b69121cc1465"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ba822810b69121cc1465`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f917640dba8c9f4d9aec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f917640dba8c9f4d9aec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0b88fbf532db7b5e05b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0b88fbf532db7b5e05b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a4d2fd16033208a299e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4a4d2fd16033208a299e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a8577970fa2a96c1b09"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a8577970fa2a96c1b09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b8ea2da307ff7b42cc5b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8ea2da307ff7b42cc5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acb2b6aa59aa1ab94d1f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-acb2b6aa59aa1ab94d1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20bf346e139d2002d002"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-20bf346e139d2002d002`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8d463e243ab5aad7520"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8d463e243ab5aad7520`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-250d11d142c844a89dee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-250d11d142c844a89dee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40b3cbdb6712acd15f78"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-40b3cbdb6712acd15f78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfffc287cd3181b053b5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dfffc287cd3181b053b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5654108685d9086e4a0f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5654108685d9086e4a0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-336baed47ed59616e057"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-336baed47ed59616e057`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef31a0ecdef794d32bda"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef31a0ecdef794d32bda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-975edf249c02520ba75c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-975edf249c02520ba75c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e74f620a06b4f79d3f5c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e74f620a06b4f79d3f5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-af087a283cc185cc27d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-af087a283cc185cc27d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b976249e5c059472ee95"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b976249e5c059472ee95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25bc6cae0adbd071684b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-25bc6cae0adbd071684b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70ea92ae019917fb5e1e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-70ea92ae019917fb5e1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-87e8605e174706f65100"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-87e8605e174706f65100`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5af0cd44a412db4e6a3a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5af0cd44a412db4e6a3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3e569d712b092bec52b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b3e569d712b092bec52b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e399195466804d052365"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e399195466804d052365`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-14e7e1066f3ff9f4c767"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-14e7e1066f3ff9f4c767`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df2963862e8e672fe380"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-df2963862e8e672fe380`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ee3e97bc731e15f3955"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5ee3e97bc731e15f3955`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4f7671c00488535b126"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c4f7671c00488535b126`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f1820dcc0190bf33c411"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f1820dcc0190bf33c411`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b24d80cf12f607a2fd59"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b24d80cf12f607a2fd59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c0c666b4428e9d94659"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7c0c666b4428e9d94659`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ae2b46bb2614fed53a3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ae2b46bb2614fed53a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f52931bf337b9e4623f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f52931bf337b9e4623f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e43cc677d0b823a0ae47"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e43cc677d0b823a0ae47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-280be923ea4067b2c1e0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-280be923ea4067b2c1e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3cc2036b60b277076c2d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3cc2036b60b277076c2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aa4f9c53bedd43e0e8b8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aa4f9c53bedd43e0e8b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1875b0a91eb9faeb6037"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1875b0a91eb9faeb6037`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5b375d451d9940676ca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f5b375d451d9940676ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5b58a50a7dbe6ea2cd7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c5b58a50a7dbe6ea2cd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d65ea8bada569310a98c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d65ea8bada569310a98c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c25d7da8ff99aa27437d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c25d7da8ff99aa27437d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b03f12a9c228c79efa9f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b03f12a9c228c79efa9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4828eacaa328980aef02"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4828eacaa328980aef02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-328c7b05fbf844fb831e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-328c7b05fbf844fb831e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df67e4e71bba5ed2b89b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-df67e4e71bba5ed2b89b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76ff2adf2f12110ae4cb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-76ff2adf2f12110ae4cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ad2dcc8049ba7b395b6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8ad2dcc8049ba7b395b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b0d86bde721de459d39b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0d86bde721de459d39b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-435f47b12a2417b8d9b2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-435f47b12a2417b8d9b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c07287bb1f37cf3ad642"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c07287bb1f37cf3ad642`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db4aef8ebe9e9f10459d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-db4aef8ebe9e9f10459d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0111ca869446c1f8cfcf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0111ca869446c1f8cfcf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-517d750b791f33fa276b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-517d750b791f33fa276b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a2255a132621ad2e30a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2a2255a132621ad2e30a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-079cd663877148481a78"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-079cd663877148481a78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3548f2dacf02693984bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3548f2dacf02693984bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-972e482569b4ee0656d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-972e482569b4ee0656d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-101e1d04594c64756f90"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-101e1d04594c64756f90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0ed286e6714e06ae4e7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e0ed286e6714e06ae4e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ad56cacafc9825886868"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad56cacafc9825886868`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-105a83b977fa0007ff77"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-105a83b977fa0007ff77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58172c2fcbe2bb53a1f8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-58172c2fcbe2bb53a1f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bbec064e511cb97f882"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6bbec064e511cb97f882`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-71286a4da40b07c7f1e9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-71286a4da40b07c7f1e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a4796584a1ade076bcf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a4796584a1ade076bcf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e9f1dc56322f6866a2c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4e9f1dc56322f6866a2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d9007d6becb3b911086"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3d9007d6becb3b911086`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-223c5b0c5bbbceaebbe5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-223c5b0c5bbbceaebbe5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a4d12f020664ab73f75"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5a4d12f020664ab73f75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea11ae9ae77e68f95291"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ea11ae9ae77e68f95291`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba65707ce800ff423f74"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ba65707ce800ff423f74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b0c1ff6e3bc8cdf302c4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0c1ff6e3bc8cdf302c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0c86a3f0fd5b1497f98"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d0c86a3f0fd5b1497f98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a518750f3d8fe659d5c8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a518750f3d8fe659d5c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42ee8d78952030fc6a1a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-42ee8d78952030fc6a1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d878954c05c19ca1101d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d878954c05c19ca1101d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7bbd349b7e94fbcd7431"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7bbd349b7e94fbcd7431`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a5cf5826bd2df8f564a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1a5cf5826bd2df8f564a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d49dd91d9c1ef035c06"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6d49dd91d9c1ef035c06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ada9f0dfe1ddcf050827"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ada9f0dfe1ddcf050827`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3627084cdb904cfc370"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f3627084cdb904cfc370`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8eebc43d37c76dbec47"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b8eebc43d37c76dbec47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98eecab0f5385fef2575"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-98eecab0f5385fef2575`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fa42f67e7bd63c536096"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fa42f67e7bd63c536096`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b316eb6c26e6d796f62"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1b316eb6c26e6d796f62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf6f4bd91360cf3e869d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bf6f4bd91360cf3e869d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb5bb06b20a246e2e4f9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cb5bb06b20a246e2e4f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b7d851ccc943001a8447"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b7d851ccc943001a8447`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fadfd4cd3b4b1b2b31b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8fadfd4cd3b4b1b2b31b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5d5b6393be0228fc12f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d5d5b6393be0228fc12f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8040499398acbfb4081"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8040499398acbfb4081`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-55e199ce74dcfed30084"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-55e199ce74dcfed30084`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78c5d027e18b447d550d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-78c5d027e18b447d550d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fccb5da23b222afb2a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8fccb5da23b222afb2a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9e59f4d9e5987e135a6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f9e59f4d9e5987e135a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-370b7746d56a249dc34a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-370b7746d56a249dc34a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1ba81a883c5ec48766c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e1ba81a883c5ec48766c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a82212c26712b2b36957"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a82212c26712b2b36957`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-265eb63ff988f066f9e9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-265eb63ff988f066f9e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6d2bbfaf81e500c582ef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6d2bbfaf81e500c582ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-207f7fafed6c5fdc3d5a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-207f7fafed6c5fdc3d5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e79c6017d0bd18529aa8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e79c6017d0bd18529aa8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34a730332f91a037ae4f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-34a730332f91a037ae4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2d1f607e406461d402a5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2d1f607e406461d402a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-578a02be7f1ad5f9aedc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-578a02be7f1ad5f9aedc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb74abb67f7dab57f944"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fb74abb67f7dab57f944`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e3c9930a890624b4d13"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2e3c9930a890624b4d13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e758bd281c980e4958bf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e758bd281c980e4958bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07d4a4b5884cc01a5d1c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-07d4a4b5884cc01a5d1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27c8ff955ead8a109cab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-27c8ff955ead8a109cab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0f291230c0bcefe08f8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f0f291230c0bcefe08f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e87e4bd11e0eaecbc6f3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e87e4bd11e0eaecbc6f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b50b9aca89e5df68a59a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b50b9aca89e5df68a59a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65a6053dd4a4433a6b26"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65a6053dd4a4433a6b26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10381e739b9fc8ae947d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10381e739b9fc8ae947d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-37a5cc03c9ebdbcf1a05"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-37a5cc03c9ebdbcf1a05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb162e301b3d94deb13f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cb162e301b3d94deb13f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b25e7342bdd39801eb9d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b25e7342bdd39801eb9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55a9c70bd489317a774a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-55a9c70bd489317a774a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d9e09dc5450224473844"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d9e09dc5450224473844`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8121aa1864d8f228ee91"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8121aa1864d8f228ee91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f7230649556453f3c58"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f7230649556453f3c58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14b662db17cf32511ee9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-14b662db17cf32511ee9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4577915363ccd00957ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4577915363ccd00957ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd2727ff987741d8cfba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dd2727ff987741d8cfba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f491fa919f373ec65971"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f491fa919f373ec65971`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1df3c074001760acc18"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f1df3c074001760acc18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc7545d40ab394d96eea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc7545d40ab394d96eea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed3f51b7b5afe5d692db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ed3f51b7b5afe5d692db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c6d7044dba5bbd36e5a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1c6d7044dba5bbd36e5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0049256bf4dc1c12b02b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0049256bf4dc1c12b02b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-002e497e194063aed971"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-002e497e194063aed971`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ee6ba10d6185b20b4b5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ee6ba10d6185b20b4b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-252a948f36dbfa25d45e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-252a948f36dbfa25d45e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6332b357f122f28a0ee1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6332b357f122f28a0ee1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-23b7f6803752e61fc6f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-23b7f6803752e61fc6f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc0fa6f4945662f8e9ff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dc0fa6f4945662f8e9ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46caa30e862dcf667ae9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-46caa30e862dcf667ae9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c924570059370f80629"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9c924570059370f80629`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d7cddc9d634faa2055f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d7cddc9d634faa2055f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9c1d020a4a00887e06f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e9c1d020a4a00887e06f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b8e5c5bff3bea7d5657"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5b8e5c5bff3bea7d5657`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37d8e246021c23b586aa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-37d8e246021c23b586aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-524d4c6b6196b21596eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-524d4c6b6196b21596eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ecf7b299976d0db445c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ecf7b299976d0db445c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-657c13af67e424ab495b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-657c13af67e424ab495b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8afa089268e06d6f69e3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8afa089268e06d6f69e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0a9facf0c0c1df29f4da"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a9facf0c0c1df29f4da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eafb52e6bb1d172f8c1a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eafb52e6bb1d172f8c1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df836ee7a7fe43de2dbd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-df836ee7a7fe43de2dbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37ebc84c402b13801c53"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-37ebc84c402b13801c53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e2f0c65d98b71787690"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e2f0c65d98b71787690`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8cf77d46ce18d90efa1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b8cf77d46ce18d90efa1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70ad169a70ea42d906d3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-70ad169a70ea42d906d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-becfff8e71edc87f0840"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-becfff8e71edc87f0840`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-310e2b671f933d78cc4f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-310e2b671f933d78cc4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe4dc88bcc4573dbfa60"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fe4dc88bcc4573dbfa60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5a10a1536d7b95251d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b5a10a1536d7b95251d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e4ba8fc3d7e0fe792a3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3e4ba8fc3d7e0fe792a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41a400db768853a55b2c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41a400db768853a55b2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0a1ab131ff8a07fe513"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0a1ab131ff8a07fe513`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4128e11c6405ed99bf11"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4128e11c6405ed99bf11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-125c069a552b168f6ce8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-125c069a552b168f6ce8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e8fd7e11ba1a6fa65cec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e8fd7e11ba1a6fa65cec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6abb3e5493d6debf5102"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6abb3e5493d6debf5102`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4c49aecc9f71f7bc45b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f4c49aecc9f71f7bc45b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-490cd3320c318223a115"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-490cd3320c318223a115`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7601424e6f5b4dab86f3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7601424e6f5b4dab86f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2a0fed177434a899f2c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e2a0fed177434a899f2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0005590fa5273f518f03"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0005590fa5273f518f03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab5cc712344f02254a23"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab5cc712344f02254a23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a3354214cf9dc7081c4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a3354214cf9dc7081c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8f172b2c6b2c9ec70f7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d8f172b2c6b2c9ec70f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2ad111b1a6655abd0a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b2ad111b1a6655abd0a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b55418e7a081dfaa8c2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8b55418e7a081dfaa8c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-051380956433ac67d676"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-051380956433ac67d676`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f5093cc297b11702423"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5f5093cc297b11702423`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8090032aad75f8e07c12"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8090032aad75f8e07c12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd2e0f579e1285530d42"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fd2e0f579e1285530d42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d7398f830bbb48975eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d7398f830bbb48975eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d679a8ed1952ae2e0eb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3d679a8ed1952ae2e0eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35ee57ef46df43e66619"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-35ee57ef46df43e66619`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eda9d1ed6eb41a8390b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eda9d1ed6eb41a8390b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41c3a7610121866570c5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41c3a7610121866570c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63424c08c20cba9cdd22"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-63424c08c20cba9cdd22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b87abc4d4aa8c7390370"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b87abc4d4aa8c7390370`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5a7cb36e8eaf9b9065e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b5a7cb36e8eaf9b9065e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ac568c11582a42f5ef65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6473d0028a30ebc81c0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-684337b52a5607d6b2e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb63f843d49afde6131f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9a3e17e58446872ffa7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c246a0fac7a1210a97d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8a74e0627317f1e6823">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a55a6c5513b50fefc7f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-350ea170251738be922b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4c2c07ed8f15f777010">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3ebf70f478be28efab5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b84a3b9cd82dad349425">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a3a35c15e80c32d55e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d405d9b5a4ff6ce0593">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-593f869951da5e50b582">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5cb94693f26e5fbc5fb1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d52ebc21277fab52fc25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c68b8cb6d61707092dbe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49e250fd49489620df08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-807a6d96d9394f96332d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-390969abbc5da468c29b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8c39934b96941f10e88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e4def0ed5487c8cbe12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a1b8e38b195e9c2a8c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d6e19705bfaca243918">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b56dd701753674575657">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf738750ac99afa282ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58d0f6c696bf8b604a33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c0e4468c04a1a0cf5801">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e9eeb0d4d8b4b1eeaa7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d617d3ba238b5a8b64f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d67d18e330592e0933e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-84bba4c2f07b6256b8ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c25eb5b421a9a38aeac5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d6626323eebaa8007bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7bffff8af88a32b8c568">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9ee76821369dc09c085e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07868e2f98aeea3c0751">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f08a74259285f6856dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80c3ed6f328fbf1344af">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0037745e9939bfc28ad8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa22d2ada248c9a929f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ae333a453b586f9caad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e542b00c9c3d70b6774b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-527003334f6838406ff9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4fa2f882804bae6eb1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-507752a9d6d3cccfb9c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5047104da83dc74628fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5e41eba0f1ce3d7d7112">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67f38fc68626c4d56ba6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-653081998e63d0e38c8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c65a24652c2375835730">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8b817a4ee7294ab1775e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53a5a68dd9bad75671bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0eadf2503074fee83a32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e403ba5228c00e2328a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b7f0f93c573f7e82f591">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d78cc5c7f13907f37285">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b985595df7582ae619e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e3f601903a278dbb6b7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c26bc7bb95fff0845528">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ea317436f7392e039b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88b213e34c1842fcb187">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4da850ec714f3458d5c5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c2b5ec79561418f11857">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-711485fc5a52482ee2cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14cf73cebc08c5b48a4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-961f39c0029c187fdf33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-655a30c3f96c7732cc40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d7636a4c016a7788087">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b317904b5c11bd92552">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4219ee0ef16fccdb3f6c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-28bb63b272b514b4212d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c8841c4ed5c028c880d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acaa3260c77fb5560a8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de8351ed80d859254c5b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-45947b5bcaf52c8419f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53a3658276efb76d2293">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c273e5f27617339b38c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98cef14217332232e157">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ac568c11582a42f5ef65"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac568c11582a42f5ef65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6473d0028a30ebc81c0c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6473d0028a30ebc81c0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-684337b52a5607d6b2e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-684337b52a5607d6b2e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb63f843d49afde6131f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bb63f843d49afde6131f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9a3e17e58446872ffa7f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9a3e17e58446872ffa7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c246a0fac7a1210a97d5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c246a0fac7a1210a97d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8a74e0627317f1e6823"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d8a74e0627317f1e6823`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a55a6c5513b50fefc7f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4a55a6c5513b50fefc7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-350ea170251738be922b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-350ea170251738be922b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4c2c07ed8f15f777010"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e4c2c07ed8f15f777010`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3ebf70f478be28efab5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c3ebf70f478be28efab5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b84a3b9cd82dad349425"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b84a3b9cd82dad349425`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a3a35c15e80c32d55e1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a3a35c15e80c32d55e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d405d9b5a4ff6ce0593"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1d405d9b5a4ff6ce0593`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-593f869951da5e50b582"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-593f869951da5e50b582`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5cb94693f26e5fbc5fb1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5cb94693f26e5fbc5fb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d52ebc21277fab52fc25"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d52ebc21277fab52fc25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c68b8cb6d61707092dbe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c68b8cb6d61707092dbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49e250fd49489620df08"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-49e250fd49489620df08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-807a6d96d9394f96332d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-807a6d96d9394f96332d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-390969abbc5da468c29b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-390969abbc5da468c29b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8c39934b96941f10e88"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c8c39934b96941f10e88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e4def0ed5487c8cbe12"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0e4def0ed5487c8cbe12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a1b8e38b195e9c2a8c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2a1b8e38b195e9c2a8c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d6e19705bfaca243918"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d6e19705bfaca243918`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b56dd701753674575657"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b56dd701753674575657`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf738750ac99afa282ff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cf738750ac99afa282ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58d0f6c696bf8b604a33"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-58d0f6c696bf8b604a33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c0e4468c04a1a0cf5801"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c0e4468c04a1a0cf5801`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e9eeb0d4d8b4b1eeaa7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2e9eeb0d4d8b4b1eeaa7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d617d3ba238b5a8b64f4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d617d3ba238b5a8b64f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d67d18e330592e0933e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1d67d18e330592e0933e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-84bba4c2f07b6256b8ce"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-84bba4c2f07b6256b8ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c25eb5b421a9a38aeac5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c25eb5b421a9a38aeac5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d6626323eebaa8007bf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4d6626323eebaa8007bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7bffff8af88a32b8c568"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7bffff8af88a32b8c568`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9ee76821369dc09c085e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9ee76821369dc09c085e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07868e2f98aeea3c0751"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-07868e2f98aeea3c0751`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f08a74259285f6856dd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5f08a74259285f6856dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80c3ed6f328fbf1344af"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-80c3ed6f328fbf1344af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0037745e9939bfc28ad8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0037745e9939bfc28ad8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa22d2ada248c9a929f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa22d2ada248c9a929f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ae333a453b586f9caad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ae333a453b586f9caad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e542b00c9c3d70b6774b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e542b00c9c3d70b6774b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-527003334f6838406ff9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-527003334f6838406ff9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4fa2f882804bae6eb1a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d4fa2f882804bae6eb1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-507752a9d6d3cccfb9c6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-507752a9d6d3cccfb9c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5047104da83dc74628fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5047104da83dc74628fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5e41eba0f1ce3d7d7112"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5e41eba0f1ce3d7d7112`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67f38fc68626c4d56ba6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67f38fc68626c4d56ba6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-653081998e63d0e38c8f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-653081998e63d0e38c8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c65a24652c2375835730"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c65a24652c2375835730`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8b817a4ee7294ab1775e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8b817a4ee7294ab1775e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53a5a68dd9bad75671bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-53a5a68dd9bad75671bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0eadf2503074fee83a32"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0eadf2503074fee83a32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e403ba5228c00e2328a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e403ba5228c00e2328a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b7f0f93c573f7e82f591"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b7f0f93c573f7e82f591`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d78cc5c7f13907f37285"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d78cc5c7f13907f37285`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b985595df7582ae619e4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b985595df7582ae619e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e3f601903a278dbb6b7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e3f601903a278dbb6b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c26bc7bb95fff0845528"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c26bc7bb95fff0845528`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ea317436f7392e039b9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ea317436f7392e039b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88b213e34c1842fcb187"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-88b213e34c1842fcb187`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4da850ec714f3458d5c5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4da850ec714f3458d5c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c2b5ec79561418f11857"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c2b5ec79561418f11857`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-711485fc5a52482ee2cb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-711485fc5a52482ee2cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14cf73cebc08c5b48a4f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-14cf73cebc08c5b48a4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-961f39c0029c187fdf33"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-961f39c0029c187fdf33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-655a30c3f96c7732cc40"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-655a30c3f96c7732cc40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d7636a4c016a7788087"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3d7636a4c016a7788087`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b317904b5c11bd92552"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8b317904b5c11bd92552`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4219ee0ef16fccdb3f6c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4219ee0ef16fccdb3f6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-28bb63b272b514b4212d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-28bb63b272b514b4212d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c8841c4ed5c028c880d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1c8841c4ed5c028c880d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acaa3260c77fb5560a8b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-acaa3260c77fb5560a8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de8351ed80d859254c5b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de8351ed80d859254c5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-45947b5bcaf52c8419f7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-45947b5bcaf52c8419f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53a3658276efb76d2293"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-53a3658276efb76d2293`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c273e5f27617339b38c0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c273e5f27617339b38c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98cef14217332232e157"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-98cef14217332232e157`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c51c66bad1e29465fa3b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1db1c08d72869e238716">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fce664983160f1bb368">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4d03c0fecaf96f71553">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c196711f8f2547f9e56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f29d78d29c8655866986">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57b280ad88fc99782334">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-259659ae365358d3c58f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-460c5a1c7736a562b9f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2be3504810604d69ea3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45dc911bddbb79da4ba1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2d70f746e7d299dd55c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0f0b4fc51701dde52690">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd646bcd3da608df768e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ebc3248356e42513607">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-601a37ed84b407dd3e4f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2b7e28d745281284d534">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c9d0b039c031f391917">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b20d9abddee1ea71b702">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-591ecc9592f6afd5ffb0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d2509eee63be96e477b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f242159d1f13fa1dbfc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47cea22fea5e38ed248c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0c18768b2a46bcfc8d5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-adcaf40bceeb125ce3f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3883542b3b64ab3b8dba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-821d4a5c5a071834c7d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c46b9926b1887896acf2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5eb6bd2b1af1c0dd9447">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07d17b075c84e37cb3be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b26f7eefd3f415f0069">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-778ccf9b517bcdb855d6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-338e9b36dfdc6c9c29ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78a7a5c994730efc5339">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-992250ca6c98a25581b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03dce7a2c324829324bd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ed32e6175114821afc49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a50d62e6eed9cc103a87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3215cc09703d58f1ce65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9c4ba66e742bf268430">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6c3ada90a709c8d480e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0060325554e93c8bf8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6b58bdf26ed2b199e4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9c9ec2656d1cc42306c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d33e50d3e18539ff5659">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d320e881b7cacd1c01d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-003e3f24c7a50f9bba91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f03fde15002ed8f4a3b0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-617aa39ddba7ec95c2c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4fa966f60db7f0d07693">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-622991b53ad80ed48bbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a72d0f22da2286c68678">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7eb5172dd1183321ee0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e22181aa36d1f45334a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b335cc1f3bc40349a183">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce5ee7e482e2650af351">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2526912e455e82ac5823">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7eb0bc079766fa5b9c39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f89f17a8f8f1147780ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ceddf74625640e4ad28">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ba57b6361c551a5f476d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bcf029de238339c5e16f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f22ec40a9853239dba64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfa946719ce01383ed43">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9c9e668887490c4a3f39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d1f5b8818d582e2b834">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83d2dfa6d27f9ce2aede">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5703c3cfea14611b1494">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-271f41fe284bd3b5265a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0d5a2ca71450e20998a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a1f89684af36e9044b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8963b26a68bb68d44143">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-88a381ff5b7bc49c5be9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62ced873421be46f4412">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e5e0d31675ff6791bc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e9470440e1b1c6ce9f5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a835b8ce197650077358">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b78f4cd5adcb709e375">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10f52bbb72af866da985">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-825e7baf665fbaf36d11">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c51c66bad1e29465fa3b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c51c66bad1e29465fa3b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1db1c08d72869e238716"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1db1c08d72869e238716`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fce664983160f1bb368"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1fce664983160f1bb368`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4d03c0fecaf96f71553"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e4d03c0fecaf96f71553`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c196711f8f2547f9e56"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c196711f8f2547f9e56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f29d78d29c8655866986"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f29d78d29c8655866986`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57b280ad88fc99782334"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-57b280ad88fc99782334`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-259659ae365358d3c58f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-259659ae365358d3c58f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-460c5a1c7736a562b9f2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-460c5a1c7736a562b9f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2be3504810604d69ea3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e2be3504810604d69ea3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45dc911bddbb79da4ba1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-45dc911bddbb79da4ba1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d2d70f746e7d299dd55c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d2d70f746e7d299dd55c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0f0b4fc51701dde52690"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0f0b4fc51701dde52690`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd646bcd3da608df768e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd646bcd3da608df768e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ebc3248356e42513607"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ebc3248356e42513607`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-601a37ed84b407dd3e4f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-601a37ed84b407dd3e4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2b7e28d745281284d534"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2b7e28d745281284d534`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c9d0b039c031f391917"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0c9d0b039c031f391917`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b20d9abddee1ea71b702"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b20d9abddee1ea71b702`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-591ecc9592f6afd5ffb0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-591ecc9592f6afd5ffb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d2509eee63be96e477b0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d2509eee63be96e477b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f242159d1f13fa1dbfc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6f242159d1f13fa1dbfc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47cea22fea5e38ed248c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-47cea22fea5e38ed248c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0c18768b2a46bcfc8d5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a0c18768b2a46bcfc8d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-adcaf40bceeb125ce3f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-adcaf40bceeb125ce3f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3883542b3b64ab3b8dba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3883542b3b64ab3b8dba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-821d4a5c5a071834c7d4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-821d4a5c5a071834c7d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c46b9926b1887896acf2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c46b9926b1887896acf2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5eb6bd2b1af1c0dd9447"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5eb6bd2b1af1c0dd9447`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07d17b075c84e37cb3be"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-07d17b075c84e37cb3be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b26f7eefd3f415f0069"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0b26f7eefd3f415f0069`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-778ccf9b517bcdb855d6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-778ccf9b517bcdb855d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-338e9b36dfdc6c9c29ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-338e9b36dfdc6c9c29ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78a7a5c994730efc5339"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-78a7a5c994730efc5339`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-992250ca6c98a25581b3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-992250ca6c98a25581b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03dce7a2c324829324bd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03dce7a2c324829324bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ed32e6175114821afc49"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ed32e6175114821afc49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a50d62e6eed9cc103a87"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a50d62e6eed9cc103a87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3215cc09703d58f1ce65"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3215cc09703d58f1ce65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9c4ba66e742bf268430"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d9c4ba66e742bf268430`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6c3ada90a709c8d480e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c3ada90a709c8d480e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0060325554e93c8bf8e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d0060325554e93c8bf8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6b58bdf26ed2b199e4b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f6b58bdf26ed2b199e4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9c9ec2656d1cc42306c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d9c9ec2656d1cc42306c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d33e50d3e18539ff5659"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d33e50d3e18539ff5659`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d320e881b7cacd1c01d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3d320e881b7cacd1c01d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-003e3f24c7a50f9bba91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-003e3f24c7a50f9bba91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f03fde15002ed8f4a3b0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f03fde15002ed8f4a3b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-617aa39ddba7ec95c2c0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-617aa39ddba7ec95c2c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4fa966f60db7f0d07693"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4fa966f60db7f0d07693`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-622991b53ad80ed48bbd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-622991b53ad80ed48bbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a72d0f22da2286c68678"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a72d0f22da2286c68678`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7eb5172dd1183321ee0a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7eb5172dd1183321ee0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e22181aa36d1f45334a3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e22181aa36d1f45334a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b335cc1f3bc40349a183"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b335cc1f3bc40349a183`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce5ee7e482e2650af351"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ce5ee7e482e2650af351`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2526912e455e82ac5823"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2526912e455e82ac5823`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7eb0bc079766fa5b9c39"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7eb0bc079766fa5b9c39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f89f17a8f8f1147780ad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f89f17a8f8f1147780ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ceddf74625640e4ad28"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7ceddf74625640e4ad28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ba57b6361c551a5f476d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ba57b6361c551a5f476d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bcf029de238339c5e16f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bcf029de238339c5e16f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f22ec40a9853239dba64"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f22ec40a9853239dba64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfa946719ce01383ed43"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cfa946719ce01383ed43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9c9e668887490c4a3f39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9c9e668887490c4a3f39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d1f5b8818d582e2b834"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0d1f5b8818d582e2b834`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83d2dfa6d27f9ce2aede"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-83d2dfa6d27f9ce2aede`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5703c3cfea14611b1494"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5703c3cfea14611b1494`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-271f41fe284bd3b5265a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-271f41fe284bd3b5265a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0d5a2ca71450e20998a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c0d5a2ca71450e20998a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a1f89684af36e9044b1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5a1f89684af36e9044b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8963b26a68bb68d44143"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8963b26a68bb68d44143`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-88a381ff5b7bc49c5be9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-88a381ff5b7bc49c5be9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62ced873421be46f4412"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-62ced873421be46f4412`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e5e0d31675ff6791bc4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5e5e0d31675ff6791bc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e9470440e1b1c6ce9f5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8e9470440e1b1c6ce9f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a835b8ce197650077358"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a835b8ce197650077358`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b78f4cd5adcb709e375"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b78f4cd5adcb709e375`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10f52bbb72af866da985"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-10f52bbb72af866da985`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-825e7baf665fbaf36d11"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-825e7baf665fbaf36d11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2293b024cdf7ede7262e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d77af82e35663961d82a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b672619ae871f57b927e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-617d7520cab143d3fdcc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-12fbfbe83222e97b6bb5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a6445633d0ecc3953fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-915c3fe309e24dbd01b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e3f99b35565c3255738">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2293b024cdf7ede7262e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2293b024cdf7ede7262e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d77af82e35663961d82a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d77af82e35663961d82a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b672619ae871f57b927e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b672619ae871f57b927e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-617d7520cab143d3fdcc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-617d7520cab143d3fdcc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-12fbfbe83222e97b6bb5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-12fbfbe83222e97b6bb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a6445633d0ecc3953fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2a6445633d0ecc3953fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-915c3fe309e24dbd01b8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-915c3fe309e24dbd01b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e3f99b35565c3255738"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e3f99b35565c3255738`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-crossing:canonical-southeast | <a href="#case-preview_review-91261d50c37a72a1b13f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-crossing:canonical-top | <a href="#case-preview_review-14d52766510d0a1a3941">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-crossing:connection-overview | <a href="#case-preview_review-42bf73329b6756e117fd">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-crossing:canonical-southeast</summary>

<a id="case-preview_review-91261d50c37a72a1b13f"></a>

**General: unverified** — `preview_review-91261d50c37a72a1b13f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-crossing:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-crossing:canonical-top</summary>

<a id="case-preview_review-14d52766510d0a1a3941"></a>

**General: unverified** — `preview_review-14d52766510d0a1a3941`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-crossing:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-crossing:connection-overview</summary>

<a id="case-preview_review-42bf73329b6756e117fd"></a>

**General: unverified** — `preview_review-42bf73329b6756e117fd`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-crossing:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).

The ground-mouth revision narrows terminal asphalt while preserving the 6 m grade interfaces, every saved traffic route, all fifteen permanent types, and the 31-cell construction union. The earlier `ddrhw-parallel-diamond-parts-01` build retains its original wider mouths and its own immutable evidence; the current revision is measured separately as `ddrhw-parallel-diamond-pedestrian-mouths-01`.
