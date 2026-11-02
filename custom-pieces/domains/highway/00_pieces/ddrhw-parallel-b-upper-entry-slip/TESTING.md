---
title: "Testing: DD RHW-4 \u2014 L2 Entry Slip Lanes \u2014 Parallel \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L2 Entry Slip Lanes — Parallel — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **DD RHW-4 — L2 Entry Slip Lanes — Parallel — Alignment B**, permanent ID `ddrhw-parallel-b-upper-entry-slip`, as **P07** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 3 cells inside its 3 × 3 bounding footprint. Both native decks at 7.5 m and 15 m; the named access is at 15 m. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-16-out` | road / 1 / primary | out | [-8.0, -35.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -35.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-17-out` | road / 1 / primary | out | [-8.0, -28.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-02-in` | road / 1 / primary | in | [-8.0, -28.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-03-in` | road / 1 / primary | in | [-3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-18-out` | road / 1 / primary | out | [-3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-04-in` | road / 1 / primary | in | [0.970563, -40.0, 6.871553]; [0.7071067811865476, 0.7071067811865476]; 0.282029323 | `path-interface-3c3a1e090aa258f38443` |
| `channel-05-in` | road / 1 / primary | in | [3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-19-out` | road / 1 / primary | out | [3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-20-out` | road / 1 / primary | out | [8.0, -32.970563, 9.675242]; [0.7071067811865166, 0.7071067811865784]; 0.282029318 | `path-interface-faa05cf1692a3270eed8` |
| `channel-21-out` | road / 1 / primary | out | [8.0, -19.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-06-in` | road / 1 / primary | in | [8.0, -19.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-22-out` | road / 1 / primary | out | [8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-07-in` | road / 1 / primary | in | [8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-08-in` | road / 1 / primary | in | [12.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-23-out` | road / 1 / primary | out | [12.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-09-in` | road / 1 / primary | in | [16.970563, -24.0, 13.253148]; [0.7071067811865294, 0.7071067811865658]; 0.282029322 | `path-interface-765b9df16671d9826fa4` |
| `channel-10-in` | road / 1 / primary | in | [19.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-24-out` | road / 1 / primary | out | [19.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-25-out` | road / 1 / primary | out | [24.0, -16.265154, 15.0]; [0.38533299504728696, 0.9227775912579843]; 0.0 | `path-interface-16588fa0800459396e51` |
| `channel-26-out` | road / 1 / primary | out | [24.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-11-in` | road / 1 / primary | in | [24.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-27-out` | road / 1 / primary | out | [24.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-12-in` | road / 1 / primary | in | [24.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-13-in` | road / 1 / primary | in | [24.671746, -8.0, 15.0]; [0.1270876618900333, 0.9918914891233439]; 0.0 | `path-interface-8d2c9bb680f06657c1f0` |
| `channel-14-in` | road / 1 / primary | in | [28.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-28-out` | road / 1 / primary | out | [28.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-15-in` | road / 1 / primary | in | [35.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-29-out` | road / 1 / primary | out | [35.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-19-out` | primary |
| road | `channel-02-in` → `channel-18-out` | primary |
| road | `channel-03-in` → `channel-17-out` | primary |
| road | `channel-04-in` → `channel-20-out` | primary |
| road | `channel-05-in` → `channel-16-out` | primary |
| road | `channel-06-in` → `channel-24-out` | primary |
| road | `channel-07-in` → `channel-23-out` | primary |
| road | `channel-08-in` → `channel-22-out` | primary |
| road | `channel-09-in` → `channel-25-out` | primary |
| road | `channel-10-in` → `channel-21-out` | primary |
| road | `channel-11-in` → `channel-29-out` | primary |
| road | `channel-12-in` → `channel-28-out` | primary |
| road | `channel-13-in` → `channel-29-out` | primary |
| road | `channel-14-in` → `channel-27-out` | primary |
| road | `channel-15-in` → `channel-26-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-15-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-upper-entry-slip
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **33,378 indexed triangles** and **15 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

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
- [ ] Route Query: 0/60 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/60 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 921, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-upper-entry-slip/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-upper-entry-slip/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-ba177d1dd6b64027ece7">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-ba177d1dd6b64027ece7"></a>

**General: unverified** — `software_resources-ba177d1dd6b64027ece7`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-ba177d1dd6b64027ece7">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-ba177d1dd6b64027ece7"></a>

**General: unverified** — `software_connectivity-ba177d1dd6b64027ece7`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-0c43370a38bdbde2b759">[ ] unverified</a> | <a href="#case-in_game_render-598c55740b38353abf38">[ ] unverified</a> | <a href="#case-in_game_render-a2b71ee51919b0202e8b">[ ] unverified</a> | <a href="#case-in_game_render-95e36309a2a7d3aa6b3b">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-0c43370a38bdbde2b759"></a>

**0° CCW: unverified** — `in_game_render-0c43370a38bdbde2b759`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-598c55740b38353abf38"></a>

**90° CCW: unverified** — `in_game_render-598c55740b38353abf38`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a2b71ee51919b0202e8b"></a>

**180° CCW: unverified** — `in_game_render-a2b71ee51919b0202e8b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-95e36309a2a7d3aa6b3b"></a>

**270° CCW: unverified** — `in_game_render-95e36309a2a7d3aa6b3b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-0c43370a38bdbde2b759">[ ] unverified</a> | <a href="#case-in_game_placement-598c55740b38353abf38">[ ] unverified</a> | <a href="#case-in_game_placement-a2b71ee51919b0202e8b">[ ] unverified</a> | <a href="#case-in_game_placement-95e36309a2a7d3aa6b3b">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-0c43370a38bdbde2b759"></a>

**0° CCW: unverified** — `in_game_placement-0c43370a38bdbde2b759`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-598c55740b38353abf38"></a>

**90° CCW: unverified** — `in_game_placement-598c55740b38353abf38`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a2b71ee51919b0202e8b"></a>

**180° CCW: unverified** — `in_game_placement-a2b71ee51919b0202e8b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-95e36309a2a7d3aa6b3b"></a>

**270° CCW: unverified** — `in_game_placement-95e36309a2a7d3aa6b3b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-0c43370a38bdbde2b759">[ ] unverified</a> | <a href="#case-in_game_demolition-598c55740b38353abf38">[ ] unverified</a> | <a href="#case-in_game_demolition-a2b71ee51919b0202e8b">[ ] unverified</a> | <a href="#case-in_game_demolition-95e36309a2a7d3aa6b3b">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-0c43370a38bdbde2b759"></a>

**0° CCW: unverified** — `in_game_demolition-0c43370a38bdbde2b759`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-598c55740b38353abf38"></a>

**90° CCW: unverified** — `in_game_demolition-598c55740b38353abf38`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a2b71ee51919b0202e8b"></a>

**180° CCW: unverified** — `in_game_demolition-a2b71ee51919b0202e8b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-95e36309a2a7d3aa6b3b"></a>

**270° CCW: unverified** — `in_game_demolition-95e36309a2a7d3aa6b3b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-0c43370a38bdbde2b759">[ ] unverified</a> | <a href="#case-in_game_save_reload-598c55740b38353abf38">[ ] unverified</a> | <a href="#case-in_game_save_reload-a2b71ee51919b0202e8b">[ ] unverified</a> | <a href="#case-in_game_save_reload-95e36309a2a7d3aa6b3b">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-0c43370a38bdbde2b759"></a>

**0° CCW: unverified** — `in_game_save_reload-0c43370a38bdbde2b759`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-598c55740b38353abf38"></a>

**90° CCW: unverified** — `in_game_save_reload-598c55740b38353abf38`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a2b71ee51919b0202e8b"></a>

**180° CCW: unverified** — `in_game_save_reload-a2b71ee51919b0202e8b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-95e36309a2a7d3aa6b3b"></a>

**270° CCW: unverified** — `in_game_save_reload-95e36309a2a7d3aa6b3b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 60 cases; unverified: 60</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-699e172a5eac895e6267">[ ] unverified</a> | <a href="#case-in_game_route_query-98cf4bcd5819765882e3">[ ] unverified</a> | <a href="#case-in_game_route_query-3d0c4f000c4371fc26db">[ ] unverified</a> | <a href="#case-in_game_route_query-ff3281ef25dcfeecea38">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-5965258daeff402033c9">[ ] unverified</a> | <a href="#case-in_game_route_query-607c2258a58fc47db36f">[ ] unverified</a> | <a href="#case-in_game_route_query-db7ec2bbc5e1490aeb6e">[ ] unverified</a> | <a href="#case-in_game_route_query-2fbbf822c7f030d4ed67">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-eb12fef37606bddbc9e1">[ ] unverified</a> | <a href="#case-in_game_route_query-be29d1186e97b6ac4167">[ ] unverified</a> | <a href="#case-in_game_route_query-185de6aab6f7357e2341">[ ] unverified</a> | <a href="#case-in_game_route_query-338622c699c99b328450">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out | — | <a href="#case-in_game_route_query-218d4d9fb4661d3f8d6b">[ ] unverified</a> | <a href="#case-in_game_route_query-2d2a977dd52ea68ce44c">[ ] unverified</a> | <a href="#case-in_game_route_query-13efa04b5a1992ed930a">[ ] unverified</a> | <a href="#case-in_game_route_query-be0d9e835503fff04424">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-0dbc5a6f37c4c2459c6c">[ ] unverified</a> | <a href="#case-in_game_route_query-f14a8bb850e6efc7c49d">[ ] unverified</a> | <a href="#case-in_game_route_query-825e95f16b279b19376b">[ ] unverified</a> | <a href="#case-in_game_route_query-f8ed8a1cef53187efe77">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out | — | <a href="#case-in_game_route_query-6387d7feaa53d3e21408">[ ] unverified</a> | <a href="#case-in_game_route_query-29afd5b3818cce9bdfa7">[ ] unverified</a> | <a href="#case-in_game_route_query-c5fe602f6435c01a7ebf">[ ] unverified</a> | <a href="#case-in_game_route_query-a202514c2f59d3987942">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out | — | <a href="#case-in_game_route_query-f6b4dec005ef6b5883a1">[ ] unverified</a> | <a href="#case-in_game_route_query-5825c853bc7e617d8242">[ ] unverified</a> | <a href="#case-in_game_route_query-c20349fe59d1cc45930f">[ ] unverified</a> | <a href="#case-in_game_route_query-84597fe7ed180a530f53">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out | — | <a href="#case-in_game_route_query-fb039b26582c98cd50de">[ ] unverified</a> | <a href="#case-in_game_route_query-56bf7adfdbe34db89227">[ ] unverified</a> | <a href="#case-in_game_route_query-7aa94608e4eaf6f48a6c">[ ] unverified</a> | <a href="#case-in_game_route_query-bf03827d921c6dcc2ff2">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out | — | <a href="#case-in_game_route_query-3917b3a9d8ee111bd3ed">[ ] unverified</a> | <a href="#case-in_game_route_query-e7d2cbc2b78721e7e450">[ ] unverified</a> | <a href="#case-in_game_route_query-64d3ab80cddfd2a5d152">[ ] unverified</a> | <a href="#case-in_game_route_query-faf4f046d6b11d30fca9">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out | — | <a href="#case-in_game_route_query-ecc5069709bfc95743fd">[ ] unverified</a> | <a href="#case-in_game_route_query-106f09954a0ecf15238d">[ ] unverified</a> | <a href="#case-in_game_route_query-381b41c9adbd9b58e135">[ ] unverified</a> | <a href="#case-in_game_route_query-bb16df24ed92cfbfbcb0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out | — | <a href="#case-in_game_route_query-c3216be99f32ad7b5021">[ ] unverified</a> | <a href="#case-in_game_route_query-5db500b4e8371c4ed981">[ ] unverified</a> | <a href="#case-in_game_route_query-a13f4d8c23af90e4dcbf">[ ] unverified</a> | <a href="#case-in_game_route_query-13836fbe119e781c0748">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out | — | <a href="#case-in_game_route_query-85c1726524329b3fe6a6">[ ] unverified</a> | <a href="#case-in_game_route_query-18d8c78130d3b445c3e6">[ ] unverified</a> | <a href="#case-in_game_route_query-d708bcd84d76a46d15ec">[ ] unverified</a> | <a href="#case-in_game_route_query-2d1ba59d66b5f5ec1848">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out | — | <a href="#case-in_game_route_query-b0166449891ae861864f">[ ] unverified</a> | <a href="#case-in_game_route_query-8a540d362422b9767985">[ ] unverified</a> | <a href="#case-in_game_route_query-099b29cc4b5de737f384">[ ] unverified</a> | <a href="#case-in_game_route_query-66b2bd7d801580255d56">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out | — | <a href="#case-in_game_route_query-7d4d4e51777996866dd4">[ ] unverified</a> | <a href="#case-in_game_route_query-d709843198cf0a0e89de">[ ] unverified</a> | <a href="#case-in_game_route_query-b957e28b19b4696da850">[ ] unverified</a> | <a href="#case-in_game_route_query-64cf4733245c11fc651c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out | — | <a href="#case-in_game_route_query-9f0bb4d87110a12150db">[ ] unverified</a> | <a href="#case-in_game_route_query-4de6d58af926f8e08868">[ ] unverified</a> | <a href="#case-in_game_route_query-05774286b2ee76b25ac7">[ ] unverified</a> | <a href="#case-in_game_route_query-11efad7da1f647ef8a33">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-699e172a5eac895e6267"></a>

**0° CCW: unverified** — `in_game_route_query-699e172a5eac895e6267`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-98cf4bcd5819765882e3"></a>

**90° CCW: unverified** — `in_game_route_query-98cf4bcd5819765882e3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-3d0c4f000c4371fc26db"></a>

**180° CCW: unverified** — `in_game_route_query-3d0c4f000c4371fc26db`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-ff3281ef25dcfeecea38"></a>

**270° CCW: unverified** — `in_game_route_query-ff3281ef25dcfeecea38`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-5965258daeff402033c9"></a>

**0° CCW: unverified** — `in_game_route_query-5965258daeff402033c9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-607c2258a58fc47db36f"></a>

**90° CCW: unverified** — `in_game_route_query-607c2258a58fc47db36f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-db7ec2bbc5e1490aeb6e"></a>

**180° CCW: unverified** — `in_game_route_query-db7ec2bbc5e1490aeb6e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-2fbbf822c7f030d4ed67"></a>

**270° CCW: unverified** — `in_game_route_query-2fbbf822c7f030d4ed67`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-eb12fef37606bddbc9e1"></a>

**0° CCW: unverified** — `in_game_route_query-eb12fef37606bddbc9e1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-be29d1186e97b6ac4167"></a>

**90° CCW: unverified** — `in_game_route_query-be29d1186e97b6ac4167`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-185de6aab6f7357e2341"></a>

**180° CCW: unverified** — `in_game_route_query-185de6aab6f7357e2341`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-338622c699c99b328450"></a>

**270° CCW: unverified** — `in_game_route_query-338622c699c99b328450`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out</summary>

<a id="case-in_game_route_query-218d4d9fb4661d3f8d6b"></a>

**0° CCW: unverified** — `in_game_route_query-218d4d9fb4661d3f8d6b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-2d2a977dd52ea68ce44c"></a>

**90° CCW: unverified** — `in_game_route_query-2d2a977dd52ea68ce44c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-13efa04b5a1992ed930a"></a>

**180° CCW: unverified** — `in_game_route_query-13efa04b5a1992ed930a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-be0d9e835503fff04424"></a>

**270° CCW: unverified** — `in_game_route_query-be0d9e835503fff04424`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-0dbc5a6f37c4c2459c6c"></a>

**0° CCW: unverified** — `in_game_route_query-0dbc5a6f37c4c2459c6c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-f14a8bb850e6efc7c49d"></a>

**90° CCW: unverified** — `in_game_route_query-f14a8bb850e6efc7c49d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-825e95f16b279b19376b"></a>

**180° CCW: unverified** — `in_game_route_query-825e95f16b279b19376b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-f8ed8a1cef53187efe77"></a>

**270° CCW: unverified** — `in_game_route_query-f8ed8a1cef53187efe77`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out</summary>

<a id="case-in_game_route_query-6387d7feaa53d3e21408"></a>

**0° CCW: unverified** — `in_game_route_query-6387d7feaa53d3e21408`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-29afd5b3818cce9bdfa7"></a>

**90° CCW: unverified** — `in_game_route_query-29afd5b3818cce9bdfa7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-c5fe602f6435c01a7ebf"></a>

**180° CCW: unverified** — `in_game_route_query-c5fe602f6435c01a7ebf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-a202514c2f59d3987942"></a>

**270° CCW: unverified** — `in_game_route_query-a202514c2f59d3987942`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out</summary>

<a id="case-in_game_route_query-f6b4dec005ef6b5883a1"></a>

**0° CCW: unverified** — `in_game_route_query-f6b4dec005ef6b5883a1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-5825c853bc7e617d8242"></a>

**90° CCW: unverified** — `in_game_route_query-5825c853bc7e617d8242`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-c20349fe59d1cc45930f"></a>

**180° CCW: unverified** — `in_game_route_query-c20349fe59d1cc45930f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-84597fe7ed180a530f53"></a>

**270° CCW: unverified** — `in_game_route_query-84597fe7ed180a530f53`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out</summary>

<a id="case-in_game_route_query-fb039b26582c98cd50de"></a>

**0° CCW: unverified** — `in_game_route_query-fb039b26582c98cd50de`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_route_query-56bf7adfdbe34db89227"></a>

**90° CCW: unverified** — `in_game_route_query-56bf7adfdbe34db89227`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_route_query-7aa94608e4eaf6f48a6c"></a>

**180° CCW: unverified** — `in_game_route_query-7aa94608e4eaf6f48a6c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_route_query-bf03827d921c6dcc2ff2"></a>

**270° CCW: unverified** — `in_game_route_query-bf03827d921c6dcc2ff2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out</summary>

<a id="case-in_game_route_query-3917b3a9d8ee111bd3ed"></a>

**0° CCW: unverified** — `in_game_route_query-3917b3a9d8ee111bd3ed`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_route_query-e7d2cbc2b78721e7e450"></a>

**90° CCW: unverified** — `in_game_route_query-e7d2cbc2b78721e7e450`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_route_query-64d3ab80cddfd2a5d152"></a>

**180° CCW: unverified** — `in_game_route_query-64d3ab80cddfd2a5d152`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_route_query-faf4f046d6b11d30fca9"></a>

**270° CCW: unverified** — `in_game_route_query-faf4f046d6b11d30fca9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out</summary>

<a id="case-in_game_route_query-ecc5069709bfc95743fd"></a>

**0° CCW: unverified** — `in_game_route_query-ecc5069709bfc95743fd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_route_query-106f09954a0ecf15238d"></a>

**90° CCW: unverified** — `in_game_route_query-106f09954a0ecf15238d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_route_query-381b41c9adbd9b58e135"></a>

**180° CCW: unverified** — `in_game_route_query-381b41c9adbd9b58e135`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_route_query-bb16df24ed92cfbfbcb0"></a>

**270° CCW: unverified** — `in_game_route_query-bb16df24ed92cfbfbcb0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out</summary>

<a id="case-in_game_route_query-c3216be99f32ad7b5021"></a>

**0° CCW: unverified** — `in_game_route_query-c3216be99f32ad7b5021`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_route_query-5db500b4e8371c4ed981"></a>

**90° CCW: unverified** — `in_game_route_query-5db500b4e8371c4ed981`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_route_query-a13f4d8c23af90e4dcbf"></a>

**180° CCW: unverified** — `in_game_route_query-a13f4d8c23af90e4dcbf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_route_query-13836fbe119e781c0748"></a>

**270° CCW: unverified** — `in_game_route_query-13836fbe119e781c0748`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out</summary>

<a id="case-in_game_route_query-85c1726524329b3fe6a6"></a>

**0° CCW: unverified** — `in_game_route_query-85c1726524329b3fe6a6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_route_query-18d8c78130d3b445c3e6"></a>

**90° CCW: unverified** — `in_game_route_query-18d8c78130d3b445c3e6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_route_query-d708bcd84d76a46d15ec"></a>

**180° CCW: unverified** — `in_game_route_query-d708bcd84d76a46d15ec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_route_query-2d1ba59d66b5f5ec1848"></a>

**270° CCW: unverified** — `in_game_route_query-2d1ba59d66b5f5ec1848`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out</summary>

<a id="case-in_game_route_query-b0166449891ae861864f"></a>

**0° CCW: unverified** — `in_game_route_query-b0166449891ae861864f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_route_query-8a540d362422b9767985"></a>

**90° CCW: unverified** — `in_game_route_query-8a540d362422b9767985`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_route_query-099b29cc4b5de737f384"></a>

**180° CCW: unverified** — `in_game_route_query-099b29cc4b5de737f384`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_route_query-66b2bd7d801580255d56"></a>

**270° CCW: unverified** — `in_game_route_query-66b2bd7d801580255d56`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out</summary>

<a id="case-in_game_route_query-7d4d4e51777996866dd4"></a>

**0° CCW: unverified** — `in_game_route_query-7d4d4e51777996866dd4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_route_query-d709843198cf0a0e89de"></a>

**90° CCW: unverified** — `in_game_route_query-d709843198cf0a0e89de`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_route_query-b957e28b19b4696da850"></a>

**180° CCW: unverified** — `in_game_route_query-b957e28b19b4696da850`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_route_query-64cf4733245c11fc651c"></a>

**270° CCW: unverified** — `in_game_route_query-64cf4733245c11fc651c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out</summary>

<a id="case-in_game_route_query-9f0bb4d87110a12150db"></a>

**0° CCW: unverified** — `in_game_route_query-9f0bb4d87110a12150db`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_route_query-4de6d58af926f8e08868"></a>

**90° CCW: unverified** — `in_game_route_query-4de6d58af926f8e08868`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_route_query-05774286b2ee76b25ac7"></a>

**180° CCW: unverified** — `in_game_route_query-05774286b2ee76b25ac7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_route_query-11efad7da1f647ef8a33"></a>

**270° CCW: unverified** — `in_game_route_query-11efad7da1f647ef8a33`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 60 cases; unverified: 60</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-699e172a5eac895e6267">[ ] unverified</a> | <a href="#case-in_game_visible_travel-98cf4bcd5819765882e3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3d0c4f000c4371fc26db">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ff3281ef25dcfeecea38">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-5965258daeff402033c9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-607c2258a58fc47db36f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-db7ec2bbc5e1490aeb6e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2fbbf822c7f030d4ed67">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-eb12fef37606bddbc9e1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-be29d1186e97b6ac4167">[ ] unverified</a> | <a href="#case-in_game_visible_travel-185de6aab6f7357e2341">[ ] unverified</a> | <a href="#case-in_game_visible_travel-338622c699c99b328450">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out | — | <a href="#case-in_game_visible_travel-218d4d9fb4661d3f8d6b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2d2a977dd52ea68ce44c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-13efa04b5a1992ed930a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-be0d9e835503fff04424">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-0dbc5a6f37c4c2459c6c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f14a8bb850e6efc7c49d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-825e95f16b279b19376b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f8ed8a1cef53187efe77">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out | — | <a href="#case-in_game_visible_travel-6387d7feaa53d3e21408">[ ] unverified</a> | <a href="#case-in_game_visible_travel-29afd5b3818cce9bdfa7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c5fe602f6435c01a7ebf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a202514c2f59d3987942">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out | — | <a href="#case-in_game_visible_travel-f6b4dec005ef6b5883a1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5825c853bc7e617d8242">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c20349fe59d1cc45930f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-84597fe7ed180a530f53">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out | — | <a href="#case-in_game_visible_travel-fb039b26582c98cd50de">[ ] unverified</a> | <a href="#case-in_game_visible_travel-56bf7adfdbe34db89227">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7aa94608e4eaf6f48a6c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bf03827d921c6dcc2ff2">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out | — | <a href="#case-in_game_visible_travel-3917b3a9d8ee111bd3ed">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e7d2cbc2b78721e7e450">[ ] unverified</a> | <a href="#case-in_game_visible_travel-64d3ab80cddfd2a5d152">[ ] unverified</a> | <a href="#case-in_game_visible_travel-faf4f046d6b11d30fca9">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out | — | <a href="#case-in_game_visible_travel-ecc5069709bfc95743fd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-106f09954a0ecf15238d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-381b41c9adbd9b58e135">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bb16df24ed92cfbfbcb0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out | — | <a href="#case-in_game_visible_travel-c3216be99f32ad7b5021">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5db500b4e8371c4ed981">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a13f4d8c23af90e4dcbf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-13836fbe119e781c0748">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out | — | <a href="#case-in_game_visible_travel-85c1726524329b3fe6a6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-18d8c78130d3b445c3e6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d708bcd84d76a46d15ec">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2d1ba59d66b5f5ec1848">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out | — | <a href="#case-in_game_visible_travel-b0166449891ae861864f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8a540d362422b9767985">[ ] unverified</a> | <a href="#case-in_game_visible_travel-099b29cc4b5de737f384">[ ] unverified</a> | <a href="#case-in_game_visible_travel-66b2bd7d801580255d56">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out | — | <a href="#case-in_game_visible_travel-7d4d4e51777996866dd4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d709843198cf0a0e89de">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b957e28b19b4696da850">[ ] unverified</a> | <a href="#case-in_game_visible_travel-64cf4733245c11fc651c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out | — | <a href="#case-in_game_visible_travel-9f0bb4d87110a12150db">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4de6d58af926f8e08868">[ ] unverified</a> | <a href="#case-in_game_visible_travel-05774286b2ee76b25ac7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-11efad7da1f647ef8a33">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-699e172a5eac895e6267"></a>

**0° CCW: unverified** — `in_game_visible_travel-699e172a5eac895e6267`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-98cf4bcd5819765882e3"></a>

**90° CCW: unverified** — `in_game_visible_travel-98cf4bcd5819765882e3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-3d0c4f000c4371fc26db"></a>

**180° CCW: unverified** — `in_game_visible_travel-3d0c4f000c4371fc26db`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-ff3281ef25dcfeecea38"></a>

**270° CCW: unverified** — `in_game_visible_travel-ff3281ef25dcfeecea38`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-5965258daeff402033c9"></a>

**0° CCW: unverified** — `in_game_visible_travel-5965258daeff402033c9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-607c2258a58fc47db36f"></a>

**90° CCW: unverified** — `in_game_visible_travel-607c2258a58fc47db36f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-db7ec2bbc5e1490aeb6e"></a>

**180° CCW: unverified** — `in_game_visible_travel-db7ec2bbc5e1490aeb6e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-2fbbf822c7f030d4ed67"></a>

**270° CCW: unverified** — `in_game_visible_travel-2fbbf822c7f030d4ed67`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-18-out; entry: channel-02-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-eb12fef37606bddbc9e1"></a>

**0° CCW: unverified** — `in_game_visible_travel-eb12fef37606bddbc9e1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-be29d1186e97b6ac4167"></a>

**90° CCW: unverified** — `in_game_visible_travel-be29d1186e97b6ac4167`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-185de6aab6f7357e2341"></a>

**180° CCW: unverified** — `in_game_visible_travel-185de6aab6f7357e2341`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-338622c699c99b328450"></a>

**270° CCW: unverified** — `in_game_visible_travel-338622c699c99b328450`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-17-out; entry: channel-03-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out</summary>

<a id="case-in_game_visible_travel-218d4d9fb4661d3f8d6b"></a>

**0° CCW: unverified** — `in_game_visible_travel-218d4d9fb4661d3f8d6b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-2d2a977dd52ea68ce44c"></a>

**90° CCW: unverified** — `in_game_visible_travel-2d2a977dd52ea68ce44c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-13efa04b5a1992ed930a"></a>

**180° CCW: unverified** — `in_game_visible_travel-13efa04b5a1992ed930a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-be0d9e835503fff04424"></a>

**270° CCW: unverified** — `in_game_visible_travel-be0d9e835503fff04424`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-20-out; entry: channel-04-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-0dbc5a6f37c4c2459c6c"></a>

**0° CCW: unverified** — `in_game_visible_travel-0dbc5a6f37c4c2459c6c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-f14a8bb850e6efc7c49d"></a>

**90° CCW: unverified** — `in_game_visible_travel-f14a8bb850e6efc7c49d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-825e95f16b279b19376b"></a>

**180° CCW: unverified** — `in_game_visible_travel-825e95f16b279b19376b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-f8ed8a1cef53187efe77"></a>

**270° CCW: unverified** — `in_game_visible_travel-f8ed8a1cef53187efe77`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-16-out; entry: channel-05-in; exit: channel-16-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out</summary>

<a id="case-in_game_visible_travel-6387d7feaa53d3e21408"></a>

**0° CCW: unverified** — `in_game_visible_travel-6387d7feaa53d3e21408`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-29afd5b3818cce9bdfa7"></a>

**90° CCW: unverified** — `in_game_visible_travel-29afd5b3818cce9bdfa7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-c5fe602f6435c01a7ebf"></a>

**180° CCW: unverified** — `in_game_visible_travel-c5fe602f6435c01a7ebf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-a202514c2f59d3987942"></a>

**270° CCW: unverified** — `in_game_visible_travel-a202514c2f59d3987942`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-24-out; entry: channel-06-in; exit: channel-24-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out</summary>

<a id="case-in_game_visible_travel-f6b4dec005ef6b5883a1"></a>

**0° CCW: unverified** — `in_game_visible_travel-f6b4dec005ef6b5883a1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-5825c853bc7e617d8242"></a>

**90° CCW: unverified** — `in_game_visible_travel-5825c853bc7e617d8242`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-c20349fe59d1cc45930f"></a>

**180° CCW: unverified** — `in_game_visible_travel-c20349fe59d1cc45930f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-84597fe7ed180a530f53"></a>

**270° CCW: unverified** — `in_game_visible_travel-84597fe7ed180a530f53`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-23-out; entry: channel-07-in; exit: channel-23-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out</summary>

<a id="case-in_game_visible_travel-fb039b26582c98cd50de"></a>

**0° CCW: unverified** — `in_game_visible_travel-fb039b26582c98cd50de`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_visible_travel-56bf7adfdbe34db89227"></a>

**90° CCW: unverified** — `in_game_visible_travel-56bf7adfdbe34db89227`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_visible_travel-7aa94608e4eaf6f48a6c"></a>

**180° CCW: unverified** — `in_game_visible_travel-7aa94608e4eaf6f48a6c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_visible_travel-bf03827d921c6dcc2ff2"></a>

**270° CCW: unverified** — `in_game_visible_travel-bf03827d921c6dcc2ff2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-22-out; entry: channel-08-in; exit: channel-22-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out</summary>

<a id="case-in_game_visible_travel-3917b3a9d8ee111bd3ed"></a>

**0° CCW: unverified** — `in_game_visible_travel-3917b3a9d8ee111bd3ed`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_visible_travel-e7d2cbc2b78721e7e450"></a>

**90° CCW: unverified** — `in_game_visible_travel-e7d2cbc2b78721e7e450`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_visible_travel-64d3ab80cddfd2a5d152"></a>

**180° CCW: unverified** — `in_game_visible_travel-64d3ab80cddfd2a5d152`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_visible_travel-faf4f046d6b11d30fca9"></a>

**270° CCW: unverified** — `in_game_visible_travel-faf4f046d6b11d30fca9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-25-out; entry: channel-09-in; exit: channel-25-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out</summary>

<a id="case-in_game_visible_travel-ecc5069709bfc95743fd"></a>

**0° CCW: unverified** — `in_game_visible_travel-ecc5069709bfc95743fd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_visible_travel-106f09954a0ecf15238d"></a>

**90° CCW: unverified** — `in_game_visible_travel-106f09954a0ecf15238d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_visible_travel-381b41c9adbd9b58e135"></a>

**180° CCW: unverified** — `in_game_visible_travel-381b41c9adbd9b58e135`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_visible_travel-bb16df24ed92cfbfbcb0"></a>

**270° CCW: unverified** — `in_game_visible_travel-bb16df24ed92cfbfbcb0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-21-out; entry: channel-10-in; exit: channel-21-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out</summary>

<a id="case-in_game_visible_travel-c3216be99f32ad7b5021"></a>

**0° CCW: unverified** — `in_game_visible_travel-c3216be99f32ad7b5021`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_visible_travel-5db500b4e8371c4ed981"></a>

**90° CCW: unverified** — `in_game_visible_travel-5db500b4e8371c4ed981`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_visible_travel-a13f4d8c23af90e4dcbf"></a>

**180° CCW: unverified** — `in_game_visible_travel-a13f4d8c23af90e4dcbf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_visible_travel-13836fbe119e781c0748"></a>

**270° CCW: unverified** — `in_game_visible_travel-13836fbe119e781c0748`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-29-out; entry: channel-11-in; exit: channel-29-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out</summary>

<a id="case-in_game_visible_travel-85c1726524329b3fe6a6"></a>

**0° CCW: unverified** — `in_game_visible_travel-85c1726524329b3fe6a6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_visible_travel-18d8c78130d3b445c3e6"></a>

**90° CCW: unverified** — `in_game_visible_travel-18d8c78130d3b445c3e6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_visible_travel-d708bcd84d76a46d15ec"></a>

**180° CCW: unverified** — `in_game_visible_travel-d708bcd84d76a46d15ec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_visible_travel-2d1ba59d66b5f5ec1848"></a>

**270° CCW: unverified** — `in_game_visible_travel-2d1ba59d66b5f5ec1848`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-28-out; entry: channel-12-in; exit: channel-28-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out</summary>

<a id="case-in_game_visible_travel-b0166449891ae861864f"></a>

**0° CCW: unverified** — `in_game_visible_travel-b0166449891ae861864f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_visible_travel-8a540d362422b9767985"></a>

**90° CCW: unverified** — `in_game_visible_travel-8a540d362422b9767985`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_visible_travel-099b29cc4b5de737f384"></a>

**180° CCW: unverified** — `in_game_visible_travel-099b29cc4b5de737f384`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_visible_travel-66b2bd7d801580255d56"></a>

**270° CCW: unverified** — `in_game_visible_travel-66b2bd7d801580255d56`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out</summary>

<a id="case-in_game_visible_travel-7d4d4e51777996866dd4"></a>

**0° CCW: unverified** — `in_game_visible_travel-7d4d4e51777996866dd4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_visible_travel-d709843198cf0a0e89de"></a>

**90° CCW: unverified** — `in_game_visible_travel-d709843198cf0a0e89de`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_visible_travel-b957e28b19b4696da850"></a>

**180° CCW: unverified** — `in_game_visible_travel-b957e28b19b4696da850`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_visible_travel-64cf4733245c11fc651c"></a>

**270° CCW: unverified** — `in_game_visible_travel-64cf4733245c11fc651c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-27-out; entry: channel-14-in; exit: channel-27-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out</summary>

<a id="case-in_game_visible_travel-9f0bb4d87110a12150db"></a>

**0° CCW: unverified** — `in_game_visible_travel-9f0bb4d87110a12150db`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_visible_travel-4de6d58af926f8e08868"></a>

**90° CCW: unverified** — `in_game_visible_travel-4de6d58af926f8e08868`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_visible_travel-05774286b2ee76b25ac7"></a>

**180° CCW: unverified** — `in_game_visible_travel-05774286b2ee76b25ac7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_visible_travel-11efad7da1f647ef8a33"></a>

**270° CCW: unverified** — `in_game_visible_travel-11efad7da1f647ef8a33`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-15-in>channel-26-out; entry: channel-15-in; exit: channel-26-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 780 cases; unverified: 780</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3acdd1be7321c9d32451">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac0d35f7e8abc2fb7941">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a819bef9ec677aff7987">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99cc534dd89f976d84ad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a3241fde4541ef113c6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-742545bed7ee9cb20e0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58d652dd79ecf954f9d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53d251158fcda1fde141">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f6208f5d46633277650c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81e8b795b18ff7ebcd4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f93a274928e87151a9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d1cd67dd073465087fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f321596f32dedf00cb16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94265b7839ca196b19e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21f5e87948955338a01c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cf460101b01436512d5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4b9ed064f217c721335a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58f0a600c82e2e56bb7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-914314b2bd6251d25c7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a269544db4772fd8a080">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c2ee9eceda1a8d4d3b39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52cbc77526049e9b6632">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4730b135f520ab11a33d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7710459ad7f1c598566e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7dad2709872826af12bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50e6acb5a69b161bc03f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d78b5a00b4bb713bf63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d54a52849e648bf0d77">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b48ddc29e8037f56c3ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d321b97c0f2da57339e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d265ddf8ce15f093f0a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07e112eeeec07411fb85">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3c797fbe4dd7d457ffe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b14410389222b457dca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ce9bd889b2cb5e0e559">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-599622f3dea012b1aacb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4e366b551a44ab1c4861">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a578f75764eba2f48b3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9693fa1ce5bcdfa69b5f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e914d3aa878eb724ae0a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d06f9ca641ef632a15c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28d80701a21e0697232f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebc01a8ec0827136c745">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da5a886ea6a5a5b6ff93">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-afe92b0f31864a0a315e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5f77b6204719dc2de14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18f7514951e79aa1670c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b72f9ced0a089da267e8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-80c5bad8c7983858f3c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e93ea7b762b78b96e80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50ec3a56d7fe273d61ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8b2bad37fe0d9436536">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e25c66a71ef8dce2ad2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e0d27c3e692eae1c10f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f28697bf5ef33f3df0c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f65a142d825915a05685">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f007aaf990b83379984d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e32093d057990a0394d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8adc1ffab83906cc684a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4b85a3a630caec80d64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-84625b9fee030b583f50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-08ee4d4b9644895dc756">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf950b25ae0fb12e7c9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e03974d4ad3392a3cef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cd8cf4dd0aac7ec79ee4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f42263cc4f166087bc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d231f3771efce7d2c924">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d3abe82c10366e04d56">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-83d09c53a47cabde50a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d222abaf262a04eb058">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b28b428dbc9cf373c3ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-299127182e20f8f0a8f2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dd94d0c4b26afcca19bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d3a6d02ea7d7683e920">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-932f8d45d8f79a4cc38c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-754dcb36fc385962e77e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6f400ae618f391e0f0f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16b99388ff27116c2f13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2066c06f07bae13919ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aca93fbce02a17506c0e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f35b20ee3c9f6b2c1752">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6fc544aa27bf7980f675">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-056b8d029481aa557f89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ab6624728e5e0f8a22d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d90abbc04920e17d14e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae172b230fb26d508337">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2e645a5c49d1b4a7ed5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69c53303f93f51b8cf14">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-327a9e05d292dc838a21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a519037092d0043950d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd1ebc5f1f01c48816aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-797d99b17f6823fa761f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ef6b94a477a5f9c88150">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6175dd771bb6abf380b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d85db220152629b9cc7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2b44b2387e3c31158e4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-295a7ba854c5e124841e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cb32b7e908adaf85368">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c2743e52f9f5e2497d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00b3060068388863804c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3c0ee1a320ff0711fbe7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd5968fb4ae93e163723">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbcd093b9424b71fbddc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8d8c30685da1dff07f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7206d18e03bc420b2e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55337717e46c7d492704">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-368ae3ad47daf6750c9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c89dd1c20c27a8e08d91">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-abe081a58257106eb7ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4ea98927a2a4e294a09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85502297af0c89193735">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7dc61e20689840804e75">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-776edbcc2cd0c13d388d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-781642974c3da8e57574">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34d8c393ca13f58ae28c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b622cb31b5d06452de0e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-765c07d78ff03c68f1c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09ddd4cfb7f366f8fe54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9afe2718acf5de3eded">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df3d922db41cf887c981">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c552b30dc442ab16eeeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c804ef5fa431bd450c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-026f8b2bc66655a0a3c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f194743d2d7bdd11022">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c0393bcf9403b2632940">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8303ef2615f96a65274d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90e05d2c1e22dc2c19ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ab989be88a1a43c7fb4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-133d082731da024513a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f22099f3855e55773052">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe3857f2b60fbc7ef184">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0326a002b25463a3646d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eae771e6ca09918eb90b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-689284558ef45b36764f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d491fed2090b63ddace">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49281dfd1d1ca4c7beed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ff748904afc0ccb0dc38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bdeb1e800245abd48826">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-419261a48a77a4e5199c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-174ab0596d76cd84cc4b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ff5bb095da905b20fff6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc1a86a1e8c5bb06baa3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a167d4f8f0fe248da65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9cc06dff225af1f3590">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1c8d3ca5a2b07415e07d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4eca963c849a55c169b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eda107e36a511ab05e42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7645bc85ad3d4895c290">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8d50c424526e5e4cc930">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf9d6668d4b0a361a938">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-495edc05d33772f4e281">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-240ef55e6029905e7aad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8d8d7141b6506297d860">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-628613f3b05476a4eabb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ab998672c5ff45ce15c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e9efa8d61bc3686c4ec">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1b0b157eb93980cf65e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99a315bceb3a9c8feb37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7acc4c7dde1bf8f266e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb85227db97c059fb045">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bd2bb01c9da1f7b29793">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9627112489ff57e4c661">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-301c2f445b375fcd853c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b7dbdce2cafc2ca8c07">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-743e6844e360d6895f18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2326af372aa2a6c757a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8f064a8f32b7af23526">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af0495de180e245fa689">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-38e22eb31981063f24c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a099e03ef754108fda3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e64438d8390a362bd59b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db1a89101df4416e0fdd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8c50078e691691fe1302">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7269e56ccb699c477fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31646cff4191c66bac7a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfc41f2f86c5b4e19d0d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a452e7518c65c12268e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77ef180c2378948523f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56beaec8a31ad9c7ecf7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b424805d927c9551f0a7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1e604eb97c47a123ea01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac9034143a14bfaa90e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd659025a454f77c1558">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04e4637e5a402439e5b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-826b7026493282d15929">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a019a8b33c0cb424e64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1642288033834c6b8f34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee2c495f7d3836028949">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5e552d991a5ef7b65e77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a4dde35fe4dcb16c773">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11c30021bbde25f5647d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0cd0f7f85aa8dff5db47">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7effd46e6e6a622f45e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c564a263ef6beedae89b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fcb9c0380e397e88fd39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cdfe6fce352f72e9f81">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c5691e21fa3c0ea179f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-705f3f4c11fc545091d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1521887c84d372e2be7a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d67df34cb51b1b37c94">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f138a03d709ff98decdc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-007c840b7efeccfd1d06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-697f906c75d3f2b0de8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b84ba9af2674af8c18b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1aca73f9a6c0a5a87a8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d17a67452253723db9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd9a8b9e3b68c08f413e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-757bebf609c6e7c9693f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4190a1998d76d8a0f435">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11554e130c2c0bfb2fbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aaf963ae1430bd93dc68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa72b91198f1d15d5396">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4412091f6b63169848a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90ee4b314fb42f027394">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fa4c2c734cc427b1e86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e13c755ec04df7a1cfca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-da0904dbfc8a22fd3fe6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1b4e32fe444eeec8d59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38f91b6ec72c79e0cdaa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f50a41e9b3a18d4d5e69">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41671e38988a42f7df9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec5c525b997c700fd0be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cd5facde3b43ce4ab58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26520df2770e0b57bb57">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4adc842bb215f378b14d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c41ac15009cd7907a95d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-667b8c866dc82c51a0d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71a965b58555e1047b21">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-67e3110ee01f9c0d53fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5cc7605365ff1ba1a421">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-955ca34b0e09e8f37850">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3aee44210a74c860e4b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-908600122a9da7766a17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0e96c0ba8b8fa47d6c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c8f5073a90a9112493e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab76ee570f63084e7f64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5bd30f37502e0bac21d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9520f2583dffad3083ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5097477f84817efbaf08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffd5e61bfca96db3c90f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-85ee76a0db681cd7b235">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81771efab20fc7b204d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4d46c68956f97f74c70">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f27fc4e265b942362d5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fa78c4f5a8d43fd49094">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44bfe437ac0f55cac917">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09d7a17c3b006bc65ce3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f92291efa8b1d849729">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b9e7ae44b387e9c2ae99">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4676457c0d821886de28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81e30a9b409cd9cc108b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0df1535cf632369a3bd7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f2b5fe81dbeb27519ccf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9012cfe7cfe537e2ebe3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-218f57dcc47c6e4543e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37a25404b5dcd6b70110">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5ca8da5cb054d526cbde">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c86e7d1982acb1104c9f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2e75ea90810fb231bd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7749ca931374cd7a655f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7769e285916862ed21d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f097ac0ec1a369c4647a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e672d7c219225ff29731">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db8089fca774ffeb8a37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2806bbea7b92a0dc7e59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2196149160a41de17762">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4370a489086b30760b04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf70fe52d53417359b9f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1cf09e6f4a9970607302">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d82115a48f9ff19ae2d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b28c15f185d17f51d54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-681808973c06e183f88e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b2e0bb0fd288487d53e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-221d6c194a9d33b95571">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7ce5938a2c9a24467b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd97403a239a002003a0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b01fea6c52e386862669">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4997d6ed82b1f39ccd35">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82c5029d57072640fcd7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee6ddf2cccab326aae41">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e1056fa308860651f207">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87db03b2521301d34706">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-203a1608ef6ae2c2a054">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83fbfa3c94440a574ad9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8cb44e8879189e9de427">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca1aa72a7cebfb336dff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-698c36816bc5cabb53cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30b05ab85d69d9229055">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ac4238d2a431a407e572">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ae00bcab569118eb710">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ee012c7bb60a71ac998">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65f009c31ff397713f5e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ac2706a2e65d5e508278">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9596ade64565faff65cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fa8e2f7800fb103ace8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e7732fbff78c0df103f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5aabaae6a573b8be1f3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c4f6a84277ee30c386f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3990ad5c372dd6e14b26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-823a53d64b4a77e111e0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-980ec6e52717e1a50eef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f08f1b38029075ff7dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cda46e768b1232be285f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14da7ed23831d1260eab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ddf098c539b1c731d38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82614956212d81088dae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab38fba6f05f8366a3b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a99ec58374e63652fae3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c79c6b2543b4a577ea48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39379c812bc602aa88e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb7d6e7de2cfdcb55976">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64488667ea7c5c511ffb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-04370f13a9a453659e1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b29ce296c34317ad4f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f045c04774a885a7b56e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f0e06a3d7002710221a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0eba6436d8588e7309ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18bc2fb6c79dbb22f734">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eec39a128ac03c017fa5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0cded9aead8fed8d35dd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6f0963a94ffc5027f98e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-050bb4ac0cb97f8a2152">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e41fa545cfa28b116fbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-683cc47a67831a50b8da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-df9d96ea827e4d8b1870">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0cd34f26720936bf4bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f590bd37ca1bb460965">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-301dad8087da450d24c3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2ae3bb2a4ffbb5a30f5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9347b67bbc394ab2f3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0c9cf690883faf8319a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-def9be4270c39eec5ea2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5b382d26aaee091f237f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bab1b9c512252d597d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-696ff7f0fbf973fc6b6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4fefe5aa04679dc06da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-84592b7d791e93ec029b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2640150cb30fa57b633">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4807e44be265d489fdd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00f62828256241b63085">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-85e558721ed957d1763b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c1fcb897f4017584779">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3abf5a635d007cdfa17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f7119c8b826af615c15">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6e92c288ad287dcdde22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9261dff2c42d5f85d09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15b4a9c9fa320acbda37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a61e55de6e2fa8eaf090">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2f4932fa67c1bb8270b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bfed6f199d46e43106f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc96360ada7ae8f4a293">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f59071cd620c46ffcbd4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dc11ceb6db5cefd0044b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9d12d713c30ca20a8d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c227b3f78e36730d740b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63bace4ed753b48e411e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bd15febcbb179a574191">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a401576c6fde01a57e80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8289e11c8006430464f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96e3772beaf9a01df0c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-240ddf1acc65ce7f44ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2fc89a9cb2bef9bd55b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee855117978c66bce228">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f37593f808fd39e1e05">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c6a1b5f3c88adde14c53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b35508e59b670438db44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-204bde1130173af93f57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b17752df360601bd65e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-db36c9aa52386010e8b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-200c3eb01343e371bd3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-645c96667a7fdd62f118">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f3b2f0ad59cbd33e6a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a37b709bf95ef9617642">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d8e89a3ec042821c619">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ab1dbf9aead7413d2cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58697aef9ba8e9ad2a3c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8e6698f01db3bb19ff00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07ae5b55ec8334af6ff8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c799d6b4abd6b8901508">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41994faa18a631954270">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d64234eee80aaaea5342">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c24583d6331354e5e522">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-962c2446a0edac8edbd5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bc324cd00b21b3bf396">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a328135a0d3ab4c52481">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26fb973a082f05fa6b03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f712cce5027be67d6e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36d9775dba1c1d8d1199">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4c6745d388cae96ca312">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35364b532ed11c3360b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32117e821618519e98b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55964b771769cfa6fac2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fb74ba1997cd3a3a90a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-950352a55f6522a10db4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25befe6c07b37524c856">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-181b5d7a0c9194b469f0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a72e867676e07de5da9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92f3657b38017311d3f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98c843c890c18611ee56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9af7193a34b1da5d5741">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d0ade269eb4fefbf1e59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64547ab9d35f4579b12f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6167f93a65b81f9cc859">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72f915dac5674a22de83">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-36a017fcc806f2e0b3e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b09b3c3248150f6d45dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffa87494aa9519d59874">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-680a5c0676575e3ee02a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-111c9922ee430d9989f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52910447738c3b76a38e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db5a02353b4f3b59687d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0e2ebc13d6d522218a0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ae81b3802e5a35a41f69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f2dc342ae39a19817ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74e394c9f6a0e3d891aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-facf2191450ba3f47240">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-46b344e9e4d5cf469d62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cef4fe0f83ddca0bb6d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a39ee67f63d9602dd968">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5199a4cb9a957ea31bb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a8dbada50759287a74bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ceb492ff0a038eb4236f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9136de2981bec5240f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a9f2a9320c57d3a6db1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ee720a8581d331d6467">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6cd6cad41b2c9bf599f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-216b70dbb1e22b22de43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34b70a6d60fe994a51fc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7127f1c479c187379b8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8578e79f8e6bcf1bc8ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5f9a55f5e1a73828453">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80119a7acdfd5f873a4c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-49f1548094dd51b75b4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-653d112ec0291a623a64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f0865c745122e663139">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7ac864550744e9fa252">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-699f3820ea852eb2d63d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e20e2656970d5fdaf66d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-895dbc71863f0361a8f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1490dcf5fdebdb3912eb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fdb22b3e81fd4c87fbe5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fbb68254f4d7c910cb1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-073067f0edded9a52bad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6b55dd72d9dbd147990">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8eaa6bfd3d6cacea80fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0082523ce6f40d8374f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d849c4c4f8bdb1c0f647">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a35b9b1f6d9a871e62dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4e84c842ad6531e8167b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bb0b7969f6aa68e9f5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e6bde6a3db67c21bf85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc99aea4f28202d4f7af">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9706c8a0f7b51f41db45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7e3007761abe4c1ef60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4687e328c103b82a5a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f8a3a3265b4f1fd3884">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-43f2444605adc333c1f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e475ff924f2148854340">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69ba50e9b90a769249cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c5b756d52b8b4a48e15">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9554d93627b01a8427b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-600daee69ab0dde50734">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c323079ff5847f91387">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15b1f5aa1024b5fba2fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4dd9d4deff93af75cf2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff40cd8ecc3cc3636154">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-837c82cd6a6b066efab3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9868a8274839047c4573">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6e7541f6c5f06e168298">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-886c6d15fdd9228cfbd8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40422ab326cded3761d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03668bc249a7ab651f98">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a713809d1da4bb01c2d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2042d5209385039b2a35">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd7031fa2dd579c98553">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fa4c12f667abe129733">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-468a517383f9f392fa94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9460cef532173a56f8dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b0271f9170cab9afa0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7837bda8eb9dd6e90728">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee0828238b6a1c5c4a6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0660679532a8114aa330">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64c6a39b16cb4b1f9def">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-960c2b52298b1623fe1b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-131920202fc31002eae0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94ec68f3bf5e3232b5c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b09ca288f05a251052f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a747e40fd2d4c5bc3dd7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e288a942a8bc080303d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b398838709296c268f54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17328b101d4ef4c7868c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d16e96cda686d5e75754">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-17ff4b8877e6a628dcfe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1787f9e73b346087831c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccf991d8a05429ab3c59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30ac1b7942b63586532f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bb76537a58e159abd75e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c639e29e8bd4646107e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1950a8ddc17970c60382">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64dc7b3c546358bbf77a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a4307838a33d945c1a39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82c8f370222dc9d1dc72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-624ac541adfdba41f14f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f0c5cd110981b6ca5bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-36c6d707423340056abf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-203dc1564d693afd7798">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51a62b123e31e6631066">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2be245610df2b2d68b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aa776321ae6432d28da5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c633bc51f2e7bdba195">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9e2722d78076ed03275">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d84c51676f3e0e41d7f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0674a15f0ddce6c8460d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa2c6b6f395164df9c11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa61d17cf468aeae4539">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e0973bc3f2dbabfe92a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-17aa94022721146e2f5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18c865f4c5ff78f527d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d2ddc35da5e4971bcdc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15bd8451962e685cc5f0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e6cae6ec06f790c8d41c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-907df42a8ec85a9c14bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ea6e090175058fe62e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc507392cf26bba3bb66">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-36d480a7f1097747dda5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-718910cd7692a9ba2cf4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b4e6907a1043aec2160">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bdf41224631a3a353e54">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ea33a1416249a3cf7ba2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df83d1156004f385d446">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e99deed66d951d89c72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1037fd17fd7f70e2e64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e2f1ee31d361ea2baf9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65aa6e8103f88b9b3824">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32b8c3c6d7b288ea3c6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9592a23ea61659c01036">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-76d784bd8914c187f6ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ee01b696ac9a2d55369">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d21b4d0d5adc8dddbbe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4511a9c3ee13c39f5bf7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-46131f462e3331f1d0bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e049bea9de7d1d8d1f71">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3a74f0b5eea9672fc53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80b345310553da6416a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-53e4cdd40f5c7b3eb936">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f4436a0a107f6b91f12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be959d7c65ca03bfe6a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe5dda110a5c8db0e340">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97f9f4968dfd7972b718">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9ac54d32b314b623e61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b9d9fd24a33cc5b835d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-403611849b5a2d0d12fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-be8d5e8446e7e4c09ee7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cd62d93c42216269643">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4baf8c783dad9a48ba8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5384761803d31a66316">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-abb93c66a9be730d7c32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26073c441d8b191fab18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e2a058c05d969adf23e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-958318acada37654f8a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e93d6e32b1f365b1d7c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bb987ffe68ced1e6b2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21dc08e8d91ae5552aa4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9bce50a82730e1f8a4c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-119167c72a3073f35ee3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c95643a939886e98c5ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b692f3df01a3dbfb5aa3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a9970b0099baea2457b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bed17964042282b17915">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a1d3a268d4834934279">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b0db57306001166ed0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2a9b12e205c1f0b5c50">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-de0fd2f420f729a6df13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0c55f1095125b8e7aa4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35fb969be0b7f04bda3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-960475667a3507592fed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee6781511ad98710054e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e35ceedeaba7b31d984f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4eeb676ee8f42ba73a6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bff703665307d4f864ba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f76499c93c543294c41c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe095b079553ee453db3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0e07f3c363412e0b1f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b264f7b5575d08ff8738">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-920e82e46790759df0d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5c5996546c76c406635">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4fd2b92fc900c764e39d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10a86c1da31a5a04f0d0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-73e3d4466b15e7702eb8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d4dd7cd6c777fbf930c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ecebd8c2331d05e833dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52b172d73c33bcbcb2cc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d585fc47ee2b4fd050ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-274852b28ccac0ebd217">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cd201277ff4abfcd632">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-533413652cd6d95b730e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7fac45f552e3d5856ade">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4320fa05c5e11dd330a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7ac671df1d07247afee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-164e69298faa310acb03">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b5cb97b1874d25a9e108">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d606145b7b7c51adee01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ee801768b99a20cb620">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-098922bbd084333c0d84">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a0309c234700d58e0d70">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afa97922cd172594627f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9a09619519c84e969b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-adb3efc782aad1cdc704">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-641e134cc0a599cb58a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ca51887769009ee8c72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cbbc732e5d48ce42629">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd6bd32b2c82bfea7f97">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3c8f70d80277fc331cbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f29c62693a54a2b2e7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ce4ce74b2d318d64f62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dc5659e4621cf46ea9d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-85a0f58e930eb6f87318">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62d550e52695e5fa7f94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad86bd3d41f075b41f91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71b3abf491f56eae2c4d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f668104611a984310d8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2debc9907d6123837202">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c64a9c9e7e6566c3067b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e59abd28eda49f7d2a24">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cd51bc40d3ae281c7f14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4840b951aab9fa2f28ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-339f71f1fc5230b27666">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e06a6905d1a3f3c35258">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc1b22e4bdaa65cda2df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-908b351f1ca7ab8bea2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9271da29596dfb3b41f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cd3896e69fa639bd37e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5973737caefa170d7089">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5403360ec9e2edd12be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f8a5effbbf054d30310">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f4c0ce5d0b81d5376ee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-da1fc780889ebca3577e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e35cd3c1e9490f37955">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bdc73cc104c4b1f847e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3dba075aa10cb9c9c068">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1efe25df8bfd5d009a99">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e95e448ec2b0302bedd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8511ba79d918d9acea4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-081181de90c8a8f77755">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-54bbbcf72fe06a6c8c43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a857557634e9dea2e7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-115b34851f6bb2b9bed4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f54ce32c82a9fc597aec">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c5e51f2e2239b27fd63b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a5b490424e88111ca97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8d0290eb8e01f377c03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83c1167025a340fa2787">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca69fb83b4d8259a25ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19623d06928324e1efe3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-890b9027b5a637c8aef8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd40571159bfbd19bc93">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2677b4611391ee88a21d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22df443ff34724f1de9f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12b127cdb8e64c11e14a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff92149e97de1009e70f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-54bcb62ac8216dc2f358">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ad14bcd51498ace4fff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9caddee8618c12610851">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84e654a366e25277a240">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ee037c5f3f3ab9a8621">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46f668cb98b4a2d9286d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4f4ed4099f09468eeef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d681c9249f8960255bd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b917633fba949c84058c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-adb086138d9286793378">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-825ff0189daf3aeb3d37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95fb5615aecd02372c8d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0bdd24b4196fa9534095">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54b776c952d3a39a76cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4fd24e0e57e0e7873b51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7594797601b7f54fdab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1154790c59257704290f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83e49c59619d9af88521">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-920f1196479e9619c818">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a301d4eadc6dbc52deef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-74bdd56f26f0e208679e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-764764c6d9dd882ab197">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-beae4bbe469cf96ea5c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55198867813d2363dd1d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-29e99877325d33679514">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c3fc255a0772560dc6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb5729cfe2ab3da142ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c28b05e5060eab3913ef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ced193f54e68fd95f7b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7d4276a0de33ac80718">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1d77a28f9620de0eed9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfada8205e90d41d8511">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f2127aac3c67f85f97bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b68128a49e8a0e4878ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbdf438c43a049f89754">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-151a569098d1fe85ad14">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-df4519992c0e8806aae2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cae672e3ca2506814189">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ccf9ada60f07ddae5d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9ee1e9a414ec1a35522">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8eb995e454acf0795ce7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f84332da803e2b4884f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac4936cbc899ed88f96a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40b0152030a9bdb2b86d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7bbfe87a073de3bd8341">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bad2e6a6b3e1eed5505d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cff0e6cba772dde3bb12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-591f536d9995c3e54e9e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9ca61069352fd02df1ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6de651efa8fb49f258e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c750e6515fdef1b1a6fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-026e6a162a17e3daceaf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a92394c84ade817c029">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-985051926ce8f2d87910">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81ca7f2180b035ff12c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e16c41d44151a3402bea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b8fed7c0ad51bc788f11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3916bce32d7d5e76daea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d78bf51b6f652c195ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-022e136eb78d83d52e18">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a4ba4603faac76000a3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5e330b965cebaa8036d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f570349c40d663532d53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92fd62c4c2758eb2ef2b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-20b32308856f6a1cd553">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37df628814782876a6a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4eee836bc0c58f021984">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f5566bb71d2b8c3a22e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-662f85a215cf60f6221b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6884c975a8cac3cc2e5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a84a00af919992f0e88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-487fb17855e400aeece2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-193f49cf5761125ef747">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2ca386a9f8d03e47239">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dab15776dd1bc1e28c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5002967d39161fbec22d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-52008417c8ec5b3039aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae360309e46d25114add">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-083bc9e2287bd9d36b56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18be5bf715a3b72baab9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-39e6823ac9f634d5697c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f528c1f6a6431e6b970d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c90c8ee4a61c28b9290e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2947239dabc7f16b6f22">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-53e3d3150f9608f41b1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26d5104aaafcfaacbfc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6ed3629655e805059b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aeeec373097106df5136">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-46c05953192b74dd1488">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83a63ac136b6a0ab35d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d115eb06e86464b30cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3d7242f9848ce395db4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3fcc56c12b02b1c7f05f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44dfade06d166f3814b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51be61a38abb6da5dbf6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e54f55e8a09b430d3062">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-125ce6e6efc930942a78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da34023bbcffabd4f0e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23805ee2a8cafdb43319">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d95faa5db7ff20f6fb22">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bbc4fc12da7b3ae8d000">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2bd62cc52314285a02c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff4323dfb29f2e740e7a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a955e13e7ba77ada201">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d306e8e25bcad7a144d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b0a29304556153ef4f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95e8dfa0c004480130a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-100de4e565eee5f6e31e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-96511a3ce553f2340937">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62d1712e8097b55585f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6283e8c5fad984f1c53d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66ead1ada0bb80f54acf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d5d8de45a97f2ab49366">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3bd684e6f68b94754790">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4215868fd604569d2b7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e79ef5c9aa17613ec52">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-15-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-25f508f3c004e9a84a80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67c28f501e3f10ed66ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc289f2a1331b8a36d04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e990b91c2371a2a951c">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3acdd1be7321c9d32451"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3acdd1be7321c9d32451`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac0d35f7e8abc2fb7941"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ac0d35f7e8abc2fb7941`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a819bef9ec677aff7987"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a819bef9ec677aff7987`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99cc534dd89f976d84ad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-99cc534dd89f976d84ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a3241fde4541ef113c6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a3241fde4541ef113c6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-742545bed7ee9cb20e0c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-742545bed7ee9cb20e0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58d652dd79ecf954f9d9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-58d652dd79ecf954f9d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53d251158fcda1fde141"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-53d251158fcda1fde141`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f6208f5d46633277650c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f6208f5d46633277650c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81e8b795b18ff7ebcd4e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-81e8b795b18ff7ebcd4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f93a274928e87151a9b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6f93a274928e87151a9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d1cd67dd073465087fe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7d1cd67dd073465087fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f321596f32dedf00cb16"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f321596f32dedf00cb16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94265b7839ca196b19e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-94265b7839ca196b19e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21f5e87948955338a01c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-21f5e87948955338a01c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cf460101b01436512d5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7cf460101b01436512d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4b9ed064f217c721335a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4b9ed064f217c721335a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58f0a600c82e2e56bb7b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-58f0a600c82e2e56bb7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-914314b2bd6251d25c7b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-914314b2bd6251d25c7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a269544db4772fd8a080"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a269544db4772fd8a080`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c2ee9eceda1a8d4d3b39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c2ee9eceda1a8d4d3b39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52cbc77526049e9b6632"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-52cbc77526049e9b6632`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4730b135f520ab11a33d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4730b135f520ab11a33d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7710459ad7f1c598566e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7710459ad7f1c598566e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7dad2709872826af12bd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7dad2709872826af12bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50e6acb5a69b161bc03f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-50e6acb5a69b161bc03f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d78b5a00b4bb713bf63"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2d78b5a00b4bb713bf63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d54a52849e648bf0d77"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8d54a52849e648bf0d77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b48ddc29e8037f56c3ff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b48ddc29e8037f56c3ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d321b97c0f2da57339e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6d321b97c0f2da57339e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d265ddf8ce15f093f0a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d265ddf8ce15f093f0a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07e112eeeec07411fb85"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-07e112eeeec07411fb85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3c797fbe4dd7d457ffe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3c797fbe4dd7d457ffe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b14410389222b457dca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b14410389222b457dca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ce9bd889b2cb5e0e559"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ce9bd889b2cb5e0e559`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-599622f3dea012b1aacb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-599622f3dea012b1aacb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4e366b551a44ab1c4861"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e366b551a44ab1c4861`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a578f75764eba2f48b3f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a578f75764eba2f48b3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9693fa1ce5bcdfa69b5f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9693fa1ce5bcdfa69b5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e914d3aa878eb724ae0a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e914d3aa878eb724ae0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d06f9ca641ef632a15c4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d06f9ca641ef632a15c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28d80701a21e0697232f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-28d80701a21e0697232f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebc01a8ec0827136c745"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ebc01a8ec0827136c745`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da5a886ea6a5a5b6ff93"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-da5a886ea6a5a5b6ff93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-afe92b0f31864a0a315e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-afe92b0f31864a0a315e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5f77b6204719dc2de14"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a5f77b6204719dc2de14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18f7514951e79aa1670c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-18f7514951e79aa1670c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b72f9ced0a089da267e8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b72f9ced0a089da267e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-80c5bad8c7983858f3c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-80c5bad8c7983858f3c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e93ea7b762b78b96e80"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5e93ea7b762b78b96e80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50ec3a56d7fe273d61ab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-50ec3a56d7fe273d61ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8b2bad37fe0d9436536"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e8b2bad37fe0d9436536`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e25c66a71ef8dce2ad2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e25c66a71ef8dce2ad2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e0d27c3e692eae1c10f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e0d27c3e692eae1c10f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f28697bf5ef33f3df0c5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f28697bf5ef33f3df0c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f65a142d825915a05685"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f65a142d825915a05685`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f007aaf990b83379984d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f007aaf990b83379984d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e32093d057990a0394d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e32093d057990a0394d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8adc1ffab83906cc684a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8adc1ffab83906cc684a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4b85a3a630caec80d64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e4b85a3a630caec80d64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-84625b9fee030b583f50"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-84625b9fee030b583f50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-08ee4d4b9644895dc756"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-08ee4d4b9644895dc756`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf950b25ae0fb12e7c9b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cf950b25ae0fb12e7c9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e03974d4ad3392a3cef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e03974d4ad3392a3cef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cd8cf4dd0aac7ec79ee4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cd8cf4dd0aac7ec79ee4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f42263cc4f166087bc4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3f42263cc4f166087bc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d231f3771efce7d2c924"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d231f3771efce7d2c924`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d3abe82c10366e04d56"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4d3abe82c10366e04d56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-83d09c53a47cabde50a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-83d09c53a47cabde50a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d222abaf262a04eb058"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7d222abaf262a04eb058`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b28b428dbc9cf373c3ab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b28b428dbc9cf373c3ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-299127182e20f8f0a8f2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-299127182e20f8f0a8f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dd94d0c4b26afcca19bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd94d0c4b26afcca19bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d3a6d02ea7d7683e920"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d3a6d02ea7d7683e920`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-932f8d45d8f79a4cc38c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-932f8d45d8f79a4cc38c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-754dcb36fc385962e77e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-754dcb36fc385962e77e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6f400ae618f391e0f0f7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6f400ae618f391e0f0f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16b99388ff27116c2f13"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-16b99388ff27116c2f13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2066c06f07bae13919ec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2066c06f07bae13919ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aca93fbce02a17506c0e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aca93fbce02a17506c0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f35b20ee3c9f6b2c1752"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f35b20ee3c9f6b2c1752`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6fc544aa27bf7980f675"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6fc544aa27bf7980f675`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-056b8d029481aa557f89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-056b8d029481aa557f89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ab6624728e5e0f8a22d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3ab6624728e5e0f8a22d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d90abbc04920e17d14e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d90abbc04920e17d14e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae172b230fb26d508337"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ae172b230fb26d508337`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2e645a5c49d1b4a7ed5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b2e645a5c49d1b4a7ed5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69c53303f93f51b8cf14"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-69c53303f93f51b8cf14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-327a9e05d292dc838a21"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-327a9e05d292dc838a21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a519037092d0043950d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2a519037092d0043950d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd1ebc5f1f01c48816aa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dd1ebc5f1f01c48816aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-797d99b17f6823fa761f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-797d99b17f6823fa761f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ef6b94a477a5f9c88150"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ef6b94a477a5f9c88150`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6175dd771bb6abf380b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d6175dd771bb6abf380b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d85db220152629b9cc7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9d85db220152629b9cc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2b44b2387e3c31158e4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f2b44b2387e3c31158e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-295a7ba854c5e124841e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-295a7ba854c5e124841e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cb32b7e908adaf85368"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8cb32b7e908adaf85368`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c2743e52f9f5e2497d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1c2743e52f9f5e2497d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00b3060068388863804c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-00b3060068388863804c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3c0ee1a320ff0711fbe7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3c0ee1a320ff0711fbe7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd5968fb4ae93e163723"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dd5968fb4ae93e163723`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbcd093b9424b71fbddc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fbcd093b9424b71fbddc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8d8c30685da1dff07f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d8d8c30685da1dff07f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7206d18e03bc420b2e9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7206d18e03bc420b2e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55337717e46c7d492704"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-55337717e46c7d492704`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-368ae3ad47daf6750c9b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-368ae3ad47daf6750c9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c89dd1c20c27a8e08d91"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c89dd1c20c27a8e08d91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-abe081a58257106eb7ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-abe081a58257106eb7ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4ea98927a2a4e294a09"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d4ea98927a2a4e294a09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85502297af0c89193735"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-85502297af0c89193735`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7dc61e20689840804e75"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7dc61e20689840804e75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-776edbcc2cd0c13d388d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-776edbcc2cd0c13d388d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-781642974c3da8e57574"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-781642974c3da8e57574`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34d8c393ca13f58ae28c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-34d8c393ca13f58ae28c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b622cb31b5d06452de0e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b622cb31b5d06452de0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-765c07d78ff03c68f1c0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-765c07d78ff03c68f1c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09ddd4cfb7f366f8fe54"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-09ddd4cfb7f366f8fe54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9afe2718acf5de3eded"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c9afe2718acf5de3eded`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df3d922db41cf887c981"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-df3d922db41cf887c981`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c552b30dc442ab16eeeb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c552b30dc442ab16eeeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c804ef5fa431bd450c8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8c804ef5fa431bd450c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-026f8b2bc66655a0a3c9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-026f8b2bc66655a0a3c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f194743d2d7bdd11022"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6f194743d2d7bdd11022`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c0393bcf9403b2632940"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c0393bcf9403b2632940`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8303ef2615f96a65274d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8303ef2615f96a65274d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90e05d2c1e22dc2c19ac"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-90e05d2c1e22dc2c19ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ab989be88a1a43c7fb4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ab989be88a1a43c7fb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-133d082731da024513a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-133d082731da024513a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f22099f3855e55773052"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f22099f3855e55773052`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe3857f2b60fbc7ef184"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fe3857f2b60fbc7ef184`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0326a002b25463a3646d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0326a002b25463a3646d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eae771e6ca09918eb90b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eae771e6ca09918eb90b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-689284558ef45b36764f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-689284558ef45b36764f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d491fed2090b63ddace"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7d491fed2090b63ddace`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49281dfd1d1ca4c7beed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-49281dfd1d1ca4c7beed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ff748904afc0ccb0dc38"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ff748904afc0ccb0dc38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bdeb1e800245abd48826"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bdeb1e800245abd48826`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-419261a48a77a4e5199c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-419261a48a77a4e5199c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-174ab0596d76cd84cc4b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-174ab0596d76cd84cc4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ff5bb095da905b20fff6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ff5bb095da905b20fff6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc1a86a1e8c5bb06baa3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bc1a86a1e8c5bb06baa3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a167d4f8f0fe248da65"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2a167d4f8f0fe248da65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9cc06dff225af1f3590"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a9cc06dff225af1f3590`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1c8d3ca5a2b07415e07d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1c8d3ca5a2b07415e07d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4eca963c849a55c169b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d4eca963c849a55c169b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eda107e36a511ab05e42"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eda107e36a511ab05e42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7645bc85ad3d4895c290"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7645bc85ad3d4895c290`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8d50c424526e5e4cc930"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8d50c424526e5e4cc930`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf9d6668d4b0a361a938"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf9d6668d4b0a361a938`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-495edc05d33772f4e281"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-495edc05d33772f4e281`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-240ef55e6029905e7aad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-240ef55e6029905e7aad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8d8d7141b6506297d860"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8d8d7141b6506297d860`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-628613f3b05476a4eabb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-628613f3b05476a4eabb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ab998672c5ff45ce15c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2ab998672c5ff45ce15c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e9efa8d61bc3686c4ec"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3e9efa8d61bc3686c4ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1b0b157eb93980cf65e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1b0b157eb93980cf65e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99a315bceb3a9c8feb37"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-99a315bceb3a9c8feb37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7acc4c7dde1bf8f266e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a7acc4c7dde1bf8f266e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb85227db97c059fb045"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eb85227db97c059fb045`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bd2bb01c9da1f7b29793"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bd2bb01c9da1f7b29793`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9627112489ff57e4c661"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9627112489ff57e4c661`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-301c2f445b375fcd853c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-301c2f445b375fcd853c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b7dbdce2cafc2ca8c07"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b7dbdce2cafc2ca8c07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-743e6844e360d6895f18"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-743e6844e360d6895f18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2326af372aa2a6c757a0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2326af372aa2a6c757a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8f064a8f32b7af23526"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b8f064a8f32b7af23526`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af0495de180e245fa689"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af0495de180e245fa689`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-38e22eb31981063f24c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-38e22eb31981063f24c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a099e03ef754108fda3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5a099e03ef754108fda3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e64438d8390a362bd59b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e64438d8390a362bd59b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db1a89101df4416e0fdd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-db1a89101df4416e0fdd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8c50078e691691fe1302"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8c50078e691691fe1302`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7269e56ccb699c477fc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c7269e56ccb699c477fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31646cff4191c66bac7a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-31646cff4191c66bac7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfc41f2f86c5b4e19d0d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dfc41f2f86c5b4e19d0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a452e7518c65c12268e9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a452e7518c65c12268e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77ef180c2378948523f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-77ef180c2378948523f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56beaec8a31ad9c7ecf7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-56beaec8a31ad9c7ecf7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b424805d927c9551f0a7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b424805d927c9551f0a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1e604eb97c47a123ea01"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e604eb97c47a123ea01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac9034143a14bfaa90e4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ac9034143a14bfaa90e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd659025a454f77c1558"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bd659025a454f77c1558`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04e4637e5a402439e5b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-04e4637e5a402439e5b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-826b7026493282d15929"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-826b7026493282d15929`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a019a8b33c0cb424e64"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2a019a8b33c0cb424e64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1642288033834c6b8f34"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1642288033834c6b8f34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee2c495f7d3836028949"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee2c495f7d3836028949`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5e552d991a5ef7b65e77"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5e552d991a5ef7b65e77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a4dde35fe4dcb16c773"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a4dde35fe4dcb16c773`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11c30021bbde25f5647d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-11c30021bbde25f5647d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0cd0f7f85aa8dff5db47"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0cd0f7f85aa8dff5db47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7effd46e6e6a622f45e1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7effd46e6e6a622f45e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c564a263ef6beedae89b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c564a263ef6beedae89b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fcb9c0380e397e88fd39"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fcb9c0380e397e88fd39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cdfe6fce352f72e9f81"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2cdfe6fce352f72e9f81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c5691e21fa3c0ea179f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c5691e21fa3c0ea179f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-705f3f4c11fc545091d9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-705f3f4c11fc545091d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1521887c84d372e2be7a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1521887c84d372e2be7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d67df34cb51b1b37c94"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7d67df34cb51b1b37c94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f138a03d709ff98decdc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f138a03d709ff98decdc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-007c840b7efeccfd1d06"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-007c840b7efeccfd1d06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-697f906c75d3f2b0de8e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-697f906c75d3f2b0de8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b84ba9af2674af8c18b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2b84ba9af2674af8c18b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1aca73f9a6c0a5a87a8d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1aca73f9a6c0a5a87a8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d17a67452253723db9d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9d17a67452253723db9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd9a8b9e3b68c08f413e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cd9a8b9e3b68c08f413e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-757bebf609c6e7c9693f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-757bebf609c6e7c9693f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4190a1998d76d8a0f435"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4190a1998d76d8a0f435`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11554e130c2c0bfb2fbb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-11554e130c2c0bfb2fbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aaf963ae1430bd93dc68"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aaf963ae1430bd93dc68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa72b91198f1d15d5396"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa72b91198f1d15d5396`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4412091f6b63169848a1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4412091f6b63169848a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90ee4b314fb42f027394"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-90ee4b314fb42f027394`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fa4c2c734cc427b1e86"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1fa4c2c734cc427b1e86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e13c755ec04df7a1cfca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e13c755ec04df7a1cfca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-da0904dbfc8a22fd3fe6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-da0904dbfc8a22fd3fe6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1b4e32fe444eeec8d59"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f1b4e32fe444eeec8d59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38f91b6ec72c79e0cdaa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-38f91b6ec72c79e0cdaa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f50a41e9b3a18d4d5e69"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f50a41e9b3a18d4d5e69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41671e38988a42f7df9a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41671e38988a42f7df9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec5c525b997c700fd0be"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ec5c525b997c700fd0be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cd5facde3b43ce4ab58"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7cd5facde3b43ce4ab58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26520df2770e0b57bb57"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-26520df2770e0b57bb57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4adc842bb215f378b14d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4adc842bb215f378b14d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c41ac15009cd7907a95d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c41ac15009cd7907a95d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-667b8c866dc82c51a0d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-667b8c866dc82c51a0d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71a965b58555e1047b21"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-71a965b58555e1047b21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-67e3110ee01f9c0d53fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-67e3110ee01f9c0d53fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5cc7605365ff1ba1a421"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5cc7605365ff1ba1a421`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-955ca34b0e09e8f37850"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-955ca34b0e09e8f37850`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3aee44210a74c860e4b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f3aee44210a74c860e4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-908600122a9da7766a17"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-908600122a9da7766a17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0e96c0ba8b8fa47d6c6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a0e96c0ba8b8fa47d6c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c8f5073a90a9112493e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c8f5073a90a9112493e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab76ee570f63084e7f64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab76ee570f63084e7f64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5bd30f37502e0bac21d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5bd30f37502e0bac21d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9520f2583dffad3083ed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9520f2583dffad3083ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5097477f84817efbaf08"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5097477f84817efbaf08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffd5e61bfca96db3c90f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ffd5e61bfca96db3c90f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-85ee76a0db681cd7b235"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-85ee76a0db681cd7b235`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81771efab20fc7b204d6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-81771efab20fc7b204d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4d46c68956f97f74c70"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c4d46c68956f97f74c70`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f27fc4e265b942362d5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f27fc4e265b942362d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fa78c4f5a8d43fd49094"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fa78c4f5a8d43fd49094`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44bfe437ac0f55cac917"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-44bfe437ac0f55cac917`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09d7a17c3b006bc65ce3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-09d7a17c3b006bc65ce3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f92291efa8b1d849729"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7f92291efa8b1d849729`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b9e7ae44b387e9c2ae99"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b9e7ae44b387e9c2ae99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4676457c0d821886de28"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4676457c0d821886de28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81e30a9b409cd9cc108b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-81e30a9b409cd9cc108b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0df1535cf632369a3bd7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0df1535cf632369a3bd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f2b5fe81dbeb27519ccf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2b5fe81dbeb27519ccf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9012cfe7cfe537e2ebe3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9012cfe7cfe537e2ebe3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-218f57dcc47c6e4543e7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-218f57dcc47c6e4543e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37a25404b5dcd6b70110"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-37a25404b5dcd6b70110`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5ca8da5cb054d526cbde"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5ca8da5cb054d526cbde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c86e7d1982acb1104c9f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c86e7d1982acb1104c9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2e75ea90810fb231bd0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2e75ea90810fb231bd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7749ca931374cd7a655f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7749ca931374cd7a655f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7769e285916862ed21d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7769e285916862ed21d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f097ac0ec1a369c4647a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f097ac0ec1a369c4647a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e672d7c219225ff29731"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e672d7c219225ff29731`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db8089fca774ffeb8a37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-db8089fca774ffeb8a37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2806bbea7b92a0dc7e59"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2806bbea7b92a0dc7e59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2196149160a41de17762"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2196149160a41de17762`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4370a489086b30760b04"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4370a489086b30760b04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf70fe52d53417359b9f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bf70fe52d53417359b9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1cf09e6f4a9970607302"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1cf09e6f4a9970607302`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d82115a48f9ff19ae2d8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d82115a48f9ff19ae2d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b28c15f185d17f51d54"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4b28c15f185d17f51d54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-681808973c06e183f88e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-681808973c06e183f88e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b2e0bb0fd288487d53e9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b2e0bb0fd288487d53e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-221d6c194a9d33b95571"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-221d6c194a9d33b95571`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7ce5938a2c9a24467b6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b7ce5938a2c9a24467b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd97403a239a002003a0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd97403a239a002003a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b01fea6c52e386862669"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b01fea6c52e386862669`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4997d6ed82b1f39ccd35"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4997d6ed82b1f39ccd35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82c5029d57072640fcd7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-82c5029d57072640fcd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee6ddf2cccab326aae41"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee6ddf2cccab326aae41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e1056fa308860651f207"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e1056fa308860651f207`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87db03b2521301d34706"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-87db03b2521301d34706`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-203a1608ef6ae2c2a054"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-203a1608ef6ae2c2a054`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83fbfa3c94440a574ad9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-83fbfa3c94440a574ad9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8cb44e8879189e9de427"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8cb44e8879189e9de427`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca1aa72a7cebfb336dff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ca1aa72a7cebfb336dff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-698c36816bc5cabb53cd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-698c36816bc5cabb53cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30b05ab85d69d9229055"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-30b05ab85d69d9229055`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ac4238d2a431a407e572"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac4238d2a431a407e572`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ae00bcab569118eb710"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ae00bcab569118eb710`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ee012c7bb60a71ac998"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3ee012c7bb60a71ac998`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65f009c31ff397713f5e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-65f009c31ff397713f5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ac2706a2e65d5e508278"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac2706a2e65d5e508278`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9596ade64565faff65cd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9596ade64565faff65cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fa8e2f7800fb103ace8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5fa8e2f7800fb103ace8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e7732fbff78c0df103f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e7732fbff78c0df103f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5aabaae6a573b8be1f3f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5aabaae6a573b8be1f3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c4f6a84277ee30c386f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1c4f6a84277ee30c386f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3990ad5c372dd6e14b26"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3990ad5c372dd6e14b26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-823a53d64b4a77e111e0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-823a53d64b4a77e111e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-980ec6e52717e1a50eef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-980ec6e52717e1a50eef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f08f1b38029075ff7dc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9f08f1b38029075ff7dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cda46e768b1232be285f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cda46e768b1232be285f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14da7ed23831d1260eab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-14da7ed23831d1260eab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ddf098c539b1c731d38"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ddf098c539b1c731d38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82614956212d81088dae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-82614956212d81088dae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab38fba6f05f8366a3b0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ab38fba6f05f8366a3b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a99ec58374e63652fae3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a99ec58374e63652fae3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c79c6b2543b4a577ea48"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c79c6b2543b4a577ea48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39379c812bc602aa88e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-39379c812bc602aa88e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb7d6e7de2cfdcb55976"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bb7d6e7de2cfdcb55976`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64488667ea7c5c511ffb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64488667ea7c5c511ffb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-04370f13a9a453659e1f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-04370f13a9a453659e1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b29ce296c34317ad4f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5b29ce296c34317ad4f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f045c04774a885a7b56e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f045c04774a885a7b56e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f0e06a3d7002710221a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8f0e06a3d7002710221a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0eba6436d8588e7309ad"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0eba6436d8588e7309ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18bc2fb6c79dbb22f734"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-18bc2fb6c79dbb22f734`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eec39a128ac03c017fa5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eec39a128ac03c017fa5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0cded9aead8fed8d35dd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0cded9aead8fed8d35dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6f0963a94ffc5027f98e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6f0963a94ffc5027f98e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-050bb4ac0cb97f8a2152"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-050bb4ac0cb97f8a2152`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e41fa545cfa28b116fbd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e41fa545cfa28b116fbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-683cc47a67831a50b8da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-683cc47a67831a50b8da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-df9d96ea827e4d8b1870"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-df9d96ea827e4d8b1870`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0cd34f26720936bf4bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d0cd34f26720936bf4bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f590bd37ca1bb460965"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f590bd37ca1bb460965`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-301dad8087da450d24c3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-301dad8087da450d24c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2ae3bb2a4ffbb5a30f5a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2ae3bb2a4ffbb5a30f5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9347b67bbc394ab2f3e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9347b67bbc394ab2f3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0c9cf690883faf8319a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a0c9cf690883faf8319a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-def9be4270c39eec5ea2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-def9be4270c39eec5ea2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5b382d26aaee091f237f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5b382d26aaee091f237f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bab1b9c512252d597d9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9bab1b9c512252d597d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-696ff7f0fbf973fc6b6c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-696ff7f0fbf973fc6b6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4fefe5aa04679dc06da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e4fefe5aa04679dc06da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-84592b7d791e93ec029b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-84592b7d791e93ec029b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2640150cb30fa57b633"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a2640150cb30fa57b633`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4807e44be265d489fdd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f4807e44be265d489fdd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00f62828256241b63085"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-00f62828256241b63085`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-85e558721ed957d1763b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-85e558721ed957d1763b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c1fcb897f4017584779"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6c1fcb897f4017584779`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3abf5a635d007cdfa17"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e3abf5a635d007cdfa17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f7119c8b826af615c15"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f7119c8b826af615c15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6e92c288ad287dcdde22"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e92c288ad287dcdde22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9261dff2c42d5f85d09"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d9261dff2c42d5f85d09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15b4a9c9fa320acbda37"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-15b4a9c9fa320acbda37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a61e55de6e2fa8eaf090"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a61e55de6e2fa8eaf090`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2f4932fa67c1bb8270b7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2f4932fa67c1bb8270b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bfed6f199d46e43106f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0bfed6f199d46e43106f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc96360ada7ae8f4a293"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc96360ada7ae8f4a293`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f59071cd620c46ffcbd4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f59071cd620c46ffcbd4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dc11ceb6db5cefd0044b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dc11ceb6db5cefd0044b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9d12d713c30ca20a8d5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b9d12d713c30ca20a8d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c227b3f78e36730d740b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c227b3f78e36730d740b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63bace4ed753b48e411e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-63bace4ed753b48e411e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bd15febcbb179a574191"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bd15febcbb179a574191`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a401576c6fde01a57e80"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a401576c6fde01a57e80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8289e11c8006430464f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a8289e11c8006430464f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96e3772beaf9a01df0c2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-96e3772beaf9a01df0c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-240ddf1acc65ce7f44ce"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-240ddf1acc65ce7f44ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2fc89a9cb2bef9bd55b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b2fc89a9cb2bef9bd55b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee855117978c66bce228"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee855117978c66bce228`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f37593f808fd39e1e05"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2f37593f808fd39e1e05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c6a1b5f3c88adde14c53"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c6a1b5f3c88adde14c53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b35508e59b670438db44"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b35508e59b670438db44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-204bde1130173af93f57"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-204bde1130173af93f57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b17752df360601bd65e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9b17752df360601bd65e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-db36c9aa52386010e8b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-db36c9aa52386010e8b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-200c3eb01343e371bd3c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-200c3eb01343e371bd3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-645c96667a7fdd62f118"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-645c96667a7fdd62f118`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f3b2f0ad59cbd33e6a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f3b2f0ad59cbd33e6a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a37b709bf95ef9617642"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a37b709bf95ef9617642`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d8e89a3ec042821c619"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7d8e89a3ec042821c619`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ab1dbf9aead7413d2cc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ab1dbf9aead7413d2cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58697aef9ba8e9ad2a3c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-58697aef9ba8e9ad2a3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8e6698f01db3bb19ff00"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8e6698f01db3bb19ff00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07ae5b55ec8334af6ff8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-07ae5b55ec8334af6ff8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c799d6b4abd6b8901508"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c799d6b4abd6b8901508`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41994faa18a631954270"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-41994faa18a631954270`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d64234eee80aaaea5342"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d64234eee80aaaea5342`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c24583d6331354e5e522"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c24583d6331354e5e522`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-962c2446a0edac8edbd5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-962c2446a0edac8edbd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bc324cd00b21b3bf396"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6bc324cd00b21b3bf396`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a328135a0d3ab4c52481"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a328135a0d3ab4c52481`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26fb973a082f05fa6b03"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-26fb973a082f05fa6b03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f712cce5027be67d6e1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1f712cce5027be67d6e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36d9775dba1c1d8d1199"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-36d9775dba1c1d8d1199`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4c6745d388cae96ca312"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4c6745d388cae96ca312`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35364b532ed11c3360b4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-35364b532ed11c3360b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32117e821618519e98b0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-32117e821618519e98b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55964b771769cfa6fac2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-55964b771769cfa6fac2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fb74ba1997cd3a3a90a2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fb74ba1997cd3a3a90a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-950352a55f6522a10db4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-950352a55f6522a10db4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25befe6c07b37524c856"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-25befe6c07b37524c856`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-181b5d7a0c9194b469f0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-181b5d7a0c9194b469f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a72e867676e07de5da9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a72e867676e07de5da9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92f3657b38017311d3f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-92f3657b38017311d3f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98c843c890c18611ee56"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-98c843c890c18611ee56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9af7193a34b1da5d5741"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9af7193a34b1da5d5741`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d0ade269eb4fefbf1e59"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0ade269eb4fefbf1e59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64547ab9d35f4579b12f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-64547ab9d35f4579b12f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6167f93a65b81f9cc859"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6167f93a65b81f9cc859`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72f915dac5674a22de83"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-72f915dac5674a22de83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-36a017fcc806f2e0b3e1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-36a017fcc806f2e0b3e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b09b3c3248150f6d45dd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b09b3c3248150f6d45dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffa87494aa9519d59874"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ffa87494aa9519d59874`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-680a5c0676575e3ee02a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-680a5c0676575e3ee02a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-111c9922ee430d9989f3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-111c9922ee430d9989f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52910447738c3b76a38e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-52910447738c3b76a38e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db5a02353b4f3b59687d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-db5a02353b4f3b59687d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0e2ebc13d6d522218a0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f0e2ebc13d6d522218a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ae81b3802e5a35a41f69"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ae81b3802e5a35a41f69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f2dc342ae39a19817ae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4f2dc342ae39a19817ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74e394c9f6a0e3d891aa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-74e394c9f6a0e3d891aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-facf2191450ba3f47240"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-facf2191450ba3f47240`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-46b344e9e4d5cf469d62"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-46b344e9e4d5cf469d62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cef4fe0f83ddca0bb6d3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cef4fe0f83ddca0bb6d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a39ee67f63d9602dd968"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a39ee67f63d9602dd968`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5199a4cb9a957ea31bb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f5199a4cb9a957ea31bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a8dbada50759287a74bd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a8dbada50759287a74bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ceb492ff0a038eb4236f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ceb492ff0a038eb4236f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9136de2981bec5240f2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a9136de2981bec5240f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a9f2a9320c57d3a6db1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a9f2a9320c57d3a6db1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ee720a8581d331d6467"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ee720a8581d331d6467`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6cd6cad41b2c9bf599f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a6cd6cad41b2c9bf599f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-216b70dbb1e22b22de43"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-216b70dbb1e22b22de43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34b70a6d60fe994a51fc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-34b70a6d60fe994a51fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7127f1c479c187379b8f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7127f1c479c187379b8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8578e79f8e6bcf1bc8ad"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8578e79f8e6bcf1bc8ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5f9a55f5e1a73828453"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d5f9a55f5e1a73828453`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80119a7acdfd5f873a4c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-80119a7acdfd5f873a4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-49f1548094dd51b75b4b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-49f1548094dd51b75b4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-653d112ec0291a623a64"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-653d112ec0291a623a64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f0865c745122e663139"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9f0865c745122e663139`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7ac864550744e9fa252"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a7ac864550744e9fa252`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-699f3820ea852eb2d63d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-699f3820ea852eb2d63d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e20e2656970d5fdaf66d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e20e2656970d5fdaf66d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-895dbc71863f0361a8f5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-895dbc71863f0361a8f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1490dcf5fdebdb3912eb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1490dcf5fdebdb3912eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fdb22b3e81fd4c87fbe5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fdb22b3e81fd4c87fbe5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fbb68254f4d7c910cb1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9fbb68254f4d7c910cb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-073067f0edded9a52bad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-073067f0edded9a52bad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6b55dd72d9dbd147990"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b6b55dd72d9dbd147990`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8eaa6bfd3d6cacea80fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8eaa6bfd3d6cacea80fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0082523ce6f40d8374f2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0082523ce6f40d8374f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d849c4c4f8bdb1c0f647"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d849c4c4f8bdb1c0f647`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a35b9b1f6d9a871e62dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a35b9b1f6d9a871e62dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4e84c842ad6531e8167b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e84c842ad6531e8167b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bb0b7969f6aa68e9f5c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8bb0b7969f6aa68e9f5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e6bde6a3db67c21bf85"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4e6bde6a3db67c21bf85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc99aea4f28202d4f7af"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bc99aea4f28202d4f7af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9706c8a0f7b51f41db45"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9706c8a0f7b51f41db45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7e3007761abe4c1ef60"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a7e3007761abe4c1ef60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4687e328c103b82a5a6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e4687e328c103b82a5a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f8a3a3265b4f1fd3884"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2f8a3a3265b4f1fd3884`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-43f2444605adc333c1f7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-43f2444605adc333c1f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e475ff924f2148854340"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e475ff924f2148854340`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69ba50e9b90a769249cb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-69ba50e9b90a769249cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c5b756d52b8b4a48e15"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3c5b756d52b8b4a48e15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9554d93627b01a8427b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9554d93627b01a8427b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-600daee69ab0dde50734"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-600daee69ab0dde50734`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c323079ff5847f91387"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2c323079ff5847f91387`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15b1f5aa1024b5fba2fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-15b1f5aa1024b5fba2fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4dd9d4deff93af75cf2a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4dd9d4deff93af75cf2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff40cd8ecc3cc3636154"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ff40cd8ecc3cc3636154`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-837c82cd6a6b066efab3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-837c82cd6a6b066efab3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9868a8274839047c4573"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9868a8274839047c4573`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6e7541f6c5f06e168298"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e7541f6c5f06e168298`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-886c6d15fdd9228cfbd8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-886c6d15fdd9228cfbd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40422ab326cded3761d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-40422ab326cded3761d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03668bc249a7ab651f98"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03668bc249a7ab651f98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a713809d1da4bb01c2d6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a713809d1da4bb01c2d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2042d5209385039b2a35"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2042d5209385039b2a35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd7031fa2dd579c98553"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bd7031fa2dd579c98553`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fa4c12f667abe129733"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8fa4c12f667abe129733`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-468a517383f9f392fa94"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-468a517383f9f392fa94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9460cef532173a56f8dc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9460cef532173a56f8dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b0271f9170cab9afa0a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2b0271f9170cab9afa0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7837bda8eb9dd6e90728"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7837bda8eb9dd6e90728`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee0828238b6a1c5c4a6f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee0828238b6a1c5c4a6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0660679532a8114aa330"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0660679532a8114aa330`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64c6a39b16cb4b1f9def"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-64c6a39b16cb4b1f9def`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-960c2b52298b1623fe1b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-960c2b52298b1623fe1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-131920202fc31002eae0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-131920202fc31002eae0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94ec68f3bf5e3232b5c8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-94ec68f3bf5e3232b5c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b09ca288f05a251052f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b09ca288f05a251052f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a747e40fd2d4c5bc3dd7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a747e40fd2d4c5bc3dd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e288a942a8bc080303d2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e288a942a8bc080303d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b398838709296c268f54"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b398838709296c268f54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17328b101d4ef4c7868c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-17328b101d4ef4c7868c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d16e96cda686d5e75754"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d16e96cda686d5e75754`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-17ff4b8877e6a628dcfe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-17ff4b8877e6a628dcfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1787f9e73b346087831c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1787f9e73b346087831c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccf991d8a05429ab3c59"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ccf991d8a05429ab3c59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30ac1b7942b63586532f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-30ac1b7942b63586532f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bb76537a58e159abd75e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bb76537a58e159abd75e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c639e29e8bd4646107e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c639e29e8bd4646107e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1950a8ddc17970c60382"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1950a8ddc17970c60382`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64dc7b3c546358bbf77a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64dc7b3c546358bbf77a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a4307838a33d945c1a39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a4307838a33d945c1a39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82c8f370222dc9d1dc72"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-82c8f370222dc9d1dc72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-624ac541adfdba41f14f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-624ac541adfdba41f14f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f0c5cd110981b6ca5bf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2f0c5cd110981b6ca5bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-36c6d707423340056abf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-36c6d707423340056abf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-203dc1564d693afd7798"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-203dc1564d693afd7798`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51a62b123e31e6631066"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-51a62b123e31e6631066`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2be245610df2b2d68b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c2be245610df2b2d68b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aa776321ae6432d28da5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aa776321ae6432d28da5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c633bc51f2e7bdba195"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0c633bc51f2e7bdba195`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9e2722d78076ed03275"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e9e2722d78076ed03275`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d84c51676f3e0e41d7f6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d84c51676f3e0e41d7f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0674a15f0ddce6c8460d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0674a15f0ddce6c8460d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa2c6b6f395164df9c11"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aa2c6b6f395164df9c11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa61d17cf468aeae4539"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aa61d17cf468aeae4539`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e0973bc3f2dbabfe92a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e0973bc3f2dbabfe92a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-17aa94022721146e2f5c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-17aa94022721146e2f5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18c865f4c5ff78f527d2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-18c865f4c5ff78f527d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d2ddc35da5e4971bcdc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5d2ddc35da5e4971bcdc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15bd8451962e685cc5f0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-15bd8451962e685cc5f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e6cae6ec06f790c8d41c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e6cae6ec06f790c8d41c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-907df42a8ec85a9c14bb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-907df42a8ec85a9c14bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ea6e090175058fe62e0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3ea6e090175058fe62e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc507392cf26bba3bb66"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc507392cf26bba3bb66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-36d480a7f1097747dda5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-36d480a7f1097747dda5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-718910cd7692a9ba2cf4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-718910cd7692a9ba2cf4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b4e6907a1043aec2160"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2b4e6907a1043aec2160`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bdf41224631a3a353e54"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bdf41224631a3a353e54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ea33a1416249a3cf7ba2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ea33a1416249a3cf7ba2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df83d1156004f385d446"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-df83d1156004f385d446`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e99deed66d951d89c72"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4e99deed66d951d89c72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1037fd17fd7f70e2e64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c1037fd17fd7f70e2e64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e2f1ee31d361ea2baf9b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2f1ee31d361ea2baf9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65aa6e8103f88b9b3824"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-65aa6e8103f88b9b3824`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32b8c3c6d7b288ea3c6c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-32b8c3c6d7b288ea3c6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9592a23ea61659c01036"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9592a23ea61659c01036`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-76d784bd8914c187f6ae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-76d784bd8914c187f6ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ee01b696ac9a2d55369"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5ee01b696ac9a2d55369`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d21b4d0d5adc8dddbbe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8d21b4d0d5adc8dddbbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4511a9c3ee13c39f5bf7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4511a9c3ee13c39f5bf7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-46131f462e3331f1d0bd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-46131f462e3331f1d0bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e049bea9de7d1d8d1f71"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e049bea9de7d1d8d1f71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3a74f0b5eea9672fc53"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e3a74f0b5eea9672fc53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80b345310553da6416a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-80b345310553da6416a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-53e4cdd40f5c7b3eb936"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-53e4cdd40f5c7b3eb936`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f4436a0a107f6b91f12"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2f4436a0a107f6b91f12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be959d7c65ca03bfe6a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-be959d7c65ca03bfe6a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe5dda110a5c8db0e340"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe5dda110a5c8db0e340`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97f9f4968dfd7972b718"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97f9f4968dfd7972b718`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9ac54d32b314b623e61"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a9ac54d32b314b623e61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b9d9fd24a33cc5b835d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1b9d9fd24a33cc5b835d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-403611849b5a2d0d12fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-403611849b5a2d0d12fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-be8d5e8446e7e4c09ee7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-be8d5e8446e7e4c09ee7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cd62d93c42216269643"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4cd62d93c42216269643`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4baf8c783dad9a48ba8b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4baf8c783dad9a48ba8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5384761803d31a66316"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b5384761803d31a66316`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-abb93c66a9be730d7c32"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-abb93c66a9be730d7c32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26073c441d8b191fab18"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-26073c441d8b191fab18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e2a058c05d969adf23e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3e2a058c05d969adf23e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-958318acada37654f8a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-958318acada37654f8a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e93d6e32b1f365b1d7c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e93d6e32b1f365b1d7c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bb987ffe68ced1e6b2a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9bb987ffe68ced1e6b2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21dc08e8d91ae5552aa4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-21dc08e8d91ae5552aa4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9bce50a82730e1f8a4c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b9bce50a82730e1f8a4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-119167c72a3073f35ee3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-119167c72a3073f35ee3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c95643a939886e98c5ed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c95643a939886e98c5ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b692f3df01a3dbfb5aa3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b692f3df01a3dbfb5aa3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a9970b0099baea2457b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9a9970b0099baea2457b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bed17964042282b17915"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bed17964042282b17915`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a1d3a268d4834934279"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a1d3a268d4834934279`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b0db57306001166ed0a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6b0db57306001166ed0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2a9b12e205c1f0b5c50"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f2a9b12e205c1f0b5c50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-de0fd2f420f729a6df13"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de0fd2f420f729a6df13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0c55f1095125b8e7aa4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c0c55f1095125b8e7aa4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35fb969be0b7f04bda3c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-35fb969be0b7f04bda3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-960475667a3507592fed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-960475667a3507592fed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee6781511ad98710054e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee6781511ad98710054e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e35ceedeaba7b31d984f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e35ceedeaba7b31d984f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4eeb676ee8f42ba73a6c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4eeb676ee8f42ba73a6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bff703665307d4f864ba"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bff703665307d4f864ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f76499c93c543294c41c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f76499c93c543294c41c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe095b079553ee453db3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fe095b079553ee453db3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0e07f3c363412e0b1f8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c0e07f3c363412e0b1f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b264f7b5575d08ff8738"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b264f7b5575d08ff8738`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-920e82e46790759df0d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-920e82e46790759df0d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5c5996546c76c406635"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c5c5996546c76c406635`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4fd2b92fc900c764e39d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4fd2b92fc900c764e39d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10a86c1da31a5a04f0d0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10a86c1da31a5a04f0d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-73e3d4466b15e7702eb8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-73e3d4466b15e7702eb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d4dd7cd6c777fbf930c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2d4dd7cd6c777fbf930c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ecebd8c2331d05e833dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ecebd8c2331d05e833dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52b172d73c33bcbcb2cc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-52b172d73c33bcbcb2cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d585fc47ee2b4fd050ad"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d585fc47ee2b4fd050ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-274852b28ccac0ebd217"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-274852b28ccac0ebd217`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cd201277ff4abfcd632"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4cd201277ff4abfcd632`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-533413652cd6d95b730e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-533413652cd6d95b730e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7fac45f552e3d5856ade"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7fac45f552e3d5856ade`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4320fa05c5e11dd330a6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4320fa05c5e11dd330a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7ac671df1d07247afee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c7ac671df1d07247afee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-164e69298faa310acb03"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-164e69298faa310acb03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b5cb97b1874d25a9e108"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b5cb97b1874d25a9e108`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d606145b7b7c51adee01"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d606145b7b7c51adee01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ee801768b99a20cb620"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8ee801768b99a20cb620`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-098922bbd084333c0d84"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-098922bbd084333c0d84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a0309c234700d58e0d70"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a0309c234700d58e0d70`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afa97922cd172594627f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-afa97922cd172594627f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9a09619519c84e969b0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a9a09619519c84e969b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-adb3efc782aad1cdc704"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-adb3efc782aad1cdc704`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-641e134cc0a599cb58a0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-641e134cc0a599cb58a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ca51887769009ee8c72"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1ca51887769009ee8c72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cbbc732e5d48ce42629"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2cbbc732e5d48ce42629`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd6bd32b2c82bfea7f97"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd6bd32b2c82bfea7f97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3c8f70d80277fc331cbd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3c8f70d80277fc331cbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f29c62693a54a2b2e7d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8f29c62693a54a2b2e7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ce4ce74b2d318d64f62"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2ce4ce74b2d318d64f62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dc5659e4621cf46ea9d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0dc5659e4621cf46ea9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-85a0f58e930eb6f87318"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-85a0f58e930eb6f87318`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62d550e52695e5fa7f94"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-62d550e52695e5fa7f94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad86bd3d41f075b41f91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ad86bd3d41f075b41f91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71b3abf491f56eae2c4d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-71b3abf491f56eae2c4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f668104611a984310d8a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f668104611a984310d8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2debc9907d6123837202"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2debc9907d6123837202`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c64a9c9e7e6566c3067b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c64a9c9e7e6566c3067b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e59abd28eda49f7d2a24"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e59abd28eda49f7d2a24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cd51bc40d3ae281c7f14"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cd51bc40d3ae281c7f14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4840b951aab9fa2f28ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4840b951aab9fa2f28ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-339f71f1fc5230b27666"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-339f71f1fc5230b27666`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e06a6905d1a3f3c35258"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e06a6905d1a3f3c35258`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc1b22e4bdaa65cda2df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc1b22e4bdaa65cda2df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-908b351f1ca7ab8bea2a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-908b351f1ca7ab8bea2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9271da29596dfb3b41f9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9271da29596dfb3b41f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cd3896e69fa639bd37e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2cd3896e69fa639bd37e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5973737caefa170d7089"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5973737caefa170d7089`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5403360ec9e2edd12be"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b5403360ec9e2edd12be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f8a5effbbf054d30310"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7f8a5effbbf054d30310`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f4c0ce5d0b81d5376ee"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5f4c0ce5d0b81d5376ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-da1fc780889ebca3577e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-da1fc780889ebca3577e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e35cd3c1e9490f37955"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e35cd3c1e9490f37955`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bdc73cc104c4b1f847e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5bdc73cc104c4b1f847e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3dba075aa10cb9c9c068"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3dba075aa10cb9c9c068`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1efe25df8bfd5d009a99"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1efe25df8bfd5d009a99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e95e448ec2b0302bedd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1e95e448ec2b0302bedd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8511ba79d918d9acea4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a8511ba79d918d9acea4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-081181de90c8a8f77755"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-081181de90c8a8f77755`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-54bbbcf72fe06a6c8c43"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-54bbbcf72fe06a6c8c43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a857557634e9dea2e7e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4a857557634e9dea2e7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-115b34851f6bb2b9bed4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-115b34851f6bb2b9bed4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f54ce32c82a9fc597aec"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f54ce32c82a9fc597aec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c5e51f2e2239b27fd63b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5e51f2e2239b27fd63b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a5b490424e88111ca97"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4a5b490424e88111ca97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8d0290eb8e01f377c03"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e8d0290eb8e01f377c03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83c1167025a340fa2787"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-83c1167025a340fa2787`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca69fb83b4d8259a25ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca69fb83b4d8259a25ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19623d06928324e1efe3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-19623d06928324e1efe3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-890b9027b5a637c8aef8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-890b9027b5a637c8aef8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd40571159bfbd19bc93"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bd40571159bfbd19bc93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2677b4611391ee88a21d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2677b4611391ee88a21d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22df443ff34724f1de9f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-22df443ff34724f1de9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12b127cdb8e64c11e14a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-12b127cdb8e64c11e14a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff92149e97de1009e70f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ff92149e97de1009e70f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-54bcb62ac8216dc2f358"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-54bcb62ac8216dc2f358`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ad14bcd51498ace4fff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7ad14bcd51498ace4fff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9caddee8618c12610851"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9caddee8618c12610851`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84e654a366e25277a240"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-84e654a366e25277a240`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ee037c5f3f3ab9a8621"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ee037c5f3f3ab9a8621`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46f668cb98b4a2d9286d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-46f668cb98b4a2d9286d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4f4ed4099f09468eeef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a4f4ed4099f09468eeef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d681c9249f8960255bd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4d681c9249f8960255bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b917633fba949c84058c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b917633fba949c84058c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-adb086138d9286793378"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-adb086138d9286793378`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-825ff0189daf3aeb3d37"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-825ff0189daf3aeb3d37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95fb5615aecd02372c8d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-95fb5615aecd02372c8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0bdd24b4196fa9534095"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0bdd24b4196fa9534095`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54b776c952d3a39a76cd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-54b776c952d3a39a76cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4fd24e0e57e0e7873b51"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4fd24e0e57e0e7873b51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7594797601b7f54fdab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c7594797601b7f54fdab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1154790c59257704290f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1154790c59257704290f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83e49c59619d9af88521"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-83e49c59619d9af88521`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-920f1196479e9619c818"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-920f1196479e9619c818`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a301d4eadc6dbc52deef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a301d4eadc6dbc52deef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-74bdd56f26f0e208679e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-74bdd56f26f0e208679e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-764764c6d9dd882ab197"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-764764c6d9dd882ab197`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-beae4bbe469cf96ea5c0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-beae4bbe469cf96ea5c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55198867813d2363dd1d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-55198867813d2363dd1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-29e99877325d33679514"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-29e99877325d33679514`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c3fc255a0772560dc6a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c3fc255a0772560dc6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb5729cfe2ab3da142ea"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cb5729cfe2ab3da142ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c28b05e5060eab3913ef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c28b05e5060eab3913ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ced193f54e68fd95f7b0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ced193f54e68fd95f7b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7d4276a0de33ac80718"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e7d4276a0de33ac80718`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1d77a28f9620de0eed9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f1d77a28f9620de0eed9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfada8205e90d41d8511"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bfada8205e90d41d8511`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f2127aac3c67f85f97bf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2127aac3c67f85f97bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b68128a49e8a0e4878ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b68128a49e8a0e4878ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbdf438c43a049f89754"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bbdf438c43a049f89754`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-151a569098d1fe85ad14"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-151a569098d1fe85ad14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-df4519992c0e8806aae2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-df4519992c0e8806aae2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cae672e3ca2506814189"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cae672e3ca2506814189`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ccf9ada60f07ddae5d9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0ccf9ada60f07ddae5d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9ee1e9a414ec1a35522"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f9ee1e9a414ec1a35522`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8eb995e454acf0795ce7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8eb995e454acf0795ce7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f84332da803e2b4884f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0f84332da803e2b4884f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac4936cbc899ed88f96a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ac4936cbc899ed88f96a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40b0152030a9bdb2b86d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40b0152030a9bdb2b86d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7bbfe87a073de3bd8341"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7bbfe87a073de3bd8341`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bad2e6a6b3e1eed5505d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bad2e6a6b3e1eed5505d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cff0e6cba772dde3bb12"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cff0e6cba772dde3bb12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-591f536d9995c3e54e9e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-591f536d9995c3e54e9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9ca61069352fd02df1ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9ca61069352fd02df1ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6de651efa8fb49f258e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6de651efa8fb49f258e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c750e6515fdef1b1a6fe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c750e6515fdef1b1a6fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-026e6a162a17e3daceaf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-026e6a162a17e3daceaf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a92394c84ade817c029"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a92394c84ade817c029`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-985051926ce8f2d87910"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-985051926ce8f2d87910`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81ca7f2180b035ff12c5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-81ca7f2180b035ff12c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e16c41d44151a3402bea"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e16c41d44151a3402bea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b8fed7c0ad51bc788f11"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8fed7c0ad51bc788f11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3916bce32d7d5e76daea"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3916bce32d7d5e76daea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d78bf51b6f652c195ac"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2d78bf51b6f652c195ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-022e136eb78d83d52e18"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-022e136eb78d83d52e18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a4ba4603faac76000a3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a4ba4603faac76000a3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5e330b965cebaa8036d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f5e330b965cebaa8036d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f570349c40d663532d53"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f570349c40d663532d53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92fd62c4c2758eb2ef2b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92fd62c4c2758eb2ef2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-20b32308856f6a1cd553"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-20b32308856f6a1cd553`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37df628814782876a6a0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-37df628814782876a6a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4eee836bc0c58f021984"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4eee836bc0c58f021984`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f5566bb71d2b8c3a22e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1f5566bb71d2b8c3a22e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-662f85a215cf60f6221b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-662f85a215cf60f6221b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6884c975a8cac3cc2e5a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6884c975a8cac3cc2e5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a84a00af919992f0e88"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5a84a00af919992f0e88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-487fb17855e400aeece2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-487fb17855e400aeece2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-193f49cf5761125ef747"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-193f49cf5761125ef747`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2ca386a9f8d03e47239"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c2ca386a9f8d03e47239`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9dab15776dd1bc1e28c8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9dab15776dd1bc1e28c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5002967d39161fbec22d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5002967d39161fbec22d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-52008417c8ec5b3039aa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-52008417c8ec5b3039aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae360309e46d25114add"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ae360309e46d25114add`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-083bc9e2287bd9d36b56"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-083bc9e2287bd9d36b56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18be5bf715a3b72baab9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-18be5bf715a3b72baab9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-39e6823ac9f634d5697c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-39e6823ac9f634d5697c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f528c1f6a6431e6b970d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f528c1f6a6431e6b970d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c90c8ee4a61c28b9290e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c90c8ee4a61c28b9290e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2947239dabc7f16b6f22"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2947239dabc7f16b6f22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-53e3d3150f9608f41b1a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-53e3d3150f9608f41b1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26d5104aaafcfaacbfc9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-26d5104aaafcfaacbfc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6ed3629655e805059b6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a6ed3629655e805059b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aeeec373097106df5136"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aeeec373097106df5136`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-46c05953192b74dd1488"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-46c05953192b74dd1488`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83a63ac136b6a0ab35d7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-83a63ac136b6a0ab35d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d115eb06e86464b30cc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6d115eb06e86464b30cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3d7242f9848ce395db4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b3d7242f9848ce395db4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3fcc56c12b02b1c7f05f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3fcc56c12b02b1c7f05f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44dfade06d166f3814b4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-44dfade06d166f3814b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51be61a38abb6da5dbf6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-51be61a38abb6da5dbf6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e54f55e8a09b430d3062"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e54f55e8a09b430d3062`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-125ce6e6efc930942a78"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-125ce6e6efc930942a78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da34023bbcffabd4f0e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-da34023bbcffabd4f0e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23805ee2a8cafdb43319"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-23805ee2a8cafdb43319`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d95faa5db7ff20f6fb22"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d95faa5db7ff20f6fb22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bbc4fc12da7b3ae8d000"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bbc4fc12da7b3ae8d000`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2bd62cc52314285a02c9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2bd62cc52314285a02c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff4323dfb29f2e740e7a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ff4323dfb29f2e740e7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a955e13e7ba77ada201"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a955e13e7ba77ada201`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d306e8e25bcad7a144d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d306e8e25bcad7a144d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b0a29304556153ef4f0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9b0a29304556153ef4f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95e8dfa0c004480130a8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-95e8dfa0c004480130a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-100de4e565eee5f6e31e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-100de4e565eee5f6e31e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-96511a3ce553f2340937"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-96511a3ce553f2340937`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62d1712e8097b55585f5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-62d1712e8097b55585f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6283e8c5fad984f1c53d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6283e8c5fad984f1c53d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66ead1ada0bb80f54acf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-66ead1ada0bb80f54acf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d5d8de45a97f2ab49366"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d5d8de45a97f2ab49366`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3bd684e6f68b94754790"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3bd684e6f68b94754790`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4215868fd604569d2b7b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4215868fd604569d2b7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e79ef5c9aa17613ec52"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7e79ef5c9aa17613ec52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-15-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-25f508f3c004e9a84a80"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-25f508f3c004e9a84a80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67c28f501e3f10ed66ce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67c28f501e3f10ed66ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc289f2a1331b8a36d04"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dc289f2a1331b8a36d04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e990b91c2371a2a951c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e990b91c2371a2a951c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-15-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-entry-slip:canonical-southeast | <a href="#case-preview_review-7e57d8f05ec259ca283a">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-entry-slip:canonical-top | <a href="#case-preview_review-c175eb019679196ddd2f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-entry-slip:connection-overview | <a href="#case-preview_review-71e3e2c30e8f180e5812">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-entry-slip:canonical-southeast</summary>

<a id="case-preview_review-7e57d8f05ec259ca283a"></a>

**General: unverified** — `preview_review-7e57d8f05ec259ca283a`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-entry-slip:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-entry-slip:canonical-top</summary>

<a id="case-preview_review-c175eb019679196ddd2f"></a>

**General: unverified** — `preview_review-c175eb019679196ddd2f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-entry-slip:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-entry-slip:connection-overview</summary>

<a id="case-preview_review-71e3e2c30e8f180e5812"></a>

**General: unverified** — `preview_review-71e3e2c30e8f180e5812`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-entry-slip:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the slip function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
