---
title: "Testing: DD RHW-4 \u2014 L1/L2 \u2194 RHW-4 L0 \u2014 Mirrored Orthogonal Transition \u2014 6 Tiles"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Mirrored Orthogonal Transition — 6 Tiles

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This scope covers the mirrored adapter’s twelve owned cells, three unowned native sockets, four complete directed car journeys, and eight external directed members. In source pose 0°, the north DD socket is in the west column: upper northbound at 15 m and lower southbound at 7.5 m. South ground traffic is west southbound from the lower deck and east northbound towards the upper deck. Require both lanes of each direction, all four proper placement rotations, separate camera rotations, no unwanted transfers, and no custom cast shadows. The [README](README.md) gives exact menu controls and all three construction orders. The original type’s observations cannot pass this counterpart.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `lower-lane-01-out` | road / 1 / primary | out | [-2.5, -88.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-a980347eab2bc32dd576` |
| `lower-lane-01-in` | road / 1 / primary | in | [-2.5, 8.0, 7.5]; [0.0, -1.0]; 0.0 | `path-interface-b2fe320b9e0bb31bdb27` |
| `upper-lane-02-out` | road / 1 / primary | out | [-2.5, 8.0, 15.0]; [0.0, 1.0]; 0.0 | `path-interface-02def3c4ce1dd299e969` |
| `lower-lane-02-out` | road / 1 / primary | out | [2.5, -88.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-3cd860990d731c95fb5e` |
| `lower-lane-02-in` | road / 1 / primary | in | [2.5, 8.0, 7.5]; [0.0, -1.0]; 0.0 | `path-interface-fddc704c2b84d595ec6f` |
| `upper-lane-01-out` | road / 1 / primary | out | [2.5, 8.0, 15.0]; [0.0, 1.0]; 0.0 | `path-interface-991f143956c37b818e99` |
| `upper-lane-02-in` | road / 1 / primary | in | [13.5, -88.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-d977a84d7a911bc0048d` |
| `upper-lane-01-in` | road / 1 / primary | in | [18.5, -88.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-57700a60d1579dc24dce` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `lower-lane-01-in` → `lower-lane-01-out` | primary |
| road | `lower-lane-02-in` → `lower-lane-02-out` | primary |
| road | `upper-lane-02-in` → `upper-lane-02-out` | primary |
| road | `upper-lane-01-in` → `upper-lane-01-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `lower-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-01-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `lower-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `upper-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 1.1.641 with the audited NAM 50 right-hand-traffic inputs, recording the actual Windows, Wine, or CrossOver environment. The DD, ground RHW-4, core, controller, and texture dependencies are declared in [piece.jsonc](piece.jsonc); their original shared fingerprints are retained in the [native input contract](../ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile/evidence/native-contract.jsonc). Follow the [shared build/install guide](../../../../docs/BUILD_AND_INSTALL.md). After installation with the game fully closed, use a disposable flat city and leave the README’s 2 × 8 connection arrangement clear, with at least three straight tiles beyond each socket. Prepare working native DD and opposing RHW-4 control lines, and confirm moving traffic on those controls first.

## 3. Software checks

The paired candidate is `dist/orthogonal-ddrhw-l0-paired-native-02`: four DAT files contain 205 resources, including 24 canonical PATHs and 122 model resources across the two types, their five zooms, and their previews. Its [saved verification](evidence/saved-native-verification.jsonc) records the exact manifest, checking sources, both type payloads, and independent resource results. The [accepted connector contract](checks/accepted-connector-contract.jsonc) binds this type’s twelve saved PATHs to its four lane journeys, eight ports, and twelve forbidden transfers. These records establish their stated software scope and retain game operation as unverified.

The independent verifier reconstructs the curves and cell cuts separately from the writer. It checks actual saved traffic heights with `UseElevation=1`, lane metadata, all four proper rotations, all five model zooms, the combined preview, complete pavement and barriers, closed support solids, continuous vehicle clearance, winding, UV orientation, and the generated native-source asphalt atlas. The mirrored northeast model-only cell `[1,0]` must retain an empty PATH. The retained original payload is compared with its first native build; only the new type receives new resource identities.

The native boundary audit compares actual adapter PATH endpoints with the pinned original NAM DD and RHW-4 PATHs in their actual socket poses. It requires all eight external members to agree in position, height, engine class, lane class, compatibility, tangent, and complementary entry/exit direction in every proper rotation. Original starter-marker selections, the eight reused native RUL1 solutions, and the native continuation rules are checked separately. The saved menu audit verifies one original button with a mirrored Tab alternative when both are selected. None of these checks records an in-game drag or a moving-car pass.

Run from the repository root; replace `BUILD_NAME` with a new candidate folder name. Building writes files but does not install them.

```sh
python3 -B custom-pieces/scp.py build --set ddrhw-orthogonal-ground-transition --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored --build dist/BUILD_NAME
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored
python3 -B tools/run_tests.py
```

## 4. Game checks

### 4.1 Menu, fresh placement, and all three connection orders

1. Open the original transition’s button under **Transportation → Highways**, press **Tab** until the query names the mirrored transition, and place it on clear ground. Use **Shift+Tab** to return to the original. Check that both shapes remain accessible and that only one top-level button appears when both are included.
2. From a fresh mirrored placement, use **RealHighway (RHW-2)** to draw outward from its DD socket and each ground socket, following README section 2.2.
3. At another site, draw inward from working prebuilt DD and RHW-4 controls to the matching adjacent native sockets, following README section 2.3. Test the DD end and both ground carriageways separately; stop outside the fixed core.
4. At a third site, place a fresh mirrored adapter directly between completed native approaches. Record each construction order independently.
5. Repeat at 90°, 180°, and 270° using **Home** and **End**. Inspect every socket’s direction and height. Also test original 0° plus mirrored 180° facing one continuous DD line: upper southbound and lower northbound must agree at both ends.

### 4.2 Route Query and moving traffic

1. Connect occupied development and useful destinations through the working controls, and run the simulation. Confirm actual cars on each native control before judging the adapter.
2. Use **Route Query** for the lower DD-to-west-ground journey and the east-ground-to-upper-DD journey in source pose 0°. Record each displayed route separately.
3. Follow actual cars from the last native tile through the entire adapter to the next native tile. Check both lanes in both directions, with correct heights throughout. Record any stopped, disappearing, wrong-way, or clipped vehicle at its exact cell and rotation.
4. Check that no car changes lanes, U-turns, or transfers between carriageways inside the fixed adapter. Repeat allowed journeys in all four placement rotations and through the original/mirrored paired-end layout.

### 4.3 Appearance, redraw, and object lifetime

1. Inspect every zoom and all four city-camera views for continuous surfaces, correctly phased native collars, yellow lines on each driver’s left, complete barriers and supports, and clear vehicle paths. Camera rotation and placement rotation are separate checks.
2. Compare Medium and High shadow settings. The piece intentionally supplies no cast shadows; record any residual triangle or detached deck shadow separately from neighbouring objects.
3. Redraw the native approaches, save the city, quit fully, and reload. Repeat the native joins and moving-car checks, and confirm that the fixed core remains intact.
4. Demolish the adapter, inspect all twelve former core cells and all three sockets for leftovers, rebuild the controls, and repeat a fresh placement.

Record only explicitly matching human observations through [the shared procedure](../../../../docs/TESTING.md). A successful build, source preview, or coloured route cannot pass a game case.

## 5. Results and known issues

The source and compiled candidate are experimental. Native resource and geometry checks have a bounded software scope; installation, menu behavior, inward dragging, outward drawing, placement between controls, actual moving cars, rendering, redraw, demolition, and save/reload remain unverified until matching human observations. The six-tile length retains compact experimental slopes rather than civil-engineering design standards. The declared vehicle envelope does not cover every replacement automaton. The generated checklist below retains the exact recorded states without borrowing the original adapter’s or a diagonal diamond’s results.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/16 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/16 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 101, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-c0b7af9fa7cef748191c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-c0b7af9fa7cef748191c"></a>

**General: unverified** — `software_resources-c0b7af9fa7cef748191c`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-c0b7af9fa7cef748191c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-c0b7af9fa7cef748191c"></a>

**General: unverified** — `software_connectivity-c0b7af9fa7cef748191c`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored:canonical-southeast | <a href="#case-preview_review-11bfe191debeaa17fe1f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored:canonical-top | <a href="#case-preview_review-333b506058f80667dc6a">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored:connection-overview | <a href="#case-preview_review-9c3424420f6a2f6a3025">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored:canonical-southeast</summary>

<a id="case-preview_review-11bfe191debeaa17fe1f"></a>

**General: unverified** — `preview_review-11bfe191debeaa17fe1f`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored:canonical-top</summary>

<a id="case-preview_review-333b506058f80667dc6a"></a>

**General: unverified** — `preview_review-333b506058f80667dc6a`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored:connection-overview</summary>

<a id="case-preview_review-9c3424420f6a2f6a3025"></a>

**General: unverified** — `preview_review-9c3424420f6a2f6a3025`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-02cd5171513d446ad225">[ ] unverified</a> | <a href="#case-in_game_render-2c3ff8cf427faaf2029b">[ ] unverified</a> | <a href="#case-in_game_render-c3387efb02df9637ed83">[ ] unverified</a> | <a href="#case-in_game_render-b39c0642c6d1d59481e1">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-02cd5171513d446ad225"></a>

**0° CCW: unverified** — `in_game_render-02cd5171513d446ad225`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2c3ff8cf427faaf2029b"></a>

**90° CCW: unverified** — `in_game_render-2c3ff8cf427faaf2029b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c3387efb02df9637ed83"></a>

**180° CCW: unverified** — `in_game_render-c3387efb02df9637ed83`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-b39c0642c6d1d59481e1"></a>

**270° CCW: unverified** — `in_game_render-b39c0642c6d1d59481e1`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-02cd5171513d446ad225">[ ] unverified</a> | <a href="#case-in_game_placement-2c3ff8cf427faaf2029b">[ ] unverified</a> | <a href="#case-in_game_placement-c3387efb02df9637ed83">[ ] unverified</a> | <a href="#case-in_game_placement-b39c0642c6d1d59481e1">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-02cd5171513d446ad225"></a>

**0° CCW: unverified** — `in_game_placement-02cd5171513d446ad225`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2c3ff8cf427faaf2029b"></a>

**90° CCW: unverified** — `in_game_placement-2c3ff8cf427faaf2029b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c3387efb02df9637ed83"></a>

**180° CCW: unverified** — `in_game_placement-c3387efb02df9637ed83`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-b39c0642c6d1d59481e1"></a>

**270° CCW: unverified** — `in_game_placement-b39c0642c6d1d59481e1`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-02cd5171513d446ad225">[ ] unverified</a> | <a href="#case-in_game_demolition-2c3ff8cf427faaf2029b">[ ] unverified</a> | <a href="#case-in_game_demolition-c3387efb02df9637ed83">[ ] unverified</a> | <a href="#case-in_game_demolition-b39c0642c6d1d59481e1">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-02cd5171513d446ad225"></a>

**0° CCW: unverified** — `in_game_demolition-02cd5171513d446ad225`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2c3ff8cf427faaf2029b"></a>

**90° CCW: unverified** — `in_game_demolition-2c3ff8cf427faaf2029b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c3387efb02df9637ed83"></a>

**180° CCW: unverified** — `in_game_demolition-c3387efb02df9637ed83`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-b39c0642c6d1d59481e1"></a>

**270° CCW: unverified** — `in_game_demolition-b39c0642c6d1d59481e1`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-02cd5171513d446ad225">[ ] unverified</a> | <a href="#case-in_game_save_reload-2c3ff8cf427faaf2029b">[ ] unverified</a> | <a href="#case-in_game_save_reload-c3387efb02df9637ed83">[ ] unverified</a> | <a href="#case-in_game_save_reload-b39c0642c6d1d59481e1">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-02cd5171513d446ad225"></a>

**0° CCW: unverified** — `in_game_save_reload-02cd5171513d446ad225`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2c3ff8cf427faaf2029b"></a>

**90° CCW: unverified** — `in_game_save_reload-2c3ff8cf427faaf2029b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c3387efb02df9637ed83"></a>

**180° CCW: unverified** — `in_game_save_reload-c3387efb02df9637ed83`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-b39c0642c6d1d59481e1"></a>

**270° CCW: unverified** — `in_game_save_reload-b39c0642c6d1d59481e1`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_route_query-47fbe843f0ca6e7e63ef">[ ] unverified</a> | <a href="#case-in_game_route_query-318529f8c5d44dffb29d">[ ] unverified</a> | <a href="#case-in_game_route_query-d8019e3ea11764e1e4a9">[ ] unverified</a> | <a href="#case-in_game_route_query-10f52dca50f3a73026ec">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_route_query-cc1794c749e1953e2727">[ ] unverified</a> | <a href="#case-in_game_route_query-7cb01fb0a28ed03a0853">[ ] unverified</a> | <a href="#case-in_game_route_query-8962b27b33f3128a461b">[ ] unverified</a> | <a href="#case-in_game_route_query-dac68d2d8bae27f5fb6e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_route_query-084ae714c2b3df99af0d">[ ] unverified</a> | <a href="#case-in_game_route_query-1b4bb8fa94770305e433">[ ] unverified</a> | <a href="#case-in_game_route_query-9bc63d9792f534d773ee">[ ] unverified</a> | <a href="#case-in_game_route_query-5242c16300ce99bb1fa1">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_route_query-1a7f130da4c638d1604e">[ ] unverified</a> | <a href="#case-in_game_route_query-d5d991ce30ff41e0882e">[ ] unverified</a> | <a href="#case-in_game_route_query-9bed52c751efe336276f">[ ] unverified</a> | <a href="#case-in_game_route_query-b533b038352632458bdc">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_route_query-47fbe843f0ca6e7e63ef"></a>

**0° CCW: unverified** — `in_game_route_query-47fbe843f0ca6e7e63ef`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-318529f8c5d44dffb29d"></a>

**90° CCW: unverified** — `in_game_route_query-318529f8c5d44dffb29d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-d8019e3ea11764e1e4a9"></a>

**180° CCW: unverified** — `in_game_route_query-d8019e3ea11764e1e4a9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-10f52dca50f3a73026ec"></a>

**270° CCW: unverified** — `in_game_route_query-10f52dca50f3a73026ec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_route_query-cc1794c749e1953e2727"></a>

**0° CCW: unverified** — `in_game_route_query-cc1794c749e1953e2727`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-7cb01fb0a28ed03a0853"></a>

**90° CCW: unverified** — `in_game_route_query-7cb01fb0a28ed03a0853`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-8962b27b33f3128a461b"></a>

**180° CCW: unverified** — `in_game_route_query-8962b27b33f3128a461b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-dac68d2d8bae27f5fb6e"></a>

**270° CCW: unverified** — `in_game_route_query-dac68d2d8bae27f5fb6e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_route_query-084ae714c2b3df99af0d"></a>

**0° CCW: unverified** — `in_game_route_query-084ae714c2b3df99af0d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-1b4bb8fa94770305e433"></a>

**90° CCW: unverified** — `in_game_route_query-1b4bb8fa94770305e433`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-9bc63d9792f534d773ee"></a>

**180° CCW: unverified** — `in_game_route_query-9bc63d9792f534d773ee`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-5242c16300ce99bb1fa1"></a>

**270° CCW: unverified** — `in_game_route_query-5242c16300ce99bb1fa1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_route_query-1a7f130da4c638d1604e"></a>

**0° CCW: unverified** — `in_game_route_query-1a7f130da4c638d1604e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-d5d991ce30ff41e0882e"></a>

**90° CCW: unverified** — `in_game_route_query-d5d991ce30ff41e0882e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-9bed52c751efe336276f"></a>

**180° CCW: unverified** — `in_game_route_query-9bed52c751efe336276f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-b533b038352632458bdc"></a>

**270° CCW: unverified** — `in_game_route_query-b533b038352632458bdc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_visible_travel-47fbe843f0ca6e7e63ef">[ ] unverified</a> | <a href="#case-in_game_visible_travel-318529f8c5d44dffb29d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d8019e3ea11764e1e4a9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-10f52dca50f3a73026ec">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_visible_travel-cc1794c749e1953e2727">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7cb01fb0a28ed03a0853">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8962b27b33f3128a461b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dac68d2d8bae27f5fb6e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_visible_travel-084ae714c2b3df99af0d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1b4bb8fa94770305e433">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9bc63d9792f534d773ee">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5242c16300ce99bb1fa1">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_visible_travel-1a7f130da4c638d1604e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d5d991ce30ff41e0882e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9bed52c751efe336276f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b533b038352632458bdc">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_visible_travel-47fbe843f0ca6e7e63ef"></a>

**0° CCW: unverified** — `in_game_visible_travel-47fbe843f0ca6e7e63ef`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-318529f8c5d44dffb29d"></a>

**90° CCW: unverified** — `in_game_visible_travel-318529f8c5d44dffb29d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-d8019e3ea11764e1e4a9"></a>

**180° CCW: unverified** — `in_game_visible_travel-d8019e3ea11764e1e4a9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-10f52dca50f3a73026ec"></a>

**270° CCW: unverified** — `in_game_visible_travel-10f52dca50f3a73026ec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_visible_travel-cc1794c749e1953e2727"></a>

**0° CCW: unverified** — `in_game_visible_travel-cc1794c749e1953e2727`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-7cb01fb0a28ed03a0853"></a>

**90° CCW: unverified** — `in_game_visible_travel-7cb01fb0a28ed03a0853`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-8962b27b33f3128a461b"></a>

**180° CCW: unverified** — `in_game_visible_travel-8962b27b33f3128a461b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-dac68d2d8bae27f5fb6e"></a>

**270° CCW: unverified** — `in_game_visible_travel-dac68d2d8bae27f5fb6e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_visible_travel-084ae714c2b3df99af0d"></a>

**0° CCW: unverified** — `in_game_visible_travel-084ae714c2b3df99af0d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-1b4bb8fa94770305e433"></a>

**90° CCW: unverified** — `in_game_visible_travel-1b4bb8fa94770305e433`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-9bc63d9792f534d773ee"></a>

**180° CCW: unverified** — `in_game_visible_travel-9bc63d9792f534d773ee`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-5242c16300ce99bb1fa1"></a>

**270° CCW: unverified** — `in_game_visible_travel-5242c16300ce99bb1fa1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_visible_travel-1a7f130da4c638d1604e"></a>

**0° CCW: unverified** — `in_game_visible_travel-1a7f130da4c638d1604e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-d5d991ce30ff41e0882e"></a>

**90° CCW: unverified** — `in_game_visible_travel-d5d991ce30ff41e0882e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-9bed52c751efe336276f"></a>

**180° CCW: unverified** — `in_game_visible_travel-9bed52c751efe336276f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-b533b038352632458bdc"></a>

**270° CCW: unverified** — `in_game_visible_travel-b533b038352632458bdc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2c84806a0ca17d9f6451">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2fbc68f19028655143a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d8a2073ba12b33211e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a41e9309a0acdbc67221">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ea49f3a8fbafcc74fbda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfbc209bef5b21636a41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abf6be5b379a92e784ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e0c29487b3b7782419f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-42239deba2cc99e0344f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d63d1b35fa12b293c627">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e5d7df05f0f57b93d30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b188b0c0b0ab86352eb7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-67d3df107ac4cc7320f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-553644fbc9a2a37a8a16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72006e2f2dfaa7e9eb4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe98533c2f04c51e4d5c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f9b4c787e08c13a272cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f691c472e9b061f0404">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ada66727bb0d03eed98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abbb004e24e9769b2e33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ece0405fca6b259d3b26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea255011ccebe807e6c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bf3a39fbdcb6c66c879">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a1d190f6496590148e5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce16aca07506500a8807">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a63e6e8d21103554bf93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59a58eecdf40c023e3dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c7e2617444754150af2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-36a0967e265de44e9ffb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1eac5371c6b366b6ac81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ea57a99b4aa6c52606d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f10db365a6e6a9734b98">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e5841ce4e5ea5afe2b2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-489a160a605ae77262ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e24f4e1014c61609a11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e080f08d548fc23d33f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8b28e223d252dbf2cbd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-08f8005a4a8da3caf97a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0b1252749d1d60b1dc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cef5233dcb88b194658a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1f792232f7cb31193122">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6477d90caf76d38dfdd7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fcfbf282215ae0bd0cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bb7adee093d36171908">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b7a215ecec175f249936">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4c390b17c12b93ce993">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75c7252d16210fbe8ae4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffe7bc2d1e38e2bd46c3">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2c84806a0ca17d9f6451"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2c84806a0ca17d9f6451`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2fbc68f19028655143a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e2fbc68f19028655143a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d8a2073ba12b33211e6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d8a2073ba12b33211e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a41e9309a0acdbc67221"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a41e9309a0acdbc67221`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ea49f3a8fbafcc74fbda"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ea49f3a8fbafcc74fbda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfbc209bef5b21636a41"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dfbc209bef5b21636a41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abf6be5b379a92e784ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-abf6be5b379a92e784ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e0c29487b3b7782419f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5e0c29487b3b7782419f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-42239deba2cc99e0344f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-42239deba2cc99e0344f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d63d1b35fa12b293c627"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d63d1b35fa12b293c627`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e5d7df05f0f57b93d30"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0e5d7df05f0f57b93d30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b188b0c0b0ab86352eb7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b188b0c0b0ab86352eb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-67d3df107ac4cc7320f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-67d3df107ac4cc7320f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-553644fbc9a2a37a8a16"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-553644fbc9a2a37a8a16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72006e2f2dfaa7e9eb4e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-72006e2f2dfaa7e9eb4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe98533c2f04c51e4d5c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe98533c2f04c51e4d5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f9b4c787e08c13a272cd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f9b4c787e08c13a272cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f691c472e9b061f0404"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1f691c472e9b061f0404`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ada66727bb0d03eed98"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ada66727bb0d03eed98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abbb004e24e9769b2e33"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-abbb004e24e9769b2e33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ece0405fca6b259d3b26"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ece0405fca6b259d3b26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea255011ccebe807e6c1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ea255011ccebe807e6c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bf3a39fbdcb6c66c879"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6bf3a39fbdcb6c66c879`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a1d190f6496590148e5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8a1d190f6496590148e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce16aca07506500a8807"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce16aca07506500a8807`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a63e6e8d21103554bf93"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a63e6e8d21103554bf93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59a58eecdf40c023e3dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-59a58eecdf40c023e3dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c7e2617444754150af2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c7e2617444754150af2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-36a0967e265de44e9ffb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-36a0967e265de44e9ffb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1eac5371c6b366b6ac81"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1eac5371c6b366b6ac81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ea57a99b4aa6c52606d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ea57a99b4aa6c52606d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f10db365a6e6a9734b98"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f10db365a6e6a9734b98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e5841ce4e5ea5afe2b2b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e5841ce4e5ea5afe2b2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-489a160a605ae77262ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-489a160a605ae77262ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e24f4e1014c61609a11"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7e24f4e1014c61609a11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e080f08d548fc23d33f6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e080f08d548fc23d33f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8b28e223d252dbf2cbd3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8b28e223d252dbf2cbd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-08f8005a4a8da3caf97a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-08f8005a4a8da3caf97a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0b1252749d1d60b1dc4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f0b1252749d1d60b1dc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cef5233dcb88b194658a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cef5233dcb88b194658a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1f792232f7cb31193122"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f792232f7cb31193122`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6477d90caf76d38dfdd7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6477d90caf76d38dfdd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fcfbf282215ae0bd0cd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5fcfbf282215ae0bd0cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bb7adee093d36171908"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5bb7adee093d36171908`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b7a215ecec175f249936"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b7a215ecec175f249936`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4c390b17c12b93ce993"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b4c390b17c12b93ce993`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75c7252d16210fbe8ae4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-75c7252d16210fbe8ae4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffe7bc2d1e38e2bd46c3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ffe7bc2d1e38e2bd46c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

On 1 November 2026, the user requested the opposite-direction counterpart after reviewing the original six-tile adapter. The source mirrors the physical geometry across x = 8 m and reverses complete directed paths, retaining native lane classes and deck identities. The native pose-2 joins also reverse lengthwise texture phase, so geometry, paths, marker flags, winding, and material coordinates are verified together. The [owning network specification](../../NETWORK_SPEC.md#164-opposite-handed-counterpart-and-native-drag-boundaries) records the reusable direction and native-boundary lessons. One existing menu-family declaration supplies the shared Tab button; no artificial assembly or new shared menu implementation is needed.
