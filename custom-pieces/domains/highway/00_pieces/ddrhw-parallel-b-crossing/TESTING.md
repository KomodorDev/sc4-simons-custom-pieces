---
title: "Testing: DD RHW-4 \u2014 L1/L2 over Avenue L0 \u2014 Diagonal 90\u00b0 \u2014 Parallel \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1/L2 over Avenue L0 — Diagonal 90° — Parallel — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **DD RHW-4 — L1/L2 over Avenue L0 — Diagonal 90° — Parallel — Alignment B**, permanent ID `ddrhw-parallel-b-crossing`, as **P01** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 3 cells inside its 2 × 2 bounding footprint. Ground Avenue at 0 m; lower deck at 7.5 m; upper deck at 15 m. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-11-out` | road / 1 / primary | out | [-8.0, -15.029437, 0.083612]; [-0.7071067811865527, -0.7071067811865424]; 0.115840789 | `path-interface-b5d8c749a9139d051e0c` |
| `channel-01-in` | road / 1 / primary | in | [-4.675154, -8.0, 0.0]; [0.1808805343321008, -0.983505074872384]; 0.0 | `path-interface-ab0dc819ba4c7fec9f5c` |
| `channel-12-out` | road / 1 / primary | out | [-3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-02-in` | road / 1 / primary | in | [-3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-03-in` | road / 1 / primary | in | [-3.2, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-13-out` | road / 1 / primary | out | [3.2, -24.0, 7.5]; [-0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-04-in` | road / 1 / primary | in | [3.2, -24.0, 15.0]; [0.7071067811865475, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-05-in` | road / 1 / primary | in | [3.2, -8.0, 0.0]; [0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-14-out` | road / 1 / primary | out | [8.0, -3.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-15-out` | road / 1 / primary | out | [8.0, 3.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-16-out` | road / 1 / primary | out | [8.0, 4.675154, 0.0]; [-0.983505074872382, 0.1808805343321116]; 0.0 | `path-interface-eb8edd053c1b618ae382` |
| `channel-17-out` | road / 1 / primary | out | [12.8, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `channel-06-in` | road / 1 / primary | in | [15.029437, 8.0, 0.083612]; [-0.7071067811865424, -0.7071067811865527]; -0.115840789 | `path-interface-42edd41fff244415427a` |
| `channel-18-out` | road / 1 / primary | out | [19.2, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `channel-07-in` | road / 1 / primary | in | [24.0, -19.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `channel-08-in` | road / 1 / primary | in | [24.0, -12.8, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `channel-09-in` | road / 1 / primary | in | [24.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-19-out` | road / 1 / primary | out | [24.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-10-in` | road / 1 / primary | in | [24.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-20-out` | road / 1 / primary | out | [24.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-21-in` | pedestrian / 2 / primary | in | [-7.3, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `channel-23-out` | pedestrian / 2 / primary | out | [8.0, 7.3, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `channel-24-out` | pedestrian / 2 / primary | out | [8.7, -24.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `channel-22-in` | pedestrian / 2 / primary | in | [24.0, -8.7, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-11-out` | primary |
| road | `channel-02-in` → `channel-20-out` | primary |
| road | `channel-03-in` → `channel-17-out` | primary |
| road | `channel-04-in` → `channel-19-out` | primary |
| road | `channel-05-in` → `channel-18-out` | primary |
| road | `channel-06-in` → `channel-16-out` | primary |
| road | `channel-07-in` → `channel-14-out` | primary |
| road | `channel-08-in` → `channel-15-out` | primary |
| road | `channel-09-in` → `channel-13-out` | primary |
| road | `channel-10-in` → `channel-12-out` | primary |
| pedestrian | `channel-21-in` → `channel-24-out` | primary |
| pedestrian | `channel-22-in` → `channel-23-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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
| road / `channel-02-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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
| road / `channel-04-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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
| road / `channel-08-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | pedestrian / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | pedestrian / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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
| road / `channel-10-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component owns 3 adaptive Avenue cells. Native ground textures can change with surrounding development, while rotating model props retain this component's non-ground geometry. Its temporary Road helper is local **[0,0]** and is not permanent ownership. Place this crossing before the northwest terminal in the first reference layout, so its empty helper corner remains available. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-crossing
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **1,190 indexed triangles** and **26 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

This type’s complete measured ports, movements, channel associations, and saved-chord witnesses are frozen in the [B accepted connector contract](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/checks/accepted-connector-contracts.jsonc). That source passed the independent saved-resource and whole-assembly checks before extraction; the generated views retain their own freshness requirements. Its precise saved grades and separately retained reviewed and sampled tangents follow the [shared precision convention](../../../../docs/CONNECTOR_METADATA.md#5-matching-procedure-and-evidence). Arbitrary-neighbour matching and game operation remain outside that record.

## 4. Game checks

1. Select this exact B type from its assembly cycle, place a fresh copy at the reference coordinate, and inspect its model, markings, barriers, and supports. Repeat proper construction rotations with Home or End; rotating the camera alone is insufficient.
2. Place the matching B neighbours from the assembly plan, connect the required native approaches, and let new traffic enter. Record Route Query separately from an actual car crossing each required join. Check both through decks wherever this type owns their fragments.
3. For ground Avenue ownership, separately inspect changing pavement appearance and moving pedestrians. A ramp driveway crosses its adjacent pedestrian route; road asphalt at that crossing is distinct from a missing sidewalk elsewhere.
4. At Medium and High shadow quality, inspect all camera views and zoom levels for unwanted custom shadows. The source's no-shadow policy is not an observed game result.
5. Save, quit, reload, and repeat representative joins. In a separate saved copy, demolish this component, inspect neighbouring native tiles and attachments, replace it, and retest.

Use the [shared observation procedure](../../../../docs/TESTING.md#4-record-one-observation), recording the exact candidate, component, orientation, neighbours, and environment. Native draggable joins, occupied-neighbour placement, visible traffic, redraw, demolition, and save/reload remain unverified without a matching human observation.

## 5. Results and known issues

This piece passed its saved-resource checks in the first native B build; its [assembly evidence](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) records the exact candidate and placed-layout scope. Final connector exports and the assembly-menu package retain their own source fingerprints and checks. **Installation and all game observations remain unverified.** The assembly’s [TESTING document](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/TESTING.md) owns the complete layout’s evidence and limits.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-crossing/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-crossing/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-ac43cbf54a8eb207563f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-ac43cbf54a8eb207563f"></a>

**General: unverified** — `software_resources-ac43cbf54a8eb207563f`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-ac43cbf54a8eb207563f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-ac43cbf54a8eb207563f"></a>

**General: unverified** — `software_connectivity-ac43cbf54a8eb207563f`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-750703a675a9a07d952b">[ ] unverified</a> | <a href="#case-in_game_render-2d583c836c19144e2a9e">[ ] unverified</a> | <a href="#case-in_game_render-129b56fdabb011fa0783">[ ] unverified</a> | <a href="#case-in_game_render-218fafc7b32a97adf64e">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-750703a675a9a07d952b"></a>

**0° CCW: unverified** — `in_game_render-750703a675a9a07d952b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2d583c836c19144e2a9e"></a>

**90° CCW: unverified** — `in_game_render-2d583c836c19144e2a9e`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-129b56fdabb011fa0783"></a>

**180° CCW: unverified** — `in_game_render-129b56fdabb011fa0783`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-218fafc7b32a97adf64e"></a>

**270° CCW: unverified** — `in_game_render-218fafc7b32a97adf64e`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-750703a675a9a07d952b">[ ] unverified</a> | <a href="#case-in_game_placement-2d583c836c19144e2a9e">[ ] unverified</a> | <a href="#case-in_game_placement-129b56fdabb011fa0783">[ ] unverified</a> | <a href="#case-in_game_placement-218fafc7b32a97adf64e">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-750703a675a9a07d952b"></a>

**0° CCW: unverified** — `in_game_placement-750703a675a9a07d952b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2d583c836c19144e2a9e"></a>

**90° CCW: unverified** — `in_game_placement-2d583c836c19144e2a9e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-129b56fdabb011fa0783"></a>

**180° CCW: unverified** — `in_game_placement-129b56fdabb011fa0783`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-218fafc7b32a97adf64e"></a>

**270° CCW: unverified** — `in_game_placement-218fafc7b32a97adf64e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-750703a675a9a07d952b">[ ] unverified</a> | <a href="#case-in_game_demolition-2d583c836c19144e2a9e">[ ] unverified</a> | <a href="#case-in_game_demolition-129b56fdabb011fa0783">[ ] unverified</a> | <a href="#case-in_game_demolition-218fafc7b32a97adf64e">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-750703a675a9a07d952b"></a>

**0° CCW: unverified** — `in_game_demolition-750703a675a9a07d952b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2d583c836c19144e2a9e"></a>

**90° CCW: unverified** — `in_game_demolition-2d583c836c19144e2a9e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-129b56fdabb011fa0783"></a>

**180° CCW: unverified** — `in_game_demolition-129b56fdabb011fa0783`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-218fafc7b32a97adf64e"></a>

**270° CCW: unverified** — `in_game_demolition-218fafc7b32a97adf64e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-750703a675a9a07d952b">[ ] unverified</a> | <a href="#case-in_game_save_reload-2d583c836c19144e2a9e">[ ] unverified</a> | <a href="#case-in_game_save_reload-129b56fdabb011fa0783">[ ] unverified</a> | <a href="#case-in_game_save_reload-218fafc7b32a97adf64e">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-750703a675a9a07d952b"></a>

**0° CCW: unverified** — `in_game_save_reload-750703a675a9a07d952b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2d583c836c19144e2a9e"></a>

**90° CCW: unverified** — `in_game_save_reload-2d583c836c19144e2a9e`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-129b56fdabb011fa0783"></a>

**180° CCW: unverified** — `in_game_save_reload-129b56fdabb011fa0783`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-218fafc7b32a97adf64e"></a>

**270° CCW: unverified** — `in_game_save_reload-218fafc7b32a97adf64e`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-3ed43d64fc51a26a2218">[ ] unverified</a> | <a href="#case-in_game_route_query-a5ccc097953d4bcf75f0">[ ] unverified</a> | <a href="#case-in_game_route_query-c417ad50e5d1ad0ea5e5">[ ] unverified</a> | <a href="#case-in_game_route_query-96c16a5ce3e09227a7a4">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out | — | <a href="#case-in_game_route_query-183a5d686495aa64a6e1">[ ] unverified</a> | <a href="#case-in_game_route_query-4b78340fd9a07226f6b8">[ ] unverified</a> | <a href="#case-in_game_route_query-4697ddfbd981bf3644b5">[ ] unverified</a> | <a href="#case-in_game_route_query-73a7872d653c4280ab3d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-88e71ccc8aab417b0087">[ ] unverified</a> | <a href="#case-in_game_route_query-12128938a5a1eaae21f0">[ ] unverified</a> | <a href="#case-in_game_route_query-e2397b5453d1d1b793a8">[ ] unverified</a> | <a href="#case-in_game_route_query-7b6659d6bb1e24f76a29">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-ab20c1b0a1e1a046ccc7">[ ] unverified</a> | <a href="#case-in_game_route_query-ed580217801cc78ff1e7">[ ] unverified</a> | <a href="#case-in_game_route_query-115b356918d33b4e315d">[ ] unverified</a> | <a href="#case-in_game_route_query-bb733292e236ec8888ed">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-dc033f53dc7413a902b9">[ ] unverified</a> | <a href="#case-in_game_route_query-2f7a4007fc56d7b0141d">[ ] unverified</a> | <a href="#case-in_game_route_query-8e645e98b6c55413320a">[ ] unverified</a> | <a href="#case-in_game_route_query-9b25f39541be0400ca15">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-ab880866d38fd312a2e7">[ ] unverified</a> | <a href="#case-in_game_route_query-22737b4f0b1f1649d4cf">[ ] unverified</a> | <a href="#case-in_game_route_query-c1c99ad1ef5af5e71525">[ ] unverified</a> | <a href="#case-in_game_route_query-3515f3e69ec2f1b08bf6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-4cde2ef1cd2dca039820">[ ] unverified</a> | <a href="#case-in_game_route_query-b38084f2c5d23cdb74b2">[ ] unverified</a> | <a href="#case-in_game_route_query-4d38eb7bc791321dead4">[ ] unverified</a> | <a href="#case-in_game_route_query-abe9b332242f4044bfb8">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out | — | <a href="#case-in_game_route_query-da5597f47efcc1396765">[ ] unverified</a> | <a href="#case-in_game_route_query-03592207a787fb2f9a34">[ ] unverified</a> | <a href="#case-in_game_route_query-cdd9975802fa991c8b51">[ ] unverified</a> | <a href="#case-in_game_route_query-43af7ac40cc245b26240">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-a6a3dbc5eff105899381">[ ] unverified</a> | <a href="#case-in_game_route_query-243725df91d490498574">[ ] unverified</a> | <a href="#case-in_game_route_query-b821c0ff7162b9180af9">[ ] unverified</a> | <a href="#case-in_game_route_query-49255ffded85b5dc191d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-ee21873a681de35569ab">[ ] unverified</a> | <a href="#case-in_game_route_query-c96e8302c5eab2154a77">[ ] unverified</a> | <a href="#case-in_game_route_query-cb57c093eb9b0d47ef5b">[ ] unverified</a> | <a href="#case-in_game_route_query-269dc6669ec09370cae3">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-3ed43d64fc51a26a2218"></a>

**0° CCW: unverified** — `in_game_route_query-3ed43d64fc51a26a2218`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-a5ccc097953d4bcf75f0"></a>

**90° CCW: unverified** — `in_game_route_query-a5ccc097953d4bcf75f0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-c417ad50e5d1ad0ea5e5"></a>

**180° CCW: unverified** — `in_game_route_query-c417ad50e5d1ad0ea5e5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-96c16a5ce3e09227a7a4"></a>

**270° CCW: unverified** — `in_game_route_query-96c16a5ce3e09227a7a4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out</summary>

<a id="case-in_game_route_query-183a5d686495aa64a6e1"></a>

**0° CCW: unverified** — `in_game_route_query-183a5d686495aa64a6e1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-4b78340fd9a07226f6b8"></a>

**90° CCW: unverified** — `in_game_route_query-4b78340fd9a07226f6b8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-4697ddfbd981bf3644b5"></a>

**180° CCW: unverified** — `in_game_route_query-4697ddfbd981bf3644b5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-73a7872d653c4280ab3d"></a>

**270° CCW: unverified** — `in_game_route_query-73a7872d653c4280ab3d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-88e71ccc8aab417b0087"></a>

**0° CCW: unverified** — `in_game_route_query-88e71ccc8aab417b0087`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-12128938a5a1eaae21f0"></a>

**90° CCW: unverified** — `in_game_route_query-12128938a5a1eaae21f0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-e2397b5453d1d1b793a8"></a>

**180° CCW: unverified** — `in_game_route_query-e2397b5453d1d1b793a8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-7b6659d6bb1e24f76a29"></a>

**270° CCW: unverified** — `in_game_route_query-7b6659d6bb1e24f76a29`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-ab20c1b0a1e1a046ccc7"></a>

**0° CCW: unverified** — `in_game_route_query-ab20c1b0a1e1a046ccc7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-ed580217801cc78ff1e7"></a>

**90° CCW: unverified** — `in_game_route_query-ed580217801cc78ff1e7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-115b356918d33b4e315d"></a>

**180° CCW: unverified** — `in_game_route_query-115b356918d33b4e315d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-bb733292e236ec8888ed"></a>

**270° CCW: unverified** — `in_game_route_query-bb733292e236ec8888ed`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-dc033f53dc7413a902b9"></a>

**0° CCW: unverified** — `in_game_route_query-dc033f53dc7413a902b9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-2f7a4007fc56d7b0141d"></a>

**90° CCW: unverified** — `in_game_route_query-2f7a4007fc56d7b0141d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-8e645e98b6c55413320a"></a>

**180° CCW: unverified** — `in_game_route_query-8e645e98b6c55413320a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-9b25f39541be0400ca15"></a>

**270° CCW: unverified** — `in_game_route_query-9b25f39541be0400ca15`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-ab880866d38fd312a2e7"></a>

**0° CCW: unverified** — `in_game_route_query-ab880866d38fd312a2e7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-22737b4f0b1f1649d4cf"></a>

**90° CCW: unverified** — `in_game_route_query-22737b4f0b1f1649d4cf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-c1c99ad1ef5af5e71525"></a>

**180° CCW: unverified** — `in_game_route_query-c1c99ad1ef5af5e71525`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-3515f3e69ec2f1b08bf6"></a>

**270° CCW: unverified** — `in_game_route_query-3515f3e69ec2f1b08bf6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-4cde2ef1cd2dca039820"></a>

**0° CCW: unverified** — `in_game_route_query-4cde2ef1cd2dca039820`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-b38084f2c5d23cdb74b2"></a>

**90° CCW: unverified** — `in_game_route_query-b38084f2c5d23cdb74b2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-4d38eb7bc791321dead4"></a>

**180° CCW: unverified** — `in_game_route_query-4d38eb7bc791321dead4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-abe9b332242f4044bfb8"></a>

**270° CCW: unverified** — `in_game_route_query-abe9b332242f4044bfb8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out</summary>

<a id="case-in_game_route_query-da5597f47efcc1396765"></a>

**0° CCW: unverified** — `in_game_route_query-da5597f47efcc1396765`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-03592207a787fb2f9a34"></a>

**90° CCW: unverified** — `in_game_route_query-03592207a787fb2f9a34`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-cdd9975802fa991c8b51"></a>

**180° CCW: unverified** — `in_game_route_query-cdd9975802fa991c8b51`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-43af7ac40cc245b26240"></a>

**270° CCW: unverified** — `in_game_route_query-43af7ac40cc245b26240`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-a6a3dbc5eff105899381"></a>

**0° CCW: unverified** — `in_game_route_query-a6a3dbc5eff105899381`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-243725df91d490498574"></a>

**90° CCW: unverified** — `in_game_route_query-243725df91d490498574`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-b821c0ff7162b9180af9"></a>

**180° CCW: unverified** — `in_game_route_query-b821c0ff7162b9180af9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-49255ffded85b5dc191d"></a>

**270° CCW: unverified** — `in_game_route_query-49255ffded85b5dc191d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-ee21873a681de35569ab"></a>

**0° CCW: unverified** — `in_game_route_query-ee21873a681de35569ab`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-c96e8302c5eab2154a77"></a>

**90° CCW: unverified** — `in_game_route_query-c96e8302c5eab2154a77`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-cb57c093eb9b0d47ef5b"></a>

**180° CCW: unverified** — `in_game_route_query-cb57c093eb9b0d47ef5b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-269dc6669ec09370cae3"></a>

**270° CCW: unverified** — `in_game_route_query-269dc6669ec09370cae3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-3ed43d64fc51a26a2218">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a5ccc097953d4bcf75f0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c417ad50e5d1ad0ea5e5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-96c16a5ce3e09227a7a4">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out | — | <a href="#case-in_game_visible_travel-183a5d686495aa64a6e1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4b78340fd9a07226f6b8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4697ddfbd981bf3644b5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-73a7872d653c4280ab3d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-88e71ccc8aab417b0087">[ ] unverified</a> | <a href="#case-in_game_visible_travel-12128938a5a1eaae21f0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e2397b5453d1d1b793a8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7b6659d6bb1e24f76a29">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-ab20c1b0a1e1a046ccc7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ed580217801cc78ff1e7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-115b356918d33b4e315d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bb733292e236ec8888ed">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-dc033f53dc7413a902b9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2f7a4007fc56d7b0141d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8e645e98b6c55413320a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9b25f39541be0400ca15">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-ab880866d38fd312a2e7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-22737b4f0b1f1649d4cf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c1c99ad1ef5af5e71525">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3515f3e69ec2f1b08bf6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-4cde2ef1cd2dca039820">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b38084f2c5d23cdb74b2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4d38eb7bc791321dead4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-abe9b332242f4044bfb8">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out | — | <a href="#case-in_game_visible_travel-da5597f47efcc1396765">[ ] unverified</a> | <a href="#case-in_game_visible_travel-03592207a787fb2f9a34">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cdd9975802fa991c8b51">[ ] unverified</a> | <a href="#case-in_game_visible_travel-43af7ac40cc245b26240">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-a6a3dbc5eff105899381">[ ] unverified</a> | <a href="#case-in_game_visible_travel-243725df91d490498574">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b821c0ff7162b9180af9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-49255ffded85b5dc191d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-ee21873a681de35569ab">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c96e8302c5eab2154a77">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cb57c093eb9b0d47ef5b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-269dc6669ec09370cae3">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-3ed43d64fc51a26a2218"></a>

**0° CCW: unverified** — `in_game_visible_travel-3ed43d64fc51a26a2218`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-a5ccc097953d4bcf75f0"></a>

**90° CCW: unverified** — `in_game_visible_travel-a5ccc097953d4bcf75f0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-c417ad50e5d1ad0ea5e5"></a>

**180° CCW: unverified** — `in_game_visible_travel-c417ad50e5d1ad0ea5e5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-96c16a5ce3e09227a7a4"></a>

**270° CCW: unverified** — `in_game_visible_travel-96c16a5ce3e09227a7a4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-11-out; entry: channel-01-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out</summary>

<a id="case-in_game_visible_travel-183a5d686495aa64a6e1"></a>

**0° CCW: unverified** — `in_game_visible_travel-183a5d686495aa64a6e1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-4b78340fd9a07226f6b8"></a>

**90° CCW: unverified** — `in_game_visible_travel-4b78340fd9a07226f6b8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-4697ddfbd981bf3644b5"></a>

**180° CCW: unverified** — `in_game_visible_travel-4697ddfbd981bf3644b5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-73a7872d653c4280ab3d"></a>

**270° CCW: unverified** — `in_game_visible_travel-73a7872d653c4280ab3d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-20-out; entry: channel-02-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-88e71ccc8aab417b0087"></a>

**0° CCW: unverified** — `in_game_visible_travel-88e71ccc8aab417b0087`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-12128938a5a1eaae21f0"></a>

**90° CCW: unverified** — `in_game_visible_travel-12128938a5a1eaae21f0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-e2397b5453d1d1b793a8"></a>

**180° CCW: unverified** — `in_game_visible_travel-e2397b5453d1d1b793a8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-7b6659d6bb1e24f76a29"></a>

**270° CCW: unverified** — `in_game_visible_travel-7b6659d6bb1e24f76a29`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-ab20c1b0a1e1a046ccc7"></a>

**0° CCW: unverified** — `in_game_visible_travel-ab20c1b0a1e1a046ccc7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-ed580217801cc78ff1e7"></a>

**90° CCW: unverified** — `in_game_visible_travel-ed580217801cc78ff1e7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-115b356918d33b4e315d"></a>

**180° CCW: unverified** — `in_game_visible_travel-115b356918d33b4e315d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-bb733292e236ec8888ed"></a>

**270° CCW: unverified** — `in_game_visible_travel-bb733292e236ec8888ed`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-19-out; entry: channel-04-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-dc033f53dc7413a902b9"></a>

**0° CCW: unverified** — `in_game_visible_travel-dc033f53dc7413a902b9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-2f7a4007fc56d7b0141d"></a>

**90° CCW: unverified** — `in_game_visible_travel-2f7a4007fc56d7b0141d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-8e645e98b6c55413320a"></a>

**180° CCW: unverified** — `in_game_visible_travel-8e645e98b6c55413320a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-9b25f39541be0400ca15"></a>

**270° CCW: unverified** — `in_game_visible_travel-9b25f39541be0400ca15`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-18-out; entry: channel-05-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-ab880866d38fd312a2e7"></a>

**0° CCW: unverified** — `in_game_visible_travel-ab880866d38fd312a2e7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-22737b4f0b1f1649d4cf"></a>

**90° CCW: unverified** — `in_game_visible_travel-22737b4f0b1f1649d4cf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-c1c99ad1ef5af5e71525"></a>

**180° CCW: unverified** — `in_game_visible_travel-c1c99ad1ef5af5e71525`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-3515f3e69ec2f1b08bf6"></a>

**270° CCW: unverified** — `in_game_visible_travel-3515f3e69ec2f1b08bf6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-16-out; entry: channel-06-in; exit: channel-16-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-4cde2ef1cd2dca039820"></a>

**0° CCW: unverified** — `in_game_visible_travel-4cde2ef1cd2dca039820`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-b38084f2c5d23cdb74b2"></a>

**90° CCW: unverified** — `in_game_visible_travel-b38084f2c5d23cdb74b2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-4d38eb7bc791321dead4"></a>

**180° CCW: unverified** — `in_game_visible_travel-4d38eb7bc791321dead4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-abe9b332242f4044bfb8"></a>

**270° CCW: unverified** — `in_game_visible_travel-abe9b332242f4044bfb8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-14-out; entry: channel-07-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out</summary>

<a id="case-in_game_visible_travel-da5597f47efcc1396765"></a>

**0° CCW: unverified** — `in_game_visible_travel-da5597f47efcc1396765`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-03592207a787fb2f9a34"></a>

**90° CCW: unverified** — `in_game_visible_travel-03592207a787fb2f9a34`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-cdd9975802fa991c8b51"></a>

**180° CCW: unverified** — `in_game_visible_travel-cdd9975802fa991c8b51`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-43af7ac40cc245b26240"></a>

**270° CCW: unverified** — `in_game_visible_travel-43af7ac40cc245b26240`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-15-out; entry: channel-08-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-a6a3dbc5eff105899381"></a>

**0° CCW: unverified** — `in_game_visible_travel-a6a3dbc5eff105899381`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-243725df91d490498574"></a>

**90° CCW: unverified** — `in_game_visible_travel-243725df91d490498574`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-b821c0ff7162b9180af9"></a>

**180° CCW: unverified** — `in_game_visible_travel-b821c0ff7162b9180af9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-49255ffded85b5dc191d"></a>

**270° CCW: unverified** — `in_game_visible_travel-49255ffded85b5dc191d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-13-out; entry: channel-09-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-ee21873a681de35569ab"></a>

**0° CCW: unverified** — `in_game_visible_travel-ee21873a681de35569ab`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-c96e8302c5eab2154a77"></a>

**90° CCW: unverified** — `in_game_visible_travel-c96e8302c5eab2154a77`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-cb57c093eb9b0d47ef5b"></a>

**180° CCW: unverified** — `in_game_visible_travel-cb57c093eb9b0d47ef5b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-269dc6669ec09370cae3"></a>

**270° CCW: unverified** — `in_game_visible_travel-269dc6669ec09370cae3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-12-out; entry: channel-10-in; exit: channel-12-out.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out | — | <a href="#case-in_game_route_query-e4b571c6ca33803df682">[ ] unverified</a> | <a href="#case-in_game_route_query-2dee6f729adedf781d63">[ ] unverified</a> | <a href="#case-in_game_route_query-e693d57e270672c1ae3d">[ ] unverified</a> | <a href="#case-in_game_route_query-6909e5127fc0328fa27b">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out | — | <a href="#case-in_game_route_query-efa363b018e5cbfe38d5">[ ] unverified</a> | <a href="#case-in_game_route_query-1e543ae95767cf304bd0">[ ] unverified</a> | <a href="#case-in_game_route_query-a58a10e3984856b91b22">[ ] unverified</a> | <a href="#case-in_game_route_query-4c4da6621cf0b19b2445">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out</summary>

<a id="case-in_game_route_query-e4b571c6ca33803df682"></a>

**0° CCW: unverified** — `in_game_route_query-e4b571c6ca33803df682`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-2dee6f729adedf781d63"></a>

**90° CCW: unverified** — `in_game_route_query-2dee6f729adedf781d63`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-e693d57e270672c1ae3d"></a>

**180° CCW: unverified** — `in_game_route_query-e693d57e270672c1ae3d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-6909e5127fc0328fa27b"></a>

**270° CCW: unverified** — `in_game_route_query-6909e5127fc0328fa27b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out</summary>

<a id="case-in_game_route_query-efa363b018e5cbfe38d5"></a>

**0° CCW: unverified** — `in_game_route_query-efa363b018e5cbfe38d5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-1e543ae95767cf304bd0"></a>

**90° CCW: unverified** — `in_game_route_query-1e543ae95767cf304bd0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-a58a10e3984856b91b22"></a>

**180° CCW: unverified** — `in_game_route_query-a58a10e3984856b91b22`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-4c4da6621cf0b19b2445"></a>

**270° CCW: unverified** — `in_game_route_query-4c4da6621cf0b19b2445`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out | — | <a href="#case-in_game_visible_travel-e4b571c6ca33803df682">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2dee6f729adedf781d63">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e693d57e270672c1ae3d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6909e5127fc0328fa27b">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out | — | <a href="#case-in_game_visible_travel-efa363b018e5cbfe38d5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1e543ae95767cf304bd0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a58a10e3984856b91b22">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4c4da6621cf0b19b2445">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out</summary>

<a id="case-in_game_visible_travel-e4b571c6ca33803df682"></a>

**0° CCW: unverified** — `in_game_visible_travel-e4b571c6ca33803df682`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-2dee6f729adedf781d63"></a>

**90° CCW: unverified** — `in_game_visible_travel-2dee6f729adedf781d63`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-e693d57e270672c1ae3d"></a>

**180° CCW: unverified** — `in_game_visible_travel-e693d57e270672c1ae3d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-6909e5127fc0328fa27b"></a>

**270° CCW: unverified** — `in_game_visible_travel-6909e5127fc0328fa27b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-21-in>channel-24-out; entry: channel-21-in; exit: channel-24-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out</summary>

<a id="case-in_game_visible_travel-efa363b018e5cbfe38d5"></a>

**0° CCW: unverified** — `in_game_visible_travel-efa363b018e5cbfe38d5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-1e543ae95767cf304bd0"></a>

**90° CCW: unverified** — `in_game_visible_travel-1e543ae95767cf304bd0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-a58a10e3984856b91b22"></a>

**180° CCW: unverified** — `in_game_visible_travel-a58a10e3984856b91b22`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-4c4da6621cf0b19b2445"></a>

**270° CCW: unverified** — `in_game_visible_travel-4c4da6621cf0b19b2445`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:channel-22-in>channel-23-out; entry: channel-22-in; exit: channel-23-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 360 cases; unverified: 360</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-37bc89a1badaff4a6398">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-386ca0fb004318e0870a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98f822742ed34cd9e21a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da0750b9cba4e483edd8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6fd65dd3d3d012294183">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21bc7405d00d0da1f1fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9f1dd2f5a122fbdd2fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f901bc0b8f397c6780e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9785372d68ca7c8c0699">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a82fb136423d0a9457f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c340d0fc72deffb29e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c05a0b298986dfbe4ce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8f46673665af92b3fa08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81bffdbfdb6432080914">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3700fdebec2b2b488a15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-143eea8b31f0b4074c8c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3b32cd2bb0d2bfb66c41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0cd584afd67c058591e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2db17a3dae7c8c85d4c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad92d72bd169e082fb0c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f1f7e366e28aba325bbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d9e9b77e7b927d564e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c566977871356635464f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95b9f5bfe86a9364e46f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-01de0e66a1ede87763c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a4f1aeb9e4960398dd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5f0815f68850138d3dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4314b9692e0ecbb9dcf9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f82d76087291f9ec5277">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92e48dde9b016706efbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3c90010c0c9cd132a18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79b3b4fc6f4c4c980867">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e48aa38ffb6efa75b2d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25b6dcc74bae04734816">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5980c102716d08afca7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2149494c73e9957f4eeb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e3ef0ae2c54ce9e0e57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3303e9cc721c042e8a6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b3da2e60357088372a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b5d52e91bcaed7a7deb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e019d2cde7d1c348356f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82c31b73afa3e2bfc866">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57df04aec0bd4771943d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3babbe61fdff749e9e27">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a1d7227b702fbc9176c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-433433114ef4c2027897">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-073374167e6349f4e5bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3405e712a6a5f90acfbe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7921d12d764e241d86e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c70b519ff68194a48483">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54e1d31b5a6e714f6ce0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec0360ed3f6d8b6ef674">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ac2b548dc2abcfacfd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b157420d64a5e22b84bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4e03053a52732205709">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c12894772f3f61f9865">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a856d25d3a4e2b9eee4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ba7c98cd105f6eb398d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c359fdedf6639296b94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6ef8c4a42aa44734fb5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-30510e339d331fba685f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64a9ae963fbd24e4931e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9785bca643a07c662a85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8baa5909951f24cbf09c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7786f98ed1b8c5800efe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aba4ba17188a9fef1e7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cb4a0eaa09160ad228c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db229013a891e8a73ade">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cb522bb473605325d02c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-284c52d83a2192978308">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30439f8afe63a04c80d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd8c48cfcb6d06db4d65">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d390cc12cf2df4669f44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c005d1d47b61f3e597f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43743bac41fced5039b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b53e5ea300e8bb3bb0f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6857b6a55a6183f57b09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-521ea27536fba11341b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42e5a7f0bc8e9a00d887">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3383ddf9227306e73ba2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-359b6e34f0188837f813">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8aefe04347a6589debbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee2adacf95400dbfc219">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9becb45bdf2b085673a2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5810dde5c1d35b9b5f79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-827d24d7a6642a9a4f69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf2f10755fa377042277">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f7a43bcbb8416b3ccb2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4571392888699a620145">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a876040fe0bf489a1571">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dace8d73e2c46e8bfb89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b07bfd2e46a81884289">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b289973be96b2df83604">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-facdf52e9c22c05db2ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a63e725e576eec0da091">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24164a4e2ee2c26fd043">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cab70b2271eaab24d621">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-843de5197e4770274bb5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14f56798a3b6abe6b946">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9cc82892cfbfd77335a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7716c673c5b59350285">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fe222352cd1946de4bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c895491b4fa2c1bf853f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58c3cb8353733c0a6e1b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a3acb9e8f6634a79076">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3f0185af33cbb2e91c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-888a6a927dde4b783cde">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ad8d9785ab0f1dd0fe2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4a649b52863ffd343249">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8b6f326c370f89501ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94ba76034d4b9aeae55a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1eaa43373c12f00bd30d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fb9f890be8f7d04db92a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57ad4777124e6766607b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c204188794fd87156ef3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffcf52d5be4768c658f9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3967be732f2d90b36ced">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9427a1255ae5dc152e7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe4dd2d6964d7f41f0ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b9b92caaf18c5d30d0c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-49564335961804065c26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6028587e11a0e71035e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8480b8da9a63059b5376">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4147f2cbf2a5d7988332">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1867e40998950b043e1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-535ed4602a28b976e2e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47d6e7c759f4790d0161">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4f0fab58b4d5794b58b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-12fe65035fc3101bae3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa6eec8c114aa50b184a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce5a65c317f5f329e88f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9e51e9fbffbc1e7fc62">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e68d9660b16e37672204">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b638e45697ad5fbe4baf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd24ff916087e85810d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afc080bf41d322c5260d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-45ed0d12c27f4a579ec3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00f5dcf058ea86e64051">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5289a10a12fa4a171ae9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb506227a93dc4c680dd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e8d7e299a45b5a546c83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae9db4296a7ae47c0ddb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-969f371d1ed2f3164558">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cd5ef848e495cc1f273">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d24bf414e65e20799c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80a0f2362772d84568b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2869dbbebb112db2167f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c1092a1a522e915742d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5cb92697435f0a40d2d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96472abd88c7ee346a0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-159c46dad2cd0c2f5f5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7fedd0223f9f1d3539b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-983566739e23336f5b2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eacced293247a7f4dede">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-088c3973d6a31bccd737">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-638cd0eade070cf04ff8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-46d565e5647089bf32ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4d642003e83ed81ae04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01bbca216816b288b805">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-043b33850b33c84d511e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-73a4d5e4c552dd4e15bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d24f339c56b06be31812">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-168515bfe8aa548c7c4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b35b8e33137234b5166">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c4ed6759db164d87a9d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-147e5818f34ff17eb7c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eeba50391588f31d69f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-430d9ae3b50fbedc60b0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0e9a08bb9f0f885b55c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49de2619da55a6b2bb5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7c113e5201393d01ba1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a67ba14d3367082b2a8f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-875946182f62232c4dd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-713fe30f4bef9ea405a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5cf498c35d740872bed8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e44374ada21680f9d0f1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d48eac9757054e6f452">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f92fc2411cbe8d60b18f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d684da49b846b157bef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce2aa6b74e8dd2e7062a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c3b2acaf9205b51570bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac71813b305ba39934a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0952a56eb8667199b09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44236131c29b67ee9eca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-48749e7ed247385d56a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-348c4940710069c0f775">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c157be125a8f96ba176">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b0db86e093072a6ef02">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a52b6b13f1da1777aaef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78ac503cc4bc68a19aed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6225441fa68106e83af3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc808fe3ec0f9bf813a5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1850d96e05c2ddd70328">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51fce6400503e2704ecd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05c71a2f4260ab36237e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2cca85d97b3ac8a875f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2887810f8197ddb35ce3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fae2dfc6117fda60ffe5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-093ae957cf6a7a7dcb2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d973a9e5a7ab2d8bfec">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bca900d5b61aab7fcfba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f4274f012983ad24eb0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ffa42fc1efeb17991bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ec01cd6e6cf51d1ef59">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c2e402e12af1f9d83b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df6674b16cfb4f5804b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e42901fd5f1d51893ea3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-616992270c5f35eb499a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-28fe1ed8feec8ec22f1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c41b43ea791dcb3726f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cc4b236757942dba9d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50269a895ec4dd52ce3d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-de3f84edb0e663ca1266">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13cf69fa2883d137b912">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-739cbfb31d6b22206a6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de03e71fc68ef403a6db">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9781c78b966cfcdc5456">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97f74c35110c0b7ac909">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ad5b387496289b3324f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6dba24548dd255f1b464">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5fbf7c4118facb222706">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e67eb83076321d40b05b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-406d2055b509450cfc2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ada34beb81a1244cfcc4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-37aec4cd464ad1a8066b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e48b4e0a3364def49f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1a977b40073bca4da74">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b51942c0f9b55303bddb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-55e35c0ae64ee86f81b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4d4d993ed4107a99542">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91b8160182a6c480ebaa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2b7566b05b2575678e5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b34e61a5daa3b8986ff7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea10bfcb47ca30bfe49f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e69abab59710d7cca7d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d68cbd8d996feb6cd41">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-432e5d8c4334bb468b9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffa01ed78995054eef8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-884beab789d8dc6c1a02">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da37654c9fd3b0b7a5c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c00ec0b2339b6daec958">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d37cfba40d521f70790">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5544a0aae427568809d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8d487ad2a59ef65f747">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-edb41a63afd0c8d826d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc5e6282f37cc211fb1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8520e89dbf7173408eff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0dba1c380342e850d3c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5f1071a6e4af307ef7f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17f1aaeccee5690d4e7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d035eb382593b07ec25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a3cf92296e830fa3f4d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc4f38da2589bf96bdd4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f7ee219710ac6d8954a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3406ce795dbabd9037f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a3add9916880531fef9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-26e66041cc7b2e3b57fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-250684495c5b65fe1d61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-128b02c38c917ec9ffe1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e83be3018f38b9356d57">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-885a34a23bcc20082941">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f580260b3d8389cca0b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ae8354dac1cff98e020">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbff0548830d3e342367">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ccc1a00413657ff88925">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85fdc38146a53a1cdb1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e21541987b4a7b5dc2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acb3d01f843f1405377f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-22a5adb914ee542fc8a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e11cce549ca4fb5871c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c50f36eb96b9f4dd51a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4bd2aa636608a599914">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-365a033fd3a4ce3b1641">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15f91cc0e6bd890d6745">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c59829fbcd4172f8550">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6fc93baf900289a7d812">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-db7d7ba7acf878265784">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd26b15b0b5ede28d880">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9040d2797e7ebc489d83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-589300ea3b3e517d5e7e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c6158af526307c0c41c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76960dbdd879a09210b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64411aec8279cae5f7ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc22bec4cfe442b9f9fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a1e567c1b28fc0def89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5309bd34cf895275445">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8980d51985c7a27c12c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1a9c0fb586318bdfa66">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f5af8f421a57d61c6dc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c740346b0b878019803">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6467d95d9090b0f3f5f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4762f72e15631804c1c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6eab32f60a9ae67f5ddb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3acd6391c19dd64747f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0d235bc1aa0ee3dd81b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b847ddb926333397ec8b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6da8c75960d0bb12f61b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9db9f2d9de24e92fa511">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f08a2b0183a6035c099e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fafa7cca17718cc4ae57">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f17653b6570a6f70e098">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e23d464b11c19f6d8ed8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bb080181aa8005a4c45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b472dc5ba72e787a6337">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-86c2a167d44451ecd466">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4aca2ab823b827aaa29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a0c6a8eb788fa9ba3d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aeb1925bf260dc2e1c25">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-58a51f940e23da69729d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3b4529a09ccd9b552a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29d71c26b081ce6b8e15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb14ff7017cafa4df3d5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-788cd9c3f1b4e6b750a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-063efbcf19873f164fe4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1705857710820c3aba9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa0acdfbc2fca1edff33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4f05b48c37d5c2e2971a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6a13987f0d80af2ab95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1a3a5d087c7a0862be8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77266b2775337456beb9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5335ea609c749fd2ee24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c06b626a32c368eb5bec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cab8204a27aebca4f71e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-238eeb00e5feed11455b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d0b8ee26aaa494785184">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e48712c4f3aa658f642a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2552585f4fc272ebe6ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0311afce2fc3882b6e68">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2fbb78084616bd44d09f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-212dcbcd27bd938a8268">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51b916a33333ea6d433c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2063035b46fd07b01d89">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f295ae0d044c78d09476">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f953ef9d2fd64d860069">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21362cb8341167317eba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88cd4ec1cc4b2b46d98a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7efe8e27efc03dac91cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db6a68f7fad38e3673d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0b50cf6487c86a9c312">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71b25820f671ce96f7e1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0351c0a9a3b821874f36">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ac7c1d5465967988976">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cdba95f5eb2db33ccae8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-256164646cb9706e1b4a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e55e7b6c58008eb387e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c748475bd0a4ae2b86f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97d2b48d5c5bcbffafc5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7916b322fb45034a0f77">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-99ddadf727ab58851eea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9391af13ded1b029dfa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-549906a557096397c6bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31eb459af916d5d2af06">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f11a3f3b88af4d975978">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86a756e5bea4240a48e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aed6bcaef3a5ccdf9c51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a520ab698470e8cc8901">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-12b63e0766e6ccc4efea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39174b9c5880f74f5bd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f98cdccc1375064cabbe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79335ff3a942f1622eb0">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-37bc89a1badaff4a6398"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-37bc89a1badaff4a6398`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-386ca0fb004318e0870a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-386ca0fb004318e0870a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98f822742ed34cd9e21a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-98f822742ed34cd9e21a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da0750b9cba4e483edd8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-da0750b9cba4e483edd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6fd65dd3d3d012294183"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6fd65dd3d3d012294183`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21bc7405d00d0da1f1fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-21bc7405d00d0da1f1fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9f1dd2f5a122fbdd2fe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d9f1dd2f5a122fbdd2fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f901bc0b8f397c6780e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3f901bc0b8f397c6780e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9785372d68ca7c8c0699"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9785372d68ca7c8c0699`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a82fb136423d0a9457f5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a82fb136423d0a9457f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c340d0fc72deffb29e7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1c340d0fc72deffb29e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c05a0b298986dfbe4ce"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c05a0b298986dfbe4ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8f46673665af92b3fa08"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8f46673665af92b3fa08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81bffdbfdb6432080914"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-81bffdbfdb6432080914`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3700fdebec2b2b488a15"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3700fdebec2b2b488a15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-143eea8b31f0b4074c8c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-143eea8b31f0b4074c8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3b32cd2bb0d2bfb66c41"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3b32cd2bb0d2bfb66c41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0cd584afd67c058591e1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0cd584afd67c058591e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2db17a3dae7c8c85d4c8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2db17a3dae7c8c85d4c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad92d72bd169e082fb0c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ad92d72bd169e082fb0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f1f7e366e28aba325bbb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f1f7e366e28aba325bbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d9e9b77e7b927d564e1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d9e9b77e7b927d564e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c566977871356635464f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c566977871356635464f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95b9f5bfe86a9364e46f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-95b9f5bfe86a9364e46f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-01de0e66a1ede87763c8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01de0e66a1ede87763c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a4f1aeb9e4960398dd3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a4f1aeb9e4960398dd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5f0815f68850138d3dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d5f0815f68850138d3dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4314b9692e0ecbb9dcf9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4314b9692e0ecbb9dcf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f82d76087291f9ec5277"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f82d76087291f9ec5277`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92e48dde9b016706efbf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-92e48dde9b016706efbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3c90010c0c9cd132a18"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a3c90010c0c9cd132a18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79b3b4fc6f4c4c980867"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-79b3b4fc6f4c4c980867`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e48aa38ffb6efa75b2d6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e48aa38ffb6efa75b2d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25b6dcc74bae04734816"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-25b6dcc74bae04734816`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5980c102716d08afca7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5980c102716d08afca7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2149494c73e9957f4eeb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2149494c73e9957f4eeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e3ef0ae2c54ce9e0e57"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e3ef0ae2c54ce9e0e57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3303e9cc721c042e8a6a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3303e9cc721c042e8a6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b3da2e60357088372a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0b3da2e60357088372a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b5d52e91bcaed7a7deb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2b5d52e91bcaed7a7deb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e019d2cde7d1c348356f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e019d2cde7d1c348356f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82c31b73afa3e2bfc866"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-82c31b73afa3e2bfc866`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57df04aec0bd4771943d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-57df04aec0bd4771943d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3babbe61fdff749e9e27"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3babbe61fdff749e9e27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a1d7227b702fbc9176c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a1d7227b702fbc9176c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-433433114ef4c2027897"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-433433114ef4c2027897`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-073374167e6349f4e5bb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-073374167e6349f4e5bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3405e712a6a5f90acfbe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3405e712a6a5f90acfbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7921d12d764e241d86e4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7921d12d764e241d86e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c70b519ff68194a48483"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c70b519ff68194a48483`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54e1d31b5a6e714f6ce0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54e1d31b5a6e714f6ce0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec0360ed3f6d8b6ef674"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ec0360ed3f6d8b6ef674`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ac2b548dc2abcfacfd6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ac2b548dc2abcfacfd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b157420d64a5e22b84bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b157420d64a5e22b84bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4e03053a52732205709"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d4e03053a52732205709`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c12894772f3f61f9865"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4c12894772f3f61f9865`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a856d25d3a4e2b9eee4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a856d25d3a4e2b9eee4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ba7c98cd105f6eb398d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9ba7c98cd105f6eb398d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c359fdedf6639296b94"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7c359fdedf6639296b94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6ef8c4a42aa44734fb5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a6ef8c4a42aa44734fb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-30510e339d331fba685f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-30510e339d331fba685f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64a9ae963fbd24e4931e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-64a9ae963fbd24e4931e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9785bca643a07c662a85"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9785bca643a07c662a85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8baa5909951f24cbf09c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8baa5909951f24cbf09c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7786f98ed1b8c5800efe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7786f98ed1b8c5800efe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aba4ba17188a9fef1e7d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aba4ba17188a9fef1e7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cb4a0eaa09160ad228c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2cb4a0eaa09160ad228c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db229013a891e8a73ade"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-db229013a891e8a73ade`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cb522bb473605325d02c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb522bb473605325d02c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-284c52d83a2192978308"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-284c52d83a2192978308`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30439f8afe63a04c80d0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-30439f8afe63a04c80d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd8c48cfcb6d06db4d65"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bd8c48cfcb6d06db4d65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d390cc12cf2df4669f44"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d390cc12cf2df4669f44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c005d1d47b61f3e597f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c005d1d47b61f3e597f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43743bac41fced5039b3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-43743bac41fced5039b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b53e5ea300e8bb3bb0f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b53e5ea300e8bb3bb0f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6857b6a55a6183f57b09"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6857b6a55a6183f57b09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-521ea27536fba11341b8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-521ea27536fba11341b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42e5a7f0bc8e9a00d887"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-42e5a7f0bc8e9a00d887`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3383ddf9227306e73ba2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3383ddf9227306e73ba2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-359b6e34f0188837f813"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-359b6e34f0188837f813`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8aefe04347a6589debbc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8aefe04347a6589debbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee2adacf95400dbfc219"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee2adacf95400dbfc219`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9becb45bdf2b085673a2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9becb45bdf2b085673a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5810dde5c1d35b9b5f79"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5810dde5c1d35b9b5f79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-827d24d7a6642a9a4f69"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-827d24d7a6642a9a4f69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf2f10755fa377042277"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bf2f10755fa377042277`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f7a43bcbb8416b3ccb2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6f7a43bcbb8416b3ccb2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4571392888699a620145"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4571392888699a620145`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a876040fe0bf489a1571"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a876040fe0bf489a1571`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dace8d73e2c46e8bfb89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dace8d73e2c46e8bfb89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b07bfd2e46a81884289"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9b07bfd2e46a81884289`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b289973be96b2df83604"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b289973be96b2df83604`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-facdf52e9c22c05db2ef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-facdf52e9c22c05db2ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a63e725e576eec0da091"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a63e725e576eec0da091`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24164a4e2ee2c26fd043"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-24164a4e2ee2c26fd043`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cab70b2271eaab24d621"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cab70b2271eaab24d621`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-843de5197e4770274bb5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-843de5197e4770274bb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14f56798a3b6abe6b946"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-14f56798a3b6abe6b946`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9cc82892cfbfd77335a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b9cc82892cfbfd77335a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7716c673c5b59350285"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7716c673c5b59350285`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fe222352cd1946de4bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5fe222352cd1946de4bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c895491b4fa2c1bf853f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c895491b4fa2c1bf853f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58c3cb8353733c0a6e1b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-58c3cb8353733c0a6e1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a3acb9e8f6634a79076"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a3acb9e8f6634a79076`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3f0185af33cbb2e91c2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b3f0185af33cbb2e91c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-888a6a927dde4b783cde"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-888a6a927dde4b783cde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ad8d9785ab0f1dd0fe2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6ad8d9785ab0f1dd0fe2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4a649b52863ffd343249"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4a649b52863ffd343249`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8b6f326c370f89501ea"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d8b6f326c370f89501ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94ba76034d4b9aeae55a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-94ba76034d4b9aeae55a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1eaa43373c12f00bd30d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1eaa43373c12f00bd30d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fb9f890be8f7d04db92a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fb9f890be8f7d04db92a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57ad4777124e6766607b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-57ad4777124e6766607b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c204188794fd87156ef3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c204188794fd87156ef3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffcf52d5be4768c658f9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ffcf52d5be4768c658f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3967be732f2d90b36ced"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3967be732f2d90b36ced`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9427a1255ae5dc152e7f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9427a1255ae5dc152e7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe4dd2d6964d7f41f0ec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fe4dd2d6964d7f41f0ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b9b92caaf18c5d30d0c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6b9b92caaf18c5d30d0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-49564335961804065c26"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-49564335961804065c26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6028587e11a0e71035e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6028587e11a0e71035e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8480b8da9a63059b5376"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8480b8da9a63059b5376`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4147f2cbf2a5d7988332"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4147f2cbf2a5d7988332`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1867e40998950b043e1c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1867e40998950b043e1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-535ed4602a28b976e2e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-535ed4602a28b976e2e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47d6e7c759f4790d0161"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-47d6e7c759f4790d0161`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4f0fab58b4d5794b58b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a4f0fab58b4d5794b58b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-12fe65035fc3101bae3d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-12fe65035fc3101bae3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa6eec8c114aa50b184a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa6eec8c114aa50b184a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce5a65c317f5f329e88f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ce5a65c317f5f329e88f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9e51e9fbffbc1e7fc62"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b9e51e9fbffbc1e7fc62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e68d9660b16e37672204"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e68d9660b16e37672204`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b638e45697ad5fbe4baf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b638e45697ad5fbe4baf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd24ff916087e85810d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fd24ff916087e85810d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afc080bf41d322c5260d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afc080bf41d322c5260d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-45ed0d12c27f4a579ec3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-45ed0d12c27f4a579ec3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00f5dcf058ea86e64051"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-00f5dcf058ea86e64051`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5289a10a12fa4a171ae9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5289a10a12fa4a171ae9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb506227a93dc4c680dd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bb506227a93dc4c680dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e8d7e299a45b5a546c83"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e8d7e299a45b5a546c83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae9db4296a7ae47c0ddb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ae9db4296a7ae47c0ddb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-969f371d1ed2f3164558"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-969f371d1ed2f3164558`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cd5ef848e495cc1f273"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2cd5ef848e495cc1f273`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d24bf414e65e20799c8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d24bf414e65e20799c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80a0f2362772d84568b8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-80a0f2362772d84568b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2869dbbebb112db2167f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2869dbbebb112db2167f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c1092a1a522e915742d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0c1092a1a522e915742d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5cb92697435f0a40d2d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5cb92697435f0a40d2d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96472abd88c7ee346a0f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-96472abd88c7ee346a0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-159c46dad2cd0c2f5f5d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-159c46dad2cd0c2f5f5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7fedd0223f9f1d3539b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b7fedd0223f9f1d3539b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-983566739e23336f5b2f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-983566739e23336f5b2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eacced293247a7f4dede"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eacced293247a7f4dede`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-088c3973d6a31bccd737"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-088c3973d6a31bccd737`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-638cd0eade070cf04ff8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-638cd0eade070cf04ff8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-46d565e5647089bf32ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-46d565e5647089bf32ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4d642003e83ed81ae04"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e4d642003e83ed81ae04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01bbca216816b288b805"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-01bbca216816b288b805`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-043b33850b33c84d511e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-043b33850b33c84d511e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-73a4d5e4c552dd4e15bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-73a4d5e4c552dd4e15bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d24f339c56b06be31812"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d24f339c56b06be31812`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-168515bfe8aa548c7c4b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-168515bfe8aa548c7c4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b35b8e33137234b5166"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b35b8e33137234b5166`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c4ed6759db164d87a9d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c4ed6759db164d87a9d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-147e5818f34ff17eb7c3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-147e5818f34ff17eb7c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eeba50391588f31d69f3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eeba50391588f31d69f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-430d9ae3b50fbedc60b0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-430d9ae3b50fbedc60b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0e9a08bb9f0f885b55c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e9a08bb9f0f885b55c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49de2619da55a6b2bb5d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-49de2619da55a6b2bb5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7c113e5201393d01ba1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a7c113e5201393d01ba1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a67ba14d3367082b2a8f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a67ba14d3367082b2a8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-875946182f62232c4dd6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-875946182f62232c4dd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-713fe30f4bef9ea405a9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-713fe30f4bef9ea405a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5cf498c35d740872bed8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5cf498c35d740872bed8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e44374ada21680f9d0f1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e44374ada21680f9d0f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d48eac9757054e6f452"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d48eac9757054e6f452`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f92fc2411cbe8d60b18f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f92fc2411cbe8d60b18f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d684da49b846b157bef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5d684da49b846b157bef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce2aa6b74e8dd2e7062a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ce2aa6b74e8dd2e7062a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c3b2acaf9205b51570bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c3b2acaf9205b51570bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac71813b305ba39934a7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ac71813b305ba39934a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0952a56eb8667199b09"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c0952a56eb8667199b09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44236131c29b67ee9eca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-44236131c29b67ee9eca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-48749e7ed247385d56a0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-48749e7ed247385d56a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-348c4940710069c0f775"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-348c4940710069c0f775`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c157be125a8f96ba176"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2c157be125a8f96ba176`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b0db86e093072a6ef02"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b0db86e093072a6ef02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a52b6b13f1da1777aaef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a52b6b13f1da1777aaef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78ac503cc4bc68a19aed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-78ac503cc4bc68a19aed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6225441fa68106e83af3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6225441fa68106e83af3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc808fe3ec0f9bf813a5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc808fe3ec0f9bf813a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1850d96e05c2ddd70328"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1850d96e05c2ddd70328`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51fce6400503e2704ecd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-51fce6400503e2704ecd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05c71a2f4260ab36237e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-05c71a2f4260ab36237e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2cca85d97b3ac8a875f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e2cca85d97b3ac8a875f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2887810f8197ddb35ce3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2887810f8197ddb35ce3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fae2dfc6117fda60ffe5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fae2dfc6117fda60ffe5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-093ae957cf6a7a7dcb2a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-093ae957cf6a7a7dcb2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d973a9e5a7ab2d8bfec"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4d973a9e5a7ab2d8bfec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bca900d5b61aab7fcfba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bca900d5b61aab7fcfba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f4274f012983ad24eb0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8f4274f012983ad24eb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ffa42fc1efeb17991bd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0ffa42fc1efeb17991bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ec01cd6e6cf51d1ef59"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7ec01cd6e6cf51d1ef59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c2e402e12af1f9d83b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c2e402e12af1f9d83b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df6674b16cfb4f5804b3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-df6674b16cfb4f5804b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e42901fd5f1d51893ea3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e42901fd5f1d51893ea3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-616992270c5f35eb499a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-616992270c5f35eb499a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-28fe1ed8feec8ec22f1c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-28fe1ed8feec8ec22f1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c41b43ea791dcb3726f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5c41b43ea791dcb3726f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cc4b236757942dba9d4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9cc4b236757942dba9d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50269a895ec4dd52ce3d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-50269a895ec4dd52ce3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-de3f84edb0e663ca1266"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de3f84edb0e663ca1266`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13cf69fa2883d137b912"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-13cf69fa2883d137b912`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-739cbfb31d6b22206a6d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-739cbfb31d6b22206a6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de03e71fc68ef403a6db"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de03e71fc68ef403a6db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9781c78b966cfcdc5456"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9781c78b966cfcdc5456`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97f74c35110c0b7ac909"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-97f74c35110c0b7ac909`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ad5b387496289b3324f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ad5b387496289b3324f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6dba24548dd255f1b464"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6dba24548dd255f1b464`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5fbf7c4118facb222706"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5fbf7c4118facb222706`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e67eb83076321d40b05b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e67eb83076321d40b05b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-406d2055b509450cfc2d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-406d2055b509450cfc2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ada34beb81a1244cfcc4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ada34beb81a1244cfcc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-37aec4cd464ad1a8066b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-37aec4cd464ad1a8066b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e48b4e0a3364def49f4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3e48b4e0a3364def49f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1a977b40073bca4da74"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a1a977b40073bca4da74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b51942c0f9b55303bddb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b51942c0f9b55303bddb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-55e35c0ae64ee86f81b1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-55e35c0ae64ee86f81b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4d4d993ed4107a99542"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f4d4d993ed4107a99542`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91b8160182a6c480ebaa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-91b8160182a6c480ebaa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2b7566b05b2575678e5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c2b7566b05b2575678e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b34e61a5daa3b8986ff7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b34e61a5daa3b8986ff7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea10bfcb47ca30bfe49f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ea10bfcb47ca30bfe49f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e69abab59710d7cca7d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e69abab59710d7cca7d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d68cbd8d996feb6cd41"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2d68cbd8d996feb6cd41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-432e5d8c4334bb468b9d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-432e5d8c4334bb468b9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffa01ed78995054eef8d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ffa01ed78995054eef8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-884beab789d8dc6c1a02"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-884beab789d8dc6c1a02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da37654c9fd3b0b7a5c2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-da37654c9fd3b0b7a5c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c00ec0b2339b6daec958"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c00ec0b2339b6daec958`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d37cfba40d521f70790"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7d37cfba40d521f70790`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5544a0aae427568809d0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5544a0aae427568809d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8d487ad2a59ef65f747"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c8d487ad2a59ef65f747`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-edb41a63afd0c8d826d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-edb41a63afd0c8d826d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc5e6282f37cc211fb1b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dc5e6282f37cc211fb1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8520e89dbf7173408eff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8520e89dbf7173408eff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0dba1c380342e850d3c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d0dba1c380342e850d3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5f1071a6e4af307ef7f3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5f1071a6e4af307ef7f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17f1aaeccee5690d4e7d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-17f1aaeccee5690d4e7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d035eb382593b07ec25"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6d035eb382593b07ec25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a3cf92296e830fa3f4d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4a3cf92296e830fa3f4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc4f38da2589bf96bdd4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc4f38da2589bf96bdd4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f7ee219710ac6d8954a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0f7ee219710ac6d8954a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3406ce795dbabd9037f4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3406ce795dbabd9037f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a3add9916880531fef9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0a3add9916880531fef9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-26e66041cc7b2e3b57fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-26e66041cc7b2e3b57fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-250684495c5b65fe1d61"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-250684495c5b65fe1d61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-128b02c38c917ec9ffe1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-128b02c38c917ec9ffe1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e83be3018f38b9356d57"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e83be3018f38b9356d57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-885a34a23bcc20082941"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-885a34a23bcc20082941`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f580260b3d8389cca0b7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f580260b3d8389cca0b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ae8354dac1cff98e020"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8ae8354dac1cff98e020`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbff0548830d3e342367"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bbff0548830d3e342367`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ccc1a00413657ff88925"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ccc1a00413657ff88925`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85fdc38146a53a1cdb1b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-85fdc38146a53a1cdb1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e21541987b4a7b5dc2c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7e21541987b4a7b5dc2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acb3d01f843f1405377f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-acb3d01f843f1405377f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-22a5adb914ee542fc8a2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-22a5adb914ee542fc8a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e11cce549ca4fb5871c8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e11cce549ca4fb5871c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c50f36eb96b9f4dd51a8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c50f36eb96b9f4dd51a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4bd2aa636608a599914"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b4bd2aa636608a599914`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-365a033fd3a4ce3b1641"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-365a033fd3a4ce3b1641`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15f91cc0e6bd890d6745"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-15f91cc0e6bd890d6745`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c59829fbcd4172f8550"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2c59829fbcd4172f8550`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6fc93baf900289a7d812"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6fc93baf900289a7d812`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-db7d7ba7acf878265784"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-db7d7ba7acf878265784`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd26b15b0b5ede28d880"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd26b15b0b5ede28d880`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9040d2797e7ebc489d83"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9040d2797e7ebc489d83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-589300ea3b3e517d5e7e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-589300ea3b3e517d5e7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c6158af526307c0c41c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c6158af526307c0c41c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76960dbdd879a09210b1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-76960dbdd879a09210b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64411aec8279cae5f7ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-64411aec8279cae5f7ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc22bec4cfe442b9f9fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc22bec4cfe442b9f9fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a1e567c1b28fc0def89"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a1e567c1b28fc0def89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5309bd34cf895275445"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b5309bd34cf895275445`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8980d51985c7a27c12c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c8980d51985c7a27c12c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1a9c0fb586318bdfa66"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b1a9c0fb586318bdfa66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f5af8f421a57d61c6dc9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f5af8f421a57d61c6dc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c740346b0b878019803"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c740346b0b878019803`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6467d95d9090b0f3f5f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b6467d95d9090b0f3f5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4762f72e15631804c1c7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4762f72e15631804c1c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6eab32f60a9ae67f5ddb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6eab32f60a9ae67f5ddb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3acd6391c19dd64747f9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3acd6391c19dd64747f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0d235bc1aa0ee3dd81b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d0d235bc1aa0ee3dd81b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b847ddb926333397ec8b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b847ddb926333397ec8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6da8c75960d0bb12f61b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6da8c75960d0bb12f61b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9db9f2d9de24e92fa511"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9db9f2d9de24e92fa511`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f08a2b0183a6035c099e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f08a2b0183a6035c099e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fafa7cca17718cc4ae57"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fafa7cca17718cc4ae57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f17653b6570a6f70e098"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f17653b6570a6f70e098`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e23d464b11c19f6d8ed8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e23d464b11c19f6d8ed8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bb080181aa8005a4c45"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6bb080181aa8005a4c45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b472dc5ba72e787a6337"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b472dc5ba72e787a6337`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-86c2a167d44451ecd466"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-86c2a167d44451ecd466`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4aca2ab823b827aaa29"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d4aca2ab823b827aaa29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a0c6a8eb788fa9ba3d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5a0c6a8eb788fa9ba3d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aeb1925bf260dc2e1c25"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aeb1925bf260dc2e1c25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-58a51f940e23da69729d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-58a51f940e23da69729d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3b4529a09ccd9b552a6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d3b4529a09ccd9b552a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29d71c26b081ce6b8e15"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-29d71c26b081ce6b8e15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb14ff7017cafa4df3d5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eb14ff7017cafa4df3d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-788cd9c3f1b4e6b750a6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-788cd9c3f1b4e6b750a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-063efbcf19873f164fe4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-063efbcf19873f164fe4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1705857710820c3aba9c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1705857710820c3aba9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa0acdfbc2fca1edff33"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa0acdfbc2fca1edff33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4f05b48c37d5c2e2971a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4f05b48c37d5c2e2971a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6a13987f0d80af2ab95"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d6a13987f0d80af2ab95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1a3a5d087c7a0862be8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e1a3a5d087c7a0862be8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77266b2775337456beb9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-77266b2775337456beb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5335ea609c749fd2ee24"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5335ea609c749fd2ee24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c06b626a32c368eb5bec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c06b626a32c368eb5bec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cab8204a27aebca4f71e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cab8204a27aebca4f71e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-238eeb00e5feed11455b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-238eeb00e5feed11455b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d0b8ee26aaa494785184"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0b8ee26aaa494785184`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e48712c4f3aa658f642a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e48712c4f3aa658f642a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2552585f4fc272ebe6ba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2552585f4fc272ebe6ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0311afce2fc3882b6e68"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0311afce2fc3882b6e68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2fbb78084616bd44d09f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2fbb78084616bd44d09f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-212dcbcd27bd938a8268"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-212dcbcd27bd938a8268`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51b916a33333ea6d433c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-51b916a33333ea6d433c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2063035b46fd07b01d89"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2063035b46fd07b01d89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f295ae0d044c78d09476"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f295ae0d044c78d09476`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f953ef9d2fd64d860069"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f953ef9d2fd64d860069`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21362cb8341167317eba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-21362cb8341167317eba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88cd4ec1cc4b2b46d98a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-88cd4ec1cc4b2b46d98a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7efe8e27efc03dac91cd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7efe8e27efc03dac91cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db6a68f7fad38e3673d0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-db6a68f7fad38e3673d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0b50cf6487c86a9c312"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c0b50cf6487c86a9c312`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71b25820f671ce96f7e1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-71b25820f671ce96f7e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0351c0a9a3b821874f36"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0351c0a9a3b821874f36`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ac7c1d5465967988976"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5ac7c1d5465967988976`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cdba95f5eb2db33ccae8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cdba95f5eb2db33ccae8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-256164646cb9706e1b4a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-256164646cb9706e1b4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e55e7b6c58008eb387e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e55e7b6c58008eb387e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c748475bd0a4ae2b86f6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c748475bd0a4ae2b86f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97d2b48d5c5bcbffafc5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-97d2b48d5c5bcbffafc5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7916b322fb45034a0f77"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7916b322fb45034a0f77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-99ddadf727ab58851eea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-99ddadf727ab58851eea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9391af13ded1b029dfa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a9391af13ded1b029dfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-549906a557096397c6bd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-549906a557096397c6bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31eb459af916d5d2af06"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-31eb459af916d5d2af06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f11a3f3b88af4d975978"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f11a3f3b88af4d975978`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86a756e5bea4240a48e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-86a756e5bea4240a48e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aed6bcaef3a5ccdf9c51"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aed6bcaef3a5ccdf9c51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a520ab698470e8cc8901"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a520ab698470e8cc8901`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-12b63e0766e6ccc4efea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-12b63e0766e6ccc4efea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39174b9c5880f74f5bd6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-39174b9c5880f74f5bd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f98cdccc1375064cabbe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f98cdccc1375064cabbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79335ff3a942f1622eb0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-79335ff3a942f1622eb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c62e88780d872cc0932">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-464426cc679990e9838a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b465cabaaf88d0a6056">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0f6be06bc87c2edace7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-66f215c25565fb82e3d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-891627372a4c953a1f47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6fd114a293594b2040d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7502b12a820cd60751eb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f4b7fc7287248f82ce39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a646e8e5ba914e2ce48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd58b91260a36f7d063c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2757aec91c2288c1566a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7cc03886ec6cf1324116">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91711477162a8e6a9a31">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3795a6a2469cdba28b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd424d1a1c244aa28618">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b7730e08769030da49e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f493b29e76bc744f2bb3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3d6c0d56f6978b699e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f16c5c805e8b136d4c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f12d34930faa9031f45b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a49d829bef79f3802d4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86c046f4bd2a4662430b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-669801aeb3f003c0d506">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fdeb12f46d6ae7d20a0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-341ba8beced742fc642b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0535c0671198b9352c11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74843e1241eee8a1c069">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-26b1744f8b97a523255a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb7e66234cac85b24a94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f124b690af881278d0eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7905a206db2097ceee4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e3cc85818ee243dc43b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d01af0cc60289de48d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40a59d9c82cd370a4ecf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a865abcc5f95ae58539b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-506f2ac4d4a5f4b42825">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43a203a7b1992eac3b86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38082e9f0cea0625e205">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5a5490f0d1deb767217">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8b31c47b3907fa199f9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f55da1a99b99a6eb591a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5c7134a8b500dba6353">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e38aebd89d0704b8a90c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dec3c275a064ba99a02a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4268dbafdae1e905b5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c91dc105ccf5bf3910d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f46099b6eb4607d5347f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6feceec79c4adf02880d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7764cc8f683f421e8649">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5011d280e079ba7100c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64e2b011d2dca38d89ff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-99331a01f5ea109e8fb0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e78f535b926a469da10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4ad8b7a5cf2c6f84586">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b8769cba5c91a1e3078">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4f4ffd6fb81302d2d0cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cd87549397308899a76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-150b046a0ce1fe018992">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b1dc58bd63c82c3c272">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-61b2e0fc335320678fc3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67a5ce0f0107ef03b486">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85eb42e4d4bcd8c341f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e870935cf3c227978a09">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c4ff262c5def83bed306">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffa6ddb498c813cd8692">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d92de54e6fd08f2f116f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12361fe8535fbc51b71a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8c1e008a9b25da841c78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ad8972f34dd7d1ef7c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7caca6c9f97d63a2d33">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed039fe55645700cf1c3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9a767dbd34b4343da575">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1bd0bffa924b061ea16c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f13e34de13ebe2d186b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bac9f04408445d00452">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41a214e08f7cec3619f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-461ab56102d35c173838">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3423e5b5ac718bf20848">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc0d6c78eee64682fa64">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c62e88780d872cc0932"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c62e88780d872cc0932`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-464426cc679990e9838a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-464426cc679990e9838a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b465cabaaf88d0a6056"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8b465cabaaf88d0a6056`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0f6be06bc87c2edace7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f0f6be06bc87c2edace7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-66f215c25565fb82e3d3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-66f215c25565fb82e3d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-891627372a4c953a1f47"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-891627372a4c953a1f47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6fd114a293594b2040d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e6fd114a293594b2040d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7502b12a820cd60751eb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7502b12a820cd60751eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f4b7fc7287248f82ce39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4b7fc7287248f82ce39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a646e8e5ba914e2ce48"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4a646e8e5ba914e2ce48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd58b91260a36f7d063c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bd58b91260a36f7d063c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2757aec91c2288c1566a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2757aec91c2288c1566a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7cc03886ec6cf1324116"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7cc03886ec6cf1324116`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91711477162a8e6a9a31"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-91711477162a8e6a9a31`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3795a6a2469cdba28b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d3795a6a2469cdba28b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd424d1a1c244aa28618"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd424d1a1c244aa28618`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b7730e08769030da49e1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b7730e08769030da49e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f493b29e76bc744f2bb3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f493b29e76bc744f2bb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3d6c0d56f6978b699e1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c3d6c0d56f6978b699e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f16c5c805e8b136d4c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5f16c5c805e8b136d4c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f12d34930faa9031f45b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f12d34930faa9031f45b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a49d829bef79f3802d4e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a49d829bef79f3802d4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86c046f4bd2a4662430b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-86c046f4bd2a4662430b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-669801aeb3f003c0d506"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-669801aeb3f003c0d506`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fdeb12f46d6ae7d20a0c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fdeb12f46d6ae7d20a0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-341ba8beced742fc642b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-341ba8beced742fc642b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0535c0671198b9352c11"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0535c0671198b9352c11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74843e1241eee8a1c069"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-74843e1241eee8a1c069`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-26b1744f8b97a523255a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-26b1744f8b97a523255a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb7e66234cac85b24a94"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bb7e66234cac85b24a94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f124b690af881278d0eb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f124b690af881278d0eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7905a206db2097ceee4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a7905a206db2097ceee4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e3cc85818ee243dc43b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e3cc85818ee243dc43b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d01af0cc60289de48d6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2d01af0cc60289de48d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40a59d9c82cd370a4ecf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-40a59d9c82cd370a4ecf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a865abcc5f95ae58539b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a865abcc5f95ae58539b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-506f2ac4d4a5f4b42825"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-506f2ac4d4a5f4b42825`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43a203a7b1992eac3b86"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-43a203a7b1992eac3b86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38082e9f0cea0625e205"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-38082e9f0cea0625e205`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5a5490f0d1deb767217"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a5a5490f0d1deb767217`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8b31c47b3907fa199f9b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8b31c47b3907fa199f9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f55da1a99b99a6eb591a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f55da1a99b99a6eb591a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5c7134a8b500dba6353"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d5c7134a8b500dba6353`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e38aebd89d0704b8a90c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e38aebd89d0704b8a90c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dec3c275a064ba99a02a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dec3c275a064ba99a02a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4268dbafdae1e905b5a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b4268dbafdae1e905b5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c91dc105ccf5bf3910d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9c91dc105ccf5bf3910d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f46099b6eb4607d5347f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f46099b6eb4607d5347f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6feceec79c4adf02880d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6feceec79c4adf02880d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7764cc8f683f421e8649"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7764cc8f683f421e8649`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5011d280e079ba7100c2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5011d280e079ba7100c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64e2b011d2dca38d89ff"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64e2b011d2dca38d89ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-99331a01f5ea109e8fb0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-99331a01f5ea109e8fb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e78f535b926a469da10"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2e78f535b926a469da10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4ad8b7a5cf2c6f84586"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f4ad8b7a5cf2c6f84586`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b8769cba5c91a1e3078"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b8769cba5c91a1e3078`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4f4ffd6fb81302d2d0cd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4f4ffd6fb81302d2d0cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cd87549397308899a76"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8cd87549397308899a76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-150b046a0ce1fe018992"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-150b046a0ce1fe018992`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b1dc58bd63c82c3c272"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9b1dc58bd63c82c3c272`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-61b2e0fc335320678fc3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-61b2e0fc335320678fc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67a5ce0f0107ef03b486"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67a5ce0f0107ef03b486`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85eb42e4d4bcd8c341f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-85eb42e4d4bcd8c341f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e870935cf3c227978a09"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e870935cf3c227978a09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c4ff262c5def83bed306"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c4ff262c5def83bed306`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffa6ddb498c813cd8692"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ffa6ddb498c813cd8692`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d92de54e6fd08f2f116f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d92de54e6fd08f2f116f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12361fe8535fbc51b71a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-12361fe8535fbc51b71a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8c1e008a9b25da841c78"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8c1e008a9b25da841c78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ad8972f34dd7d1ef7c8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ad8972f34dd7d1ef7c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7caca6c9f97d63a2d33"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c7caca6c9f97d63a2d33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed039fe55645700cf1c3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ed039fe55645700cf1c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9a767dbd34b4343da575"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9a767dbd34b4343da575`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1bd0bffa924b061ea16c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1bd0bffa924b061ea16c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f13e34de13ebe2d186b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1f13e34de13ebe2d186b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bac9f04408445d00452"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0bac9f04408445d00452`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41a214e08f7cec3619f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41a214e08f7cec3619f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-461ab56102d35c173838"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-461ab56102d35c173838`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3423e5b5ac718bf20848"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3423e5b5ac718bf20848`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc0d6c78eee64682fa64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc0d6c78eee64682fa64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d4176577dd20765e9d84">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0648358c8bce0b70f5af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99d1bd82d4058f546745">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2337101a318e1a66d56b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1cf3d70ca368177885a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f6760b2d0690c7f74f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3c396ec0b53ec609964">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf981ac0b796296c18a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4dc2a04e3ebcddd1bf6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e6884aacefaddd2b95d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d4156354e26142cb432">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75542e69bef50dad6173">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ca335f6487105eb8846">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d05ebaadac4bcc8b0a8c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89c2caa4f38b741d8171">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8d4936825271c24d04d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-80ca95f2cf3f424e5b00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30c072993192ee5ccbec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce569028c4cb28033401">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36ca92e91e97d111a75d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4a68e01ffe01015eb070">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8128641a859dadec1265">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62bcc01272d79abed366">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06d419059c368c2a1679">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5b9bd9e1765914ef7438">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6463770ee8691c0d60cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e1380a2fa4268eff590">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0736d35864f6e8214d11">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0fe1ec2b955d7b901b46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f61f2c9cb166845b0091">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2ec71fb572896bfcba4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd49379a6a90e44f08c5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c986009c04c0b2572d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-257ebd6bc8d86daa30f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce27ee3f865dbe11142e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8455bc9c533925ecf234">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e0225273e96ae61159c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7c0503794da46b871a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b866cb4c9aa198abf9f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f48816c3b66fb3fd0701">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c68f11d0635952045e5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60020209782ef6a153b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e44fb364391927be77b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f12c7804487bc1a7795c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7aef069bd6395ffd443">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8100093474af8846a4cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70ab28473bfa2335a4ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89cf35e4aa633380b967">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-467f24889d24681adeeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32364a42a124a5f18ae2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5780badd8ea60628f58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0edbef95934a2aadd20">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-987d2f6e2376d31e2eba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38072ecb496f4b425ffc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4279f23f2464f67cb831">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6eccba058d4d64e71900">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b6f04798f947f5ed30d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ddf28368eb03b7c6b785">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c01eb3f405d601cc8f13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07a34d4cc3385cd9c3c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4c9a43746d68d6be5392">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76c5346a7f4cff609b3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a196934ec63cc646df03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-665e1d5946c03f655ada">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6d590950d87fde41f881">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6611b8eb42dad6c485e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d6e1e5bab13487796a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b38459530ef043e5bf1d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6eee45b3b2188785de66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28b0b46b5403caf51a04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a5a5104dddddd4e1514">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09aa8330da88a9407d29">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e400b01104186d8c2196">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1605e5245fcf5b271ce0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-550579770747913a80bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30c96f2761ec0b898a6d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7a92ff9e84a7d4e835a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67e6b7b60ac160d0163b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8edb43283cab954d0c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5af04bf00aa00796221">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d4176577dd20765e9d84"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d4176577dd20765e9d84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0648358c8bce0b70f5af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0648358c8bce0b70f5af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99d1bd82d4058f546745"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-99d1bd82d4058f546745`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2337101a318e1a66d56b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2337101a318e1a66d56b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1cf3d70ca368177885a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1cf3d70ca368177885a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f6760b2d0690c7f74f7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9f6760b2d0690c7f74f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3c396ec0b53ec609964"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d3c396ec0b53ec609964`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf981ac0b796296c18a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bf981ac0b796296c18a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4dc2a04e3ebcddd1bf6e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4dc2a04e3ebcddd1bf6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e6884aacefaddd2b95d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9e6884aacefaddd2b95d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d4156354e26142cb432"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4d4156354e26142cb432`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75542e69bef50dad6173"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-75542e69bef50dad6173`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ca335f6487105eb8846"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ca335f6487105eb8846`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d05ebaadac4bcc8b0a8c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d05ebaadac4bcc8b0a8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89c2caa4f38b741d8171"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-89c2caa4f38b741d8171`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8d4936825271c24d04d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d8d4936825271c24d04d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-80ca95f2cf3f424e5b00"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-80ca95f2cf3f424e5b00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30c072993192ee5ccbec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-30c072993192ee5ccbec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce569028c4cb28033401"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ce569028c4cb28033401`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36ca92e91e97d111a75d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-36ca92e91e97d111a75d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4a68e01ffe01015eb070"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4a68e01ffe01015eb070`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8128641a859dadec1265"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8128641a859dadec1265`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62bcc01272d79abed366"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-62bcc01272d79abed366`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06d419059c368c2a1679"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-06d419059c368c2a1679`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5b9bd9e1765914ef7438"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5b9bd9e1765914ef7438`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6463770ee8691c0d60cf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6463770ee8691c0d60cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e1380a2fa4268eff590"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1e1380a2fa4268eff590`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0736d35864f6e8214d11"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0736d35864f6e8214d11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0fe1ec2b955d7b901b46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0fe1ec2b955d7b901b46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f61f2c9cb166845b0091"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f61f2c9cb166845b0091`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2ec71fb572896bfcba4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a2ec71fb572896bfcba4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd49379a6a90e44f08c5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd49379a6a90e44f08c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c986009c04c0b2572d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c986009c04c0b2572d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-257ebd6bc8d86daa30f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-257ebd6bc8d86daa30f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce27ee3f865dbe11142e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ce27ee3f865dbe11142e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8455bc9c533925ecf234"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8455bc9c533925ecf234`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e0225273e96ae61159c4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e0225273e96ae61159c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7c0503794da46b871a3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d7c0503794da46b871a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b866cb4c9aa198abf9f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9b866cb4c9aa198abf9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f48816c3b66fb3fd0701"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f48816c3b66fb3fd0701`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c68f11d0635952045e5a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c68f11d0635952045e5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60020209782ef6a153b7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-60020209782ef6a153b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e44fb364391927be77b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9e44fb364391927be77b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f12c7804487bc1a7795c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f12c7804487bc1a7795c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-11-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7aef069bd6395ffd443"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7aef069bd6395ffd443`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8100093474af8846a4cd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8100093474af8846a4cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70ab28473bfa2335a4ef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-70ab28473bfa2335a4ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89cf35e4aa633380b967"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-89cf35e4aa633380b967`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-12-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-467f24889d24681adeeb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-467f24889d24681adeeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32364a42a124a5f18ae2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-32364a42a124a5f18ae2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5780badd8ea60628f58"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d5780badd8ea60628f58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0edbef95934a2aadd20"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b0edbef95934a2aadd20`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-13-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-987d2f6e2376d31e2eba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-987d2f6e2376d31e2eba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38072ecb496f4b425ffc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-38072ecb496f4b425ffc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4279f23f2464f67cb831"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4279f23f2464f67cb831`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6eccba058d4d64e71900"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6eccba058d4d64e71900`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-14-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b6f04798f947f5ed30d3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b6f04798f947f5ed30d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ddf28368eb03b7c6b785"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ddf28368eb03b7c6b785`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c01eb3f405d601cc8f13"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c01eb3f405d601cc8f13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07a34d4cc3385cd9c3c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-07a34d4cc3385cd9c3c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-15-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4c9a43746d68d6be5392"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4c9a43746d68d6be5392`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76c5346a7f4cff609b3a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-76c5346a7f4cff609b3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a196934ec63cc646df03"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a196934ec63cc646df03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-665e1d5946c03f655ada"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-665e1d5946c03f655ada`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-16-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6d590950d87fde41f881"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6d590950d87fde41f881`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6611b8eb42dad6c485e1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6611b8eb42dad6c485e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d6e1e5bab13487796a1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3d6e1e5bab13487796a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b38459530ef043e5bf1d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b38459530ef043e5bf1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-17-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6eee45b3b2188785de66"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6eee45b3b2188785de66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28b0b46b5403caf51a04"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-28b0b46b5403caf51a04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a5a5104dddddd4e1514"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8a5a5104dddddd4e1514`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09aa8330da88a9407d29"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-09aa8330da88a9407d29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-18-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e400b01104186d8c2196"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e400b01104186d8c2196`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1605e5245fcf5b271ce0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1605e5245fcf5b271ce0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-550579770747913a80bd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-550579770747913a80bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30c96f2761ec0b898a6d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-30c96f2761ec0b898a6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-19-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7a92ff9e84a7d4e835a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7a92ff9e84a7d4e835a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67e6b7b60ac160d0163b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67e6b7b60ac160d0163b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8edb43283cab954d0c4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c8edb43283cab954d0c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5af04bf00aa00796221"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e5af04bf00aa00796221`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-20-out; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-89f7a798d21fb186fc78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c64d3233684cd6c8d6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-670b52c144be072fec4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6058af2dd62444e47aad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f9825c3b2d7818c439a4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb5adb274f617e044f56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0d7983d68eb8f6c220b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b413978081a6b2f610db">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-89f7a798d21fb186fc78"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-89f7a798d21fb186fc78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c64d3233684cd6c8d6f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9c64d3233684cd6c8d6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-670b52c144be072fec4b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-670b52c144be072fec4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6058af2dd62444e47aad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6058af2dd62444e47aad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-21-in; to port: channel-23-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f9825c3b2d7818c439a4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f9825c3b2d7818c439a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb5adb274f617e044f56"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bb5adb274f617e044f56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0d7983d68eb8f6c220b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d0d7983d68eb8f6c220b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b413978081a6b2f610db"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b413978081a6b2f610db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-22-in; to port: channel-24-out; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-crossing:canonical-southeast | <a href="#case-preview_review-0bfcf3443e7fbbd06293">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-crossing:canonical-top | <a href="#case-preview_review-5adcf1d4cde9287253f2">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-crossing:connection-overview | <a href="#case-preview_review-a2f10cc2e46bc3a67f19">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-crossing:canonical-southeast</summary>

<a id="case-preview_review-0bfcf3443e7fbbd06293"></a>

**General: unverified** — `preview_review-0bfcf3443e7fbbd06293`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-crossing:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-crossing:canonical-top</summary>

<a id="case-preview_review-5adcf1d4cde9287253f2"></a>

**General: unverified** — `preview_review-5adcf1d4cde9287253f2`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-crossing:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-crossing:connection-overview</summary>

<a id="case-preview_review-a2f10cc2e46bc3a67f19"></a>

**General: unverified** — `preview_review-a2f10cc2e46bc3a67f19`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-crossing:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the crossing function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
