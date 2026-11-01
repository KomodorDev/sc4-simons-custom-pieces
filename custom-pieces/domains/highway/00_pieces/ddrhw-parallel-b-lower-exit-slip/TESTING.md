---
title: "Testing: DD RHW-4 \u2014 L1 Exit Slip Lanes \u2014 Parallel \u2014 Alignment B"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1 Exit Slip Lanes — Parallel — Alignment B

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Test **DD RHW-4 — L1 Exit Slip Lanes — Parallel — Alignment B**, permanent ID `ddrhw-parallel-b-lower-exit-slip`, as **P04** of the [Alignment B assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md). This type owns 2 cells inside its 2 × 2 bounding footprint. Both native decks at 7.5 m and 15 m; the named access is at 7.5 m. Its saved traffic ownership and new identifiers are specific to B; A's reports and human observations are not inherited.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-10-out` | road / 1 / primary | out | [-8.0, -15.029437, 6.390578]; [-0.7071067811865476, -0.7071067811865476]; -0.179116252 | `path-interface-bead969a8cb1cad1321c` |
| `channel-11-out` | road / 1 / primary | out | [-3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-01-in` | road / 1 / primary | in | [-3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-02-in` | road / 1 / primary | in | [-0.265154, -8.0, 7.5]; [-0.9227775912579548, -0.38533299504735774]; 0.0 | `path-interface-ab935b18644984f76935` |
| `channel-12-out` | road / 1 / primary | out | [3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-03-in` | road / 1 / primary | in | [3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-04-in` | road / 1 / primary | in | [8.0, -19.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-13-out` | road / 1 / primary | out | [8.0, -19.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-05-in` | road / 1 / primary | in | [8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-14-out` | road / 1 / primary | out | [8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-15-out` | road / 1 / primary | out | [8.0, -7.155817, 7.5]; [-0.9822199574877394, -0.1877337346157676]; 0.0 | `path-interface-afca8d54413ff2cb80d4` |
| `channel-16-out` | road / 1 / primary | out | [12.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-06-in` | road / 1 / primary | in | [12.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-17-out` | road / 1 / primary | out | [19.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-07-in` | road / 1 / primary | in | [19.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-08-in` | road / 1 / primary | in | [24.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-18-out` | road / 1 / primary | out | [24.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-09-in` | road / 1 / primary | in | [24.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-19-out` | road / 1 / primary | out | [24.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-14-out` | primary |
| road | `channel-02-in` → `channel-10-out` | primary |
| road | `channel-03-in` → `channel-13-out` | primary |
| road | `channel-04-in` → `channel-12-out` | primary |
| road | `channel-05-in` → `channel-11-out` | primary |
| road | `channel-06-in` → `channel-19-out` | primary |
| road | `channel-07-in` → `channel-18-out` | primary |
| road | `channel-08-in` → `channel-17-out` | primary |
| road | `channel-09-in` → `channel-15-out` | primary |
| road | `channel-09-in` → `channel-16-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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
| road / `channel-02-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-10-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including the intended Wine or CrossOver environment. Keep the audited native inputs and supported NAM DLL described in the [build guide](../../../../docs/BUILD_AND_INSTALL.md). The nested assembly menu additionally requires the Submenus DLL, SC4ResourceLoadingHooks DLL version 2.0.1 or later, and `submenu-essentials.dat`.

Use flat ground in a disposable city, and follow this piece's [placement instructions](README.md#2-piece-and-placement). This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here. Preserve the original city before destructive tests. Close the game fully before a future installation, restart it, and place fresh B controls because B uses new resource and construction identifiers.

## 3. Software checks

From the repository root, run these checks against the first native candidate, and match its exact manifest to the delivery evidence:

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/parallel-diamond-alignment-b-native-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-b-lower-exit-slip
python3 -B tools/run_tests.py
```

The first native build **parallel-diamond-alignment-b-native-01** passed this piece’s actual saved model and PATH checks: **51,117 indexed triangles** and **10 directed route fragments**. Its five saved zoom models agree, the canonical preview matches its saved cells, and disabled-shadow checks retain zero shadow resources and zero T21 carrier references. The [whole-assembly report](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/evidence/saved-assembly.jsonc) binds this DAT’s hash to its native manifest and checks its placed joins, native boundaries, car support, texture seams, and proper PATH rotations. Generated connections below retain their narrower intrinsic scope. Software checks never record a human game pass.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-lower-exit-slip/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-b-lower-exit-slip/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-ff9ce034c4b285775371">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-ff9ce034c4b285775371"></a>

**General: unverified** — `software_resources-ff9ce034c4b285775371`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-ff9ce034c4b285775371">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-ff9ce034c4b285775371"></a>

**General: unverified** — `software_connectivity-ff9ce034c4b285775371`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-c149460b9bb96b43189c">[ ] unverified</a> | <a href="#case-in_game_render-575b89c58145ff0619e9">[ ] unverified</a> | <a href="#case-in_game_render-d534aa439e29067b027c">[ ] unverified</a> | <a href="#case-in_game_render-2d1089d696d584daaa46">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-c149460b9bb96b43189c"></a>

**0° CCW: unverified** — `in_game_render-c149460b9bb96b43189c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-575b89c58145ff0619e9"></a>

**90° CCW: unverified** — `in_game_render-575b89c58145ff0619e9`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-d534aa439e29067b027c"></a>

**180° CCW: unverified** — `in_game_render-d534aa439e29067b027c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2d1089d696d584daaa46"></a>

**270° CCW: unverified** — `in_game_render-2d1089d696d584daaa46`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-c149460b9bb96b43189c">[ ] unverified</a> | <a href="#case-in_game_placement-575b89c58145ff0619e9">[ ] unverified</a> | <a href="#case-in_game_placement-d534aa439e29067b027c">[ ] unverified</a> | <a href="#case-in_game_placement-2d1089d696d584daaa46">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-c149460b9bb96b43189c"></a>

**0° CCW: unverified** — `in_game_placement-c149460b9bb96b43189c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-575b89c58145ff0619e9"></a>

**90° CCW: unverified** — `in_game_placement-575b89c58145ff0619e9`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-d534aa439e29067b027c"></a>

**180° CCW: unverified** — `in_game_placement-d534aa439e29067b027c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2d1089d696d584daaa46"></a>

**270° CCW: unverified** — `in_game_placement-2d1089d696d584daaa46`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-c149460b9bb96b43189c">[ ] unverified</a> | <a href="#case-in_game_demolition-575b89c58145ff0619e9">[ ] unverified</a> | <a href="#case-in_game_demolition-d534aa439e29067b027c">[ ] unverified</a> | <a href="#case-in_game_demolition-2d1089d696d584daaa46">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-c149460b9bb96b43189c"></a>

**0° CCW: unverified** — `in_game_demolition-c149460b9bb96b43189c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-575b89c58145ff0619e9"></a>

**90° CCW: unverified** — `in_game_demolition-575b89c58145ff0619e9`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-d534aa439e29067b027c"></a>

**180° CCW: unverified** — `in_game_demolition-d534aa439e29067b027c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2d1089d696d584daaa46"></a>

**270° CCW: unverified** — `in_game_demolition-2d1089d696d584daaa46`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-c149460b9bb96b43189c">[ ] unverified</a> | <a href="#case-in_game_save_reload-575b89c58145ff0619e9">[ ] unverified</a> | <a href="#case-in_game_save_reload-d534aa439e29067b027c">[ ] unverified</a> | <a href="#case-in_game_save_reload-2d1089d696d584daaa46">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-c149460b9bb96b43189c"></a>

**0° CCW: unverified** — `in_game_save_reload-c149460b9bb96b43189c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-575b89c58145ff0619e9"></a>

**90° CCW: unverified** — `in_game_save_reload-575b89c58145ff0619e9`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-d534aa439e29067b027c"></a>

**180° CCW: unverified** — `in_game_save_reload-d534aa439e29067b027c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2d1089d696d584daaa46"></a>

**270° CCW: unverified** — `in_game_save_reload-2d1089d696d584daaa46`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-66ccbc65ba8db91dce10">[ ] unverified</a> | <a href="#case-in_game_route_query-68a264c92084c65ba880">[ ] unverified</a> | <a href="#case-in_game_route_query-102126764e860c7e4b9b">[ ] unverified</a> | <a href="#case-in_game_route_query-c4bab1b74e96a0826b7b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out | — | <a href="#case-in_game_route_query-0472fa25ca66e7fb4e31">[ ] unverified</a> | <a href="#case-in_game_route_query-1cc4483583cdc5d9b0ba">[ ] unverified</a> | <a href="#case-in_game_route_query-9a940a9cad3e3c9e0aa8">[ ] unverified</a> | <a href="#case-in_game_route_query-8493f4b3ab551b6605dc">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-dacbb371cb614834008b">[ ] unverified</a> | <a href="#case-in_game_route_query-d35553422f04e2ca278e">[ ] unverified</a> | <a href="#case-in_game_route_query-fc1092832f6749e93963">[ ] unverified</a> | <a href="#case-in_game_route_query-bd374ea69f4adf789f95">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-64932ca7bed9b988ba9c">[ ] unverified</a> | <a href="#case-in_game_route_query-19d8953cabc7ad8c897f">[ ] unverified</a> | <a href="#case-in_game_route_query-9547afd10df013f731fc">[ ] unverified</a> | <a href="#case-in_game_route_query-86532bd73b0e249148d5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-18b3f543fb1f0f29fa82">[ ] unverified</a> | <a href="#case-in_game_route_query-477660bde217096253f6">[ ] unverified</a> | <a href="#case-in_game_route_query-478bbc915de0774406e5">[ ] unverified</a> | <a href="#case-in_game_route_query-dddf5065971b417ab732">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-abbefb985bb65a708b66">[ ] unverified</a> | <a href="#case-in_game_route_query-fde492c7b32cbc7433d1">[ ] unverified</a> | <a href="#case-in_game_route_query-8ca106a53bcf6e8f821f">[ ] unverified</a> | <a href="#case-in_game_route_query-e2a0347461229ef20c7c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-3de67bef7e0007fe5746">[ ] unverified</a> | <a href="#case-in_game_route_query-2f645c0b30a615ab0028">[ ] unverified</a> | <a href="#case-in_game_route_query-55395436ed53c1476349">[ ] unverified</a> | <a href="#case-in_game_route_query-e816dec4b67ef00a5b72">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-155cdf86bba942c1d913">[ ] unverified</a> | <a href="#case-in_game_route_query-00ba075ed19c0551691c">[ ] unverified</a> | <a href="#case-in_game_route_query-a22cee15bbd13bfdb0f0">[ ] unverified</a> | <a href="#case-in_game_route_query-0edcb6d71c71786e4dc0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out | — | <a href="#case-in_game_route_query-948d73cfe0603d541698">[ ] unverified</a> | <a href="#case-in_game_route_query-9f0a07a827798f4815e6">[ ] unverified</a> | <a href="#case-in_game_route_query-2056f0788b029937fcca">[ ] unverified</a> | <a href="#case-in_game_route_query-42f4c8fa68450e085591">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-50eec1bdd8f240a0d847">[ ] unverified</a> | <a href="#case-in_game_route_query-b13e350c642c2996693e">[ ] unverified</a> | <a href="#case-in_game_route_query-2b1c42d859c61d960123">[ ] unverified</a> | <a href="#case-in_game_route_query-d30e7b1b2e2715b0742e">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-66ccbc65ba8db91dce10"></a>

**0° CCW: unverified** — `in_game_route_query-66ccbc65ba8db91dce10`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-68a264c92084c65ba880"></a>

**90° CCW: unverified** — `in_game_route_query-68a264c92084c65ba880`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-102126764e860c7e4b9b"></a>

**180° CCW: unverified** — `in_game_route_query-102126764e860c7e4b9b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-c4bab1b74e96a0826b7b"></a>

**270° CCW: unverified** — `in_game_route_query-c4bab1b74e96a0826b7b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out</summary>

<a id="case-in_game_route_query-0472fa25ca66e7fb4e31"></a>

**0° CCW: unverified** — `in_game_route_query-0472fa25ca66e7fb4e31`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-1cc4483583cdc5d9b0ba"></a>

**90° CCW: unverified** — `in_game_route_query-1cc4483583cdc5d9b0ba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-9a940a9cad3e3c9e0aa8"></a>

**180° CCW: unverified** — `in_game_route_query-9a940a9cad3e3c9e0aa8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_route_query-8493f4b3ab551b6605dc"></a>

**270° CCW: unverified** — `in_game_route_query-8493f4b3ab551b6605dc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-dacbb371cb614834008b"></a>

**0° CCW: unverified** — `in_game_route_query-dacbb371cb614834008b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-d35553422f04e2ca278e"></a>

**90° CCW: unverified** — `in_game_route_query-d35553422f04e2ca278e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-fc1092832f6749e93963"></a>

**180° CCW: unverified** — `in_game_route_query-fc1092832f6749e93963`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-bd374ea69f4adf789f95"></a>

**270° CCW: unverified** — `in_game_route_query-bd374ea69f4adf789f95`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-64932ca7bed9b988ba9c"></a>

**0° CCW: unverified** — `in_game_route_query-64932ca7bed9b988ba9c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-19d8953cabc7ad8c897f"></a>

**90° CCW: unverified** — `in_game_route_query-19d8953cabc7ad8c897f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-9547afd10df013f731fc"></a>

**180° CCW: unverified** — `in_game_route_query-9547afd10df013f731fc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-86532bd73b0e249148d5"></a>

**270° CCW: unverified** — `in_game_route_query-86532bd73b0e249148d5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-18b3f543fb1f0f29fa82"></a>

**0° CCW: unverified** — `in_game_route_query-18b3f543fb1f0f29fa82`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-477660bde217096253f6"></a>

**90° CCW: unverified** — `in_game_route_query-477660bde217096253f6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-478bbc915de0774406e5"></a>

**180° CCW: unverified** — `in_game_route_query-478bbc915de0774406e5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-dddf5065971b417ab732"></a>

**270° CCW: unverified** — `in_game_route_query-dddf5065971b417ab732`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-abbefb985bb65a708b66"></a>

**0° CCW: unverified** — `in_game_route_query-abbefb985bb65a708b66`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-fde492c7b32cbc7433d1"></a>

**90° CCW: unverified** — `in_game_route_query-fde492c7b32cbc7433d1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-8ca106a53bcf6e8f821f"></a>

**180° CCW: unverified** — `in_game_route_query-8ca106a53bcf6e8f821f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-e2a0347461229ef20c7c"></a>

**270° CCW: unverified** — `in_game_route_query-e2a0347461229ef20c7c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-3de67bef7e0007fe5746"></a>

**0° CCW: unverified** — `in_game_route_query-3de67bef7e0007fe5746`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-2f645c0b30a615ab0028"></a>

**90° CCW: unverified** — `in_game_route_query-2f645c0b30a615ab0028`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-55395436ed53c1476349"></a>

**180° CCW: unverified** — `in_game_route_query-55395436ed53c1476349`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-e816dec4b67ef00a5b72"></a>

**270° CCW: unverified** — `in_game_route_query-e816dec4b67ef00a5b72`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-155cdf86bba942c1d913"></a>

**0° CCW: unverified** — `in_game_route_query-155cdf86bba942c1d913`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-00ba075ed19c0551691c"></a>

**90° CCW: unverified** — `in_game_route_query-00ba075ed19c0551691c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-a22cee15bbd13bfdb0f0"></a>

**180° CCW: unverified** — `in_game_route_query-a22cee15bbd13bfdb0f0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-0edcb6d71c71786e4dc0"></a>

**270° CCW: unverified** — `in_game_route_query-0edcb6d71c71786e4dc0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out</summary>

<a id="case-in_game_route_query-948d73cfe0603d541698"></a>

**0° CCW: unverified** — `in_game_route_query-948d73cfe0603d541698`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-9f0a07a827798f4815e6"></a>

**90° CCW: unverified** — `in_game_route_query-9f0a07a827798f4815e6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-2056f0788b029937fcca"></a>

**180° CCW: unverified** — `in_game_route_query-2056f0788b029937fcca`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-42f4c8fa68450e085591"></a>

**270° CCW: unverified** — `in_game_route_query-42f4c8fa68450e085591`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-50eec1bdd8f240a0d847"></a>

**0° CCW: unverified** — `in_game_route_query-50eec1bdd8f240a0d847`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-b13e350c642c2996693e"></a>

**90° CCW: unverified** — `in_game_route_query-b13e350c642c2996693e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-2b1c42d859c61d960123"></a>

**180° CCW: unverified** — `in_game_route_query-2b1c42d859c61d960123`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-d30e7b1b2e2715b0742e"></a>

**270° CCW: unverified** — `in_game_route_query-d30e7b1b2e2715b0742e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-66ccbc65ba8db91dce10">[ ] unverified</a> | <a href="#case-in_game_visible_travel-68a264c92084c65ba880">[ ] unverified</a> | <a href="#case-in_game_visible_travel-102126764e860c7e4b9b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c4bab1b74e96a0826b7b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out | — | <a href="#case-in_game_visible_travel-0472fa25ca66e7fb4e31">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1cc4483583cdc5d9b0ba">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9a940a9cad3e3c9e0aa8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8493f4b3ab551b6605dc">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-dacbb371cb614834008b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d35553422f04e2ca278e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fc1092832f6749e93963">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bd374ea69f4adf789f95">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-64932ca7bed9b988ba9c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-19d8953cabc7ad8c897f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9547afd10df013f731fc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-86532bd73b0e249148d5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-18b3f543fb1f0f29fa82">[ ] unverified</a> | <a href="#case-in_game_visible_travel-477660bde217096253f6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-478bbc915de0774406e5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dddf5065971b417ab732">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-abbefb985bb65a708b66">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fde492c7b32cbc7433d1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8ca106a53bcf6e8f821f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e2a0347461229ef20c7c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-3de67bef7e0007fe5746">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2f645c0b30a615ab0028">[ ] unverified</a> | <a href="#case-in_game_visible_travel-55395436ed53c1476349">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e816dec4b67ef00a5b72">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-155cdf86bba942c1d913">[ ] unverified</a> | <a href="#case-in_game_visible_travel-00ba075ed19c0551691c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a22cee15bbd13bfdb0f0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0edcb6d71c71786e4dc0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out | — | <a href="#case-in_game_visible_travel-948d73cfe0603d541698">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9f0a07a827798f4815e6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2056f0788b029937fcca">[ ] unverified</a> | <a href="#case-in_game_visible_travel-42f4c8fa68450e085591">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-50eec1bdd8f240a0d847">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b13e350c642c2996693e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2b1c42d859c61d960123">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d30e7b1b2e2715b0742e">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-66ccbc65ba8db91dce10"></a>

**0° CCW: unverified** — `in_game_visible_travel-66ccbc65ba8db91dce10`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-68a264c92084c65ba880"></a>

**90° CCW: unverified** — `in_game_visible_travel-68a264c92084c65ba880`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-102126764e860c7e4b9b"></a>

**180° CCW: unverified** — `in_game_visible_travel-102126764e860c7e4b9b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-c4bab1b74e96a0826b7b"></a>

**270° CCW: unverified** — `in_game_visible_travel-c4bab1b74e96a0826b7b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out</summary>

<a id="case-in_game_visible_travel-0472fa25ca66e7fb4e31"></a>

**0° CCW: unverified** — `in_game_visible_travel-0472fa25ca66e7fb4e31`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-1cc4483583cdc5d9b0ba"></a>

**90° CCW: unverified** — `in_game_visible_travel-1cc4483583cdc5d9b0ba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-9a940a9cad3e3c9e0aa8"></a>

**180° CCW: unverified** — `in_game_visible_travel-9a940a9cad3e3c9e0aa8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

<a id="case-in_game_visible_travel-8493f4b3ab551b6605dc"></a>

**270° CCW: unverified** — `in_game_visible_travel-8493f4b3ab551b6605dc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-10-out; entry: channel-02-in; exit: channel-10-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-dacbb371cb614834008b"></a>

**0° CCW: unverified** — `in_game_visible_travel-dacbb371cb614834008b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-d35553422f04e2ca278e"></a>

**90° CCW: unverified** — `in_game_visible_travel-d35553422f04e2ca278e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-fc1092832f6749e93963"></a>

**180° CCW: unverified** — `in_game_visible_travel-fc1092832f6749e93963`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-bd374ea69f4adf789f95"></a>

**270° CCW: unverified** — `in_game_visible_travel-bd374ea69f4adf789f95`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-64932ca7bed9b988ba9c"></a>

**0° CCW: unverified** — `in_game_visible_travel-64932ca7bed9b988ba9c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-19d8953cabc7ad8c897f"></a>

**90° CCW: unverified** — `in_game_visible_travel-19d8953cabc7ad8c897f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-9547afd10df013f731fc"></a>

**180° CCW: unverified** — `in_game_visible_travel-9547afd10df013f731fc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-86532bd73b0e249148d5"></a>

**270° CCW: unverified** — `in_game_visible_travel-86532bd73b0e249148d5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-18b3f543fb1f0f29fa82"></a>

**0° CCW: unverified** — `in_game_visible_travel-18b3f543fb1f0f29fa82`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-477660bde217096253f6"></a>

**90° CCW: unverified** — `in_game_visible_travel-477660bde217096253f6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-478bbc915de0774406e5"></a>

**180° CCW: unverified** — `in_game_visible_travel-478bbc915de0774406e5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-dddf5065971b417ab732"></a>

**270° CCW: unverified** — `in_game_visible_travel-dddf5065971b417ab732`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-abbefb985bb65a708b66"></a>

**0° CCW: unverified** — `in_game_visible_travel-abbefb985bb65a708b66`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-fde492c7b32cbc7433d1"></a>

**90° CCW: unverified** — `in_game_visible_travel-fde492c7b32cbc7433d1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-8ca106a53bcf6e8f821f"></a>

**180° CCW: unverified** — `in_game_visible_travel-8ca106a53bcf6e8f821f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-e2a0347461229ef20c7c"></a>

**270° CCW: unverified** — `in_game_visible_travel-e2a0347461229ef20c7c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-3de67bef7e0007fe5746"></a>

**0° CCW: unverified** — `in_game_visible_travel-3de67bef7e0007fe5746`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-2f645c0b30a615ab0028"></a>

**90° CCW: unverified** — `in_game_visible_travel-2f645c0b30a615ab0028`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-55395436ed53c1476349"></a>

**180° CCW: unverified** — `in_game_visible_travel-55395436ed53c1476349`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-e816dec4b67ef00a5b72"></a>

**270° CCW: unverified** — `in_game_visible_travel-e816dec4b67ef00a5b72`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-155cdf86bba942c1d913"></a>

**0° CCW: unverified** — `in_game_visible_travel-155cdf86bba942c1d913`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-00ba075ed19c0551691c"></a>

**90° CCW: unverified** — `in_game_visible_travel-00ba075ed19c0551691c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-a22cee15bbd13bfdb0f0"></a>

**180° CCW: unverified** — `in_game_visible_travel-a22cee15bbd13bfdb0f0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-0edcb6d71c71786e4dc0"></a>

**270° CCW: unverified** — `in_game_visible_travel-0edcb6d71c71786e4dc0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out</summary>

<a id="case-in_game_visible_travel-948d73cfe0603d541698"></a>

**0° CCW: unverified** — `in_game_visible_travel-948d73cfe0603d541698`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-9f0a07a827798f4815e6"></a>

**90° CCW: unverified** — `in_game_visible_travel-9f0a07a827798f4815e6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-2056f0788b029937fcca"></a>

**180° CCW: unverified** — `in_game_visible_travel-2056f0788b029937fcca`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-42f4c8fa68450e085591"></a>

**270° CCW: unverified** — `in_game_visible_travel-42f4c8fa68450e085591`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-15-out; entry: channel-09-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-50eec1bdd8f240a0d847"></a>

**0° CCW: unverified** — `in_game_visible_travel-50eec1bdd8f240a0d847`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-b13e350c642c2996693e"></a>

**90° CCW: unverified** — `in_game_visible_travel-b13e350c642c2996693e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-2b1c42d859c61d960123"></a>

**180° CCW: unverified** — `in_game_visible_travel-2b1c42d859c61d960123`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-d30e7b1b2e2715b0742e"></a>

**270° CCW: unverified** — `in_game_visible_travel-d30e7b1b2e2715b0742e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-16-out; entry: channel-09-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 320 cases; unverified: 320</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0e49f22d0b91540ac41d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e29c9156024402e89111">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed5c276bcb7b01adb2d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b01b4d78d365a5b53f59">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-068af5231506f8e364f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c0dcda2585bda5ac35a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66129fdb3d1670a220bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f10ef0115a174524ceaf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8549730f3101b9ce6f4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2e516b0db837c74c9aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc1d2ac493c6ff1a14bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-158fc1ac41cd85f71369">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c22cc2983e6710a0943c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-777b76f39ac968720bae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-288519a8a5dc802e413a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47cde5d443a834f655ad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-18996e341f673c014f7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04862e828c66920051fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb08f3f287513915b312">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db3f6bc294be3a8db66f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-82666ea2d60b7f7c8057">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7946065d596723cc202">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1eae91ced0573a366b63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f4a69ff0b79baeaad4d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a38724157adbe249c74a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a50a994a7cfb040bc0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-279a9947c6c42a640155">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7708ec01cdfd4ccbbfa3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a9ce9b143b62a6e92d1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ea30d17e4030ac14272">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-843348f52f8fe8ed7131">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0f503a378ad78224a84">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b1b7894eb168be5a4ed5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13e0b7e32044aebc0c25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4389cd8b02e1b2af42cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-411f260ae0c07c0b74aa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5244c57f2fcb31c7e50b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6751623da82eed57e8d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70daa5281cda164d791e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-102e7fc62aa919f89c1c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cf2921ed561997ea785d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2320263ade5d4ab63059">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f73b4c28d001f3eb46e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80a34aa983fa4cef2bc3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6dd0537e3bd48750c1db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0244587bc3f73080909">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c289bf59d073182fcaee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e791a89795fb93f887e9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dfec688f86dea81a14f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48810aae42d78ef72be0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-274fece92f95a4d809ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4d0d2832f55e99f57e4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-38f30774ed1d7160f953">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5962e8f1e4bcc39e0b7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc0d5cf7a5fe19776f43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-934cbd1d89d7567eed03">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-927b9052e8be683d4ce6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39c0345e32f6b20898c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b335df4fca81dea84e00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e609e3060952f3d14ec">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-75554fc2fdafeb4e4e68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cd915894da1bbfdd8ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee1938c5d8abe98210b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00d72ad045c844ff49a4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-010ebdc8a00478c8dd08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-748bfc0b7e91545a61e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94bc2b06d6605b5db254">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d5c14344386b5867782">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9a5c83b2aa5a1e745548">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ceabcfced4cf192f2e00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac640e2db289ec32f0a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10b723cc6720f609c73c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-736272655b1787a36cd5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0eb6baf232c53f04e110">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc32b977faa7b0c29887">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63158715baef6b66cb0e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e58bb0ba8a6ef94bd61f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-073a9024c4f45642ae85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b02b40bfd6d41a84a57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45f4d9b9e5e88c319f29">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4cbe5f5c168c0755d96a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-949e520a103930459193">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b3dfb3cce2587c7b643">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35557b77acc597a92fc9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-868a0457b82b4b27739c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-faceb0064cd2fbe5b3a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f004d3ecdfaa640d3f9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3170206eecb31ddbf58e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-764a328d9dbc84ceff4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c18532330be3291a0cc8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bb3f8928bec217a22a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57651c9f4a84755adfad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9c8cfd53cd16788278bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8a8fdf201fdb6d9e934">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50c03bfb8c9249b3b1c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a041fdd032a1170be41e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c922a6c6526e1eaccc26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd7dea7919aeab889e93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f32c38be8306729c4e73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ff07eff7e7748ac8332">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10d53b55ad8e3b8cb89e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48b85a78757a37bc40dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fcc2f8425f6d93af6e3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4fe15fc705490b72423">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f46afaf6e2f6feb989dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0fbb59d381b54edb7681">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-014cd9aa40c38e4207fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89310c81c6f21f4bfe0c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-69b3d7b34e36035beed2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e400251b546c04eb863">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4295c828038ad4351d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da5d84d93818e2004d5d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f974d11b5d952ab062be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5b77cb0bd0fcd7e3a76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69019809a52030c27789">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d0d03b4a53af8009db1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7ca368a896dfae69bc32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13faf2e1c04039f6dc29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89ac07b74d6be40129f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe6c193bea67c89e6082">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-18c8c479a23e45996098">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3bc0e299948d48308df3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b59a9e2686d19aaf7e0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1618ce25cbb5f0fe2a25">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9815b3fc3f5615a82f48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d569bb2d03979c3bff18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cf8d550f8f63e05ea57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4014608aa60e47ade287">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0901d80b2d512f978b46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39b867eddc6344b90529">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5aa3d26bbed2c0a59cc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbf678308ae5c8c2fab3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b31abf7e8602b4be2dd9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e294e3f6c22019ca1a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bf3b6b3c0732328524d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5183f2b287ae0b6a8ab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e2ce7f28291d6b9f10a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a310200e01575a6c4101">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4c67af6478137d37227">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61793b9b972db4e814a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41e3882fc6a54435751e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a3443877257f3ed1799">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c935f53a21abd5ed202f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b184df4a5c6a09ea0b8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a8bd5c9703c7f4591474">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac120feefc860565bf8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a720291d82ba1ec80d45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99ca526c9792515c6c4a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f9a60e8ba0d6b6f78d55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f32ca58df195e22f8c64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b44603bb51d52ba7da9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5acfbdca96180b0258af">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee3a9e8d90f996c1a401">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aba48a057d7dc7b3b813">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9fe7b622b524728fb94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b14db5e40c7f93c33d2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bea7b6d265f1f4bcefe8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f62c3f0a1e2be043997">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0cdcde87b2698bae0780">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06dacd286c8f832d9f8e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b03ea8bddf396277b9bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-779f93fccef31bbf60ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acf6ead635f74d0b97ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82df859dcc7494f93709">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eaad0b755d5ebe55e7e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35876c1a03359d49fa6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e7a1b0fef6a6766e228">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1021dd46d72f19f2c65c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c242ea95f71ec200661">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df5ab4e4984c90117933">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fa3ae328b794cb8dab1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4f53cbcd1c9b5422558">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e4077c17871354fd44f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e7665beadac9dabdaf9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab0e04bd4ccae5e8dad5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb5876f770466a35c5b3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-22d782a9655782b81930">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e4a3f02f8407decd2d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edd85fb1f6c794939b69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af6b39c5a2a661290793">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-df8de60e3c755b5c7199">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25b10cb1af890050fe78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cece497a3c856b1c367">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e89d8cc6ba8140d6e6f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-263eead1136617c251bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f04463e30b61166dbc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98adcd37cd5125330532">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2a3b1f01af7eac5af99">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f2d0ec9cc483df514253">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-136ce125c390dfe825a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bafc8b6504808296a04b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0118d480363158e3cb23">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e531a78885c193ea22f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41db64a6b2515d28d6f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d206930de345c9890ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61126f067e96839b651b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-23f9ab816b63b9c6265b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1908e98100157eb2c350">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1370bb7a85a08073e082">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0136502c37ed84b5167e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8bb9a11dda378d304a07">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee75e62b0a7db7a210ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26e79b03b59791be8e3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a68adeff08154409a65b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-026ee28ad7583f57cf79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-462235d9f6d5070c4353">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-964dd1174ae9018a33a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c6be1516ae1e67e978f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f308190f60231c5fff62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4fee9de90bb319776b13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-663b6a63b3964dc358aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1431d37002369c5730f5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b4593808f48f014c8c5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dd135bd6ac649a0fabf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-861623fe72440538d394">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f46aa330aaf973449303">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4c9c381b845dbd9205be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa25d8a5ae647a02a45f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6b540ae1e73043310a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80b81d34766912101939">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e73c639e69681b3bdca8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4c43d1c607f14c9f2cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5708832dac9085ef95ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42853fd3da031912baa1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fa8697456fbfd8005704">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bdb5d39dcb243a7f4f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42d8e869143fceae9cc7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9133a97c293fab5e308">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b535deaaa573959a515d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d8a337b1e2eb0f6305a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0898aad174af2557abe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38fd17f840776823aa86">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-09bc1307b2df324175fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47ff4e767eba6e1e50cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32c5cb6f51535e753950">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25af26a8111237f178ed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f9889ba227b2d146ddce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc6347a23e155ce69918">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a70605e3017db626874">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-367c85bf8cd67f4ff6e3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f389b512fb50c3cbdd0b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa277d5ff9f522bf56df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60426a90b1618bce19b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98cd8318477c78f207ce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-57af3b76e79f59992ae7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-014b6ae69d1223156de1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e390797f48c95701cc77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eac147f10c2fa4b7074a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-82824adabfde13ae6c69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a37638ef7e952a6ce5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7eed06c0e03384317f2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f0247022a556f26a670">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ba47d197fed962eaf1db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8803174657a5a1eca252">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be467193e5973a749cc8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e4652dcb57d2da3dfea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-55ba30e3b6cdf4da48b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62459b136429f43fe45f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80c8acb397aad2e162d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0edd3442784aded95230">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b50fd085be4e4fee5acc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28cf66905be260fc8724">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d776e1c30bf4619b1e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4308cc199fc80fa51c04">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee98152b251116a9ac96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3bfca8b4413f63a99f14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ec4c7635bf3fa649ce8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a068eb23035131afa9b5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7271206cc83d890f70c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-462b2dc882e0d763682d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94aa6853174171a46c51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-133d7d2bae756817bbf1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-505865c694cf366e216e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3752a5ae2e94d97c77f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9c94136eefe9d05e03e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18c1e80c9824ff2610e6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d23f889d979e10007238">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c1d14c729a3f123c9b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51490c6b8ea6c40b8615">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84fc485e043b80d1b0a0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-63e5311c72dcea159ce8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1286b951fc7cdf6a5ea4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c51bb3ff23940e942c4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ea58c2dfa3db6035acd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-69154ea9d1b4b3965138">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29cdded20d39d2c7d077">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4e5114f4cbe30a896ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84e428bc64d45c9eb7a6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a5712996d4a1acafca8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a9ec7010c425bf2c436">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab54f34587fb943f6bc1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9af73f3c91666b4d402">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d11b62aad828bc567d1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-131600ba88856fe61e1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae5f3eb0fbfc1667bcae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7d090db835c0904fc98">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1112fab7ed23e05f7791">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f036c88cf6b3c42fcd8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fdd24d423993e07a8fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7460721e4b97be3b8e11">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4e7f953816177372527d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2e09cd33c135a053e54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-925ab7df4f441253da1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55bae50af7afa8ce433c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d1f13c777e8bcaf3436e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bb2738a508ad4ff491c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d0c5dd73000947e6000">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af4d7588e948cfc781c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e1f94786d8182ad44f25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae0961ab57da2dd0c363">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2d216a4e7be1fcdd425">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10e58b8cc92f5db1bfdd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e17270fb0675e1a87682">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a314e1feeffd414328eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bdb4c2180c973601ba6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a78575d21dbb41b519fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9cd046b1cc5ab7ea2d60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e0822d644c2303728c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31daf9ce89b3b9a71f90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25d90b76c4a9a86602bb">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0e49f22d0b91540ac41d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e49f22d0b91540ac41d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e29c9156024402e89111"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e29c9156024402e89111`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed5c276bcb7b01adb2d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed5c276bcb7b01adb2d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b01b4d78d365a5b53f59"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b01b4d78d365a5b53f59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-068af5231506f8e364f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-068af5231506f8e364f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c0dcda2585bda5ac35a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6c0dcda2585bda5ac35a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66129fdb3d1670a220bd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-66129fdb3d1670a220bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f10ef0115a174524ceaf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f10ef0115a174524ceaf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8549730f3101b9ce6f4b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8549730f3101b9ce6f4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2e516b0db837c74c9aa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c2e516b0db837c74c9aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc1d2ac493c6ff1a14bc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dc1d2ac493c6ff1a14bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-158fc1ac41cd85f71369"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-158fc1ac41cd85f71369`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c22cc2983e6710a0943c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c22cc2983e6710a0943c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-777b76f39ac968720bae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-777b76f39ac968720bae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-288519a8a5dc802e413a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-288519a8a5dc802e413a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47cde5d443a834f655ad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-47cde5d443a834f655ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-18996e341f673c014f7b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-18996e341f673c014f7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04862e828c66920051fb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-04862e828c66920051fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb08f3f287513915b312"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eb08f3f287513915b312`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db3f6bc294be3a8db66f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-db3f6bc294be3a8db66f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-82666ea2d60b7f7c8057"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-82666ea2d60b7f7c8057`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7946065d596723cc202"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e7946065d596723cc202`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1eae91ced0573a366b63"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1eae91ced0573a366b63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f4a69ff0b79baeaad4d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3f4a69ff0b79baeaad4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a38724157adbe249c74a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a38724157adbe249c74a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a50a994a7cfb040bc0f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a50a994a7cfb040bc0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-279a9947c6c42a640155"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-279a9947c6c42a640155`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7708ec01cdfd4ccbbfa3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7708ec01cdfd4ccbbfa3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a9ce9b143b62a6e92d1c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a9ce9b143b62a6e92d1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ea30d17e4030ac14272"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ea30d17e4030ac14272`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-843348f52f8fe8ed7131"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-843348f52f8fe8ed7131`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0f503a378ad78224a84"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e0f503a378ad78224a84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b1b7894eb168be5a4ed5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b1b7894eb168be5a4ed5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13e0b7e32044aebc0c25"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-13e0b7e32044aebc0c25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4389cd8b02e1b2af42cd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4389cd8b02e1b2af42cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-411f260ae0c07c0b74aa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-411f260ae0c07c0b74aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5244c57f2fcb31c7e50b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5244c57f2fcb31c7e50b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6751623da82eed57e8d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6751623da82eed57e8d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70daa5281cda164d791e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-70daa5281cda164d791e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-102e7fc62aa919f89c1c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-102e7fc62aa919f89c1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cf2921ed561997ea785d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cf2921ed561997ea785d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2320263ade5d4ab63059"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2320263ade5d4ab63059`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f73b4c28d001f3eb46e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2f73b4c28d001f3eb46e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80a34aa983fa4cef2bc3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-80a34aa983fa4cef2bc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6dd0537e3bd48750c1db"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6dd0537e3bd48750c1db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0244587bc3f73080909"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a0244587bc3f73080909`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c289bf59d073182fcaee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c289bf59d073182fcaee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e791a89795fb93f887e9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e791a89795fb93f887e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dfec688f86dea81a14f7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dfec688f86dea81a14f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48810aae42d78ef72be0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48810aae42d78ef72be0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-274fece92f95a4d809ac"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-274fece92f95a4d809ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4d0d2832f55e99f57e4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4d0d2832f55e99f57e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-38f30774ed1d7160f953"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-38f30774ed1d7160f953`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5962e8f1e4bcc39e0b7b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5962e8f1e4bcc39e0b7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc0d5cf7a5fe19776f43"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc0d5cf7a5fe19776f43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-934cbd1d89d7567eed03"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-934cbd1d89d7567eed03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-927b9052e8be683d4ce6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-927b9052e8be683d4ce6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39c0345e32f6b20898c6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-39c0345e32f6b20898c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b335df4fca81dea84e00"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b335df4fca81dea84e00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e609e3060952f3d14ec"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e609e3060952f3d14ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-75554fc2fdafeb4e4e68"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-75554fc2fdafeb4e4e68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cd915894da1bbfdd8ab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7cd915894da1bbfdd8ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee1938c5d8abe98210b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee1938c5d8abe98210b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00d72ad045c844ff49a4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-00d72ad045c844ff49a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-010ebdc8a00478c8dd08"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-010ebdc8a00478c8dd08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-748bfc0b7e91545a61e6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-748bfc0b7e91545a61e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94bc2b06d6605b5db254"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-94bc2b06d6605b5db254`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d5c14344386b5867782"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1d5c14344386b5867782`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9a5c83b2aa5a1e745548"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9a5c83b2aa5a1e745548`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ceabcfced4cf192f2e00"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ceabcfced4cf192f2e00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac640e2db289ec32f0a6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ac640e2db289ec32f0a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10b723cc6720f609c73c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10b723cc6720f609c73c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-736272655b1787a36cd5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-736272655b1787a36cd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0eb6baf232c53f04e110"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0eb6baf232c53f04e110`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc32b977faa7b0c29887"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cc32b977faa7b0c29887`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63158715baef6b66cb0e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-63158715baef6b66cb0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e58bb0ba8a6ef94bd61f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e58bb0ba8a6ef94bd61f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-073a9024c4f45642ae85"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-073a9024c4f45642ae85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b02b40bfd6d41a84a57"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5b02b40bfd6d41a84a57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45f4d9b9e5e88c319f29"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-45f4d9b9e5e88c319f29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4cbe5f5c168c0755d96a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4cbe5f5c168c0755d96a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-949e520a103930459193"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-949e520a103930459193`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b3dfb3cce2587c7b643"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4b3dfb3cce2587c7b643`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35557b77acc597a92fc9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-35557b77acc597a92fc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-868a0457b82b4b27739c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-868a0457b82b4b27739c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-faceb0064cd2fbe5b3a6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-faceb0064cd2fbe5b3a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f004d3ecdfaa640d3f9c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f004d3ecdfaa640d3f9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3170206eecb31ddbf58e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3170206eecb31ddbf58e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-764a328d9dbc84ceff4e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-764a328d9dbc84ceff4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c18532330be3291a0cc8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c18532330be3291a0cc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bb3f8928bec217a22a1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6bb3f8928bec217a22a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57651c9f4a84755adfad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-57651c9f4a84755adfad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9c8cfd53cd16788278bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9c8cfd53cd16788278bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8a8fdf201fdb6d9e934"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d8a8fdf201fdb6d9e934`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50c03bfb8c9249b3b1c2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-50c03bfb8c9249b3b1c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a041fdd032a1170be41e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a041fdd032a1170be41e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c922a6c6526e1eaccc26"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c922a6c6526e1eaccc26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd7dea7919aeab889e93"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd7dea7919aeab889e93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f32c38be8306729c4e73"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f32c38be8306729c4e73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ff07eff7e7748ac8332"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ff07eff7e7748ac8332`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-10d53b55ad8e3b8cb89e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-10d53b55ad8e3b8cb89e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48b85a78757a37bc40dd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48b85a78757a37bc40dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fcc2f8425f6d93af6e3d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fcc2f8425f6d93af6e3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4fe15fc705490b72423"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b4fe15fc705490b72423`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f46afaf6e2f6feb989dd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f46afaf6e2f6feb989dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0fbb59d381b54edb7681"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0fbb59d381b54edb7681`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-014cd9aa40c38e4207fe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-014cd9aa40c38e4207fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89310c81c6f21f4bfe0c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-89310c81c6f21f4bfe0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-69b3d7b34e36035beed2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-69b3d7b34e36035beed2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e400251b546c04eb863"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1e400251b546c04eb863`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4295c828038ad4351d0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e4295c828038ad4351d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da5d84d93818e2004d5d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-da5d84d93818e2004d5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f974d11b5d952ab062be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f974d11b5d952ab062be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5b77cb0bd0fcd7e3a76"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c5b77cb0bd0fcd7e3a76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69019809a52030c27789"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-69019809a52030c27789`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d0d03b4a53af8009db1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d0d03b4a53af8009db1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7ca368a896dfae69bc32"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7ca368a896dfae69bc32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13faf2e1c04039f6dc29"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-13faf2e1c04039f6dc29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89ac07b74d6be40129f3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-89ac07b74d6be40129f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe6c193bea67c89e6082"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe6c193bea67c89e6082`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-18c8c479a23e45996098"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-18c8c479a23e45996098`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3bc0e299948d48308df3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3bc0e299948d48308df3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b59a9e2686d19aaf7e0d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b59a9e2686d19aaf7e0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1618ce25cbb5f0fe2a25"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1618ce25cbb5f0fe2a25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9815b3fc3f5615a82f48"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9815b3fc3f5615a82f48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d569bb2d03979c3bff18"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d569bb2d03979c3bff18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1cf8d550f8f63e05ea57"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1cf8d550f8f63e05ea57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4014608aa60e47ade287"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4014608aa60e47ade287`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0901d80b2d512f978b46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0901d80b2d512f978b46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39b867eddc6344b90529"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-39b867eddc6344b90529`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5aa3d26bbed2c0a59cc0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5aa3d26bbed2c0a59cc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbf678308ae5c8c2fab3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cbf678308ae5c8c2fab3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b31abf7e8602b4be2dd9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b31abf7e8602b4be2dd9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e294e3f6c22019ca1a9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0e294e3f6c22019ca1a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bf3b6b3c0732328524d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0bf3b6b3c0732328524d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5183f2b287ae0b6a8ab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b5183f2b287ae0b6a8ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e2ce7f28291d6b9f10a6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2ce7f28291d6b9f10a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a310200e01575a6c4101"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a310200e01575a6c4101`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4c67af6478137d37227"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a4c67af6478137d37227`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61793b9b972db4e814a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-61793b9b972db4e814a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41e3882fc6a54435751e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41e3882fc6a54435751e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a3443877257f3ed1799"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8a3443877257f3ed1799`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c935f53a21abd5ed202f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c935f53a21abd5ed202f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b184df4a5c6a09ea0b8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2b184df4a5c6a09ea0b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a8bd5c9703c7f4591474"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a8bd5c9703c7f4591474`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac120feefc860565bf8a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ac120feefc860565bf8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a720291d82ba1ec80d45"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a720291d82ba1ec80d45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99ca526c9792515c6c4a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-99ca526c9792515c6c4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f9a60e8ba0d6b6f78d55"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f9a60e8ba0d6b6f78d55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f32ca58df195e22f8c64"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f32ca58df195e22f8c64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b44603bb51d52ba7da9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3b44603bb51d52ba7da9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5acfbdca96180b0258af"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5acfbdca96180b0258af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee3a9e8d90f996c1a401"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee3a9e8d90f996c1a401`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aba48a057d7dc7b3b813"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aba48a057d7dc7b3b813`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9fe7b622b524728fb94"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f9fe7b622b524728fb94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b14db5e40c7f93c33d2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b14db5e40c7f93c33d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bea7b6d265f1f4bcefe8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bea7b6d265f1f4bcefe8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f62c3f0a1e2be043997"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4f62c3f0a1e2be043997`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0cdcde87b2698bae0780"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0cdcde87b2698bae0780`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06dacd286c8f832d9f8e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-06dacd286c8f832d9f8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b03ea8bddf396277b9bd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b03ea8bddf396277b9bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-779f93fccef31bbf60ce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-779f93fccef31bbf60ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acf6ead635f74d0b97ee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-acf6ead635f74d0b97ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82df859dcc7494f93709"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-82df859dcc7494f93709`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eaad0b755d5ebe55e7e4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eaad0b755d5ebe55e7e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35876c1a03359d49fa6f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-35876c1a03359d49fa6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e7a1b0fef6a6766e228"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3e7a1b0fef6a6766e228`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1021dd46d72f19f2c65c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1021dd46d72f19f2c65c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c242ea95f71ec200661"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c242ea95f71ec200661`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df5ab4e4984c90117933"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-df5ab4e4984c90117933`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fa3ae328b794cb8dab1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5fa3ae328b794cb8dab1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4f53cbcd1c9b5422558"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4f53cbcd1c9b5422558`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e4077c17871354fd44f1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e4077c17871354fd44f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e7665beadac9dabdaf9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e7665beadac9dabdaf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab0e04bd4ccae5e8dad5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ab0e04bd4ccae5e8dad5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb5876f770466a35c5b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cb5876f770466a35c5b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-22d782a9655782b81930"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-22d782a9655782b81930`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e4a3f02f8407decd2d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5e4a3f02f8407decd2d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edd85fb1f6c794939b69"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-edd85fb1f6c794939b69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af6b39c5a2a661290793"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af6b39c5a2a661290793`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-df8de60e3c755b5c7199"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-df8de60e3c755b5c7199`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25b10cb1af890050fe78"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-25b10cb1af890050fe78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cece497a3c856b1c367"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8cece497a3c856b1c367`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e89d8cc6ba8140d6e6f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3e89d8cc6ba8140d6e6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-263eead1136617c251bf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-263eead1136617c251bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f04463e30b61166dbc0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9f04463e30b61166dbc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98adcd37cd5125330532"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-98adcd37cd5125330532`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d2a3b1f01af7eac5af99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d2a3b1f01af7eac5af99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f2d0ec9cc483df514253"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2d0ec9cc483df514253`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-136ce125c390dfe825a9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-136ce125c390dfe825a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bafc8b6504808296a04b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bafc8b6504808296a04b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0118d480363158e3cb23"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0118d480363158e3cb23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e531a78885c193ea22f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e531a78885c193ea22f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41db64a6b2515d28d6f3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-41db64a6b2515d28d6f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d206930de345c9890ce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6d206930de345c9890ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61126f067e96839b651b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-61126f067e96839b651b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-23f9ab816b63b9c6265b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-23f9ab816b63b9c6265b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1908e98100157eb2c350"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1908e98100157eb2c350`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1370bb7a85a08073e082"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1370bb7a85a08073e082`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0136502c37ed84b5167e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0136502c37ed84b5167e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8bb9a11dda378d304a07"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8bb9a11dda378d304a07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee75e62b0a7db7a210ce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ee75e62b0a7db7a210ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26e79b03b59791be8e3a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-26e79b03b59791be8e3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a68adeff08154409a65b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a68adeff08154409a65b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-026ee28ad7583f57cf79"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-026ee28ad7583f57cf79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-462235d9f6d5070c4353"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-462235d9f6d5070c4353`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-964dd1174ae9018a33a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-964dd1174ae9018a33a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c6be1516ae1e67e978f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6c6be1516ae1e67e978f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f308190f60231c5fff62"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f308190f60231c5fff62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4fee9de90bb319776b13"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4fee9de90bb319776b13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-663b6a63b3964dc358aa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-663b6a63b3964dc358aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1431d37002369c5730f5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1431d37002369c5730f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b4593808f48f014c8c5e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b4593808f48f014c8c5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dd135bd6ac649a0fabf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0dd135bd6ac649a0fabf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-861623fe72440538d394"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-861623fe72440538d394`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f46aa330aaf973449303"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f46aa330aaf973449303`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4c9c381b845dbd9205be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4c9c381b845dbd9205be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa25d8a5ae647a02a45f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa25d8a5ae647a02a45f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6b540ae1e73043310a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d6b540ae1e73043310a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80b81d34766912101939"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-80b81d34766912101939`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e73c639e69681b3bdca8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e73c639e69681b3bdca8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4c43d1c607f14c9f2cc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e4c43d1c607f14c9f2cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5708832dac9085ef95ca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5708832dac9085ef95ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42853fd3da031912baa1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-42853fd3da031912baa1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fa8697456fbfd8005704"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fa8697456fbfd8005704`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bdb5d39dcb243a7f4f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5bdb5d39dcb243a7f4f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42d8e869143fceae9cc7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-42d8e869143fceae9cc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9133a97c293fab5e308"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c9133a97c293fab5e308`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b535deaaa573959a515d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b535deaaa573959a515d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d8a337b1e2eb0f6305a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0d8a337b1e2eb0f6305a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0898aad174af2557abe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a0898aad174af2557abe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38fd17f840776823aa86"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-38fd17f840776823aa86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-09bc1307b2df324175fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-09bc1307b2df324175fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47ff4e767eba6e1e50cf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-47ff4e767eba6e1e50cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32c5cb6f51535e753950"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-32c5cb6f51535e753950`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25af26a8111237f178ed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-25af26a8111237f178ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f9889ba227b2d146ddce"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f9889ba227b2d146ddce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc6347a23e155ce69918"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dc6347a23e155ce69918`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a70605e3017db626874"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4a70605e3017db626874`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-367c85bf8cd67f4ff6e3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-367c85bf8cd67f4ff6e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f389b512fb50c3cbdd0b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f389b512fb50c3cbdd0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa277d5ff9f522bf56df"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aa277d5ff9f522bf56df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60426a90b1618bce19b9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-60426a90b1618bce19b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98cd8318477c78f207ce"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-98cd8318477c78f207ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-57af3b76e79f59992ae7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-57af3b76e79f59992ae7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-014b6ae69d1223156de1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-014b6ae69d1223156de1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e390797f48c95701cc77"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e390797f48c95701cc77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eac147f10c2fa4b7074a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eac147f10c2fa4b7074a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-82824adabfde13ae6c69"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-82824adabfde13ae6c69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a37638ef7e952a6ce5d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7a37638ef7e952a6ce5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7eed06c0e03384317f2c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7eed06c0e03384317f2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f0247022a556f26a670"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7f0247022a556f26a670`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ba47d197fed962eaf1db"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ba47d197fed962eaf1db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8803174657a5a1eca252"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8803174657a5a1eca252`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be467193e5973a749cc8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-be467193e5973a749cc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e4652dcb57d2da3dfea"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5e4652dcb57d2da3dfea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-55ba30e3b6cdf4da48b7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-55ba30e3b6cdf4da48b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62459b136429f43fe45f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-62459b136429f43fe45f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80c8acb397aad2e162d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-80c8acb397aad2e162d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0edd3442784aded95230"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0edd3442784aded95230`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b50fd085be4e4fee5acc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b50fd085be4e4fee5acc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28cf66905be260fc8724"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-28cf66905be260fc8724`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d776e1c30bf4619b1e4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9d776e1c30bf4619b1e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4308cc199fc80fa51c04"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4308cc199fc80fa51c04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee98152b251116a9ac96"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee98152b251116a9ac96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3bfca8b4413f63a99f14"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3bfca8b4413f63a99f14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ec4c7635bf3fa649ce8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4ec4c7635bf3fa649ce8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a068eb23035131afa9b5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a068eb23035131afa9b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7271206cc83d890f70c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7271206cc83d890f70c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-462b2dc882e0d763682d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-462b2dc882e0d763682d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94aa6853174171a46c51"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-94aa6853174171a46c51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-133d7d2bae756817bbf1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-133d7d2bae756817bbf1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-505865c694cf366e216e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-505865c694cf366e216e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3752a5ae2e94d97c77f7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3752a5ae2e94d97c77f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9c94136eefe9d05e03e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c9c94136eefe9d05e03e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18c1e80c9824ff2610e6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-18c1e80c9824ff2610e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d23f889d979e10007238"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d23f889d979e10007238`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c1d14c729a3f123c9b5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c1d14c729a3f123c9b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51490c6b8ea6c40b8615"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-51490c6b8ea6c40b8615`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84fc485e043b80d1b0a0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-84fc485e043b80d1b0a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-63e5311c72dcea159ce8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-63e5311c72dcea159ce8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1286b951fc7cdf6a5ea4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1286b951fc7cdf6a5ea4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c51bb3ff23940e942c4f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c51bb3ff23940e942c4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ea58c2dfa3db6035acd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6ea58c2dfa3db6035acd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-69154ea9d1b4b3965138"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-69154ea9d1b4b3965138`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29cdded20d39d2c7d077"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-29cdded20d39d2c7d077`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4e5114f4cbe30a896ce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c4e5114f4cbe30a896ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84e428bc64d45c9eb7a6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-84e428bc64d45c9eb7a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a5712996d4a1acafca8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a5712996d4a1acafca8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a9ec7010c425bf2c436"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a9ec7010c425bf2c436`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab54f34587fb943f6bc1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ab54f34587fb943f6bc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9af73f3c91666b4d402"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b9af73f3c91666b4d402`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-10-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d11b62aad828bc567d1c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d11b62aad828bc567d1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-131600ba88856fe61e1a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-131600ba88856fe61e1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae5f3eb0fbfc1667bcae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ae5f3eb0fbfc1667bcae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7d090db835c0904fc98"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c7d090db835c0904fc98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1112fab7ed23e05f7791"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1112fab7ed23e05f7791`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f036c88cf6b3c42fcd8e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f036c88cf6b3c42fcd8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fdd24d423993e07a8fd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9fdd24d423993e07a8fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7460721e4b97be3b8e11"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7460721e4b97be3b8e11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4e7f953816177372527d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4e7f953816177372527d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2e09cd33c135a053e54"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b2e09cd33c135a053e54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-925ab7df4f441253da1e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-925ab7df4f441253da1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55bae50af7afa8ce433c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-55bae50af7afa8ce433c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d1f13c777e8bcaf3436e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d1f13c777e8bcaf3436e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bb2738a508ad4ff491c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6bb2738a508ad4ff491c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d0c5dd73000947e6000"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d0c5dd73000947e6000`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af4d7588e948cfc781c2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af4d7588e948cfc781c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e1f94786d8182ad44f25"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e1f94786d8182ad44f25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae0961ab57da2dd0c363"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ae0961ab57da2dd0c363`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d2d216a4e7be1fcdd425"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d2d216a4e7be1fcdd425`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10e58b8cc92f5db1bfdd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10e58b8cc92f5db1bfdd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e17270fb0675e1a87682"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e17270fb0675e1a87682`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a314e1feeffd414328eb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a314e1feeffd414328eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bdb4c2180c973601ba6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5bdb4c2180c973601ba6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a78575d21dbb41b519fe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a78575d21dbb41b519fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9cd046b1cc5ab7ea2d60"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9cd046b1cc5ab7ea2d60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e0822d644c2303728c4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e0822d644c2303728c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31daf9ce89b3b9a71f90"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-31daf9ce89b3b9a71f90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25d90b76c4a9a86602bb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-25d90b76c4a9a86602bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-exit-slip:canonical-southeast | <a href="#case-preview_review-56bbd85fb3e2174f26b4">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-exit-slip:canonical-top | <a href="#case-preview_review-f603453698867a1aa7fa">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-b-lower-exit-slip:connection-overview | <a href="#case-preview_review-2d73964a15ca36b78efc">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-exit-slip:canonical-southeast</summary>

<a id="case-preview_review-56bbd85fb3e2174f26b4"></a>

**General: unverified** — `preview_review-56bbd85fb3e2174f26b4`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-exit-slip:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-exit-slip:canonical-top</summary>

<a id="case-preview_review-f603453698867a1aa7fa"></a>

**General: unverified** — `preview_review-f603453698867a1aa7fa`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-exit-slip:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-b-lower-exit-slip:connection-overview</summary>

<a id="case-preview_review-2d73964a15ca36b78efc"></a>

**General: unverified** — `preview_review-2d73964a15ca36b78efc`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-b-lower-exit-slip:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The complementary diagonal Avenue phase required a new whole-cell partition while retaining the accepted close parallel physical design. This separately allocated type serves the slip function of Alignment B and keeps the existing Alignment A type intact. Complete native and ramp traffic fragments determine its minimum ownership; visual similarity alone is insufficient for whole-type reuse. The shared submenu exposes one independent component cycle for each alignment.
