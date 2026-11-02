---
title: "Testing: DD RHW-4 \u2014 L2 Exit Slip Lanes \u2014 Parallel \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L2 Exit Slip Lanes — Parallel — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **DD RHW-4 — L2 Exit Slip Lanes — Parallel — Alignment B**, permanent ID `ddrhw-parallel-b-upper-exit-slip`, as **P06** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 3 cells inside its 3 × 3 bounding footprint. Both native decks at 7.5 m and 15 m; the named access is at 15 m. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-15-out` | road / 1 / primary | out | [-8.0, -35.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -35.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-16-out` | road / 1 / primary | out | [-8.0, -28.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-02-in` | road / 1 / primary | in | [-8.0, -28.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-03-in` | road / 1 / primary | in | [-3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-17-out` | road / 1 / primary | out | [-3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-04-in` | road / 1 / primary | in | [3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-18-out` | road / 1 / primary | out | [3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-19-out` | road / 1 / primary | out | [8.0, -24.671746, 15.0]; [0.9918914891233439, 0.1270876618900333]; 0.0 | `path-interface-dfc49a604de1ebc10b30` |
| `channel-20-out` | road / 1 / primary | out | [8.0, -19.2, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-05-in` | road / 1 / primary | in | [8.0, -19.2, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-21-out` | road / 1 / primary | out | [8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-06-in` | road / 1 / primary | in | [8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-07-in` | road / 1 / primary | in | [12.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-22-out` | road / 1 / primary | out | [12.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-08-in` | road / 1 / primary | in | [16.265154, -24.0, 15.0]; [0.9227775912579843, 0.38533299504728696]; 0.0 | `path-interface-2575dc74752582c1c38f` |
| `channel-09-in` | road / 1 / primary | in | [19.2, -8.0, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-23-out` | road / 1 / primary | out | [19.2, -8.0, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-24-out` | road / 1 / primary | out | [24.0, -16.970563, 13.253148]; [0.7071067811865294, 0.7071067811865658]; -0.282029322 | `path-interface-481a9f04963a1402d262` |
| `channel-25-out` | road / 1 / primary | out | [24.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-10-in` | road / 1 / primary | in | [24.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-26-out` | road / 1 / primary | out | [24.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-11-in` | road / 1 / primary | in | [24.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-12-in` | road / 1 / primary | in | [28.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-27-out` | road / 1 / primary | out | [28.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-13-in` | road / 1 / primary | in | [32.970563, -8.0, 9.675242]; [0.7071067811865784, 0.7071067811865166]; -0.282029318 | `path-interface-55a6a5bf7f0b33d60b89` |
| `channel-14-in` | road / 1 / primary | in | [35.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-28-out` | road / 1 / primary | out | [35.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-29-out` | road / 1 / primary | out | [40.0, -0.970563, 6.871553]; [0.7071067811865476, 0.7071067811865476]; -0.282029323 | `path-interface-6de14d4db7fbc1b8f4fd` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-19-out` | primary |
| road | `channel-01-in` → `channel-18-out` | primary |
| road | `channel-02-in` → `channel-17-out` | primary |
| road | `channel-03-in` → `channel-16-out` | primary |
| road | `channel-04-in` → `channel-15-out` | primary |
| road | `channel-05-in` → `channel-23-out` | primary |
| road | `channel-06-in` → `channel-22-out` | primary |
| road | `channel-07-in` → `channel-21-out` | primary |
| road | `channel-08-in` → `channel-24-out` | primary |
| road | `channel-09-in` → `channel-20-out` | primary |
| road | `channel-10-in` → `channel-28-out` | primary |
| road | `channel-11-in` → `channel-27-out` | primary |
| road | `channel-12-in` → `channel-26-out` | primary |
| road | `channel-13-in` → `channel-29-out` | primary |
| road | `channel-14-in` → `channel-25-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
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
| road / `channel-02-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
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
| road / `channel-03-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
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
| road / `channel-04-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-25-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
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
| road / `channel-11-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-11-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
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
| road / `channel-12-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-12-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-13-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
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
| road / `channel-14-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-21-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-22-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-23-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-24-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-26-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-27-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-28-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-14-in` | road / `channel-29-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-upper-exit-slip
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **31,793 indexed triangles** and **15 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-upper-exit-slip/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-upper-exit-slip/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-0fda03ea04e8723e4ee2">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-0fda03ea04e8723e4ee2"></a>

**General: unverified** — `software_resources-0fda03ea04e8723e4ee2`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-0fda03ea04e8723e4ee2">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-0fda03ea04e8723e4ee2"></a>

**General: unverified** — `software_connectivity-0fda03ea04e8723e4ee2`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-11fb118aebb6a1c0f65c">[ ] unverified</a> | <a href="#case-in_game_render-ae34ff6d3e77c8bfd817">[ ] unverified</a> | <a href="#case-in_game_render-c3fc5d0b336959f51fd4">[ ] unverified</a> | <a href="#case-in_game_render-c2a8bda19203fc124078">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-11fb118aebb6a1c0f65c"></a>

**0° CCW: unverified** — `in_game_render-11fb118aebb6a1c0f65c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ae34ff6d3e77c8bfd817"></a>

**90° CCW: unverified** — `in_game_render-ae34ff6d3e77c8bfd817`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c3fc5d0b336959f51fd4"></a>

**180° CCW: unverified** — `in_game_render-c3fc5d0b336959f51fd4`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c2a8bda19203fc124078"></a>

**270° CCW: unverified** — `in_game_render-c2a8bda19203fc124078`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-11fb118aebb6a1c0f65c">[ ] unverified</a> | <a href="#case-in_game_placement-ae34ff6d3e77c8bfd817">[ ] unverified</a> | <a href="#case-in_game_placement-c3fc5d0b336959f51fd4">[ ] unverified</a> | <a href="#case-in_game_placement-c2a8bda19203fc124078">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-11fb118aebb6a1c0f65c"></a>

**0° CCW: unverified** — `in_game_placement-11fb118aebb6a1c0f65c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ae34ff6d3e77c8bfd817"></a>

**90° CCW: unverified** — `in_game_placement-ae34ff6d3e77c8bfd817`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c3fc5d0b336959f51fd4"></a>

**180° CCW: unverified** — `in_game_placement-c3fc5d0b336959f51fd4`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c2a8bda19203fc124078"></a>

**270° CCW: unverified** — `in_game_placement-c2a8bda19203fc124078`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-11fb118aebb6a1c0f65c">[ ] unverified</a> | <a href="#case-in_game_demolition-ae34ff6d3e77c8bfd817">[ ] unverified</a> | <a href="#case-in_game_demolition-c3fc5d0b336959f51fd4">[ ] unverified</a> | <a href="#case-in_game_demolition-c2a8bda19203fc124078">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-11fb118aebb6a1c0f65c"></a>

**0° CCW: unverified** — `in_game_demolition-11fb118aebb6a1c0f65c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ae34ff6d3e77c8bfd817"></a>

**90° CCW: unverified** — `in_game_demolition-ae34ff6d3e77c8bfd817`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c3fc5d0b336959f51fd4"></a>

**180° CCW: unverified** — `in_game_demolition-c3fc5d0b336959f51fd4`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c2a8bda19203fc124078"></a>

**270° CCW: unverified** — `in_game_demolition-c2a8bda19203fc124078`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-11fb118aebb6a1c0f65c">[ ] unverified</a> | <a href="#case-in_game_save_reload-ae34ff6d3e77c8bfd817">[ ] unverified</a> | <a href="#case-in_game_save_reload-c3fc5d0b336959f51fd4">[ ] unverified</a> | <a href="#case-in_game_save_reload-c2a8bda19203fc124078">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-11fb118aebb6a1c0f65c"></a>

**0° CCW: unverified** — `in_game_save_reload-11fb118aebb6a1c0f65c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ae34ff6d3e77c8bfd817"></a>

**90° CCW: unverified** — `in_game_save_reload-ae34ff6d3e77c8bfd817`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c3fc5d0b336959f51fd4"></a>

**180° CCW: unverified** — `in_game_save_reload-c3fc5d0b336959f51fd4`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c2a8bda19203fc124078"></a>

**270° CCW: unverified** — `in_game_save_reload-c2a8bda19203fc124078`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 60 cases; unverified: 60</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-f15fdf6d3262ff08b54f">[ ] unverified</a> | <a href="#case-in_game_route_query-71ae863aed93c578149e">[ ] unverified</a> | <a href="#case-in_game_route_query-2ac9ed7b9b29dc8b6b6d">[ ] unverified</a> | <a href="#case-in_game_route_query-cb833108f0419287698d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-36e938f0ff6ccac560fc">[ ] unverified</a> | <a href="#case-in_game_route_query-18dfe18b25a1099d178e">[ ] unverified</a> | <a href="#case-in_game_route_query-265be0cd940b6d7ad066">[ ] unverified</a> | <a href="#case-in_game_route_query-9df87b3af2530f0f453d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-96ab85494cf96da974ee">[ ] unverified</a> | <a href="#case-in_game_route_query-2cbca1e9ffb8f0d72004">[ ] unverified</a> | <a href="#case-in_game_route_query-62106f4c0da2c440b1a0">[ ] unverified</a> | <a href="#case-in_game_route_query-8ae0f14b06bf7bb02664">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-89b78e45ea9a7115eb2f">[ ] unverified</a> | <a href="#case-in_game_route_query-b07dde441fddf0de5b9d">[ ] unverified</a> | <a href="#case-in_game_route_query-e9cc05801bb907d38710">[ ] unverified</a> | <a href="#case-in_game_route_query-db81f5a58d3a1f02db38">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out | — | <a href="#case-in_game_route_query-b72a58e1abc94eda9ee4">[ ] unverified</a> | <a href="#case-in_game_route_query-77db5a7e57f062788f32">[ ] unverified</a> | <a href="#case-in_game_route_query-83e80f9f57dadfb8996a">[ ] unverified</a> | <a href="#case-in_game_route_query-856adcea624f5e4e1e62">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out | — | <a href="#case-in_game_route_query-ed5c5fd66fcc01e0e7e4">[ ] unverified</a> | <a href="#case-in_game_route_query-d9de47fe25d9d3d53e85">[ ] unverified</a> | <a href="#case-in_game_route_query-57ffe68d4f66e9c8b2b1">[ ] unverified</a> | <a href="#case-in_game_route_query-cf4f76a789e291eb7b7a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out | — | <a href="#case-in_game_route_query-a58a585befe92df602ee">[ ] unverified</a> | <a href="#case-in_game_route_query-82e88d47d61ea59cefa9">[ ] unverified</a> | <a href="#case-in_game_route_query-a298e489ab7090f82738">[ ] unverified</a> | <a href="#case-in_game_route_query-fe7d7649319fee1dede3">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out | — | <a href="#case-in_game_route_query-ac8f575ee14f80adee57">[ ] unverified</a> | <a href="#case-in_game_route_query-47152052eda266947f05">[ ] unverified</a> | <a href="#case-in_game_route_query-167338fe31f32f29509a">[ ] unverified</a> | <a href="#case-in_game_route_query-c0d3dca839ae64c4e732">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out | — | <a href="#case-in_game_route_query-caf1355a6b565e39a043">[ ] unverified</a> | <a href="#case-in_game_route_query-1d0d3955ea88f5ac95f4">[ ] unverified</a> | <a href="#case-in_game_route_query-7fc2934c52fb4dff16d9">[ ] unverified</a> | <a href="#case-in_game_route_query-b2cc61db31f73121f841">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out | — | <a href="#case-in_game_route_query-6c7a1eb2bc9611bad1b1">[ ] unverified</a> | <a href="#case-in_game_route_query-03f4dccb01c1bbe2ae27">[ ] unverified</a> | <a href="#case-in_game_route_query-04cce97a7b6b5f9c8ecd">[ ] unverified</a> | <a href="#case-in_game_route_query-180e0aeccda6ba94efb7">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out | — | <a href="#case-in_game_route_query-b6a44d9079a41dfd88d0">[ ] unverified</a> | <a href="#case-in_game_route_query-be619b9d06a620810b35">[ ] unverified</a> | <a href="#case-in_game_route_query-16f18fc16ba1a39ce126">[ ] unverified</a> | <a href="#case-in_game_route_query-ef19a74f7f680ec992f1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out | — | <a href="#case-in_game_route_query-1d31778119ce9e056078">[ ] unverified</a> | <a href="#case-in_game_route_query-6bc598163d6566aa659f">[ ] unverified</a> | <a href="#case-in_game_route_query-d994eff237616fafbb08">[ ] unverified</a> | <a href="#case-in_game_route_query-2c8ef0513238016cdc8a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out | — | <a href="#case-in_game_route_query-0ad3392b598fc7f66f1e">[ ] unverified</a> | <a href="#case-in_game_route_query-c7af67dbfc86bda9443f">[ ] unverified</a> | <a href="#case-in_game_route_query-e8d8898fce27b62e6ad7">[ ] unverified</a> | <a href="#case-in_game_route_query-b20f1eeca918516855af">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out | — | <a href="#case-in_game_route_query-d420fdc2db15e4e7215a">[ ] unverified</a> | <a href="#case-in_game_route_query-14c94cfd853404717be8">[ ] unverified</a> | <a href="#case-in_game_route_query-b7f12c8eef979e9f65dd">[ ] unverified</a> | <a href="#case-in_game_route_query-552570e9ca6ce21f7c33">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out | — | <a href="#case-in_game_route_query-7482898f2de323941acd">[ ] unverified</a> | <a href="#case-in_game_route_query-faeaf949497a015e0c64">[ ] unverified</a> | <a href="#case-in_game_route_query-ca0a60162ecfa52af849">[ ] unverified</a> | <a href="#case-in_game_route_query-3ddf2c1d16d236bf5a56">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-f15fdf6d3262ff08b54f"></a>

**0° CCW: unverified** — `in_game_route_query-f15fdf6d3262ff08b54f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-71ae863aed93c578149e"></a>

**90° CCW: unverified** — `in_game_route_query-71ae863aed93c578149e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-2ac9ed7b9b29dc8b6b6d"></a>

**180° CCW: unverified** — `in_game_route_query-2ac9ed7b9b29dc8b6b6d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-cb833108f0419287698d"></a>

**270° CCW: unverified** — `in_game_route_query-cb833108f0419287698d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-36e938f0ff6ccac560fc"></a>

**0° CCW: unverified** — `in_game_route_query-36e938f0ff6ccac560fc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-18dfe18b25a1099d178e"></a>

**90° CCW: unverified** — `in_game_route_query-18dfe18b25a1099d178e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-265be0cd940b6d7ad066"></a>

**180° CCW: unverified** — `in_game_route_query-265be0cd940b6d7ad066`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-9df87b3af2530f0f453d"></a>

**270° CCW: unverified** — `in_game_route_query-9df87b3af2530f0f453d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-96ab85494cf96da974ee"></a>

**0° CCW: unverified** — `in_game_route_query-96ab85494cf96da974ee`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-2cbca1e9ffb8f0d72004"></a>

**90° CCW: unverified** — `in_game_route_query-2cbca1e9ffb8f0d72004`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-62106f4c0da2c440b1a0"></a>

**180° CCW: unverified** — `in_game_route_query-62106f4c0da2c440b1a0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-8ae0f14b06bf7bb02664"></a>

**270° CCW: unverified** — `in_game_route_query-8ae0f14b06bf7bb02664`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-89b78e45ea9a7115eb2f"></a>

**0° CCW: unverified** — `in_game_route_query-89b78e45ea9a7115eb2f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-b07dde441fddf0de5b9d"></a>

**90° CCW: unverified** — `in_game_route_query-b07dde441fddf0de5b9d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-e9cc05801bb907d38710"></a>

**180° CCW: unverified** — `in_game_route_query-e9cc05801bb907d38710`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-db81f5a58d3a1f02db38"></a>

**270° CCW: unverified** — `in_game_route_query-db81f5a58d3a1f02db38`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out</summary>

<a id="case-in_game_route_query-b72a58e1abc94eda9ee4"></a>

**0° CCW: unverified** — `in_game_route_query-b72a58e1abc94eda9ee4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-77db5a7e57f062788f32"></a>

**90° CCW: unverified** — `in_game_route_query-77db5a7e57f062788f32`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-83e80f9f57dadfb8996a"></a>

**180° CCW: unverified** — `in_game_route_query-83e80f9f57dadfb8996a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-856adcea624f5e4e1e62"></a>

**270° CCW: unverified** — `in_game_route_query-856adcea624f5e4e1e62`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out</summary>

<a id="case-in_game_route_query-ed5c5fd66fcc01e0e7e4"></a>

**0° CCW: unverified** — `in_game_route_query-ed5c5fd66fcc01e0e7e4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-d9de47fe25d9d3d53e85"></a>

**90° CCW: unverified** — `in_game_route_query-d9de47fe25d9d3d53e85`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-57ffe68d4f66e9c8b2b1"></a>

**180° CCW: unverified** — `in_game_route_query-57ffe68d4f66e9c8b2b1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_route_query-cf4f76a789e291eb7b7a"></a>

**270° CCW: unverified** — `in_game_route_query-cf4f76a789e291eb7b7a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out</summary>

<a id="case-in_game_route_query-a58a585befe92df602ee"></a>

**0° CCW: unverified** — `in_game_route_query-a58a585befe92df602ee`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_route_query-82e88d47d61ea59cefa9"></a>

**90° CCW: unverified** — `in_game_route_query-82e88d47d61ea59cefa9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_route_query-a298e489ab7090f82738"></a>

**180° CCW: unverified** — `in_game_route_query-a298e489ab7090f82738`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_route_query-fe7d7649319fee1dede3"></a>

**270° CCW: unverified** — `in_game_route_query-fe7d7649319fee1dede3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out</summary>

<a id="case-in_game_route_query-ac8f575ee14f80adee57"></a>

**0° CCW: unverified** — `in_game_route_query-ac8f575ee14f80adee57`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_route_query-47152052eda266947f05"></a>

**90° CCW: unverified** — `in_game_route_query-47152052eda266947f05`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_route_query-167338fe31f32f29509a"></a>

**180° CCW: unverified** — `in_game_route_query-167338fe31f32f29509a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_route_query-c0d3dca839ae64c4e732"></a>

**270° CCW: unverified** — `in_game_route_query-c0d3dca839ae64c4e732`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out</summary>

<a id="case-in_game_route_query-caf1355a6b565e39a043"></a>

**0° CCW: unverified** — `in_game_route_query-caf1355a6b565e39a043`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-1d0d3955ea88f5ac95f4"></a>

**90° CCW: unverified** — `in_game_route_query-1d0d3955ea88f5ac95f4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-7fc2934c52fb4dff16d9"></a>

**180° CCW: unverified** — `in_game_route_query-7fc2934c52fb4dff16d9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_route_query-b2cc61db31f73121f841"></a>

**270° CCW: unverified** — `in_game_route_query-b2cc61db31f73121f841`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out</summary>

<a id="case-in_game_route_query-6c7a1eb2bc9611bad1b1"></a>

**0° CCW: unverified** — `in_game_route_query-6c7a1eb2bc9611bad1b1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-03f4dccb01c1bbe2ae27"></a>

**90° CCW: unverified** — `in_game_route_query-03f4dccb01c1bbe2ae27`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-04cce97a7b6b5f9c8ecd"></a>

**180° CCW: unverified** — `in_game_route_query-04cce97a7b6b5f9c8ecd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-180e0aeccda6ba94efb7"></a>

**270° CCW: unverified** — `in_game_route_query-180e0aeccda6ba94efb7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out</summary>

<a id="case-in_game_route_query-b6a44d9079a41dfd88d0"></a>

**0° CCW: unverified** — `in_game_route_query-b6a44d9079a41dfd88d0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_route_query-be619b9d06a620810b35"></a>

**90° CCW: unverified** — `in_game_route_query-be619b9d06a620810b35`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_route_query-16f18fc16ba1a39ce126"></a>

**180° CCW: unverified** — `in_game_route_query-16f18fc16ba1a39ce126`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_route_query-ef19a74f7f680ec992f1"></a>

**270° CCW: unverified** — `in_game_route_query-ef19a74f7f680ec992f1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out</summary>

<a id="case-in_game_route_query-1d31778119ce9e056078"></a>

**0° CCW: unverified** — `in_game_route_query-1d31778119ce9e056078`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_route_query-6bc598163d6566aa659f"></a>

**90° CCW: unverified** — `in_game_route_query-6bc598163d6566aa659f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_route_query-d994eff237616fafbb08"></a>

**180° CCW: unverified** — `in_game_route_query-d994eff237616fafbb08`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_route_query-2c8ef0513238016cdc8a"></a>

**270° CCW: unverified** — `in_game_route_query-2c8ef0513238016cdc8a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out</summary>

<a id="case-in_game_route_query-0ad3392b598fc7f66f1e"></a>

**0° CCW: unverified** — `in_game_route_query-0ad3392b598fc7f66f1e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_route_query-c7af67dbfc86bda9443f"></a>

**90° CCW: unverified** — `in_game_route_query-c7af67dbfc86bda9443f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_route_query-e8d8898fce27b62e6ad7"></a>

**180° CCW: unverified** — `in_game_route_query-e8d8898fce27b62e6ad7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_route_query-b20f1eeca918516855af"></a>

**270° CCW: unverified** — `in_game_route_query-b20f1eeca918516855af`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out</summary>

<a id="case-in_game_route_query-d420fdc2db15e4e7215a"></a>

**0° CCW: unverified** — `in_game_route_query-d420fdc2db15e4e7215a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_route_query-14c94cfd853404717be8"></a>

**90° CCW: unverified** — `in_game_route_query-14c94cfd853404717be8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_route_query-b7f12c8eef979e9f65dd"></a>

**180° CCW: unverified** — `in_game_route_query-b7f12c8eef979e9f65dd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_route_query-552570e9ca6ce21f7c33"></a>

**270° CCW: unverified** — `in_game_route_query-552570e9ca6ce21f7c33`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out</summary>

<a id="case-in_game_route_query-7482898f2de323941acd"></a>

**0° CCW: unverified** — `in_game_route_query-7482898f2de323941acd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_route_query-faeaf949497a015e0c64"></a>

**90° CCW: unverified** — `in_game_route_query-faeaf949497a015e0c64`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_route_query-ca0a60162ecfa52af849"></a>

**180° CCW: unverified** — `in_game_route_query-ca0a60162ecfa52af849`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_route_query-3ddf2c1d16d236bf5a56"></a>

**270° CCW: unverified** — `in_game_route_query-3ddf2c1d16d236bf5a56`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 60 cases; unverified: 60</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-f15fdf6d3262ff08b54f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-71ae863aed93c578149e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2ac9ed7b9b29dc8b6b6d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cb833108f0419287698d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-36e938f0ff6ccac560fc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-18dfe18b25a1099d178e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-265be0cd940b6d7ad066">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9df87b3af2530f0f453d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-96ab85494cf96da974ee">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2cbca1e9ffb8f0d72004">[ ] unverified</a> | <a href="#case-in_game_visible_travel-62106f4c0da2c440b1a0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8ae0f14b06bf7bb02664">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-89b78e45ea9a7115eb2f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b07dde441fddf0de5b9d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e9cc05801bb907d38710">[ ] unverified</a> | <a href="#case-in_game_visible_travel-db81f5a58d3a1f02db38">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out | — | <a href="#case-in_game_visible_travel-b72a58e1abc94eda9ee4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-77db5a7e57f062788f32">[ ] unverified</a> | <a href="#case-in_game_visible_travel-83e80f9f57dadfb8996a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-856adcea624f5e4e1e62">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out | — | <a href="#case-in_game_visible_travel-ed5c5fd66fcc01e0e7e4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d9de47fe25d9d3d53e85">[ ] unverified</a> | <a href="#case-in_game_visible_travel-57ffe68d4f66e9c8b2b1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cf4f76a789e291eb7b7a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out | — | <a href="#case-in_game_visible_travel-a58a585befe92df602ee">[ ] unverified</a> | <a href="#case-in_game_visible_travel-82e88d47d61ea59cefa9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a298e489ab7090f82738">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fe7d7649319fee1dede3">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out | — | <a href="#case-in_game_visible_travel-ac8f575ee14f80adee57">[ ] unverified</a> | <a href="#case-in_game_visible_travel-47152052eda266947f05">[ ] unverified</a> | <a href="#case-in_game_visible_travel-167338fe31f32f29509a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c0d3dca839ae64c4e732">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out | — | <a href="#case-in_game_visible_travel-caf1355a6b565e39a043">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1d0d3955ea88f5ac95f4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7fc2934c52fb4dff16d9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b2cc61db31f73121f841">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out | — | <a href="#case-in_game_visible_travel-6c7a1eb2bc9611bad1b1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-03f4dccb01c1bbe2ae27">[ ] unverified</a> | <a href="#case-in_game_visible_travel-04cce97a7b6b5f9c8ecd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-180e0aeccda6ba94efb7">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out | — | <a href="#case-in_game_visible_travel-b6a44d9079a41dfd88d0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-be619b9d06a620810b35">[ ] unverified</a> | <a href="#case-in_game_visible_travel-16f18fc16ba1a39ce126">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ef19a74f7f680ec992f1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out | — | <a href="#case-in_game_visible_travel-1d31778119ce9e056078">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6bc598163d6566aa659f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d994eff237616fafbb08">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2c8ef0513238016cdc8a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out | — | <a href="#case-in_game_visible_travel-0ad3392b598fc7f66f1e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c7af67dbfc86bda9443f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e8d8898fce27b62e6ad7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b20f1eeca918516855af">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out | — | <a href="#case-in_game_visible_travel-d420fdc2db15e4e7215a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-14c94cfd853404717be8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b7f12c8eef979e9f65dd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-552570e9ca6ce21f7c33">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out | — | <a href="#case-in_game_visible_travel-7482898f2de323941acd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-faeaf949497a015e0c64">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ca0a60162ecfa52af849">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3ddf2c1d16d236bf5a56">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-f15fdf6d3262ff08b54f"></a>

**0° CCW: unverified** — `in_game_visible_travel-f15fdf6d3262ff08b54f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-71ae863aed93c578149e"></a>

**90° CCW: unverified** — `in_game_visible_travel-71ae863aed93c578149e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-2ac9ed7b9b29dc8b6b6d"></a>

**180° CCW: unverified** — `in_game_visible_travel-2ac9ed7b9b29dc8b6b6d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-cb833108f0419287698d"></a>

**270° CCW: unverified** — `in_game_visible_travel-cb833108f0419287698d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-19-out; entry: channel-01-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-36e938f0ff6ccac560fc"></a>

**0° CCW: unverified** — `in_game_visible_travel-36e938f0ff6ccac560fc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-18dfe18b25a1099d178e"></a>

**90° CCW: unverified** — `in_game_visible_travel-18dfe18b25a1099d178e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-265be0cd940b6d7ad066"></a>

**180° CCW: unverified** — `in_game_visible_travel-265be0cd940b6d7ad066`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-9df87b3af2530f0f453d"></a>

**270° CCW: unverified** — `in_game_visible_travel-9df87b3af2530f0f453d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-18-out; entry: channel-01-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-96ab85494cf96da974ee"></a>

**0° CCW: unverified** — `in_game_visible_travel-96ab85494cf96da974ee`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-2cbca1e9ffb8f0d72004"></a>

**90° CCW: unverified** — `in_game_visible_travel-2cbca1e9ffb8f0d72004`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-62106f4c0da2c440b1a0"></a>

**180° CCW: unverified** — `in_game_visible_travel-62106f4c0da2c440b1a0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-8ae0f14b06bf7bb02664"></a>

**270° CCW: unverified** — `in_game_visible_travel-8ae0f14b06bf7bb02664`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-17-out; entry: channel-02-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-89b78e45ea9a7115eb2f"></a>

**0° CCW: unverified** — `in_game_visible_travel-89b78e45ea9a7115eb2f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-b07dde441fddf0de5b9d"></a>

**90° CCW: unverified** — `in_game_visible_travel-b07dde441fddf0de5b9d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-e9cc05801bb907d38710"></a>

**180° CCW: unverified** — `in_game_visible_travel-e9cc05801bb907d38710`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-db81f5a58d3a1f02db38"></a>

**270° CCW: unverified** — `in_game_visible_travel-db81f5a58d3a1f02db38`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-16-out; entry: channel-03-in; exit: channel-16-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out</summary>

<a id="case-in_game_visible_travel-b72a58e1abc94eda9ee4"></a>

**0° CCW: unverified** — `in_game_visible_travel-b72a58e1abc94eda9ee4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-77db5a7e57f062788f32"></a>

**90° CCW: unverified** — `in_game_visible_travel-77db5a7e57f062788f32`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-83e80f9f57dadfb8996a"></a>

**180° CCW: unverified** — `in_game_visible_travel-83e80f9f57dadfb8996a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-856adcea624f5e4e1e62"></a>

**270° CCW: unverified** — `in_game_visible_travel-856adcea624f5e4e1e62`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out</summary>

<a id="case-in_game_visible_travel-ed5c5fd66fcc01e0e7e4"></a>

**0° CCW: unverified** — `in_game_visible_travel-ed5c5fd66fcc01e0e7e4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-d9de47fe25d9d3d53e85"></a>

**90° CCW: unverified** — `in_game_visible_travel-d9de47fe25d9d3d53e85`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-57ffe68d4f66e9c8b2b1"></a>

**180° CCW: unverified** — `in_game_visible_travel-57ffe68d4f66e9c8b2b1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out.

No observation recorded.

<a id="case-in_game_visible_travel-cf4f76a789e291eb7b7a"></a>

**270° CCW: unverified** — `in_game_visible_travel-cf4f76a789e291eb7b7a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-23-out; entry: channel-05-in; exit: channel-23-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out</summary>

<a id="case-in_game_visible_travel-a58a585befe92df602ee"></a>

**0° CCW: unverified** — `in_game_visible_travel-a58a585befe92df602ee`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_visible_travel-82e88d47d61ea59cefa9"></a>

**90° CCW: unverified** — `in_game_visible_travel-82e88d47d61ea59cefa9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_visible_travel-a298e489ab7090f82738"></a>

**180° CCW: unverified** — `in_game_visible_travel-a298e489ab7090f82738`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out.

No observation recorded.

<a id="case-in_game_visible_travel-fe7d7649319fee1dede3"></a>

**270° CCW: unverified** — `in_game_visible_travel-fe7d7649319fee1dede3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-22-out; entry: channel-06-in; exit: channel-22-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out</summary>

<a id="case-in_game_visible_travel-ac8f575ee14f80adee57"></a>

**0° CCW: unverified** — `in_game_visible_travel-ac8f575ee14f80adee57`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_visible_travel-47152052eda266947f05"></a>

**90° CCW: unverified** — `in_game_visible_travel-47152052eda266947f05`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_visible_travel-167338fe31f32f29509a"></a>

**180° CCW: unverified** — `in_game_visible_travel-167338fe31f32f29509a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out.

No observation recorded.

<a id="case-in_game_visible_travel-c0d3dca839ae64c4e732"></a>

**270° CCW: unverified** — `in_game_visible_travel-c0d3dca839ae64c4e732`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-21-out; entry: channel-07-in; exit: channel-21-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out</summary>

<a id="case-in_game_visible_travel-caf1355a6b565e39a043"></a>

**0° CCW: unverified** — `in_game_visible_travel-caf1355a6b565e39a043`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-1d0d3955ea88f5ac95f4"></a>

**90° CCW: unverified** — `in_game_visible_travel-1d0d3955ea88f5ac95f4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-7fc2934c52fb4dff16d9"></a>

**180° CCW: unverified** — `in_game_visible_travel-7fc2934c52fb4dff16d9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out.

No observation recorded.

<a id="case-in_game_visible_travel-b2cc61db31f73121f841"></a>

**270° CCW: unverified** — `in_game_visible_travel-b2cc61db31f73121f841`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-24-out; entry: channel-08-in; exit: channel-24-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out</summary>

<a id="case-in_game_visible_travel-6c7a1eb2bc9611bad1b1"></a>

**0° CCW: unverified** — `in_game_visible_travel-6c7a1eb2bc9611bad1b1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-03f4dccb01c1bbe2ae27"></a>

**90° CCW: unverified** — `in_game_visible_travel-03f4dccb01c1bbe2ae27`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-04cce97a7b6b5f9c8ecd"></a>

**180° CCW: unverified** — `in_game_visible_travel-04cce97a7b6b5f9c8ecd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-180e0aeccda6ba94efb7"></a>

**270° CCW: unverified** — `in_game_visible_travel-180e0aeccda6ba94efb7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out</summary>

<a id="case-in_game_visible_travel-b6a44d9079a41dfd88d0"></a>

**0° CCW: unverified** — `in_game_visible_travel-b6a44d9079a41dfd88d0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_visible_travel-be619b9d06a620810b35"></a>

**90° CCW: unverified** — `in_game_visible_travel-be619b9d06a620810b35`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_visible_travel-16f18fc16ba1a39ce126"></a>

**180° CCW: unverified** — `in_game_visible_travel-16f18fc16ba1a39ce126`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out.

No observation recorded.

<a id="case-in_game_visible_travel-ef19a74f7f680ec992f1"></a>

**270° CCW: unverified** — `in_game_visible_travel-ef19a74f7f680ec992f1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-28-out; entry: channel-10-in; exit: channel-28-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out</summary>

<a id="case-in_game_visible_travel-1d31778119ce9e056078"></a>

**0° CCW: unverified** — `in_game_visible_travel-1d31778119ce9e056078`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_visible_travel-6bc598163d6566aa659f"></a>

**90° CCW: unverified** — `in_game_visible_travel-6bc598163d6566aa659f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_visible_travel-d994eff237616fafbb08"></a>

**180° CCW: unverified** — `in_game_visible_travel-d994eff237616fafbb08`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out.

No observation recorded.

<a id="case-in_game_visible_travel-2c8ef0513238016cdc8a"></a>

**270° CCW: unverified** — `in_game_visible_travel-2c8ef0513238016cdc8a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-11-in>channel-27-out; entry: channel-11-in; exit: channel-27-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out</summary>

<a id="case-in_game_visible_travel-0ad3392b598fc7f66f1e"></a>

**0° CCW: unverified** — `in_game_visible_travel-0ad3392b598fc7f66f1e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_visible_travel-c7af67dbfc86bda9443f"></a>

**90° CCW: unverified** — `in_game_visible_travel-c7af67dbfc86bda9443f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_visible_travel-e8d8898fce27b62e6ad7"></a>

**180° CCW: unverified** — `in_game_visible_travel-e8d8898fce27b62e6ad7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out.

No observation recorded.

<a id="case-in_game_visible_travel-b20f1eeca918516855af"></a>

**270° CCW: unverified** — `in_game_visible_travel-b20f1eeca918516855af`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-12-in>channel-26-out; entry: channel-12-in; exit: channel-26-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out</summary>

<a id="case-in_game_visible_travel-d420fdc2db15e4e7215a"></a>

**0° CCW: unverified** — `in_game_visible_travel-d420fdc2db15e4e7215a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_visible_travel-14c94cfd853404717be8"></a>

**90° CCW: unverified** — `in_game_visible_travel-14c94cfd853404717be8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_visible_travel-b7f12c8eef979e9f65dd"></a>

**180° CCW: unverified** — `in_game_visible_travel-b7f12c8eef979e9f65dd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

<a id="case-in_game_visible_travel-552570e9ca6ce21f7c33"></a>

**270° CCW: unverified** — `in_game_visible_travel-552570e9ca6ce21f7c33`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-13-in>channel-29-out; entry: channel-13-in; exit: channel-29-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out</summary>

<a id="case-in_game_visible_travel-7482898f2de323941acd"></a>

**0° CCW: unverified** — `in_game_visible_travel-7482898f2de323941acd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_visible_travel-faeaf949497a015e0c64"></a>

**90° CCW: unverified** — `in_game_visible_travel-faeaf949497a015e0c64`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_visible_travel-ca0a60162ecfa52af849"></a>

**180° CCW: unverified** — `in_game_visible_travel-ca0a60162ecfa52af849`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out.

No observation recorded.

<a id="case-in_game_visible_travel-3ddf2c1d16d236bf5a56"></a>

**270° CCW: unverified** — `in_game_visible_travel-3ddf2c1d16d236bf5a56`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-14-in>channel-25-out; entry: channel-14-in; exit: channel-25-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 780 cases; unverified: 780</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-84edd9ed7244cf47f598">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6dc0827762b3d073196c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a56139f34f77d0839f0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a944b8a75e012c403a84">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eb87d40e8c3d118dbfd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffe5d27001b6160a6fe5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02edc7a8d4ec948a3510">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d766d90c473fda1ec048">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-464e00e4cc834c9bbb14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4521ade40f4b9d1cf5d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7fa372fb9c73384452d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2af2d94a21ece2719489">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d0551a87182d87248388">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fff15d181a99fab16408">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8707fea1a9ac327056ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91f0ec45496997099ea2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5ec3d0a1f40daa82fc6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e08ffdd00de19c05780c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c7e937c3aa3dd165eb3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a8d31364bbc9be23f4d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9efe37202c7390a34258">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec3623b3567a2e2f72ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2501f6e546753b112eba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ef709f5eac2b6374cc6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e65de01d1e02fffca08a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-554c99381c740933f831">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3689144d1664808f5756">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa46d2efed962c97dbeb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7967fe49dd64bf4df98f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a38665d1caf349cd1f44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36f3725ebd43145cae96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2caad8a80053ddc4e79a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e8d284f53e9e2d3db7d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fff475124aa317db2804">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16afed866e6ba31beee4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c51b126d64132957d44c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-26cd95505a69c0916f44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4147affbcce9189b94f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccac45e1df3080486735">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d82bdb1eb369c145ebe2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9974c46a51ec4692e83d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e87a68f5a6bacdcc195">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0888f53a7b372b52ab1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e09e80a9d458b343ed0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8fef8ee4ea404ff818bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e044e841b61e60a8a687">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3e6daff3c5dfdfd1fdb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7311cd9ed63d3a7f361">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fa484b2520c48464f15d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b57ee742675db2c036f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-784d7a145a0ff86431d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19da1e0e18db1d958ba7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d99e2f991dca589850f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24e912e9495ff6cbbd26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e34493967fad3e7f032">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1504e611d1a1b9e9a73b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6e51db4470f855305836">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02edd766ef1074f8ade1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51635cd29719269a3c17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25b5d249e94b155b5d4c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97ca54e79ed0af693ef3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd66bbc346989106cb87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eba25e41beeeef5f4b3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d41bf58a7247746b4e69">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b8fedfc998f034efed51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4754246b5f2ca8c8abd9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81c921a9c9b28f252acc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1df6ae1654eaf277424">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9fdaf80a247efa167812">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31e2cce32419b5cbe91b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e12afd517beb1af66c79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4d7a1691988c0d16c07">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7500700c71e0583bfdb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae16ab6564a490147ed5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07710f3e7b85a4accf25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-515ff61f21e20fb2c5b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3783542425c2cace0512">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38b3f0144b0c559faf6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b75091ac5c4b504629ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-085caf7176b8234a3eb0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9bfc9f74ca8fe4b84e42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2883c530e0d654af8803">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24b1aa271865d4efd8f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-641d8ff27c5a88346d35">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-261b104837df790e30de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bff2813609f2ad7f396d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42ab7c514413349a3350">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0948f8bf7356745f659c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6ab7e1e61ca291305e85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d1a3d31654edf7dbc93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c92088ad8034e78c7f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bac1ebb60978aa140c6c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-896d036f9471ea3d7a24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e262063fc9038f287330">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-373a9ce5cad183628428">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e4d03cbc8ac8f87ad13">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-13c14d73f6365d0c3939">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa82f93197fd0cfe8ded">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afc8fd4d4ea00e2da144">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09adaf08dd2947e45427">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca4946de3c6a10419034">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67f964bb08324af3d9bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6db48ec8c590142aa18f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c9df9d30cc0c046a8bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1e49899541005c2c510d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47c1223aea4158a4db46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4af4803014a2cf20db69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49cfa04774e72c6a1ea5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ecd10515a6f810978f6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d30204cd15a7096fb9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f706998447db7b8f7bb2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b645d59096849f36099">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-01ca4d1f4f88d42aa0fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e59237e931d9cc07a40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8890ce635b4d5decf11d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8de2259a26596cd3fe7d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a13f83fd614a06e3a654">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-008a493d29f8fe0838e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4f5aae8c333515f34a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf54db6ca3267585f878">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7b58f799a15d89f04ebe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e1434e27c48a354ee41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e583984cd8678cd81827">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42ce9aa1a11c3c2019fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a9a499d8dd05181790c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4d46ed87c8b79f929e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d54628be05dd503192a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89af3f543d738a7ad3b3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3576324bc3f3361199ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70b99e76c926003040b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce309f35e4475d82aae3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dda9d9f3735315fc60d6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-044064da0b8d30689a3b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d3e014cd9db0f1a0fb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65e21229166e5ab222d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cfec3e01e39ea7c4ec8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f355f60a27c178bfb666">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9d8f6183ac866c2c935">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01053a24fa2826e89e9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29480d4280a9eb589144">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fb4c52c2461c35aec390">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7a8677684c5d0ab3878">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5aed2cc6d26f921cf294">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74c6f8075ecbb7eb18a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-62935e6170aae5447e98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5b0e925d1c95a3d05a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1000be3183ab18e7c91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ef47b1f3ef85fd5d4a0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ac1d358c37eb320165f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56f9e93f3f8b29407ea7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e498c8008a98b875b122">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e41a48a644889062db32">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c1ec262db489472ceb0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9df44d25ed7e1d82212d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74098abcac596b6a1656">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-715c0c87dc6c2d308791">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cef28d7570a1ac3f6b94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe6dc5992e0c1a1634b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d5c2bfffcae422f0cf4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8abc3d5ff4a2d0f1fc33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-001f2cb42db370307b31">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f8638d9e67e093ad527">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be2a599f14bf20200577">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84808f8984dbecc6f972">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3094b0beee7d90f78797">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc0c1d4405ea566d44e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e59540a2bbcf3885c38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17e74edd6b0983c09c01">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-43be845b1d7c57eddaaf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52650896b66a48d61a8c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a76945fe79685ac7fb06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bd394a1267ad9cf706a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-79728c1a335cf747cedb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c076588f4c39e1016f33">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfb300cdb063b05cfb93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc30ee39f1cf43281bf2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b6f75d04649266519838">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-787858f77ae93d830aef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e15ba9927df2bf8a80b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff3b423bcb43bfb2f736">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d2a32561be0141f1758b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff44746a847a41a2ec2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d99b94503e6831d83919">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1dd31b679fc32e28944">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2bf43b752dd6e900a0cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4fbf36b980b23c94e87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dde3f33385114bd0b459">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61fe0c738760b456cad6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c973a6e070d95995b8f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ee8eb472b394953ea7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8119cc1f3ced82a4a18c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0143db22ad2f12fb3b28">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c33b609c8789a1dbf91b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b5d5388bb0530a3d3c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-752ed74bc9190e0718fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d747bace2816cfb19dd6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b401adaa139ae12cc32d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d258514824cfed370514">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5cf815249735ec3f0cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15a093238779e4199757">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f03c13cbbc064f2381c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cc9083138ff6c705b7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-957d0d53cba5cc2e921c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd194b24ab5ea075fed4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b918747ef9c36892ec49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c4a874d202f8756385c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f44f38a9c5f0e5a828ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d77ddc1fbeb8e94a5c5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3b9951ce6afe7ad9b227">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c1d4c27aa15c31ff8e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-625206ef61818f466929">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6f6ff44575de0eff550">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-00703f7774cc51f83312">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ac4deb72c2befece52b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ad4617d04fc0be836db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9508fae8532f2e434c27">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b93678edd40776586c6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9be438b007cabb5c22c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6211cc43fe0bfe557b3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-032382de1fce3652efea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6668afbdb310287f63be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b107756e2027ab53a1c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abc37a349819d04f8646">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd11f5b6476f64543105">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6bb1b08ca88dd562165b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e39b85873df95206721">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e853f66db95bdb6f8b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b654f18836d0e129656">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2056097033752f102ab4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9312922577afc5f811e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67cea2b7d803810d895c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc67a965db33bfe317d7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-68af14102f4a1292c0cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f2aca1030b4a70845fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0eefb904d28693014b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fc6ea35b08938d61426">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3379366c73aa0c5d3564">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d912af754a7c00dc573">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad39444655869ed6d4b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c47792dc20792dcc9abe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6d292b65c5bcc78caef0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e89ddbb4f3ea761ad06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d113dae5816da18aac59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40a51fa8679f749be041">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9a71790a97990b4c64ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f22b4f395b8f022574bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc155e8ff9b37b4371b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e493123a728f061cc461">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3718a9de40c47a223413">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a42cfefadaddb82efc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d428d97eb74309a3dfa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92788f688bc93fb60a72">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5303952cd8932973d864">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0dcee7feb7d60742484">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-312164f9fa3a4318f6ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2fd66d70d755ea9b9060">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-db8a9c690bf165f16ad6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6959d8f0176a28a54df0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca55a59b67915e65c4f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-619be7071da8c4b91a64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ad554e81493b577556ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b51195094697a8e69f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af8fe3ffff0361e030e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c84428a987816c31141">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3b05fcb7ba123a3d2a3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b659851e103b2087139">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff2b8a92a6cef7692577">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48154943771ddc99c2d4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9bd007428fb20aecb0b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a53d77dbb6df334a443">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-589279c720c3d7a41e4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6287ef7e4b8943cbc27">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-abe928d1e46293577570">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab82dddb7f13d816a2ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6dbd57f569045d5a8215">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffcd2d99a16d56d3fecd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7bf16c9eb132e125f17d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58d7ec560c11b9d1c3d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45c8c8a52de36ebc0671">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84b67aa32f03f837e630">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4466ab19d64a135e7a81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7798f07dad4093f525f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2e6ddd3ba549d34c8d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c0059681bf536a02c42">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0782b5b4001048d9c417">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a56f7a2337f936752c34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5de2e9dc7fd6d0dfb5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-596f53e865752d716b72">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-17100b503233299bc16f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49856e0121bcfc7547ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60c8ef913031be8c9508">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa256ba0e44ea222c185">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-89c41688d0e0ade3d634">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72a90439f2ee2fb397cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9df9298ba214bf828a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9b502b96984fb1ac24f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-95d6a24d597571df7359">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e7318dfeb0ed8b2fe2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75be88f8945db2ac1ffe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0ceab3acec5d202acb0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1941374d0e39583d565f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1ba9ef2cfd7895a2e43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6d4c3d890e58d2949dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-635195aa90effe52b864">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-34dc3654bd32c4628d54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30aadc9ee80ca0605028">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0538046f8a575531cdc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3cb17f374d0f128bea4d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5b701b7b8e4fed6646e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afd86eff8ce2e6c01415">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64ce246a4383c2c98329">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebef18f9a2cc5cd97b68">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7172d9a14338049fe10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-08a7ea2a62fb48759a01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90e2c42a929d547163c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5b0e24f41c2d5367748">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9bd9843c74fc045e0eeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46faa9b2e4bb962f93fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dda7390dfde0584a26b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39a43b1abddc2ace5cd3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f09d3e4272ffd88fa280">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-288f439348e6dd690c7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-775a68b9aada54e371b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b35e34ebe306f72f645">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c36e8608d2bd66a1aaba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66015d2ee491918eb013">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d925d1358f30496540e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae9644f53bee475a7e85">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5cf45076aaeedaddbbbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ba940cc46e152602ab1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05a1488ad865a63b5f46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fb8be1320ec2b82d122">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b651562f17dbeaab38eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24719c8da2d943804f24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98994878762043c70403">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d652a525012c8e721987">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4f93d6e621f76aafe7d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8b3da1888d2870f848d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fc994a75099a0876ba3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e845eded551af0159a9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1abd9af1a70b2bb4583b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fdf4bde1c55b9a1b65df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5855831f9aba98d8d5bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c4e4a1beea8e00aa89e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4ac85f20b62dc096d28e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-249be002ec400dcca469">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24957091cb3c41eb0f2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8447fb8d83b0f6de38a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e2bca7cdb4847cf21b55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eadaac1dce6d5fe306f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acd5994cf6c200eaedad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-094d78c197d0d259ef2f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4cf63bc6cc8cdf5ec8c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0aefb7315cd8f449dfe0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e156aead373da8ad278a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be003bb82ab363174a8e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ec0d974e1c4b6e292db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbcd04ec531c05661728">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-973c201b410033070f64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-240ff19fd6567bab9772">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cac0d615b67fa9100c91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0368869332ccdaee4385">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03bd2ebe62c35ddbaaf7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bd6111491aba10584c5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-57732e6caa9943f47728">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f850137341991f578306">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a571e984076ceee7d69e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4063dbac6e6a5bb18c99">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9d69c1222fcddd241d35">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0355dca5bca10b867350">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0bacffd4d8147f5d669">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b98a3696846570c1597d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4428c91aa0c6b1d75b20">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c382ff09ff12d397b56f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79a0b70d3765a2c489ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ecf52a5f4d6b10aa5148">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6bce69e5e7e557ed0c69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88759e3dff4e063a1b4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf10331f70f02be386dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b41f1f0a7bf1387e7c3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f0cec7675466993227ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84c37834b3e2bec7d646">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fae800fdd990cbdef5e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d3042fa76805d665c11">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eacf6e89f3defab0aff2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77150e9da947a0cf6fb6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-adbc902645fadc59facb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51f3dd6e6fc298cc491c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-172ea99462de02ca87ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2bead9adac695ad9649">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0e176c3c643a7be3e41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2be4834e4752e3c373ea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b2a6c9caa2c8c7e069af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c267fa81e849340a295">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b515ffee856cd7b5bb41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2eb16d4f1ea943c96340">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-880a4b2508119014cb2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbb32aa765d0ccb8a061">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61a90d1e4802069c7e98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe62e0cdb96ebb69b070">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-60526dbb1bf709423717">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abb9ea8440a6ea150575">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c6399d0222904925802">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-183725654d0f107fe55c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ecdcbd83563c32a0694d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e4b0368f49ef60e0ac4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27004f7787968ef8ce5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7726b568134d41020c33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-20c9bbed78eb72650203">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73d813e863e101e59c08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66c586d5160a60dd8e17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffda3f055d04dc91b7cb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2246e7ad665409468c59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e930aef4cc99ee70d5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ab52fdb9d5ac05c2cbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9680ed86a4dd350ce68">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5b8509f498e7c7b770dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71b0cdc5ebf3aa59f6a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-155f71ac38fc376d91b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b24fce7cf16496f7e35c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a63ef07c7871d210c19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4766b01f2f8fed64d509">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f990807e98438110786d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-309d03e44ec1eeb4d0c0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3ea52daf7941b59d6aa5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-122794312b4bdd8d28e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-586bfe389cd4f6211f93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61e9ee73bb3c2ce9ebd2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-95841317b89e395e719f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31e459a532c48589f61b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b48aa14129b46fd6851">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f703a80363cec910431">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b1c3557aea1fa69a66dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb08f1703027aa33ec4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e13d2892a459a14ac26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b36c44263668d25b017c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b7e7cd99b79de81f8c14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-309c56996ccf1de9f54e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e7e72ce927fbe8bbb24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f9b4e218a791151091e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d274f4865e222ec09c3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11b1d3f01c7dcb276a15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6133ecf9dbc37f13895e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e68acc06600d2387cfad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4a306069bf048319a0de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b908a07212bf30f7befe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c38c608ed2e1b011072">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd068a814449f6a16635">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-adb51a3ffc7b54cf9be1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d9e047ffe9892c293c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f58addce443993cce4c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f56bcde4b87416c72d1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97b5f3a3be182463aae7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88bfc7a730f8c975357a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e22b4d6da57c448ff1d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9275e3b63cfdb8929cc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e72cb7b1cc4bcba7bf6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cb1ceb04639c57fba6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-930759b690934d43f6f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56df2ce8fb0840824724">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-685ce1b7a52a11170791">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-735892bb368e3d41c1ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd7cea2a0e75da38b202">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2681dadc6e36a3cdb359">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-89e0066bac2026114a14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75238fa3010ae7eab61b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c35875c32a00ddf2d73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90e39e481a0b9f60938e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-60b4a9fe372384ccf3fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1be7902715466da5dc74">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a49e42e7f3e670c51ef7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94a8668762d15f1ed97d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-526b30919053b308fb27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73799b4eae34c99f708c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8aaa813902416fd32c72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77dc35ee4d2536a02272">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7e095df1c5ddb8e2e8d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ba654807fec63978b38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a17996a46009ae4e091">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48f1452d515bd6e06659">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1cc42f90147acc0a2e93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77118495a13a0cb96197">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aaca296c2af045213ddd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-750c69fa1e32787eded5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97fea147433dcc59fbe2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7658b9aaf6d90f8e90a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35178048e4ddd4221a08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7bc9518bdffa5cdacd1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7d6f13f5112948ead29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a81040f0560d385cd8c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6392355f18caaa9a725c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ab103ccf3a0956c4ba0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3af249450d0e38c09f2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-806156c8c261884a225a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-108d43225cbd589845ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e47cbd97bf9a6cf1a60c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f6d7969345e3c207322c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98ce26feb7e646485017">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99d0c49bc460da9f35e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f6d97b6ab1bae731b9b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-323ea9231215d804cce8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8845a09480c8c6e6f3f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22afc876873531b16272">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3ef84d1dec3a11775ef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fddfa6fdd123f119e5d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1505c25275fd047dfa87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e80994ed5378faae4a7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53103f0fbce62257aabc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-667d9ba12df045fd211a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a66e82963b9e5a8e7473">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ef06fcb2240b028041a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6d7fbb2041f1b7bebc4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4bf4f670950359a41909">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0889dedebd572998a08b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8460eb5a38d7973545a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91cb28c7db6485be32bc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-185d58e1fd71920472d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5194ade900fd0ffdd0b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0fd50e816e1389cefd11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-060c9dabd11be0b95525">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a100f5f4389838fed7e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a48e3b1f2228038cea07">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4af3ab0e0caab5f9c40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51ca183fea7ee0058407">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-99c039f00ffee27b82c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ba088311724184099aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a2108a157de2170179f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-499c04a710c06cdfe65f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ebb066d4441c064d977">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c9aaf7d088fba0fab06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e71f8f224630ed6c7ed7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b5006f05ebeaa529cd6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1c0dac6ec5a22cb93673">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5271b123c70df25b6ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d22c284b9fdd5e4da8d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69dbac597780954f3e51">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ec0ae224e0e564c475c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d93c88cebaff4b9f37e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94d6ee2edd58604bd853">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ced11c1310fee8c11fc5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-858cde169445bf625a12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd002f81becf4b7990ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09a37145cab346cd27fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b9d74ef5eb67cbddb56">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3b50da22d028d1ce080d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bd2ade2d8ba993e53d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de9ea27a9391f3a80ce0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-251dcb8b4e4db053844c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-15fc0a306a8476a776c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b9fa7cde4f532d29862">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f365dab49abd2c75c1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa516db39de73f5ac8c6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4ac67af7c6fcc0b3e566">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-761ca9b25002a7a2fd77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb2e9346f6c8b4689713">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0a2cd3b9bff06985e15">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-16b9689224eb13f22abc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd8f2cad7c52ab5277e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-531da4fcf7964705508f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d5dcba38daad4b7246b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5659e84cf80c61fde7c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35f456a27a2bfb1c2928">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4d8d21c0cb5b5a80862">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f46e4704ed58f519338e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d09effb98e5b5dc135c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76e979f4b4e8fee87b7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e568ac65a852efe67ec8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0fed258f6d853f5c713">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca2d6b8ad33bdde7eca4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ea3414b244ca10d31af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52637fd5e9da9ddd20f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bf4f9af4c0679100db1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e44bf47e79bae795b303">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5d49e2f49ac0b5fbe22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58168091fa05caf13e01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-617e63cc417919ea0200">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f0362a74a1e5354bf0d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14e8231bf12f98395b11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9380b4f2cd2c592ec23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dc4facfc643a7cc0654">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-81fd53e09141884b01dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e2e0ff646c495d3a102">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4601e72078911b5ef0fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cd0cfaa368f9d77c636">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8acd7b6fb3463ee6c3ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71a87346f28c7e153431">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-854b61aa6924b791a958">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e8826cbd5504c37ca3d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce326bc2201aa860080e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-088ecffc5df86dc784ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44790673b2ca35b13876">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e76a120c3449142af4b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ced4311eefb15236c297">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9771e1776b623f393a24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4281a1091fd6670866a4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0bc55feb0a929948240">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-384ab53ac5d474d1aad9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-231f75b0ddaeb56de9be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b212b02092bb189b7a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-723ba1f999eb6c6f0317">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d8630c5687bfc0287a86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee3caac4642696e4256e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2883da9dbb46f750f4f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd24284306a02d5e3082">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b1d692f5aadc46b2ee0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae098c25733bd22ccf18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2803c32bf6e1645492f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a49db6fc72310d7baed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-11-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d507a0f03789d6ff4503">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0a4f8ff51fb85b8e8df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f4984a5f80a6e6fad01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33f18da8428d62174006">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d658770ee2567b4b61e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4551fa1cb536228d9757">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af786cf08042b544bdc8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1735217ec9ee875f5c70">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-392687966bb41b607734">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2356daac6c6afcaa82a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ef38fb7abb3e72cb367">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-034dea23633e6145f496">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b897e64533580a578e27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47046f2ca81693f8e49d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f071eb0f3a520228ecc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ed95eebf9e8f3b3c625">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-beaa22159b1ddf20283c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cf5bb565ce556146f19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ce326ece1a7526c1510">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10ad994a85b1c336c929">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-891a4d95814dd3db8593">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-100d6ae6f4b8901ccbfd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9ba7a0b80397597baf6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b4467e451fa4ed6c088">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e68c662241a0ad79cf0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c955188d6ce8eb0e1aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1412afb74329a91e1b68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3646f423936bfcd24052">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2006b073d2f6494fab61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d19863e4cc76e40921a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6216780266205c7cadd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a672e87a3f33366ba46">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-42d3293402110f06421f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c450baa93ae67e7c0493">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62fe341d254a4d424367">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d14e3ce7c88c4e531916">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-27d27ec5288eec9fb186">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9405260f3f7fcad90cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbc5c5d2826f3bb96699">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44a1def53b9fbbdca9c0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-04ed2f137c7d00de90ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe12635a0e89c644bdcf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-594b00ca4d77e3060e2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8dc3e72903b1843815c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-856e8655b6c91bfbcdf3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ff750b8ec56b229ae4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d30d9c49493121e8085">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6081811a500d5e40564">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-61c90af13a3835473e22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b440d1a40fb35cc3183">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11bc4c14eec4713d9f81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-692c6ca71f7ccb0b72db">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8cebb5b1c05fb5c28f67">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ee6b6d9059d08048272">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44a5b0550b7e12282c2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f2a2cee6b644427d111">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eaf8080921a491f92f27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00405e4ecf74a0aaa044">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e28bbb69496dab679e75">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-419eac17fa00eda0069a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f51d0f6815bd2d1314d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6854dc6c13571bdb5b0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-984f93a94695e479e33d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-08e54b65ad4c227c5c58">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a8eea7d1e5e91e757074">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-398eb433e28f6e9a4176">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b35aa613dafa38e0c01a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f4368148f8c6ce54a34">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c7bd4b0b3f3d6e74a181">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb358306c4bb5a98ee9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7401bddbf40d3acba72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7c8ad96c5ad6c3825ff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-be769c3d58d54f251e67">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81269b222644dcb17122">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-277cfa6fded7f0c658ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b857311b0d3c4a4fc173">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0289e918136962f6e2d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05fc6dd54c480ea021a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a743ea84732b28d67dc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe3233af2215b09e156f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-602625e5184897e22d27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd5b74c8da85d276d713">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ddc5ca598fd5b0bfb119">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7a32b86503e31817a97">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-99a00a73da5e16f3be4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd1fc978319d9ac61187">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fadef93e33b3e3e6d174">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0b2ffe90e7338368bf9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6f55670442d7f6e8e414">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23959b7da85a04b7d6c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1ea79085ef0a47f489c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e4bc732ca806e33a338">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-661e8faa6427c6a9f6a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b35a4ecf9585f9827e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de1c486f14b995a9548d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccc58fa73794a0a45df8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ee8326e9d6ed07d20b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-162894aa042eebd9e6c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e9656e944fecc975595">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-786ca5a5bcf20da2d2c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1008e664a648aa2bea37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-143805fd036f248db040">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c8255dff800da72f8f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7e0e68c4c5e9e5cb299">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6378bce2caae67dab396">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9630558b6a57bb12ea08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14b182e59e8b97a53cfc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce299eeacc52661e4ad5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c166ac67ee1bfef54852">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae2e47150ab879683d88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d645a29355d920855ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73ffd4e4d71b42f6b613">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a68993964ffbe16cdec6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-246ce82a2de04a5937a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49f5280b7ae9ec0951ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-940f73723287d79cb9a3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1d71267c862adee41294">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-946874d4cf73ac589b2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3d2a67f6ea1893c4f26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec626a4215a65ebb0dd1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-784cebda3cd1d6f632ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9713b38a887573bbd5a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1463b2ed5b9a198acf2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93a7b97d82de18b5caa7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cbc049e3f045bd9a61a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2013e5c00c7b6501f358">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7feaa262c1f95c84730">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1087b03759cffabe3ebc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5bc7ef41f5d5fe8e30bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c62eb256005998f66482">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74eb1164a4cd205d0919">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2190251a58219d1bf2ee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a243309eeaea9cc6177">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8505ebcc440fe5ad48fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bdda989d9abd93c129cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfb0dc166f5957c12ac8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c172846c7a166f7e12ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70c187232d493efcf574">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-399ab78a1a26c9ef92c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bd80eba4c0aa0cd57d0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a572f9ae2c5df795da9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9572816d6dc6b73e7cd8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2fd9532fc6b8e82133a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d88b1332eae5497ef8c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d0168dba6a2687e4dd81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c410723b2e7433933dd7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e2aa5eadcb7653ed28a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ae763684523bb51500a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2f4461d70df58a0c666c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79c33b79dc5601c94d61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-257a0cf7bc33e0eddb81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0ccca94a6f005cfbfc9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b56cf1d86b453dc35397">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a886ef2a50e085bff75">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df91268fe1451684ef1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f79fa36776467611f95">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dd30e0cdb85c0489557d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e85415cdc5f3c5f84ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebb36699ee13a99d2e3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7f1064f087aa3718cfa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0351cd50b9f76a530e77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79a75020a936c8dc2d47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa3a4962a8858c98d741">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1a282428f1e054699a6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d6f240438d458eea0709">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0beb062884be6194b53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c673283b9b42fb86d97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e9bcf3dff745f35e770">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-90bd756b9e4e100ea02a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f43251e755e55b5ff07">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-797bb75d21a01a366a55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6bf50c81c1e1ae127b1">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-84edd9ed7244cf47f598"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-84edd9ed7244cf47f598`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6dc0827762b3d073196c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6dc0827762b3d073196c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a56139f34f77d0839f0a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a56139f34f77d0839f0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a944b8a75e012c403a84"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a944b8a75e012c403a84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eb87d40e8c3d118dbfd0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eb87d40e8c3d118dbfd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffe5d27001b6160a6fe5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ffe5d27001b6160a6fe5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02edc7a8d4ec948a3510"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-02edc7a8d4ec948a3510`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d766d90c473fda1ec048"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d766d90c473fda1ec048`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-464e00e4cc834c9bbb14"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-464e00e4cc834c9bbb14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4521ade40f4b9d1cf5d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4521ade40f4b9d1cf5d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7fa372fb9c73384452d7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7fa372fb9c73384452d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2af2d94a21ece2719489"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2af2d94a21ece2719489`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d0551a87182d87248388"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0551a87182d87248388`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fff15d181a99fab16408"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fff15d181a99fab16408`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8707fea1a9ac327056ef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8707fea1a9ac327056ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91f0ec45496997099ea2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-91f0ec45496997099ea2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5ec3d0a1f40daa82fc6f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5ec3d0a1f40daa82fc6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e08ffdd00de19c05780c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e08ffdd00de19c05780c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c7e937c3aa3dd165eb3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6c7e937c3aa3dd165eb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a8d31364bbc9be23f4d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5a8d31364bbc9be23f4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9efe37202c7390a34258"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9efe37202c7390a34258`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec3623b3567a2e2f72ae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ec3623b3567a2e2f72ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2501f6e546753b112eba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2501f6e546753b112eba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ef709f5eac2b6374cc6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2ef709f5eac2b6374cc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e65de01d1e02fffca08a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e65de01d1e02fffca08a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-554c99381c740933f831"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-554c99381c740933f831`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3689144d1664808f5756"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3689144d1664808f5756`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa46d2efed962c97dbeb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aa46d2efed962c97dbeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7967fe49dd64bf4df98f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7967fe49dd64bf4df98f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a38665d1caf349cd1f44"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a38665d1caf349cd1f44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36f3725ebd43145cae96"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-36f3725ebd43145cae96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2caad8a80053ddc4e79a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2caad8a80053ddc4e79a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e8d284f53e9e2d3db7d3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e8d284f53e9e2d3db7d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fff475124aa317db2804"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fff475124aa317db2804`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16afed866e6ba31beee4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-16afed866e6ba31beee4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c51b126d64132957d44c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c51b126d64132957d44c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-26cd95505a69c0916f44"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-26cd95505a69c0916f44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4147affbcce9189b94f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4147affbcce9189b94f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccac45e1df3080486735"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ccac45e1df3080486735`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d82bdb1eb369c145ebe2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d82bdb1eb369c145ebe2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9974c46a51ec4692e83d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9974c46a51ec4692e83d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e87a68f5a6bacdcc195"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5e87a68f5a6bacdcc195`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0888f53a7b372b52ab1e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0888f53a7b372b52ab1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e09e80a9d458b343ed0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e09e80a9d458b343ed0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8fef8ee4ea404ff818bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8fef8ee4ea404ff818bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e044e841b61e60a8a687"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e044e841b61e60a8a687`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3e6daff3c5dfdfd1fdb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f3e6daff3c5dfdfd1fdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7311cd9ed63d3a7f361"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b7311cd9ed63d3a7f361`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fa484b2520c48464f15d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fa484b2520c48464f15d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b57ee742675db2c036f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b57ee742675db2c036f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-784d7a145a0ff86431d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-784d7a145a0ff86431d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19da1e0e18db1d958ba7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-19da1e0e18db1d958ba7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d99e2f991dca589850f4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d99e2f991dca589850f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24e912e9495ff6cbbd26"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-24e912e9495ff6cbbd26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e34493967fad3e7f032"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0e34493967fad3e7f032`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1504e611d1a1b9e9a73b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1504e611d1a1b9e9a73b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6e51db4470f855305836"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e51db4470f855305836`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02edd766ef1074f8ade1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-02edd766ef1074f8ade1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51635cd29719269a3c17"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-51635cd29719269a3c17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25b5d249e94b155b5d4c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-25b5d249e94b155b5d4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97ca54e79ed0af693ef3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97ca54e79ed0af693ef3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd66bbc346989106cb87"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bd66bbc346989106cb87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eba25e41beeeef5f4b3f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eba25e41beeeef5f4b3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d41bf58a7247746b4e69"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d41bf58a7247746b4e69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b8fedfc998f034efed51"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8fedfc998f034efed51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4754246b5f2ca8c8abd9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4754246b5f2ca8c8abd9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81c921a9c9b28f252acc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-81c921a9c9b28f252acc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1df6ae1654eaf277424"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e1df6ae1654eaf277424`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9fdaf80a247efa167812"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9fdaf80a247efa167812`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31e2cce32419b5cbe91b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-31e2cce32419b5cbe91b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e12afd517beb1af66c79"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e12afd517beb1af66c79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4d7a1691988c0d16c07"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d4d7a1691988c0d16c07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7500700c71e0583bfdb7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7500700c71e0583bfdb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae16ab6564a490147ed5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ae16ab6564a490147ed5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07710f3e7b85a4accf25"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-07710f3e7b85a4accf25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-515ff61f21e20fb2c5b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-515ff61f21e20fb2c5b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3783542425c2cace0512"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3783542425c2cace0512`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38b3f0144b0c559faf6b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-38b3f0144b0c559faf6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b75091ac5c4b504629ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b75091ac5c4b504629ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-085caf7176b8234a3eb0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-085caf7176b8234a3eb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9bfc9f74ca8fe4b84e42"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9bfc9f74ca8fe4b84e42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2883c530e0d654af8803"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2883c530e0d654af8803`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24b1aa271865d4efd8f3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-24b1aa271865d4efd8f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-641d8ff27c5a88346d35"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-641d8ff27c5a88346d35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-261b104837df790e30de"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-261b104837df790e30de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bff2813609f2ad7f396d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bff2813609f2ad7f396d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42ab7c514413349a3350"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-42ab7c514413349a3350`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0948f8bf7356745f659c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0948f8bf7356745f659c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6ab7e1e61ca291305e85"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ab7e1e61ca291305e85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d1a3d31654edf7dbc93"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0d1a3d31654edf7dbc93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c92088ad8034e78c7f2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2c92088ad8034e78c7f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bac1ebb60978aa140c6c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bac1ebb60978aa140c6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-896d036f9471ea3d7a24"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-896d036f9471ea3d7a24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e262063fc9038f287330"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e262063fc9038f287330`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-373a9ce5cad183628428"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-373a9ce5cad183628428`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e4d03cbc8ac8f87ad13"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3e4d03cbc8ac8f87ad13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-13c14d73f6365d0c3939"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-13c14d73f6365d0c3939`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa82f93197fd0cfe8ded"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa82f93197fd0cfe8ded`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afc8fd4d4ea00e2da144"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-afc8fd4d4ea00e2da144`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09adaf08dd2947e45427"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-09adaf08dd2947e45427`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca4946de3c6a10419034"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca4946de3c6a10419034`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67f964bb08324af3d9bd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67f964bb08324af3d9bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6db48ec8c590142aa18f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6db48ec8c590142aa18f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c9df9d30cc0c046a8bf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5c9df9d30cc0c046a8bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1e49899541005c2c510d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e49899541005c2c510d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47c1223aea4158a4db46"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-47c1223aea4158a4db46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4af4803014a2cf20db69"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4af4803014a2cf20db69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49cfa04774e72c6a1ea5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-49cfa04774e72c6a1ea5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ecd10515a6f810978f6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ecd10515a6f810978f6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d30204cd15a7096fb9b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2d30204cd15a7096fb9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f706998447db7b8f7bb2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f706998447db7b8f7bb2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b645d59096849f36099"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7b645d59096849f36099`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-01ca4d1f4f88d42aa0fa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01ca4d1f4f88d42aa0fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e59237e931d9cc07a40"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5e59237e931d9cc07a40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8890ce635b4d5decf11d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8890ce635b4d5decf11d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8de2259a26596cd3fe7d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8de2259a26596cd3fe7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a13f83fd614a06e3a654"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a13f83fd614a06e3a654`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-008a493d29f8fe0838e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-008a493d29f8fe0838e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4f5aae8c333515f34a8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b4f5aae8c333515f34a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf54db6ca3267585f878"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bf54db6ca3267585f878`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7b58f799a15d89f04ebe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7b58f799a15d89f04ebe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e1434e27c48a354ee41"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2e1434e27c48a354ee41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e583984cd8678cd81827"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e583984cd8678cd81827`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42ce9aa1a11c3c2019fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-42ce9aa1a11c3c2019fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a9a499d8dd05181790c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a9a499d8dd05181790c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4d46ed87c8b79f929e6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d4d46ed87c8b79f929e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d54628be05dd503192a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8d54628be05dd503192a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89af3f543d738a7ad3b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-89af3f543d738a7ad3b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3576324bc3f3361199ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3576324bc3f3361199ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70b99e76c926003040b7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-70b99e76c926003040b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce309f35e4475d82aae3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ce309f35e4475d82aae3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dda9d9f3735315fc60d6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dda9d9f3735315fc60d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-044064da0b8d30689a3b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-044064da0b8d30689a3b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d3e014cd9db0f1a0fb9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0d3e014cd9db0f1a0fb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65e21229166e5ab222d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65e21229166e5ab222d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cfec3e01e39ea7c4ec8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7cfec3e01e39ea7c4ec8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f355f60a27c178bfb666"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f355f60a27c178bfb666`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9d8f6183ac866c2c935"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a9d8f6183ac866c2c935`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01053a24fa2826e89e9e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-01053a24fa2826e89e9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29480d4280a9eb589144"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-29480d4280a9eb589144`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fb4c52c2461c35aec390"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fb4c52c2461c35aec390`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7a8677684c5d0ab3878"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d7a8677684c5d0ab3878`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5aed2cc6d26f921cf294"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5aed2cc6d26f921cf294`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74c6f8075ecbb7eb18a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-74c6f8075ecbb7eb18a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-62935e6170aae5447e98"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-62935e6170aae5447e98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5b0e925d1c95a3d05a2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f5b0e925d1c95a3d05a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1000be3183ab18e7c91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f1000be3183ab18e7c91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ef47b1f3ef85fd5d4a0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7ef47b1f3ef85fd5d4a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ac1d358c37eb320165f1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac1d358c37eb320165f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56f9e93f3f8b29407ea7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-56f9e93f3f8b29407ea7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e498c8008a98b875b122"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e498c8008a98b875b122`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e41a48a644889062db32"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e41a48a644889062db32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c1ec262db489472ceb0c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c1ec262db489472ceb0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9df44d25ed7e1d82212d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9df44d25ed7e1d82212d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74098abcac596b6a1656"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-74098abcac596b6a1656`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-715c0c87dc6c2d308791"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-715c0c87dc6c2d308791`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cef28d7570a1ac3f6b94"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cef28d7570a1ac3f6b94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe6dc5992e0c1a1634b7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fe6dc5992e0c1a1634b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d5c2bfffcae422f0cf4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9d5c2bfffcae422f0cf4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8abc3d5ff4a2d0f1fc33"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8abc3d5ff4a2d0f1fc33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-001f2cb42db370307b31"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-001f2cb42db370307b31`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f8638d9e67e093ad527"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1f8638d9e67e093ad527`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be2a599f14bf20200577"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-be2a599f14bf20200577`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84808f8984dbecc6f972"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-84808f8984dbecc6f972`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3094b0beee7d90f78797"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3094b0beee7d90f78797`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc0c1d4405ea566d44e4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fc0c1d4405ea566d44e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e59540a2bbcf3885c38"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0e59540a2bbcf3885c38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17e74edd6b0983c09c01"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-17e74edd6b0983c09c01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-43be845b1d7c57eddaaf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-43be845b1d7c57eddaaf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52650896b66a48d61a8c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-52650896b66a48d61a8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a76945fe79685ac7fb06"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a76945fe79685ac7fb06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bd394a1267ad9cf706a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8bd394a1267ad9cf706a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-79728c1a335cf747cedb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-79728c1a335cf747cedb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c076588f4c39e1016f33"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c076588f4c39e1016f33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfb300cdb063b05cfb93"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dfb300cdb063b05cfb93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc30ee39f1cf43281bf2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cc30ee39f1cf43281bf2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b6f75d04649266519838"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b6f75d04649266519838`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-787858f77ae93d830aef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-787858f77ae93d830aef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e15ba9927df2bf8a80b3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e15ba9927df2bf8a80b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff3b423bcb43bfb2f736"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ff3b423bcb43bfb2f736`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d2a32561be0141f1758b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d2a32561be0141f1758b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff44746a847a41a2ec2d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ff44746a847a41a2ec2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d99b94503e6831d83919"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d99b94503e6831d83919`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1dd31b679fc32e28944"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a1dd31b679fc32e28944`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2bf43b752dd6e900a0cc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2bf43b752dd6e900a0cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4fbf36b980b23c94e87"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f4fbf36b980b23c94e87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dde3f33385114bd0b459"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dde3f33385114bd0b459`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61fe0c738760b456cad6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-61fe0c738760b456cad6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c973a6e070d95995b8f4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c973a6e070d95995b8f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ee8eb472b394953ea7e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4ee8eb472b394953ea7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8119cc1f3ced82a4a18c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8119cc1f3ced82a4a18c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0143db22ad2f12fb3b28"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0143db22ad2f12fb3b28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c33b609c8789a1dbf91b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c33b609c8789a1dbf91b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b5d5388bb0530a3d3c2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4b5d5388bb0530a3d3c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-752ed74bc9190e0718fc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-752ed74bc9190e0718fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d747bace2816cfb19dd6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d747bace2816cfb19dd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b401adaa139ae12cc32d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b401adaa139ae12cc32d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d258514824cfed370514"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d258514824cfed370514`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5cf815249735ec3f0cd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d5cf815249735ec3f0cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15a093238779e4199757"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-15a093238779e4199757`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f03c13cbbc064f2381c0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f03c13cbbc064f2381c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1cc9083138ff6c705b7d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1cc9083138ff6c705b7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-957d0d53cba5cc2e921c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-957d0d53cba5cc2e921c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd194b24ab5ea075fed4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd194b24ab5ea075fed4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b918747ef9c36892ec49"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b918747ef9c36892ec49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c4a874d202f8756385c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9c4a874d202f8756385c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f44f38a9c5f0e5a828ed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f44f38a9c5f0e5a828ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d77ddc1fbeb8e94a5c5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4d77ddc1fbeb8e94a5c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3b9951ce6afe7ad9b227"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3b9951ce6afe7ad9b227`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c1d4c27aa15c31ff8e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2c1d4c27aa15c31ff8e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-625206ef61818f466929"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-625206ef61818f466929`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6f6ff44575de0eff550"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b6f6ff44575de0eff550`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-00703f7774cc51f83312"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-00703f7774cc51f83312`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ac4deb72c2befece52b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7ac4deb72c2befece52b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ad4617d04fc0be836db"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ad4617d04fc0be836db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9508fae8532f2e434c27"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9508fae8532f2e434c27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b93678edd40776586c6e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b93678edd40776586c6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9be438b007cabb5c22c8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9be438b007cabb5c22c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6211cc43fe0bfe557b3a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6211cc43fe0bfe557b3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-032382de1fce3652efea"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-032382de1fce3652efea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6668afbdb310287f63be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6668afbdb310287f63be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b107756e2027ab53a1c6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b107756e2027ab53a1c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abc37a349819d04f8646"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-abc37a349819d04f8646`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd11f5b6476f64543105"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bd11f5b6476f64543105`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6bb1b08ca88dd562165b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6bb1b08ca88dd562165b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e39b85873df95206721"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5e39b85873df95206721`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e853f66db95bdb6f8b9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9e853f66db95bdb6f8b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b654f18836d0e129656"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8b654f18836d0e129656`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2056097033752f102ab4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2056097033752f102ab4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9312922577afc5f811e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e9312922577afc5f811e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67cea2b7d803810d895c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67cea2b7d803810d895c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc67a965db33bfe317d7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc67a965db33bfe317d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-68af14102f4a1292c0cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-68af14102f4a1292c0cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f2aca1030b4a70845fb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3f2aca1030b4a70845fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0eefb904d28693014b4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e0eefb904d28693014b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fc6ea35b08938d61426"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3fc6ea35b08938d61426`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3379366c73aa0c5d3564"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3379366c73aa0c5d3564`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d912af754a7c00dc573"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6d912af754a7c00dc573`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad39444655869ed6d4b1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ad39444655869ed6d4b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c47792dc20792dcc9abe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c47792dc20792dcc9abe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6d292b65c5bcc78caef0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6d292b65c5bcc78caef0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e89ddbb4f3ea761ad06"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5e89ddbb4f3ea761ad06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d113dae5816da18aac59"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d113dae5816da18aac59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40a51fa8679f749be041"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40a51fa8679f749be041`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9a71790a97990b4c64ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9a71790a97990b4c64ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f22b4f395b8f022574bb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f22b4f395b8f022574bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc155e8ff9b37b4371b2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc155e8ff9b37b4371b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e493123a728f061cc461"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e493123a728f061cc461`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3718a9de40c47a223413"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3718a9de40c47a223413`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a42cfefadaddb82efc9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7a42cfefadaddb82efc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d428d97eb74309a3dfa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8d428d97eb74309a3dfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92788f688bc93fb60a72"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92788f688bc93fb60a72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5303952cd8932973d864"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5303952cd8932973d864`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0dcee7feb7d60742484"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c0dcee7feb7d60742484`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-312164f9fa3a4318f6ab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-312164f9fa3a4318f6ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2fd66d70d755ea9b9060"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2fd66d70d755ea9b9060`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-db8a9c690bf165f16ad6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-db8a9c690bf165f16ad6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6959d8f0176a28a54df0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6959d8f0176a28a54df0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca55a59b67915e65c4f9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ca55a59b67915e65c4f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-619be7071da8c4b91a64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-619be7071da8c4b91a64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ad554e81493b577556ab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad554e81493b577556ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b51195094697a8e69f6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9b51195094697a8e69f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af8fe3ffff0361e030e9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-af8fe3ffff0361e030e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c84428a987816c31141"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5c84428a987816c31141`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3b05fcb7ba123a3d2a3d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3b05fcb7ba123a3d2a3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b659851e103b2087139"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6b659851e103b2087139`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff2b8a92a6cef7692577"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ff2b8a92a6cef7692577`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48154943771ddc99c2d4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-48154943771ddc99c2d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9bd007428fb20aecb0b1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9bd007428fb20aecb0b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a53d77dbb6df334a443"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3a53d77dbb6df334a443`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-589279c720c3d7a41e4d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-589279c720c3d7a41e4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6287ef7e4b8943cbc27"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c6287ef7e4b8943cbc27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-abe928d1e46293577570"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-abe928d1e46293577570`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab82dddb7f13d816a2ae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ab82dddb7f13d816a2ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6dbd57f569045d5a8215"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6dbd57f569045d5a8215`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffcd2d99a16d56d3fecd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ffcd2d99a16d56d3fecd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7bf16c9eb132e125f17d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7bf16c9eb132e125f17d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58d7ec560c11b9d1c3d2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-58d7ec560c11b9d1c3d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45c8c8a52de36ebc0671"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-45c8c8a52de36ebc0671`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84b67aa32f03f837e630"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-84b67aa32f03f837e630`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4466ab19d64a135e7a81"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4466ab19d64a135e7a81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7798f07dad4093f525f2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7798f07dad4093f525f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2e6ddd3ba549d34c8d4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2e6ddd3ba549d34c8d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c0059681bf536a02c42"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1c0059681bf536a02c42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0782b5b4001048d9c417"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0782b5b4001048d9c417`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a56f7a2337f936752c34"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a56f7a2337f936752c34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5de2e9dc7fd6d0dfb5d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a5de2e9dc7fd6d0dfb5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-596f53e865752d716b72"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-596f53e865752d716b72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-17100b503233299bc16f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-17100b503233299bc16f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49856e0121bcfc7547ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-49856e0121bcfc7547ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60c8ef913031be8c9508"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-60c8ef913031be8c9508`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa256ba0e44ea222c185"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa256ba0e44ea222c185`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-89c41688d0e0ade3d634"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-89c41688d0e0ade3d634`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72a90439f2ee2fb397cb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-72a90439f2ee2fb397cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9df9298ba214bf828a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b9df9298ba214bf828a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9b502b96984fb1ac24f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b9b502b96984fb1ac24f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-95d6a24d597571df7359"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-95d6a24d597571df7359`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e7318dfeb0ed8b2fe2d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9e7318dfeb0ed8b2fe2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75be88f8945db2ac1ffe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-75be88f8945db2ac1ffe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0ceab3acec5d202acb0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c0ceab3acec5d202acb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1941374d0e39583d565f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1941374d0e39583d565f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1ba9ef2cfd7895a2e43"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b1ba9ef2cfd7895a2e43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6d4c3d890e58d2949dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e6d4c3d890e58d2949dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-635195aa90effe52b864"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-635195aa90effe52b864`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-34dc3654bd32c4628d54"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-34dc3654bd32c4628d54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30aadc9ee80ca0605028"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-30aadc9ee80ca0605028`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0538046f8a575531cdc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b0538046f8a575531cdc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3cb17f374d0f128bea4d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3cb17f374d0f128bea4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5b701b7b8e4fed6646e2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5b701b7b8e4fed6646e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afd86eff8ce2e6c01415"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-afd86eff8ce2e6c01415`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64ce246a4383c2c98329"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-64ce246a4383c2c98329`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebef18f9a2cc5cd97b68"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ebef18f9a2cc5cd97b68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7172d9a14338049fe10"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7172d9a14338049fe10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-08a7ea2a62fb48759a01"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-08a7ea2a62fb48759a01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90e2c42a929d547163c4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-90e2c42a929d547163c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5b0e24f41c2d5367748"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c5b0e24f41c2d5367748`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9bd9843c74fc045e0eeb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9bd9843c74fc045e0eeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46faa9b2e4bb962f93fb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-46faa9b2e4bb962f93fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dda7390dfde0584a26b9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dda7390dfde0584a26b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39a43b1abddc2ace5cd3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39a43b1abddc2ace5cd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f09d3e4272ffd88fa280"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f09d3e4272ffd88fa280`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-288f439348e6dd690c7f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-288f439348e6dd690c7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-775a68b9aada54e371b2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-775a68b9aada54e371b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b35e34ebe306f72f645"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1b35e34ebe306f72f645`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c36e8608d2bd66a1aaba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c36e8608d2bd66a1aaba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66015d2ee491918eb013"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-66015d2ee491918eb013`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d925d1358f30496540e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7d925d1358f30496540e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae9644f53bee475a7e85"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ae9644f53bee475a7e85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5cf45076aaeedaddbbbf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5cf45076aaeedaddbbbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ba940cc46e152602ab1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8ba940cc46e152602ab1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05a1488ad865a63b5f46"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-05a1488ad865a63b5f46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fb8be1320ec2b82d122"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8fb8be1320ec2b82d122`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b651562f17dbeaab38eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b651562f17dbeaab38eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24719c8da2d943804f24"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-24719c8da2d943804f24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98994878762043c70403"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-98994878762043c70403`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d652a525012c8e721987"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d652a525012c8e721987`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4f93d6e621f76aafe7d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4f93d6e621f76aafe7d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8b3da1888d2870f848d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b8b3da1888d2870f848d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fc994a75099a0876ba3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8fc994a75099a0876ba3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e845eded551af0159a9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8e845eded551af0159a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1abd9af1a70b2bb4583b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1abd9af1a70b2bb4583b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fdf4bde1c55b9a1b65df"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fdf4bde1c55b9a1b65df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5855831f9aba98d8d5bc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5855831f9aba98d8d5bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c4e4a1beea8e00aa89e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1c4e4a1beea8e00aa89e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4ac85f20b62dc096d28e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4ac85f20b62dc096d28e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-249be002ec400dcca469"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-249be002ec400dcca469`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24957091cb3c41eb0f2a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-24957091cb3c41eb0f2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8447fb8d83b0f6de38a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8447fb8d83b0f6de38a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e2bca7cdb4847cf21b55"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2bca7cdb4847cf21b55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eadaac1dce6d5fe306f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eadaac1dce6d5fe306f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acd5994cf6c200eaedad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-acd5994cf6c200eaedad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-094d78c197d0d259ef2f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-094d78c197d0d259ef2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4cf63bc6cc8cdf5ec8c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4cf63bc6cc8cdf5ec8c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0aefb7315cd8f449dfe0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0aefb7315cd8f449dfe0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e156aead373da8ad278a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e156aead373da8ad278a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be003bb82ab363174a8e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-be003bb82ab363174a8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ec0d974e1c4b6e292db"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ec0d974e1c4b6e292db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbcd04ec531c05661728"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fbcd04ec531c05661728`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-973c201b410033070f64"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-973c201b410033070f64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-240ff19fd6567bab9772"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-240ff19fd6567bab9772`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cac0d615b67fa9100c91"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cac0d615b67fa9100c91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0368869332ccdaee4385"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0368869332ccdaee4385`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03bd2ebe62c35ddbaaf7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-03bd2ebe62c35ddbaaf7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bd6111491aba10584c5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8bd6111491aba10584c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-57732e6caa9943f47728"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-57732e6caa9943f47728`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f850137341991f578306"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f850137341991f578306`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a571e984076ceee7d69e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a571e984076ceee7d69e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4063dbac6e6a5bb18c99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4063dbac6e6a5bb18c99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9d69c1222fcddd241d35"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9d69c1222fcddd241d35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0355dca5bca10b867350"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0355dca5bca10b867350`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0bacffd4d8147f5d669"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a0bacffd4d8147f5d669`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b98a3696846570c1597d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b98a3696846570c1597d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4428c91aa0c6b1d75b20"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4428c91aa0c6b1d75b20`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c382ff09ff12d397b56f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c382ff09ff12d397b56f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79a0b70d3765a2c489ed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-79a0b70d3765a2c489ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ecf52a5f4d6b10aa5148"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ecf52a5f4d6b10aa5148`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6bce69e5e7e557ed0c69"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6bce69e5e7e557ed0c69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88759e3dff4e063a1b4f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-88759e3dff4e063a1b4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf10331f70f02be386dd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cf10331f70f02be386dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b41f1f0a7bf1387e7c3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1b41f1f0a7bf1387e7c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f0cec7675466993227ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f0cec7675466993227ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84c37834b3e2bec7d646"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-84c37834b3e2bec7d646`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fae800fdd990cbdef5e1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fae800fdd990cbdef5e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d3042fa76805d665c11"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1d3042fa76805d665c11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eacf6e89f3defab0aff2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eacf6e89f3defab0aff2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77150e9da947a0cf6fb6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-77150e9da947a0cf6fb6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-adbc902645fadc59facb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-adbc902645fadc59facb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51f3dd6e6fc298cc491c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-51f3dd6e6fc298cc491c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-172ea99462de02ca87ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-172ea99462de02ca87ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2bead9adac695ad9649"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b2bead9adac695ad9649`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0e176c3c643a7be3e41"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c0e176c3c643a7be3e41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2be4834e4752e3c373ea"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2be4834e4752e3c373ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b2a6c9caa2c8c7e069af"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b2a6c9caa2c8c7e069af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c267fa81e849340a295"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2c267fa81e849340a295`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b515ffee856cd7b5bb41"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b515ffee856cd7b5bb41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2eb16d4f1ea943c96340"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2eb16d4f1ea943c96340`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-880a4b2508119014cb2e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-880a4b2508119014cb2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbb32aa765d0ccb8a061"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cbb32aa765d0ccb8a061`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61a90d1e4802069c7e98"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-61a90d1e4802069c7e98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe62e0cdb96ebb69b070"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe62e0cdb96ebb69b070`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-60526dbb1bf709423717"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-60526dbb1bf709423717`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abb9ea8440a6ea150575"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-abb9ea8440a6ea150575`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c6399d0222904925802"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9c6399d0222904925802`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-183725654d0f107fe55c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-183725654d0f107fe55c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ecdcbd83563c32a0694d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ecdcbd83563c32a0694d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e4b0368f49ef60e0ac4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3e4b0368f49ef60e0ac4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27004f7787968ef8ce5c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-27004f7787968ef8ce5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7726b568134d41020c33"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7726b568134d41020c33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-20c9bbed78eb72650203"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-20c9bbed78eb72650203`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73d813e863e101e59c08"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-73d813e863e101e59c08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66c586d5160a60dd8e17"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-66c586d5160a60dd8e17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffda3f055d04dc91b7cb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ffda3f055d04dc91b7cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2246e7ad665409468c59"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2246e7ad665409468c59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e930aef4cc99ee70d5e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7e930aef4cc99ee70d5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ab52fdb9d5ac05c2cbb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2ab52fdb9d5ac05c2cbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9680ed86a4dd350ce68"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e9680ed86a4dd350ce68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5b8509f498e7c7b770dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5b8509f498e7c7b770dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71b0cdc5ebf3aa59f6a3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-71b0cdc5ebf3aa59f6a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-155f71ac38fc376d91b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-155f71ac38fc376d91b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b24fce7cf16496f7e35c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b24fce7cf16496f7e35c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a63ef07c7871d210c19"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a63ef07c7871d210c19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4766b01f2f8fed64d509"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4766b01f2f8fed64d509`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f990807e98438110786d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f990807e98438110786d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-309d03e44ec1eeb4d0c0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-309d03e44ec1eeb4d0c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3ea52daf7941b59d6aa5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3ea52daf7941b59d6aa5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-122794312b4bdd8d28e7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-122794312b4bdd8d28e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-586bfe389cd4f6211f93"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-586bfe389cd4f6211f93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61e9ee73bb3c2ce9ebd2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-61e9ee73bb3c2ce9ebd2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-95841317b89e395e719f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-95841317b89e395e719f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31e459a532c48589f61b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-31e459a532c48589f61b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b48aa14129b46fd6851"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4b48aa14129b46fd6851`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f703a80363cec910431"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f703a80363cec910431`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b1c3557aea1fa69a66dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b1c3557aea1fa69a66dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb08f1703027aa33ec4a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eb08f1703027aa33ec4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e13d2892a459a14ac26"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2e13d2892a459a14ac26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b36c44263668d25b017c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b36c44263668d25b017c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b7e7cd99b79de81f8c14"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b7e7cd99b79de81f8c14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-309c56996ccf1de9f54e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-309c56996ccf1de9f54e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e7e72ce927fbe8bbb24"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6e7e72ce927fbe8bbb24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f9b4e218a791151091e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f9b4e218a791151091e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d274f4865e222ec09c3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d274f4865e222ec09c3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11b1d3f01c7dcb276a15"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-11b1d3f01c7dcb276a15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6133ecf9dbc37f13895e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6133ecf9dbc37f13895e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e68acc06600d2387cfad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e68acc06600d2387cfad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4a306069bf048319a0de"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4a306069bf048319a0de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b908a07212bf30f7befe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b908a07212bf30f7befe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c38c608ed2e1b011072"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c38c608ed2e1b011072`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd068a814449f6a16635"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fd068a814449f6a16635`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-adb51a3ffc7b54cf9be1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-adb51a3ffc7b54cf9be1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d9e047ffe9892c293c1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d9e047ffe9892c293c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f58addce443993cce4c8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f58addce443993cce4c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f56bcde4b87416c72d1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8f56bcde4b87416c72d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97b5f3a3be182463aae7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97b5f3a3be182463aae7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88bfc7a730f8c975357a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-88bfc7a730f8c975357a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e22b4d6da57c448ff1d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5e22b4d6da57c448ff1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9275e3b63cfdb8929cc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d9275e3b63cfdb8929cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e72cb7b1cc4bcba7bf6d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e72cb7b1cc4bcba7bf6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cb1ceb04639c57fba6f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2cb1ceb04639c57fba6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-930759b690934d43f6f7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-930759b690934d43f6f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56df2ce8fb0840824724"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-56df2ce8fb0840824724`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-685ce1b7a52a11170791"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-685ce1b7a52a11170791`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-735892bb368e3d41c1ac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-735892bb368e3d41c1ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd7cea2a0e75da38b202"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cd7cea2a0e75da38b202`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2681dadc6e36a3cdb359"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2681dadc6e36a3cdb359`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-89e0066bac2026114a14"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-89e0066bac2026114a14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75238fa3010ae7eab61b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-75238fa3010ae7eab61b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c35875c32a00ddf2d73"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3c35875c32a00ddf2d73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90e39e481a0b9f60938e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-90e39e481a0b9f60938e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-60b4a9fe372384ccf3fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-60b4a9fe372384ccf3fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1be7902715466da5dc74"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1be7902715466da5dc74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a49e42e7f3e670c51ef7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a49e42e7f3e670c51ef7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94a8668762d15f1ed97d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-94a8668762d15f1ed97d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-526b30919053b308fb27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-526b30919053b308fb27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73799b4eae34c99f708c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-73799b4eae34c99f708c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8aaa813902416fd32c72"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8aaa813902416fd32c72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77dc35ee4d2536a02272"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-77dc35ee4d2536a02272`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7e095df1c5ddb8e2e8d4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7e095df1c5ddb8e2e8d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ba654807fec63978b38"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5ba654807fec63978b38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a17996a46009ae4e091"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4a17996a46009ae4e091`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48f1452d515bd6e06659"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-48f1452d515bd6e06659`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1cc42f90147acc0a2e93"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1cc42f90147acc0a2e93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77118495a13a0cb96197"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-77118495a13a0cb96197`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aaca296c2af045213ddd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aaca296c2af045213ddd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-750c69fa1e32787eded5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-750c69fa1e32787eded5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97fea147433dcc59fbe2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97fea147433dcc59fbe2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7658b9aaf6d90f8e90a8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7658b9aaf6d90f8e90a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35178048e4ddd4221a08"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-35178048e4ddd4221a08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7bc9518bdffa5cdacd1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e7bc9518bdffa5cdacd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7d6f13f5112948ead29"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7d6f13f5112948ead29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a81040f0560d385cd8c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8a81040f0560d385cd8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6392355f18caaa9a725c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6392355f18caaa9a725c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ab103ccf3a0956c4ba0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7ab103ccf3a0956c4ba0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3af249450d0e38c09f2b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3af249450d0e38c09f2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-806156c8c261884a225a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-806156c8c261884a225a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-108d43225cbd589845ab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-108d43225cbd589845ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e47cbd97bf9a6cf1a60c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e47cbd97bf9a6cf1a60c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f6d7969345e3c207322c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f6d7969345e3c207322c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98ce26feb7e646485017"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-98ce26feb7e646485017`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99d0c49bc460da9f35e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-99d0c49bc460da9f35e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f6d97b6ab1bae731b9b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f6d97b6ab1bae731b9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-323ea9231215d804cce8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-323ea9231215d804cce8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8845a09480c8c6e6f3f4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8845a09480c8c6e6f3f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22afc876873531b16272"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-22afc876873531b16272`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3ef84d1dec3a11775ef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d3ef84d1dec3a11775ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fddfa6fdd123f119e5d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fddfa6fdd123f119e5d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1505c25275fd047dfa87"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1505c25275fd047dfa87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e80994ed5378faae4a7c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e80994ed5378faae4a7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53103f0fbce62257aabc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-53103f0fbce62257aabc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-667d9ba12df045fd211a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-667d9ba12df045fd211a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a66e82963b9e5a8e7473"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a66e82963b9e5a8e7473`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ef06fcb2240b028041a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5ef06fcb2240b028041a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6d7fbb2041f1b7bebc4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a6d7fbb2041f1b7bebc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4bf4f670950359a41909"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4bf4f670950359a41909`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0889dedebd572998a08b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0889dedebd572998a08b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8460eb5a38d7973545a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8460eb5a38d7973545a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91cb28c7db6485be32bc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-91cb28c7db6485be32bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-185d58e1fd71920472d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-185d58e1fd71920472d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5194ade900fd0ffdd0b2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5194ade900fd0ffdd0b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0fd50e816e1389cefd11"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0fd50e816e1389cefd11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-060c9dabd11be0b95525"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-060c9dabd11be0b95525`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a100f5f4389838fed7e1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a100f5f4389838fed7e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a48e3b1f2228038cea07"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a48e3b1f2228038cea07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4af3ab0e0caab5f9c40"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d4af3ab0e0caab5f9c40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51ca183fea7ee0058407"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-51ca183fea7ee0058407`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-99c039f00ffee27b82c0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-99c039f00ffee27b82c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ba088311724184099aa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ba088311724184099aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a2108a157de2170179f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8a2108a157de2170179f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-499c04a710c06cdfe65f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-499c04a710c06cdfe65f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ebb066d4441c064d977"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ebb066d4441c064d977`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c9aaf7d088fba0fab06"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0c9aaf7d088fba0fab06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e71f8f224630ed6c7ed7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e71f8f224630ed6c7ed7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b5006f05ebeaa529cd6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2b5006f05ebeaa529cd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1c0dac6ec5a22cb93673"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1c0dac6ec5a22cb93673`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5271b123c70df25b6ae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c5271b123c70df25b6ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d22c284b9fdd5e4da8d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d22c284b9fdd5e4da8d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69dbac597780954f3e51"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-69dbac597780954f3e51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ec0ae224e0e564c475c4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ec0ae224e0e564c475c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d93c88cebaff4b9f37e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d93c88cebaff4b9f37e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94d6ee2edd58604bd853"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-94d6ee2edd58604bd853`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ced11c1310fee8c11fc5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ced11c1310fee8c11fc5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-858cde169445bf625a12"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-858cde169445bf625a12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd002f81becf4b7990ff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd002f81becf4b7990ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09a37145cab346cd27fd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-09a37145cab346cd27fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b9d74ef5eb67cbddb56"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8b9d74ef5eb67cbddb56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3b50da22d028d1ce080d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3b50da22d028d1ce080d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bd2ade2d8ba993e53d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8bd2ade2d8ba993e53d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de9ea27a9391f3a80ce0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-de9ea27a9391f3a80ce0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-251dcb8b4e4db053844c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-251dcb8b4e4db053844c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-15fc0a306a8476a776c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-15fc0a306a8476a776c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b9fa7cde4f532d29862"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6b9fa7cde4f532d29862`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f365dab49abd2c75c1f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6f365dab49abd2c75c1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa516db39de73f5ac8c6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa516db39de73f5ac8c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4ac67af7c6fcc0b3e566"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4ac67af7c6fcc0b3e566`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-761ca9b25002a7a2fd77"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-761ca9b25002a7a2fd77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb2e9346f6c8b4689713"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cb2e9346f6c8b4689713`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0a2cd3b9bff06985e15"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f0a2cd3b9bff06985e15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-16b9689224eb13f22abc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-16b9689224eb13f22abc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd8f2cad7c52ab5277e1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cd8f2cad7c52ab5277e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-531da4fcf7964705508f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-531da4fcf7964705508f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d5dcba38daad4b7246b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0d5dcba38daad4b7246b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5659e84cf80c61fde7c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5659e84cf80c61fde7c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35f456a27a2bfb1c2928"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-35f456a27a2bfb1c2928`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4d8d21c0cb5b5a80862"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c4d8d21c0cb5b5a80862`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f46e4704ed58f519338e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f46e4704ed58f519338e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d09effb98e5b5dc135c1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d09effb98e5b5dc135c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76e979f4b4e8fee87b7d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-76e979f4b4e8fee87b7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e568ac65a852efe67ec8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e568ac65a852efe67ec8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0fed258f6d853f5c713"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b0fed258f6d853f5c713`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca2d6b8ad33bdde7eca4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca2d6b8ad33bdde7eca4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ea3414b244ca10d31af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8ea3414b244ca10d31af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52637fd5e9da9ddd20f2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-52637fd5e9da9ddd20f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bf4f9af4c0679100db1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5bf4f9af4c0679100db1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e44bf47e79bae795b303"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e44bf47e79bae795b303`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5d49e2f49ac0b5fbe22"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d5d49e2f49ac0b5fbe22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58168091fa05caf13e01"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-58168091fa05caf13e01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-617e63cc417919ea0200"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-617e63cc417919ea0200`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f0362a74a1e5354bf0d2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f0362a74a1e5354bf0d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14e8231bf12f98395b11"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-14e8231bf12f98395b11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9380b4f2cd2c592ec23"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e9380b4f2cd2c592ec23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9dc4facfc643a7cc0654"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9dc4facfc643a7cc0654`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-81fd53e09141884b01dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-81fd53e09141884b01dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e2e0ff646c495d3a102"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1e2e0ff646c495d3a102`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4601e72078911b5ef0fd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4601e72078911b5ef0fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cd0cfaa368f9d77c636"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8cd0cfaa368f9d77c636`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8acd7b6fb3463ee6c3ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8acd7b6fb3463ee6c3ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71a87346f28c7e153431"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-71a87346f28c7e153431`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-854b61aa6924b791a958"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-854b61aa6924b791a958`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e8826cbd5504c37ca3d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5e8826cbd5504c37ca3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce326bc2201aa860080e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce326bc2201aa860080e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-088ecffc5df86dc784ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-088ecffc5df86dc784ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44790673b2ca35b13876"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-44790673b2ca35b13876`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e76a120c3449142af4b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8e76a120c3449142af4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ced4311eefb15236c297"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ced4311eefb15236c297`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9771e1776b623f393a24"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9771e1776b623f393a24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4281a1091fd6670866a4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4281a1091fd6670866a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0bc55feb0a929948240"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b0bc55feb0a929948240`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-384ab53ac5d474d1aad9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-384ab53ac5d474d1aad9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-231f75b0ddaeb56de9be"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-231f75b0ddaeb56de9be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b212b02092bb189b7a6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6b212b02092bb189b7a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-723ba1f999eb6c6f0317"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-723ba1f999eb6c6f0317`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d8630c5687bfc0287a86"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d8630c5687bfc0287a86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee3caac4642696e4256e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ee3caac4642696e4256e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2883da9dbb46f750f4f7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2883da9dbb46f750f4f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd24284306a02d5e3082"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fd24284306a02d5e3082`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b1d692f5aadc46b2ee0e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b1d692f5aadc46b2ee0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae098c25733bd22ccf18"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ae098c25733bd22ccf18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2803c32bf6e1645492f7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2803c32bf6e1645492f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a49db6fc72310d7baed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a49db6fc72310d7baed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-11-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d507a0f03789d6ff4503"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d507a0f03789d6ff4503`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0a4f8ff51fb85b8e8df"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b0a4f8ff51fb85b8e8df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f4984a5f80a6e6fad01"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5f4984a5f80a6e6fad01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33f18da8428d62174006"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-33f18da8428d62174006`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-11-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d658770ee2567b4b61e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d658770ee2567b4b61e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4551fa1cb536228d9757"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4551fa1cb536228d9757`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af786cf08042b544bdc8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-af786cf08042b544bdc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1735217ec9ee875f5c70"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1735217ec9ee875f5c70`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-392687966bb41b607734"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-392687966bb41b607734`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2356daac6c6afcaa82a0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2356daac6c6afcaa82a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ef38fb7abb3e72cb367"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3ef38fb7abb3e72cb367`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-034dea23633e6145f496"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-034dea23633e6145f496`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b897e64533580a578e27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b897e64533580a578e27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47046f2ca81693f8e49d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-47046f2ca81693f8e49d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f071eb0f3a520228ecc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2f071eb0f3a520228ecc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ed95eebf9e8f3b3c625"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3ed95eebf9e8f3b3c625`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-beaa22159b1ddf20283c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-beaa22159b1ddf20283c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1cf5bb565ce556146f19"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1cf5bb565ce556146f19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ce326ece1a7526c1510"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ce326ece1a7526c1510`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10ad994a85b1c336c929"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10ad994a85b1c336c929`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-891a4d95814dd3db8593"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-891a4d95814dd3db8593`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-100d6ae6f4b8901ccbfd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-100d6ae6f4b8901ccbfd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9ba7a0b80397597baf6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d9ba7a0b80397597baf6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b4467e451fa4ed6c088"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b4467e451fa4ed6c088`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e68c662241a0ad79cf0a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e68c662241a0ad79cf0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c955188d6ce8eb0e1aa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0c955188d6ce8eb0e1aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1412afb74329a91e1b68"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1412afb74329a91e1b68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3646f423936bfcd24052"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3646f423936bfcd24052`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2006b073d2f6494fab61"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2006b073d2f6494fab61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d19863e4cc76e40921a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3d19863e4cc76e40921a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6216780266205c7cadd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d6216780266205c7cadd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a672e87a3f33366ba46"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4a672e87a3f33366ba46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-42d3293402110f06421f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-42d3293402110f06421f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c450baa93ae67e7c0493"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c450baa93ae67e7c0493`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62fe341d254a4d424367"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-62fe341d254a4d424367`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d14e3ce7c88c4e531916"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d14e3ce7c88c4e531916`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-27d27ec5288eec9fb186"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-27d27ec5288eec9fb186`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9405260f3f7fcad90cf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d9405260f3f7fcad90cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbc5c5d2826f3bb96699"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cbc5c5d2826f3bb96699`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44a1def53b9fbbdca9c0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-44a1def53b9fbbdca9c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-04ed2f137c7d00de90ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-04ed2f137c7d00de90ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe12635a0e89c644bdcf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fe12635a0e89c644bdcf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-594b00ca4d77e3060e2d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-594b00ca4d77e3060e2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8dc3e72903b1843815c2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8dc3e72903b1843815c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-856e8655b6c91bfbcdf3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-856e8655b6c91bfbcdf3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ff750b8ec56b229ae4f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ff750b8ec56b229ae4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d30d9c49493121e8085"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5d30d9c49493121e8085`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6081811a500d5e40564"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f6081811a500d5e40564`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-61c90af13a3835473e22"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-61c90af13a3835473e22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b440d1a40fb35cc3183"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b440d1a40fb35cc3183`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11bc4c14eec4713d9f81"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-11bc4c14eec4713d9f81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-692c6ca71f7ccb0b72db"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-692c6ca71f7ccb0b72db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8cebb5b1c05fb5c28f67"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8cebb5b1c05fb5c28f67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ee6b6d9059d08048272"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ee6b6d9059d08048272`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44a5b0550b7e12282c2a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-44a5b0550b7e12282c2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f2a2cee6b644427d111"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3f2a2cee6b644427d111`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eaf8080921a491f92f27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eaf8080921a491f92f27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00405e4ecf74a0aaa044"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-00405e4ecf74a0aaa044`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e28bbb69496dab679e75"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e28bbb69496dab679e75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-419eac17fa00eda0069a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-419eac17fa00eda0069a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-12-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f51d0f6815bd2d1314d2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f51d0f6815bd2d1314d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6854dc6c13571bdb5b0c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6854dc6c13571bdb5b0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-984f93a94695e479e33d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-984f93a94695e479e33d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-08e54b65ad4c227c5c58"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-08e54b65ad4c227c5c58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a8eea7d1e5e91e757074"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a8eea7d1e5e91e757074`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-398eb433e28f6e9a4176"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-398eb433e28f6e9a4176`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b35aa613dafa38e0c01a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b35aa613dafa38e0c01a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f4368148f8c6ce54a34"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7f4368148f8c6ce54a34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c7bd4b0b3f3d6e74a181"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c7bd4b0b3f3d6e74a181`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb358306c4bb5a98ee9a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fb358306c4bb5a98ee9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7401bddbf40d3acba72"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c7401bddbf40d3acba72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7c8ad96c5ad6c3825ff"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f7c8ad96c5ad6c3825ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-be769c3d58d54f251e67"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-be769c3d58d54f251e67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81269b222644dcb17122"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-81269b222644dcb17122`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-277cfa6fded7f0c658ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-277cfa6fded7f0c658ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b857311b0d3c4a4fc173"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b857311b0d3c4a4fc173`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0289e918136962f6e2d4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0289e918136962f6e2d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05fc6dd54c480ea021a6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-05fc6dd54c480ea021a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a743ea84732b28d67dc9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a743ea84732b28d67dc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe3233af2215b09e156f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe3233af2215b09e156f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-602625e5184897e22d27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-602625e5184897e22d27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd5b74c8da85d276d713"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cd5b74c8da85d276d713`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ddc5ca598fd5b0bfb119"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ddc5ca598fd5b0bfb119`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7a32b86503e31817a97"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a7a32b86503e31817a97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-99a00a73da5e16f3be4e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-99a00a73da5e16f3be4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd1fc978319d9ac61187"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd1fc978319d9ac61187`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fadef93e33b3e3e6d174"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fadef93e33b3e3e6d174`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0b2ffe90e7338368bf9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c0b2ffe90e7338368bf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6f55670442d7f6e8e414"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6f55670442d7f6e8e414`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23959b7da85a04b7d6c7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-23959b7da85a04b7d6c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1ea79085ef0a47f489c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e1ea79085ef0a47f489c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e4bc732ca806e33a338"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2e4bc732ca806e33a338`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-661e8faa6427c6a9f6a0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-661e8faa6427c6a9f6a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b35a4ecf9585f9827e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4b35a4ecf9585f9827e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de1c486f14b995a9548d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-de1c486f14b995a9548d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccc58fa73794a0a45df8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ccc58fa73794a0a45df8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ee8326e9d6ed07d20b0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ee8326e9d6ed07d20b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-162894aa042eebd9e6c6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-162894aa042eebd9e6c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e9656e944fecc975595"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9e9656e944fecc975595`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-786ca5a5bcf20da2d2c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-786ca5a5bcf20da2d2c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1008e664a648aa2bea37"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1008e664a648aa2bea37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-143805fd036f248db040"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-143805fd036f248db040`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c8255dff800da72f8f5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1c8255dff800da72f8f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7e0e68c4c5e9e5cb299"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a7e0e68c4c5e9e5cb299`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-25-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6378bce2caae67dab396"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6378bce2caae67dab396`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9630558b6a57bb12ea08"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9630558b6a57bb12ea08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14b182e59e8b97a53cfc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-14b182e59e8b97a53cfc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce299eeacc52661e4ad5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ce299eeacc52661e4ad5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c166ac67ee1bfef54852"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c166ac67ee1bfef54852`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae2e47150ab879683d88"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ae2e47150ab879683d88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d645a29355d920855ce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5d645a29355d920855ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73ffd4e4d71b42f6b613"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-73ffd4e4d71b42f6b613`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a68993964ffbe16cdec6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a68993964ffbe16cdec6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-246ce82a2de04a5937a8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-246ce82a2de04a5937a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49f5280b7ae9ec0951ad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-49f5280b7ae9ec0951ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-940f73723287d79cb9a3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-940f73723287d79cb9a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-13-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1d71267c862adee41294"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1d71267c862adee41294`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-946874d4cf73ac589b2c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-946874d4cf73ac589b2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3d2a67f6ea1893c4f26"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c3d2a67f6ea1893c4f26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec626a4215a65ebb0dd1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ec626a4215a65ebb0dd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-784cebda3cd1d6f632ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-784cebda3cd1d6f632ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9713b38a887573bbd5a2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9713b38a887573bbd5a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1463b2ed5b9a198acf2c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1463b2ed5b9a198acf2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93a7b97d82de18b5caa7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-93a7b97d82de18b5caa7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cbc049e3f045bd9a61a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cbc049e3f045bd9a61a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2013e5c00c7b6501f358"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2013e5c00c7b6501f358`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7feaa262c1f95c84730"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b7feaa262c1f95c84730`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1087b03759cffabe3ebc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1087b03759cffabe3ebc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5bc7ef41f5d5fe8e30bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5bc7ef41f5d5fe8e30bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c62eb256005998f66482"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c62eb256005998f66482`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74eb1164a4cd205d0919"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-74eb1164a4cd205d0919`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2190251a58219d1bf2ee"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2190251a58219d1bf2ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a243309eeaea9cc6177"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a243309eeaea9cc6177`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8505ebcc440fe5ad48fe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8505ebcc440fe5ad48fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bdda989d9abd93c129cc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bdda989d9abd93c129cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfb0dc166f5957c12ac8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cfb0dc166f5957c12ac8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c172846c7a166f7e12ed"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c172846c7a166f7e12ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70c187232d493efcf574"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-70c187232d493efcf574`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-399ab78a1a26c9ef92c0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-399ab78a1a26c9ef92c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bd80eba4c0aa0cd57d0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6bd80eba4c0aa0cd57d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a572f9ae2c5df795da9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a572f9ae2c5df795da9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9572816d6dc6b73e7cd8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9572816d6dc6b73e7cd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2fd9532fc6b8e82133a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2fd9532fc6b8e82133a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d88b1332eae5497ef8c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d88b1332eae5497ef8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-21-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d0168dba6a2687e4dd81"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0168dba6a2687e4dd81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c410723b2e7433933dd7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c410723b2e7433933dd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e2aa5eadcb7653ed28a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2e2aa5eadcb7653ed28a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ae763684523bb51500a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2ae763684523bb51500a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-22-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2f4461d70df58a0c666c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2f4461d70df58a0c666c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79c33b79dc5601c94d61"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-79c33b79dc5601c94d61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-257a0cf7bc33e0eddb81"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-257a0cf7bc33e0eddb81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0ccca94a6f005cfbfc9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a0ccca94a6f005cfbfc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-23-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b56cf1d86b453dc35397"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b56cf1d86b453dc35397`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a886ef2a50e085bff75"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2a886ef2a50e085bff75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df91268fe1451684ef1a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-df91268fe1451684ef1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f79fa36776467611f95"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2f79fa36776467611f95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-24-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dd30e0cdb85c0489557d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd30e0cdb85c0489557d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e85415cdc5f3c5f84ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1e85415cdc5f3c5f84ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebb36699ee13a99d2e3e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ebb36699ee13a99d2e3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7f1064f087aa3718cfa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c7f1064f087aa3718cfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-26-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0351cd50b9f76a530e77"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0351cd50b9f76a530e77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79a75020a936c8dc2d47"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-79a75020a936c8dc2d47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa3a4962a8858c98d741"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aa3a4962a8858c98d741`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1a282428f1e054699a6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c1a282428f1e054699a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-27-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d6f240438d458eea0709"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d6f240438d458eea0709`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0beb062884be6194b53"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b0beb062884be6194b53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c673283b9b42fb86d97"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1c673283b9b42fb86d97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e9bcf3dff745f35e770"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e9bcf3dff745f35e770`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-28-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-90bd756b9e4e100ea02a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-90bd756b9e4e100ea02a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f43251e755e55b5ff07"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9f43251e755e55b5ff07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-797bb75d21a01a366a55"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-797bb75d21a01a366a55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6bf50c81c1e1ae127b1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a6bf50c81c1e1ae127b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-14-in; to port: channel-29-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-exit-slip:canonical-southeast | <a href="#case-preview_review-57e6a7ed61083c05f5c7">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-exit-slip:canonical-top | <a href="#case-preview_review-d8487ad37032b37bcc74">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-upper-exit-slip:connection-overview | <a href="#case-preview_review-f4daf90fd3e2d68bf529">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-exit-slip:canonical-southeast</summary>

<a id="case-preview_review-57e6a7ed61083c05f5c7"></a>

**General: unverified** — `preview_review-57e6a7ed61083c05f5c7`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-exit-slip:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-exit-slip:canonical-top</summary>

<a id="case-preview_review-d8487ad37032b37bcc74"></a>

**General: unverified** — `preview_review-d8487ad37032b37bcc74`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-exit-slip:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-upper-exit-slip:connection-overview</summary>

<a id="case-preview_review-f4daf90fd3e2d68bf529"></a>

**General: unverified** — `preview_review-f4daf90fd3e2d68bf529`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-upper-exit-slip:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the slip function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
