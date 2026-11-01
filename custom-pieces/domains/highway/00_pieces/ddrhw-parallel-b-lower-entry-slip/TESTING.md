---
title: "Testing: DD RHW-4 \u2014 L1 Entry Slip Lanes \u2014 Parallel \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1 Entry Slip Lanes — Parallel — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **DD RHW-4 — L1 Entry Slip Lanes — Parallel — Alignment B**, permanent ID `ddrhw-parallel-b-lower-entry-slip`, as **P05** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 2 cells inside its 2 × 2 bounding footprint. Both native decks at 7.5 m and 15 m; the named access is at 7.5 m. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-11-out` | road / 1 / primary | out | [-3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-01-in` | road / 1 / primary | in | [-3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-12-out` | road / 1 / primary | out | [3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-02-in` | road / 1 / primary | in | [3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-03-in` | road / 1 / primary | in | [7.155817, -8.0, 7.5]; [-0.1877337346157676, -0.9822199574877394]; 0.0 | `path-interface-df8ba0b6bf00c020149a` |
| `channel-04-in` | road / 1 / primary | in | [8.0, -19.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-13-out` | road / 1 / primary | out | [8.0, -19.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-05-in` | road / 1 / primary | in | [8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-14-out` | road / 1 / primary | out | [8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-15-out` | road / 1 / primary | out | [8.0, 0.265154, 7.5]; [-0.38533299504733237, -0.9227775912579653]; 0.0 | `path-interface-7da54e874457c77b5294` |
| `channel-16-out` | road / 1 / primary | out | [12.8, -8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-06-in` | road / 1 / primary | in | [12.8, -8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-07-in` | road / 1 / primary | in | [15.029437, 8.0, 6.390578]; [-0.7071067811865476, -0.7071067811865476]; 0.179116252 | `path-interface-758253be5f8ec9e11340` |
| `channel-17-out` | road / 1 / primary | out | [19.2, -8.0, 7.5]; [-0.7071067811865478, -0.7071067811865474]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-08-in` | road / 1 / primary | in | [19.2, -8.0, 15.0]; [0.7071067811865478, 0.7071067811865474]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-09-in` | road / 1 / primary | in | [24.0, -3.2, 7.5]; [-0.7071067811865478, -0.7071067811865474]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-18-out` | road / 1 / primary | out | [24.0, -3.2, 15.0]; [0.7071067811865478, 0.7071067811865474]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-10-in` | road / 1 / primary | in | [24.0, 3.2, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-19-out` | road / 1 / primary | out | [24.0, 3.2, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-14-out` | primary |
| road | `channel-02-in` → `channel-13-out` | primary |
| road | `channel-03-in` → `channel-11-out` | primary |
| road | `channel-04-in` → `channel-12-out` | primary |
| road | `channel-05-in` → `channel-11-out` | primary |
| road | `channel-06-in` → `channel-19-out` | primary |
| road | `channel-07-in` → `channel-15-out` | primary |
| road | `channel-08-in` → `channel-18-out` | primary |
| road | `channel-09-in` → `channel-17-out` | primary |
| road | `channel-10-in` → `channel-16-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-lower-entry-slip
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **48,548 indexed triangles** and **10 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

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
- [ ] Route Query: 0/40 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/40 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 421, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-lower-entry-slip/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-lower-entry-slip/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b93711ed3421d9c4e174">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b93711ed3421d9c4e174"></a>

**General: unverified** — `software_resources-b93711ed3421d9c4e174`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b93711ed3421d9c4e174">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b93711ed3421d9c4e174"></a>

**General: unverified** — `software_connectivity-b93711ed3421d9c4e174`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-29ff742febf764c2e5cb">[ ] unverified</a> | <a href="#case-in_game_render-885a2abd815eefaa55ad">[ ] unverified</a> | <a href="#case-in_game_render-2fcee1eda24d266e0ac1">[ ] unverified</a> | <a href="#case-in_game_render-1800d232087f0a4ac5c7">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-29ff742febf764c2e5cb"></a>

**0° CCW: unverified** — `in_game_render-29ff742febf764c2e5cb`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-885a2abd815eefaa55ad"></a>

**90° CCW: unverified** — `in_game_render-885a2abd815eefaa55ad`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2fcee1eda24d266e0ac1"></a>

**180° CCW: unverified** — `in_game_render-2fcee1eda24d266e0ac1`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1800d232087f0a4ac5c7"></a>

**270° CCW: unverified** — `in_game_render-1800d232087f0a4ac5c7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-29ff742febf764c2e5cb">[ ] unverified</a> | <a href="#case-in_game_placement-885a2abd815eefaa55ad">[ ] unverified</a> | <a href="#case-in_game_placement-2fcee1eda24d266e0ac1">[ ] unverified</a> | <a href="#case-in_game_placement-1800d232087f0a4ac5c7">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-29ff742febf764c2e5cb"></a>

**0° CCW: unverified** — `in_game_placement-29ff742febf764c2e5cb`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-885a2abd815eefaa55ad"></a>

**90° CCW: unverified** — `in_game_placement-885a2abd815eefaa55ad`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2fcee1eda24d266e0ac1"></a>

**180° CCW: unverified** — `in_game_placement-2fcee1eda24d266e0ac1`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1800d232087f0a4ac5c7"></a>

**270° CCW: unverified** — `in_game_placement-1800d232087f0a4ac5c7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-29ff742febf764c2e5cb">[ ] unverified</a> | <a href="#case-in_game_demolition-885a2abd815eefaa55ad">[ ] unverified</a> | <a href="#case-in_game_demolition-2fcee1eda24d266e0ac1">[ ] unverified</a> | <a href="#case-in_game_demolition-1800d232087f0a4ac5c7">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-29ff742febf764c2e5cb"></a>

**0° CCW: unverified** — `in_game_demolition-29ff742febf764c2e5cb`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-885a2abd815eefaa55ad"></a>

**90° CCW: unverified** — `in_game_demolition-885a2abd815eefaa55ad`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2fcee1eda24d266e0ac1"></a>

**180° CCW: unverified** — `in_game_demolition-2fcee1eda24d266e0ac1`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1800d232087f0a4ac5c7"></a>

**270° CCW: unverified** — `in_game_demolition-1800d232087f0a4ac5c7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-29ff742febf764c2e5cb">[ ] unverified</a> | <a href="#case-in_game_save_reload-885a2abd815eefaa55ad">[ ] unverified</a> | <a href="#case-in_game_save_reload-2fcee1eda24d266e0ac1">[ ] unverified</a> | <a href="#case-in_game_save_reload-1800d232087f0a4ac5c7">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-29ff742febf764c2e5cb"></a>

**0° CCW: unverified** — `in_game_save_reload-29ff742febf764c2e5cb`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-885a2abd815eefaa55ad"></a>

**90° CCW: unverified** — `in_game_save_reload-885a2abd815eefaa55ad`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2fcee1eda24d266e0ac1"></a>

**180° CCW: unverified** — `in_game_save_reload-2fcee1eda24d266e0ac1`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1800d232087f0a4ac5c7"></a>

**270° CCW: unverified** — `in_game_save_reload-1800d232087f0a4ac5c7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-7fde8b4fc6206fbd1ad4">[ ] unverified</a> | <a href="#case-in_game_route_query-e156ce2c0b9b8f69bd99">[ ] unverified</a> | <a href="#case-in_game_route_query-97c60f95e6e176208d8a">[ ] unverified</a> | <a href="#case-in_game_route_query-617a9bd9b59d650b8357">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-513688fbe40046bd9aff">[ ] unverified</a> | <a href="#case-in_game_route_query-46b0c40930aab63f501c">[ ] unverified</a> | <a href="#case-in_game_route_query-d9c035152eeac1d518bd">[ ] unverified</a> | <a href="#case-in_game_route_query-aebd091b5c2d9e14a43d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-4a8541a721bd328d01c6">[ ] unverified</a> | <a href="#case-in_game_route_query-006316f28562df82e260">[ ] unverified</a> | <a href="#case-in_game_route_query-d16125f1c91b52754e26">[ ] unverified</a> | <a href="#case-in_game_route_query-9fe5e2dcadfcd2c8328e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-d6b6769f2c6328a8553a">[ ] unverified</a> | <a href="#case-in_game_route_query-c2502a04dfb1bc1aec0e">[ ] unverified</a> | <a href="#case-in_game_route_query-289942c19c40305420f1">[ ] unverified</a> | <a href="#case-in_game_route_query-fb42a133906b13bfb98e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-a74fcdc16e9ba96ccd0d">[ ] unverified</a> | <a href="#case-in_game_route_query-0e021db6df8a81cef29b">[ ] unverified</a> | <a href="#case-in_game_route_query-2e4ebcc9d011b371f56b">[ ] unverified</a> | <a href="#case-in_game_route_query-e745937480121ac7591c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-8177877dc4db33e225a9">[ ] unverified</a> | <a href="#case-in_game_route_query-b1257dfbb22044072889">[ ] unverified</a> | <a href="#case-in_game_route_query-986c2a69f037565595b7">[ ] unverified</a> | <a href="#case-in_game_route_query-6458bd696c8a93dc0dbb">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out | — | <a href="#case-in_game_route_query-a485e252c4d37d4d33b5">[ ] unverified</a> | <a href="#case-in_game_route_query-f4536a6b3490b18e1510">[ ] unverified</a> | <a href="#case-in_game_route_query-76eccca1b76112ca4240">[ ] unverified</a> | <a href="#case-in_game_route_query-c78c30abf2d088ca4b6e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-1fc9ea092c9cb1d2fb3b">[ ] unverified</a> | <a href="#case-in_game_route_query-42d264fd8125722bdc65">[ ] unverified</a> | <a href="#case-in_game_route_query-0d8f8bd7c676ce1c00df">[ ] unverified</a> | <a href="#case-in_game_route_query-faf466b48dc7a3eaec7d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-e28ef7484058cfcfc32d">[ ] unverified</a> | <a href="#case-in_game_route_query-4bc0a85331057ea48536">[ ] unverified</a> | <a href="#case-in_game_route_query-fae4baec8eb12395296c">[ ] unverified</a> | <a href="#case-in_game_route_query-8df4268dfe4a33181998">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-bad96b9546be2fd42be9">[ ] unverified</a> | <a href="#case-in_game_route_query-d7257a599ba249037093">[ ] unverified</a> | <a href="#case-in_game_route_query-bb3a0b92ed4f15be86bf">[ ] unverified</a> | <a href="#case-in_game_route_query-e5b7f730c13193990ee4">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-7fde8b4fc6206fbd1ad4"></a>

**0° CCW: unverified** — `in_game_route_query-7fde8b4fc6206fbd1ad4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-e156ce2c0b9b8f69bd99"></a>

**90° CCW: unverified** — `in_game_route_query-e156ce2c0b9b8f69bd99`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-97c60f95e6e176208d8a"></a>

**180° CCW: unverified** — `in_game_route_query-97c60f95e6e176208d8a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-617a9bd9b59d650b8357"></a>

**270° CCW: unverified** — `in_game_route_query-617a9bd9b59d650b8357`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-513688fbe40046bd9aff"></a>

**0° CCW: unverified** — `in_game_route_query-513688fbe40046bd9aff`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-46b0c40930aab63f501c"></a>

**90° CCW: unverified** — `in_game_route_query-46b0c40930aab63f501c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-d9c035152eeac1d518bd"></a>

**180° CCW: unverified** — `in_game_route_query-d9c035152eeac1d518bd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-aebd091b5c2d9e14a43d"></a>

**270° CCW: unverified** — `in_game_route_query-aebd091b5c2d9e14a43d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-4a8541a721bd328d01c6"></a>

**0° CCW: unverified** — `in_game_route_query-4a8541a721bd328d01c6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-006316f28562df82e260"></a>

**90° CCW: unverified** — `in_game_route_query-006316f28562df82e260`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-d16125f1c91b52754e26"></a>

**180° CCW: unverified** — `in_game_route_query-d16125f1c91b52754e26`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-9fe5e2dcadfcd2c8328e"></a>

**270° CCW: unverified** — `in_game_route_query-9fe5e2dcadfcd2c8328e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-d6b6769f2c6328a8553a"></a>

**0° CCW: unverified** — `in_game_route_query-d6b6769f2c6328a8553a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-c2502a04dfb1bc1aec0e"></a>

**90° CCW: unverified** — `in_game_route_query-c2502a04dfb1bc1aec0e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-289942c19c40305420f1"></a>

**180° CCW: unverified** — `in_game_route_query-289942c19c40305420f1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-fb42a133906b13bfb98e"></a>

**270° CCW: unverified** — `in_game_route_query-fb42a133906b13bfb98e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-a74fcdc16e9ba96ccd0d"></a>

**0° CCW: unverified** — `in_game_route_query-a74fcdc16e9ba96ccd0d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-0e021db6df8a81cef29b"></a>

**90° CCW: unverified** — `in_game_route_query-0e021db6df8a81cef29b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-2e4ebcc9d011b371f56b"></a>

**180° CCW: unverified** — `in_game_route_query-2e4ebcc9d011b371f56b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-e745937480121ac7591c"></a>

**270° CCW: unverified** — `in_game_route_query-e745937480121ac7591c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-8177877dc4db33e225a9"></a>

**0° CCW: unverified** — `in_game_route_query-8177877dc4db33e225a9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-b1257dfbb22044072889"></a>

**90° CCW: unverified** — `in_game_route_query-b1257dfbb22044072889`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-986c2a69f037565595b7"></a>

**180° CCW: unverified** — `in_game_route_query-986c2a69f037565595b7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-6458bd696c8a93dc0dbb"></a>

**270° CCW: unverified** — `in_game_route_query-6458bd696c8a93dc0dbb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out</summary>

<a id="case-in_game_route_query-a485e252c4d37d4d33b5"></a>

**0° CCW: unverified** — `in_game_route_query-a485e252c4d37d4d33b5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-f4536a6b3490b18e1510"></a>

**90° CCW: unverified** — `in_game_route_query-f4536a6b3490b18e1510`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-76eccca1b76112ca4240"></a>

**180° CCW: unverified** — `in_game_route_query-76eccca1b76112ca4240`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-c78c30abf2d088ca4b6e"></a>

**270° CCW: unverified** — `in_game_route_query-c78c30abf2d088ca4b6e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-1fc9ea092c9cb1d2fb3b"></a>

**0° CCW: unverified** — `in_game_route_query-1fc9ea092c9cb1d2fb3b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-42d264fd8125722bdc65"></a>

**90° CCW: unverified** — `in_game_route_query-42d264fd8125722bdc65`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-0d8f8bd7c676ce1c00df"></a>

**180° CCW: unverified** — `in_game_route_query-0d8f8bd7c676ce1c00df`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-faf466b48dc7a3eaec7d"></a>

**270° CCW: unverified** — `in_game_route_query-faf466b48dc7a3eaec7d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-e28ef7484058cfcfc32d"></a>

**0° CCW: unverified** — `in_game_route_query-e28ef7484058cfcfc32d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-4bc0a85331057ea48536"></a>

**90° CCW: unverified** — `in_game_route_query-4bc0a85331057ea48536`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-fae4baec8eb12395296c"></a>

**180° CCW: unverified** — `in_game_route_query-fae4baec8eb12395296c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-8df4268dfe4a33181998"></a>

**270° CCW: unverified** — `in_game_route_query-8df4268dfe4a33181998`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-bad96b9546be2fd42be9"></a>

**0° CCW: unverified** — `in_game_route_query-bad96b9546be2fd42be9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-d7257a599ba249037093"></a>

**90° CCW: unverified** — `in_game_route_query-d7257a599ba249037093`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-bb3a0b92ed4f15be86bf"></a>

**180° CCW: unverified** — `in_game_route_query-bb3a0b92ed4f15be86bf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-e5b7f730c13193990ee4"></a>

**270° CCW: unverified** — `in_game_route_query-e5b7f730c13193990ee4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-7fde8b4fc6206fbd1ad4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e156ce2c0b9b8f69bd99">[ ] unverified</a> | <a href="#case-in_game_visible_travel-97c60f95e6e176208d8a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-617a9bd9b59d650b8357">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-513688fbe40046bd9aff">[ ] unverified</a> | <a href="#case-in_game_visible_travel-46b0c40930aab63f501c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d9c035152eeac1d518bd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-aebd091b5c2d9e14a43d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-4a8541a721bd328d01c6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-006316f28562df82e260">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d16125f1c91b52754e26">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9fe5e2dcadfcd2c8328e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-d6b6769f2c6328a8553a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c2502a04dfb1bc1aec0e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-289942c19c40305420f1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fb42a133906b13bfb98e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-a74fcdc16e9ba96ccd0d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0e021db6df8a81cef29b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2e4ebcc9d011b371f56b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e745937480121ac7591c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-8177877dc4db33e225a9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b1257dfbb22044072889">[ ] unverified</a> | <a href="#case-in_game_visible_travel-986c2a69f037565595b7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6458bd696c8a93dc0dbb">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out | — | <a href="#case-in_game_visible_travel-a485e252c4d37d4d33b5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f4536a6b3490b18e1510">[ ] unverified</a> | <a href="#case-in_game_visible_travel-76eccca1b76112ca4240">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c78c30abf2d088ca4b6e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-1fc9ea092c9cb1d2fb3b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-42d264fd8125722bdc65">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0d8f8bd7c676ce1c00df">[ ] unverified</a> | <a href="#case-in_game_visible_travel-faf466b48dc7a3eaec7d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-e28ef7484058cfcfc32d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4bc0a85331057ea48536">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fae4baec8eb12395296c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8df4268dfe4a33181998">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-bad96b9546be2fd42be9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d7257a599ba249037093">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bb3a0b92ed4f15be86bf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e5b7f730c13193990ee4">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-7fde8b4fc6206fbd1ad4"></a>

**0° CCW: unverified** — `in_game_visible_travel-7fde8b4fc6206fbd1ad4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-e156ce2c0b9b8f69bd99"></a>

**90° CCW: unverified** — `in_game_visible_travel-e156ce2c0b9b8f69bd99`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-97c60f95e6e176208d8a"></a>

**180° CCW: unverified** — `in_game_visible_travel-97c60f95e6e176208d8a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-617a9bd9b59d650b8357"></a>

**270° CCW: unverified** — `in_game_visible_travel-617a9bd9b59d650b8357`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-513688fbe40046bd9aff"></a>

**0° CCW: unverified** — `in_game_visible_travel-513688fbe40046bd9aff`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-46b0c40930aab63f501c"></a>

**90° CCW: unverified** — `in_game_visible_travel-46b0c40930aab63f501c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-d9c035152eeac1d518bd"></a>

**180° CCW: unverified** — `in_game_visible_travel-d9c035152eeac1d518bd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-aebd091b5c2d9e14a43d"></a>

**270° CCW: unverified** — `in_game_visible_travel-aebd091b5c2d9e14a43d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-4a8541a721bd328d01c6"></a>

**0° CCW: unverified** — `in_game_visible_travel-4a8541a721bd328d01c6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-006316f28562df82e260"></a>

**90° CCW: unverified** — `in_game_visible_travel-006316f28562df82e260`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-d16125f1c91b52754e26"></a>

**180° CCW: unverified** — `in_game_visible_travel-d16125f1c91b52754e26`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-9fe5e2dcadfcd2c8328e"></a>

**270° CCW: unverified** — `in_game_visible_travel-9fe5e2dcadfcd2c8328e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-11-out; entry: channel-03-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-d6b6769f2c6328a8553a"></a>

**0° CCW: unverified** — `in_game_visible_travel-d6b6769f2c6328a8553a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-c2502a04dfb1bc1aec0e"></a>

**90° CCW: unverified** — `in_game_visible_travel-c2502a04dfb1bc1aec0e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-289942c19c40305420f1"></a>

**180° CCW: unverified** — `in_game_visible_travel-289942c19c40305420f1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-fb42a133906b13bfb98e"></a>

**270° CCW: unverified** — `in_game_visible_travel-fb42a133906b13bfb98e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-a74fcdc16e9ba96ccd0d"></a>

**0° CCW: unverified** — `in_game_visible_travel-a74fcdc16e9ba96ccd0d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-0e021db6df8a81cef29b"></a>

**90° CCW: unverified** — `in_game_visible_travel-0e021db6df8a81cef29b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-2e4ebcc9d011b371f56b"></a>

**180° CCW: unverified** — `in_game_visible_travel-2e4ebcc9d011b371f56b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-e745937480121ac7591c"></a>

**270° CCW: unverified** — `in_game_visible_travel-e745937480121ac7591c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-8177877dc4db33e225a9"></a>

**0° CCW: unverified** — `in_game_visible_travel-8177877dc4db33e225a9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-b1257dfbb22044072889"></a>

**90° CCW: unverified** — `in_game_visible_travel-b1257dfbb22044072889`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-986c2a69f037565595b7"></a>

**180° CCW: unverified** — `in_game_visible_travel-986c2a69f037565595b7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-6458bd696c8a93dc0dbb"></a>

**270° CCW: unverified** — `in_game_visible_travel-6458bd696c8a93dc0dbb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out</summary>

<a id="case-in_game_visible_travel-a485e252c4d37d4d33b5"></a>

**0° CCW: unverified** — `in_game_visible_travel-a485e252c4d37d4d33b5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-f4536a6b3490b18e1510"></a>

**90° CCW: unverified** — `in_game_visible_travel-f4536a6b3490b18e1510`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-76eccca1b76112ca4240"></a>

**180° CCW: unverified** — `in_game_visible_travel-76eccca1b76112ca4240`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-c78c30abf2d088ca4b6e"></a>

**270° CCW: unverified** — `in_game_visible_travel-c78c30abf2d088ca4b6e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-1fc9ea092c9cb1d2fb3b"></a>

**0° CCW: unverified** — `in_game_visible_travel-1fc9ea092c9cb1d2fb3b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-42d264fd8125722bdc65"></a>

**90° CCW: unverified** — `in_game_visible_travel-42d264fd8125722bdc65`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-0d8f8bd7c676ce1c00df"></a>

**180° CCW: unverified** — `in_game_visible_travel-0d8f8bd7c676ce1c00df`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-faf466b48dc7a3eaec7d"></a>

**270° CCW: unverified** — `in_game_visible_travel-faf466b48dc7a3eaec7d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-e28ef7484058cfcfc32d"></a>

**0° CCW: unverified** — `in_game_visible_travel-e28ef7484058cfcfc32d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-4bc0a85331057ea48536"></a>

**90° CCW: unverified** — `in_game_visible_travel-4bc0a85331057ea48536`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-fae4baec8eb12395296c"></a>

**180° CCW: unverified** — `in_game_visible_travel-fae4baec8eb12395296c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-8df4268dfe4a33181998"></a>

**270° CCW: unverified** — `in_game_visible_travel-8df4268dfe4a33181998`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-bad96b9546be2fd42be9"></a>

**0° CCW: unverified** — `in_game_visible_travel-bad96b9546be2fd42be9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-d7257a599ba249037093"></a>

**90° CCW: unverified** — `in_game_visible_travel-d7257a599ba249037093`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-bb3a0b92ed4f15be86bf"></a>

**180° CCW: unverified** — `in_game_visible_travel-bb3a0b92ed4f15be86bf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-e5b7f730c13193990ee4"></a>

**270° CCW: unverified** — `in_game_visible_travel-e5b7f730c13193990ee4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 320 cases; unverified: 320</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-94d4b18206429adfc5e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c38828bdd527be6974ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-156ec59c77453f2fb4e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-482b9a558be0ae2849eb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f08708d5d6fa07bb66a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7db8271eebc97f041712">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8654804e674e68e68023">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-598086097eb20da4b2f4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a2c8d525b392150dfd96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ace301689eec1aa01fca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-648f5cd5b143331d8ea0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e424c5e3fab39104f333">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5e5125e492fcc0f904f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0368987c72318c7bc43e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9c4da197ae25e8fbf7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c89da95c800afb3f386">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-77980bdedce008d68ae1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e638e952e69ff0e032e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ff058ca7a80929868a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cddb2d8efdcd65d31610">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a6899ca24084a157d2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5119c2abad26003795aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-267b638124fcc6ad8c3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-08593e3c24c6fc2250c9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cde641306ef4cf4cbcef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a134e822063762ff8d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-618e4c3fac7490dd9eaf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92c39278db04ceabd94d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7be9380bfbb354d63185">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f3ebff047c93009b51f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b382380c752358ff813">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3faaf95004d2307f4776">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3f565fa0c323a9c73756">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25388092812d8c1a8e89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1decc2efc65ae2e6313d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a37bfa8303d75a1177a3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-67684e05cd45530b26b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4eb42987367eb29f07a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a0e8ffaec7f7482d6f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-382b20e9d45f486d7c17">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3a69404a81af36c4a52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45784e883af926f5d0c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-127b300b6285ee747b69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c1b737d57dda12df0e7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bdeb37e9b92ebb5d5542">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1e56109d6f9ca102335">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ca3fa3aa4967296f460">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd8260dcdbc67b07277f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e8896a6ffb7b10b3f51f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84074e61e40cafbe8afc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81ed0f6bb0ce72412263">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09167edf4f727a35db63">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-11c70cb135234a5b8bb2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7823dd70315708d1be1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6db05e64ba9c9f3bd0cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c755623b2bded543be2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-174cba9629867cca76b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2a762b83aa807b3cdd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6951352be6c4fca8c494">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ed61d50f51a7f55996d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c804c939002990aa7cd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cea590b919fa5bea6d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62ebde113a296aa74afb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbf60d46d9f91afc0a8f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3c06866f4e3f65048c58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4de743be0f0ca2298bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64208706c5d2ef2316ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2dea2f0c0f4a1ff338b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-51f84a1b91908fde640e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c11d5c876607cd1f5b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7492e55a91f704725b10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9502fb7bf57f66d18012">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c20060def61713fbec39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cccbbce4c44032b7780d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a0f7f3100a7096dd95b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45261ebd7a2c6eefc7d5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e189badda694bd40ff4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a9a4d549eab55159d88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef8f98e3a5ddb1655f4c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b14189aa6230c22d4da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-81311c336d12deeb804b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4589653ea7bc321f8d72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bf633312314b20979fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a53c4bffd1a16608f352">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3eb94af836a06fd6b022">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cb0eda56c6e0296c116">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50457f90a7d16074b406">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01eb10428c2ed0562490">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca6ce9c486650bf52d83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b6260de12a4f5537009">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81baa1b06e73f7c11dcd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83a4b69d01613f65dd05">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a11fcd557e69eaed342">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4cb727a6a69efa495af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e1fac2271a89d163f89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc8024cab0d555ea8ca3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-363f343fd2edcb858639">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b325d516345471fb759">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c53346bcb18736533b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a43fed1a2f4d668cc3e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-865ff3455fdaa075edec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1097d5070ea5e6394433">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffc9b5a826e4e2506b88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3418004072a44fc63b99">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8c2bbfcf74646fe6aa4c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ac82a73c6bd27a98ea4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83cecd600006e104656e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bcfe433ae0b90eff43da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0d0b11c78615b557503a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef0912de29dd66971ee8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c40647f6ae4dbc1e6f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68e79b6b8359262a44da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-be74bfe7e1948f84d03e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1688114b18798fe20706">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a17bfdc3da4e1ef4b186">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad0e22d43b521de75b6e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-805f050897b3f81a97ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e661f9d46fb186f795e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b239cc2bd337af0c67a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-401b86b7fea74c59c54b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a22d6358affc10a3bcf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3888f95fe68e2c64258b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af55c1300fc24d592952">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3dfd6bf89af064fd46dd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-82b135631f0516874208">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68389310d79206d0ffe3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8bc1542a4a335b0ee66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b7503f88c34ef1c2c64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e377e6f23c7f31e6def5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ad574ca651e947be4fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a3b6636faaf8e6880f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a270dde447a358aca18">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d5bdd5534945adbba6a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fec94a2dd851311e3c39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-137a38134ed72bee3d49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ca9af662e0df9d9a0ce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e7702a56919b66352c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1db4480985e25a0029e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85ee6eef778014e080b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a93f741b466b6b36b67">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3578e40aa18f0eb6d612">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b91319da9c7c4c3bd227">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7d8766a50ef41a36db5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dcaae5dc0974c3e192f1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1124cd39a3238d07e9cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9fd0be04b470ed2eb2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ffd7efad769c060853e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3797ac08747faf0204c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-897d03274e0f7cd46e2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4385f3859da5d359e1d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-031e80ef563fb581a0ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f310cbb796cdf7c7b0c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e8ddd3b3fdce62a5c71b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ab2412698ff35f2ac1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4270353ef44f4e2c1e68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-075cb1a273365e9f791d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6bb8d4923d445ece7ba7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54509c1852d611591707">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a56b1cc18cb1efee5d58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87eff3ec5a53836c1021">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-53ed37e650e49f997f4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1daf15053c8690396d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-371791769ae4ae9be910">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bc87b7a99ed153a0096">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-80866287187b39dd54cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f132dde61324f6c22ee7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5b8cf9530de87e56d76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6acdcc16ed38e9531108">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b578b8f42cd79916f349">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-259bda604918408959dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72f4474c083f93199d65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4811c6b7c7e1f9167a5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5417a9f185a2f444be4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2f529f11ee2928f6a21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a4cf0ae7e7ac5e7d669">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-792570d486841efb6b90">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e089a86806d2939a455">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebdb74d309759bb80d66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75a9f4f0700b5016482a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-678e07e2ad6591016f90">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e803868e484442f53319">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27fc4032d12171b5209f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6450a3bcc92596d09c3b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ef07ac4033890913e0e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca6f83c2bcff85f14faa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-283008b6595888e3ec2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7eb3a52ac048bc106cbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7bdbe62323287f01f753">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4a7d6670cc6cf0a133b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1e7b369860123d55724">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ca06a9370c19dc35e0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5fe3d9f65b39a55f730">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-efc5b0b3ab0788a57f73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6b551e1836485c24743">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c6a99d1e2d281555543">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03148b2f7599f5422ed7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc1344d73719c61f82d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d8399a1055a7c3ffb99">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4930114240f2c85333a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14ea08e859fc540a2c1a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e8e9683b6c8e7318d1a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b55b1cd216371fe0e249">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f71069d704e22ae62485">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2f736226f24849f26ca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-80323d5d84d0434c3797">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f37bcde571f09d5cfb11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c1b034f06129e5ec71d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d0fc834f23121e71cba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-893e9918599ba0aa44cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cc72793d12ed7fb7539">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50e1ca6dcd2cb25ec806">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-350efd663290733cc0f1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-56d970b43df615067ab0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2011625addf30a448d40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b5ac96975d41c0d96a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0321a9963a585ea253de">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c59fe08bcb6bde42a608">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a7a1a8bd235d28b3a9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c16aa17e7441c4d7f97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89738acb42836cb62013">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ff4ed4674cc821842152">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec80d50f57700d6706cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68c80ed30c07cd0f9a3b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e60582322bfc56a9729">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6bae99747cf3f8252460">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-434e74fb04879438bade">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bcdc923626dc23e0a35e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5fd4df2a08fb9f0c6d0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2117b22c4a7deacf0c0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f032584382f66fd15cbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7ce550fd5593fe4aa8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad8e57c12ee71eb78171">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-16df1e6958ce94b5e2cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de06cf83012a4286795b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed32bf7b539062286d6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40c81b71d74fd75f6780">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-faf7f955ffeb1eab09c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-adb4f788bc88c8b63398">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38403f0628f0b3c83813">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8046ca9caf8527648dd1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9da3e6d75b88d2473569">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc338949f8e3f9e16410">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9534e73248a11d0294bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-893f6d4121d3a616339a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f2933f43de637649804a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9955bf0edda05f32d14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3baa6bb6072f3b15b33">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dcf03233f2cd75f017fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-76301c55dc2023ff12bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a8450d754bcd579d4d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fa77f9ea99e7c36b45b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc11391630a1af531055">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f54212176b97c9877f7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1dce867321431dec5070">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74e95e3d08f0387e60e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cac69397b45db95927b8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-967fe322a8d2a3189d52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d0f178341d2441a9e98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13d15402a1d4349bf5ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a79d496734cdf1936270">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6732191f03b01fb2c5ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfaf38fbe6bad9e784f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bec97c308009b79634e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a968d59f34f204e2edfe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-003ebc0cec57350d15ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ed0955018e8411362f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04b577aec9a9d279eed8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dcad556f48b72ffa1f47">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7a01c8fb6133ce7588ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b6ebf9710ce1289ead3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3547b6a40ebc4fa30d1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71124b679c4e9ba90ef4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-08ccdb85b899149874fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5cb331b456d22b4354b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30b43bcd252a0a38b770">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b1acd362d6d60b54dd6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1f5002d87ecea923caf5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b43aa8b5c314392cdb0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe3dfdca5bb9d6b75356">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04cac88f979b2f712185">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-62be2aee189f5e6f3dcb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fa448c0deca383c3ed2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-442e634da13ff6ca6bb8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6698c479e80e5b07681">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-35158724bb8559828c0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-133b8d1022414b7f104e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1336d61bf48e0688011d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cafa18304c98118b5aca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8cf909bbfb3b5ac37a82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6dbab1d1b173a19c1429">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f012a7cd31fb323d15b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8eb42cb4333a3a391d6c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-23eac39c379ba2f0db42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8650ce814f56e9409581">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7af41db06d7c2738ac93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f4394e83667f4e2a516">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b67e9ae37b50ece62a7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e605b9021d05e0d2bc95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b52a62ce5eb6b1ba0f9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d24bd7f52e817bdf2da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ba7641f58c7991f4e1a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9035408bdc406ad2c7d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63c79338b9cf67ebcd12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-067a4c654256ec82446b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-51ec101f9e160399541b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ffd6eef09337acf7d7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ab6b70361340fc36bfd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7c76a4c160dc175b4f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ffa21fbd17186e8631a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3bc0991cd228b2010a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31ff5412d13cce0765d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-181cd8b627ab463b092c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f831b11480553900fab3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01839b9165405280209f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3db6ba30e5096f803835">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03b852c954d8ab74e34a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dcc343b0d4231dd3eb05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f79e687c2bd3aeb91651">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5490e5f64decd3160193">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47bffd6029df6b9b00a2">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-94d4b18206429adfc5e7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-94d4b18206429adfc5e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c38828bdd527be6974ea"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c38828bdd527be6974ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-156ec59c77453f2fb4e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-156ec59c77453f2fb4e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-482b9a558be0ae2849eb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-482b9a558be0ae2849eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f08708d5d6fa07bb66a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f08708d5d6fa07bb66a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7db8271eebc97f041712"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7db8271eebc97f041712`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8654804e674e68e68023"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8654804e674e68e68023`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-598086097eb20da4b2f4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-598086097eb20da4b2f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a2c8d525b392150dfd96"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a2c8d525b392150dfd96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ace301689eec1aa01fca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ace301689eec1aa01fca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-648f5cd5b143331d8ea0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-648f5cd5b143331d8ea0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e424c5e3fab39104f333"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e424c5e3fab39104f333`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5e5125e492fcc0f904f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5e5125e492fcc0f904f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0368987c72318c7bc43e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0368987c72318c7bc43e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9c4da197ae25e8fbf7c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f9c4da197ae25e8fbf7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c89da95c800afb3f386"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4c89da95c800afb3f386`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-77980bdedce008d68ae1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-77980bdedce008d68ae1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e638e952e69ff0e032e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0e638e952e69ff0e032e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ff058ca7a80929868a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7ff058ca7a80929868a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cddb2d8efdcd65d31610"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cddb2d8efdcd65d31610`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a6899ca24084a157d2b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a6899ca24084a157d2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5119c2abad26003795aa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5119c2abad26003795aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-267b638124fcc6ad8c3e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-267b638124fcc6ad8c3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-08593e3c24c6fc2250c9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-08593e3c24c6fc2250c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cde641306ef4cf4cbcef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cde641306ef4cf4cbcef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a134e822063762ff8d8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a134e822063762ff8d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-618e4c3fac7490dd9eaf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-618e4c3fac7490dd9eaf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92c39278db04ceabd94d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92c39278db04ceabd94d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7be9380bfbb354d63185"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7be9380bfbb354d63185`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f3ebff047c93009b51f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4f3ebff047c93009b51f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b382380c752358ff813"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9b382380c752358ff813`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3faaf95004d2307f4776"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3faaf95004d2307f4776`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3f565fa0c323a9c73756"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f565fa0c323a9c73756`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25388092812d8c1a8e89"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-25388092812d8c1a8e89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1decc2efc65ae2e6313d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1decc2efc65ae2e6313d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a37bfa8303d75a1177a3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a37bfa8303d75a1177a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-67684e05cd45530b26b1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-67684e05cd45530b26b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4eb42987367eb29f07a9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4eb42987367eb29f07a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a0e8ffaec7f7482d6f2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0a0e8ffaec7f7482d6f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-382b20e9d45f486d7c17"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-382b20e9d45f486d7c17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3a69404a81af36c4a52"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3a69404a81af36c4a52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45784e883af926f5d0c3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-45784e883af926f5d0c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-127b300b6285ee747b69"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-127b300b6285ee747b69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c1b737d57dda12df0e7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8c1b737d57dda12df0e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bdeb37e9b92ebb5d5542"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bdeb37e9b92ebb5d5542`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1e56109d6f9ca102335"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b1e56109d6f9ca102335`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ca3fa3aa4967296f460"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ca3fa3aa4967296f460`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd8260dcdbc67b07277f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bd8260dcdbc67b07277f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e8896a6ffb7b10b3f51f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e8896a6ffb7b10b3f51f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84074e61e40cafbe8afc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-84074e61e40cafbe8afc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81ed0f6bb0ce72412263"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-81ed0f6bb0ce72412263`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09167edf4f727a35db63"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-09167edf4f727a35db63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-11c70cb135234a5b8bb2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-11c70cb135234a5b8bb2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7823dd70315708d1be1e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7823dd70315708d1be1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6db05e64ba9c9f3bd0cf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6db05e64ba9c9f3bd0cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c755623b2bded543be2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4c755623b2bded543be2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-174cba9629867cca76b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-174cba9629867cca76b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2a762b83aa807b3cdd0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e2a762b83aa807b3cdd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6951352be6c4fca8c494"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6951352be6c4fca8c494`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ed61d50f51a7f55996d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9ed61d50f51a7f55996d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c804c939002990aa7cd6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c804c939002990aa7cd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cea590b919fa5bea6d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6cea590b919fa5bea6d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62ebde113a296aa74afb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-62ebde113a296aa74afb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbf60d46d9f91afc0a8f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fbf60d46d9f91afc0a8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3c06866f4e3f65048c58"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3c06866f4e3f65048c58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4de743be0f0ca2298bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b4de743be0f0ca2298bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64208706c5d2ef2316ed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-64208706c5d2ef2316ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2dea2f0c0f4a1ff338b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e2dea2f0c0f4a1ff338b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-51f84a1b91908fde640e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-51f84a1b91908fde640e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c11d5c876607cd1f5b8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9c11d5c876607cd1f5b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7492e55a91f704725b10"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7492e55a91f704725b10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9502fb7bf57f66d18012"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9502fb7bf57f66d18012`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c20060def61713fbec39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c20060def61713fbec39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cccbbce4c44032b7780d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cccbbce4c44032b7780d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a0f7f3100a7096dd95b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9a0f7f3100a7096dd95b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45261ebd7a2c6eefc7d5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-45261ebd7a2c6eefc7d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e189badda694bd40ff4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e189badda694bd40ff4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a9a4d549eab55159d88"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a9a4d549eab55159d88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef8f98e3a5ddb1655f4c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ef8f98e3a5ddb1655f4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b14189aa6230c22d4da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b14189aa6230c22d4da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-81311c336d12deeb804b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-81311c336d12deeb804b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4589653ea7bc321f8d72"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4589653ea7bc321f8d72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bf633312314b20979fc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8bf633312314b20979fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a53c4bffd1a16608f352"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a53c4bffd1a16608f352`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3eb94af836a06fd6b022"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3eb94af836a06fd6b022`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cb0eda56c6e0296c116"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7cb0eda56c6e0296c116`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50457f90a7d16074b406"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-50457f90a7d16074b406`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01eb10428c2ed0562490"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-01eb10428c2ed0562490`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca6ce9c486650bf52d83"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca6ce9c486650bf52d83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b6260de12a4f5537009"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b6260de12a4f5537009`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81baa1b06e73f7c11dcd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-81baa1b06e73f7c11dcd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83a4b69d01613f65dd05"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-83a4b69d01613f65dd05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a11fcd557e69eaed342"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a11fcd557e69eaed342`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4cb727a6a69efa495af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c4cb727a6a69efa495af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e1fac2271a89d163f89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8e1fac2271a89d163f89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc8024cab0d555ea8ca3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc8024cab0d555ea8ca3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-363f343fd2edcb858639"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-363f343fd2edcb858639`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b325d516345471fb759"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6b325d516345471fb759`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c53346bcb18736533b2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c53346bcb18736533b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a43fed1a2f4d668cc3e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a43fed1a2f4d668cc3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-865ff3455fdaa075edec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-865ff3455fdaa075edec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1097d5070ea5e6394433"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1097d5070ea5e6394433`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffc9b5a826e4e2506b88"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ffc9b5a826e4e2506b88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3418004072a44fc63b99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3418004072a44fc63b99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8c2bbfcf74646fe6aa4c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8c2bbfcf74646fe6aa4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ac82a73c6bd27a98ea4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0ac82a73c6bd27a98ea4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83cecd600006e104656e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-83cecd600006e104656e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bcfe433ae0b90eff43da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bcfe433ae0b90eff43da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0d0b11c78615b557503a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0d0b11c78615b557503a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef0912de29dd66971ee8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef0912de29dd66971ee8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c40647f6ae4dbc1e6f2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3c40647f6ae4dbc1e6f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68e79b6b8359262a44da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68e79b6b8359262a44da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-be74bfe7e1948f84d03e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-be74bfe7e1948f84d03e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1688114b18798fe20706"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1688114b18798fe20706`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a17bfdc3da4e1ef4b186"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a17bfdc3da4e1ef4b186`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad0e22d43b521de75b6e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ad0e22d43b521de75b6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-805f050897b3f81a97ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-805f050897b3f81a97ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e661f9d46fb186f795e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e661f9d46fb186f795e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b239cc2bd337af0c67a2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b239cc2bd337af0c67a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-401b86b7fea74c59c54b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-401b86b7fea74c59c54b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a22d6358affc10a3bcf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a22d6358affc10a3bcf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3888f95fe68e2c64258b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3888f95fe68e2c64258b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af55c1300fc24d592952"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-af55c1300fc24d592952`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3dfd6bf89af064fd46dd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3dfd6bf89af064fd46dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-82b135631f0516874208"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-82b135631f0516874208`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68389310d79206d0ffe3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-68389310d79206d0ffe3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8bc1542a4a335b0ee66"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d8bc1542a4a335b0ee66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b7503f88c34ef1c2c64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b7503f88c34ef1c2c64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e377e6f23c7f31e6def5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e377e6f23c7f31e6def5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ad574ca651e947be4fb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5ad574ca651e947be4fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a3b6636faaf8e6880f6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2a3b6636faaf8e6880f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a270dde447a358aca18"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1a270dde447a358aca18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d5bdd5534945adbba6a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d5bdd5534945adbba6a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fec94a2dd851311e3c39"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fec94a2dd851311e3c39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-137a38134ed72bee3d49"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-137a38134ed72bee3d49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ca9af662e0df9d9a0ce"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6ca9af662e0df9d9a0ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e7702a56919b66352c6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e7702a56919b66352c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1db4480985e25a0029e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1db4480985e25a0029e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85ee6eef778014e080b6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-85ee6eef778014e080b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a93f741b466b6b36b67"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5a93f741b466b6b36b67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3578e40aa18f0eb6d612"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3578e40aa18f0eb6d612`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b91319da9c7c4c3bd227"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b91319da9c7c4c3bd227`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7d8766a50ef41a36db5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b7d8766a50ef41a36db5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dcaae5dc0974c3e192f1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dcaae5dc0974c3e192f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1124cd39a3238d07e9cd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1124cd39a3238d07e9cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9fd0be04b470ed2eb2b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b9fd0be04b470ed2eb2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ffd7efad769c060853e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7ffd7efad769c060853e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3797ac08747faf0204c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c3797ac08747faf0204c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-897d03274e0f7cd46e2b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-897d03274e0f7cd46e2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4385f3859da5d359e1d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4385f3859da5d359e1d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-031e80ef563fb581a0ec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-031e80ef563fb581a0ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f310cbb796cdf7c7b0c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7f310cbb796cdf7c7b0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e8ddd3b3fdce62a5c71b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e8ddd3b3fdce62a5c71b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ab2412698ff35f2ac1e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1ab2412698ff35f2ac1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4270353ef44f4e2c1e68"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4270353ef44f4e2c1e68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-075cb1a273365e9f791d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-075cb1a273365e9f791d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6bb8d4923d445ece7ba7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6bb8d4923d445ece7ba7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54509c1852d611591707"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-54509c1852d611591707`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a56b1cc18cb1efee5d58"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a56b1cc18cb1efee5d58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87eff3ec5a53836c1021"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-87eff3ec5a53836c1021`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-53ed37e650e49f997f4b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-53ed37e650e49f997f4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1daf15053c8690396d2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d1daf15053c8690396d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-371791769ae4ae9be910"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-371791769ae4ae9be910`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bc87b7a99ed153a0096"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6bc87b7a99ed153a0096`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-80866287187b39dd54cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-80866287187b39dd54cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f132dde61324f6c22ee7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f132dde61324f6c22ee7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5b8cf9530de87e56d76"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5b8cf9530de87e56d76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6acdcc16ed38e9531108"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6acdcc16ed38e9531108`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b578b8f42cd79916f349"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b578b8f42cd79916f349`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-259bda604918408959dd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-259bda604918408959dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72f4474c083f93199d65"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-72f4474c083f93199d65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4811c6b7c7e1f9167a5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d4811c6b7c7e1f9167a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5417a9f185a2f444be4f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5417a9f185a2f444be4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2f529f11ee2928f6a21"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e2f529f11ee2928f6a21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a4cf0ae7e7ac5e7d669"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6a4cf0ae7e7ac5e7d669`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-792570d486841efb6b90"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-792570d486841efb6b90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e089a86806d2939a455"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e089a86806d2939a455`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebdb74d309759bb80d66"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ebdb74d309759bb80d66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75a9f4f0700b5016482a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-75a9f4f0700b5016482a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-678e07e2ad6591016f90"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-678e07e2ad6591016f90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e803868e484442f53319"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e803868e484442f53319`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27fc4032d12171b5209f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-27fc4032d12171b5209f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6450a3bcc92596d09c3b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6450a3bcc92596d09c3b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ef07ac4033890913e0e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0ef07ac4033890913e0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca6f83c2bcff85f14faa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca6f83c2bcff85f14faa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-283008b6595888e3ec2a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-283008b6595888e3ec2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7eb3a52ac048bc106cbb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7eb3a52ac048bc106cbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7bdbe62323287f01f753"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7bdbe62323287f01f753`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4a7d6670cc6cf0a133b9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4a7d6670cc6cf0a133b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1e7b369860123d55724"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b1e7b369860123d55724`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ca06a9370c19dc35e0a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8ca06a9370c19dc35e0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5fe3d9f65b39a55f730"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a5fe3d9f65b39a55f730`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-efc5b0b3ab0788a57f73"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-efc5b0b3ab0788a57f73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6b551e1836485c24743"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b6b551e1836485c24743`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c6a99d1e2d281555543"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c6a99d1e2d281555543`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03148b2f7599f5422ed7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03148b2f7599f5422ed7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc1344d73719c61f82d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc1344d73719c61f82d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d8399a1055a7c3ffb99"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0d8399a1055a7c3ffb99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4930114240f2c85333a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4930114240f2c85333a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14ea08e859fc540a2c1a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-14ea08e859fc540a2c1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e8e9683b6c8e7318d1a6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e8e9683b6c8e7318d1a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b55b1cd216371fe0e249"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b55b1cd216371fe0e249`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f71069d704e22ae62485"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f71069d704e22ae62485`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2f736226f24849f26ca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a2f736226f24849f26ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-80323d5d84d0434c3797"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-80323d5d84d0434c3797`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f37bcde571f09d5cfb11"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f37bcde571f09d5cfb11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c1b034f06129e5ec71d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5c1b034f06129e5ec71d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d0fc834f23121e71cba"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d0fc834f23121e71cba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-893e9918599ba0aa44cb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-893e9918599ba0aa44cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cc72793d12ed7fb7539"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4cc72793d12ed7fb7539`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50e1ca6dcd2cb25ec806"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-50e1ca6dcd2cb25ec806`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-350efd663290733cc0f1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-350efd663290733cc0f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-56d970b43df615067ab0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-56d970b43df615067ab0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2011625addf30a448d40"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2011625addf30a448d40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b5ac96975d41c0d96a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5b5ac96975d41c0d96a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0321a9963a585ea253de"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0321a9963a585ea253de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c59fe08bcb6bde42a608"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c59fe08bcb6bde42a608`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a7a1a8bd235d28b3a9e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a7a1a8bd235d28b3a9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c16aa17e7441c4d7f97"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c16aa17e7441c4d7f97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89738acb42836cb62013"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-89738acb42836cb62013`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ff4ed4674cc821842152"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ff4ed4674cc821842152`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec80d50f57700d6706cc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ec80d50f57700d6706cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68c80ed30c07cd0f9a3b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-68c80ed30c07cd0f9a3b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e60582322bfc56a9729"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e60582322bfc56a9729`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6bae99747cf3f8252460"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6bae99747cf3f8252460`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-434e74fb04879438bade"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-434e74fb04879438bade`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bcdc923626dc23e0a35e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bcdc923626dc23e0a35e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5fd4df2a08fb9f0c6d0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e5fd4df2a08fb9f0c6d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2117b22c4a7deacf0c0e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2117b22c4a7deacf0c0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f032584382f66fd15cbf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f032584382f66fd15cbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7ce550fd5593fe4aa8d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c7ce550fd5593fe4aa8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad8e57c12ee71eb78171"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ad8e57c12ee71eb78171`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-16df1e6958ce94b5e2cd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-16df1e6958ce94b5e2cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de06cf83012a4286795b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-de06cf83012a4286795b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed32bf7b539062286d6c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed32bf7b539062286d6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40c81b71d74fd75f6780"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40c81b71d74fd75f6780`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-faf7f955ffeb1eab09c6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-faf7f955ffeb1eab09c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-adb4f788bc88c8b63398"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-adb4f788bc88c8b63398`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38403f0628f0b3c83813"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-38403f0628f0b3c83813`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8046ca9caf8527648dd1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8046ca9caf8527648dd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9da3e6d75b88d2473569"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9da3e6d75b88d2473569`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc338949f8e3f9e16410"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cc338949f8e3f9e16410`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9534e73248a11d0294bf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9534e73248a11d0294bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-893f6d4121d3a616339a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-893f6d4121d3a616339a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f2933f43de637649804a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2933f43de637649804a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9955bf0edda05f32d14"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c9955bf0edda05f32d14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3baa6bb6072f3b15b33"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f3baa6bb6072f3b15b33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dcf03233f2cd75f017fe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dcf03233f2cd75f017fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-76301c55dc2023ff12bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-76301c55dc2023ff12bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a8450d754bcd579d4d7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8a8450d754bcd579d4d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fa77f9ea99e7c36b45b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3fa77f9ea99e7c36b45b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc11391630a1af531055"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cc11391630a1af531055`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f54212176b97c9877f7d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f54212176b97c9877f7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1dce867321431dec5070"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1dce867321431dec5070`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74e95e3d08f0387e60e2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-74e95e3d08f0387e60e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cac69397b45db95927b8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cac69397b45db95927b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-967fe322a8d2a3189d52"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-967fe322a8d2a3189d52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d0f178341d2441a9e98"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1d0f178341d2441a9e98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13d15402a1d4349bf5ad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-13d15402a1d4349bf5ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a79d496734cdf1936270"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a79d496734cdf1936270`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6732191f03b01fb2c5ce"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6732191f03b01fb2c5ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfaf38fbe6bad9e784f0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bfaf38fbe6bad9e784f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bec97c308009b79634e4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bec97c308009b79634e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a968d59f34f204e2edfe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a968d59f34f204e2edfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-003ebc0cec57350d15ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-003ebc0cec57350d15ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ed0955018e8411362f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ed0955018e8411362f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04b577aec9a9d279eed8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-04b577aec9a9d279eed8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dcad556f48b72ffa1f47"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dcad556f48b72ffa1f47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7a01c8fb6133ce7588ad"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7a01c8fb6133ce7588ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b6ebf9710ce1289ead3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b6ebf9710ce1289ead3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3547b6a40ebc4fa30d1a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3547b6a40ebc4fa30d1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71124b679c4e9ba90ef4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-71124b679c4e9ba90ef4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-08ccdb85b899149874fa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-08ccdb85b899149874fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5cb331b456d22b4354b6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5cb331b456d22b4354b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30b43bcd252a0a38b770"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-30b43bcd252a0a38b770`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b1acd362d6d60b54dd6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b1acd362d6d60b54dd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1f5002d87ecea923caf5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f5002d87ecea923caf5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b43aa8b5c314392cdb0d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b43aa8b5c314392cdb0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe3dfdca5bb9d6b75356"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fe3dfdca5bb9d6b75356`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04cac88f979b2f712185"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-04cac88f979b2f712185`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-62be2aee189f5e6f3dcb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-62be2aee189f5e6f3dcb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fa448c0deca383c3ed2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5fa448c0deca383c3ed2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-442e634da13ff6ca6bb8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-442e634da13ff6ca6bb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6698c479e80e5b07681"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d6698c479e80e5b07681`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-35158724bb8559828c0d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35158724bb8559828c0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-133b8d1022414b7f104e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-133b8d1022414b7f104e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1336d61bf48e0688011d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1336d61bf48e0688011d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cafa18304c98118b5aca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cafa18304c98118b5aca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8cf909bbfb3b5ac37a82"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8cf909bbfb3b5ac37a82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6dbab1d1b173a19c1429"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6dbab1d1b173a19c1429`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f012a7cd31fb323d15b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7f012a7cd31fb323d15b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8eb42cb4333a3a391d6c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8eb42cb4333a3a391d6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-23eac39c379ba2f0db42"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-23eac39c379ba2f0db42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8650ce814f56e9409581"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8650ce814f56e9409581`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7af41db06d7c2738ac93"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7af41db06d7c2738ac93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f4394e83667f4e2a516"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5f4394e83667f4e2a516`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b67e9ae37b50ece62a7c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b67e9ae37b50ece62a7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e605b9021d05e0d2bc95"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e605b9021d05e0d2bc95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b52a62ce5eb6b1ba0f9b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b52a62ce5eb6b1ba0f9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d24bd7f52e817bdf2da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0d24bd7f52e817bdf2da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ba7641f58c7991f4e1a1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ba7641f58c7991f4e1a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9035408bdc406ad2c7d6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9035408bdc406ad2c7d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63c79338b9cf67ebcd12"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-63c79338b9cf67ebcd12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-067a4c654256ec82446b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-067a4c654256ec82446b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-51ec101f9e160399541b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-51ec101f9e160399541b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ffd6eef09337acf7d7e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ffd6eef09337acf7d7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ab6b70361340fc36bfd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ab6b70361340fc36bfd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7c76a4c160dc175b4f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d7c76a4c160dc175b4f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ffa21fbd17186e8631a7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ffa21fbd17186e8631a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3bc0991cd228b2010a1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e3bc0991cd228b2010a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31ff5412d13cce0765d7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-31ff5412d13cce0765d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-181cd8b627ab463b092c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-181cd8b627ab463b092c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f831b11480553900fab3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f831b11480553900fab3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01839b9165405280209f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-01839b9165405280209f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3db6ba30e5096f803835"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3db6ba30e5096f803835`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03b852c954d8ab74e34a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03b852c954d8ab74e34a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dcc343b0d4231dd3eb05"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dcc343b0d4231dd3eb05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f79e687c2bd3aeb91651"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f79e687c2bd3aeb91651`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5490e5f64decd3160193"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5490e5f64decd3160193`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47bffd6029df6b9b00a2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-47bffd6029df6b9b00a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-entry-slip:canonical-southeast | <a href="#case-preview_review-b2cf926b956f0dbb0a35">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-entry-slip:canonical-top | <a href="#case-preview_review-05be39ed572b081462e2">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-entry-slip:connection-overview | <a href="#case-preview_review-f2c34e251143114b35bf">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-entry-slip:canonical-southeast</summary>

<a id="case-preview_review-b2cf926b956f0dbb0a35"></a>

**General: unverified** — `preview_review-b2cf926b956f0dbb0a35`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-entry-slip:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-entry-slip:canonical-top</summary>

<a id="case-preview_review-05be39ed572b081462e2"></a>

**General: unverified** — `preview_review-05be39ed572b081462e2`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-entry-slip:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-entry-slip:connection-overview</summary>

<a id="case-preview_review-f2c34e251143114b35bf"></a>

**General: unverified** — `preview_review-f2c34e251143114b35bf`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-entry-slip:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the slip function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
