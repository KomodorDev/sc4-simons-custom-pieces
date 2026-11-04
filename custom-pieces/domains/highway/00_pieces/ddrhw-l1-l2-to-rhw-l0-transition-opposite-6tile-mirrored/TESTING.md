---
title: "Testing: DD RHW-4 \u2014 L1/L2 \u2194 RHW-4 L0 \u2014 Mirrored Orthogonal Transition \u2014 Opposite Upper Descent \u2014 6 Tiles"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Mirrored Orthogonal Transition — Opposite Upper Descent — 6 Tiles

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Check this new type independently of the retained transition pair. It owns twelve cells in a 2 × 6 core, has one model-only cell at (0,0), and requests three unowned native sockets. Require four complete same-lane car journeys, eight exterior directed members, all four proper rotations, complete saved pavement and supports, driver-left yellow markings, and a flat constrained terrain base. These are opposite-upper-side choices within the existing orthogonal grid, rather than another relative grid alignment.

In source pose 0°, the DD socket is in the east column, with upper northbound out of the adapter at 15 m and lower southbound in at 7.5 m. West ground: upper-deck traffic northbound into the adapter. East ground: lower-deck traffic southbound out. Actual upper travel is northbound, and lower travel is southbound. The full player sequence is in the [README](README.md#2-piece-and-placement).

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `upper-lane-02-in` | road / 1 / primary | in | [-2.5, -88.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-d977a84d7a911bc0048d` |
| `upper-lane-01-in` | road / 1 / primary | in | [2.5, -88.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-57700a60d1579dc24dce` |
| `lower-lane-01-out` | road / 1 / primary | out | [13.5, -88.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-a980347eab2bc32dd576` |
| `lower-lane-01-in` | road / 1 / primary | in | [13.5, 8.0, 7.5]; [0.0, -1.0]; 0.0 | `path-interface-b2fe320b9e0bb31bdb27` |
| `upper-lane-02-out` | road / 1 / primary | out | [13.5, 8.0, 15.0]; [0.0, 1.0]; 0.0 | `path-interface-02def3c4ce1dd299e969` |
| `lower-lane-02-out` | road / 1 / primary | out | [18.5, -88.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-3cd860990d731c95fb5e` |
| `lower-lane-02-in` | road / 1 / primary | in | [18.5, 8.0, 7.5]; [0.0, -1.0]; 0.0 | `path-interface-fddc704c2b84d595ec6f` |
| `upper-lane-01-out` | road / 1 / primary | out | [18.5, 8.0, 15.0]; [0.0, 1.0]; 0.0 | `path-interface-991f143956c37b818e99` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `upper-lane-02-in` → `upper-lane-02-out` | primary |
| road | `upper-lane-01-in` → `upper-lane-01-out` | primary |
| road | `lower-lane-01-in` → `lower-lane-01-out` | primary |
| road | `lower-lane-02-in` → `lower-lane-02-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `upper-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 Deluxe 1.1.641 and the audited NAM 50 right-hand-traffic profile; record whether Windows runs directly or through Wine/CrossOver. Use a disposable flat city and a verified candidate containing the exact type. Close the game before changing Plugins, restart afterward, and place a fresh adapter on clean flat ground. Keep the two existing transition types and their observations separate. A small development build is not a complete replacement for a larger managed installation.

The source frame has north DD boundary at north = 8 m and south ground boundaries at north = −88 m. The common core is x = −8 to 24 m, two columns centred at x = 0 and 16 m, and six rows with centres at north = 0, −16, −32, −48, −64, and −80 m. Leave the README's 2 × 8 connection arrangement clear, plus at least three native continuation tiles beyond each socket. Test outward dragging, inward dragging from working controls, and direct placement beside completed approaches separately.

| Native boundary | Joining core cell | Unowned socket | Original NAM model / pose | Required service |
| --- | --- | --- | --- | --- |
| North DD | [1,0] | [1,−1] | `57530000` / 2 | Two upper northbound lanes at 15 m and two lower southbound lanes at 7.5 m |
| South upper carriageway | [0,5] | [0,6] | `57030000` / 2 | Two upper-linked northbound lanes at 0 m |
| South lower carriageway | [1,5] | [1,6] | `57030000` / 0 | Two lower-linked southbound lanes at 0 m |

The dimensions above describe construction ownership. The native profile has an approximately 1 mm origin overhang whose faded model continuation may cross the **west long edge** when the upper road is on x = 0 m. This follows the native DD pose and traffic phase, independently of physical plan reflection. Measure the complete saved projection and source-profile coverage, rather than copying the opposite existing shape's overhang allowance. The core still owns twelve cells, and the native check arrangement still spans 2 × 8 cells.

A donor pose is an internal clockwise quarter-turn count; pose 0 is unchanged, and pose 2 is 180°. Whole-piece placements use their separately labelled rotation convention. Both native decks must agree together at the DD boundary; one matching lane or similar-looking picture is insufficient.

## 3. Software checks

### 3.1 Build and inspect actual saved resources

From the repository root, use the [Python setup](../../../../docs/BUILD_AND_INSTALL.md#31-python-setup-for-a-checkout-or-source-zip), replace `BUILD_NAME` with an unused directory name, and run the following commands. They compile the two new types only; building does not install them.

```sh
python3 -B custom-pieces/scp.py build --include ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile --include ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/domains/highway/tools/freeze_orthogonal_transition_connectors.py custom-pieces/dist/BUILD_NAME --piece ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored
python3 -B -m scp_highway.connections --root custom-pieces --build custom-pieces/dist/BUILD_NAME --piece ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored
```

The acceptance checks must decode every saved lane and indexed triangle. Require native endpoint positions, classes, directions, flat collars, and all four proper rotations; `UseElevation=1`; all five zoom models and the combined preview; 14 complete support solids; the 2.5 m × 3.8 m car corridor; complete deck and barrier geometry; and exact native materials, winding, texture coordinates, and bounded original overhang. Ground native lane classes 1 and 2 are distinct from DD classes 0 and 1. The model-only cell must keep an intentionally empty PATH. A source curve or metadata table does not establish these saved-resource results.

The construction layout must retain twelve `#` core cells, with all three helpers unowned and unconstrained by the core mask. The measured engine mechanism ties all 21 core ground vertices into one common-height group. Check it in every proper rotation, while preserving each modeled road height. It selects no absolute world altitude. Compare the retained two types' actual model, PATH, and texture bytes against their accepted baseline rather than silently rebuilding a different original.

### 3.2 Generate and inspect selected documentation artifacts

After the accepted connector contract and saved-resource extraction are current, author this type's source-bound physical connector groups:

```sh
python3 -B - <<'PYDOC'
from pathlib import Path
from scp_highway.connections import write_connector_groups
write_connector_groups(Path('custom-pieces'), ['ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored'])
PYDOC
```

Replace `/path/to/SimCity 4/Plugins` below with the existing audited texture folder, retaining the quotation marks. The folder is read only. The piece's authored asphalt atlas must come from its own checked DAT before external NAM textures are resolved.

```sh
python3 -B custom-pieces/scp.py connectors refresh --domain highway --piece ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored --build dist/BUILD_NAME --plugins '/path/to/SimCity 4/Plugins'
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored --build dist/BUILD_NAME --plugins '/path/to/SimCity 4/Plugins'
python3 -B -m scp.preview --catalog --root custom-pieces --output custom-pieces/dist/BUILD_NAME --plugins '/path/to/SimCity 4/Plugins' --include ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored --views angled top
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored
python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p 'test_orthogonal_transition*.py' -v
python3 -B tools/run_tests.py
```

Inspect the actual angled, top, thumbnail, and connection-overview PNGs. Require complete models, readable names and cards, correct native directions, correctly phased yellow lines, and matching input/output fingerprints. Only accepted saved models may supply production artwork. Report skipped proprietary-input checks separately from passing configured native tests. Packaging and installation remain separate captures.

## 4. Game checks

### 4.1 Menu, fresh placement, and terrain

1. Open the original family button under **Transportation → Highways → SCP → Pieces** when its anchor is installed. Use **Tab** or **Shift+Tab** until the query names **DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Mirrored Orthogonal Transition — Opposite Upper Descent — 6 Tiles**. Check the two retained shapes still work as separate selections, and that a click places only this complete adapter.
2. Follow the [exact source-pose arrangement](README.md#21-reserve-the-core-and-three-native-sockets). Use a flat base, keep the three native socket cells clear, and place a fresh adapter. Inspect whether the twelve-cell terrain stays level, without a hole or ridge, and whether the ordinary native tiles appear correctly.
3. Repeat placement separately beside a matching prebuilt connection near a diagonal Y arm, beside the right-hand straight arm, and farther away followed by manual native dragging. Record the actual native alignment, arm, gap, terrain, and adapter rotation. These controls compare construction conditions; a prior report about the retained mirrored type is not a result for this new type.
4. Repeat at 90°, 180°, and 270° with **Home** and **End**. Placement rotation and city-camera rotation are separate checks.

### 4.2 Native joining, Route Query, and moving traffic

1. Follow the README's outward drawing, inward dragging, and direct prebuilt-placement procedures as separate tests at all three sockets. Never drag through the fixed twelve-cell core.
2. Confirm useful moving traffic on the ordinary DD and ground controls first. Supply origins and destinations through those controls, run the simulation, and use **Route Query** for each of this type's four same-lane journeys.
3. Follow actual cars from the last native tile through the complete adapter to the next native tile. Check both lanes, their directions, their complete height changes, and driver-left yellow markings. Record Route Query and visible travel separately.
4. Confirm that no lane change, U-turn, or transfer between the opposing carriageways occurs inside the fixed adapter. A successful construction or a coloured query line does not establish moving traffic.

### 4.3 Appearance and object lifetime

Inspect every zoom and all four camera views for complete pavement, barriers, supports, native profile contact, and yellow lines. Compare Medium and High shadow settings: custom cast shadows are disabled. Redraw ordinary approaches, replace one adapter, save, quit fully, reload, and repeat the native joins and lane journeys. After demolition, inspect all twelve old core cells and the three sockets for leftovers. Record exact candidate, environment, rotation, construction order, and observed result through the [shared observation procedure](../../../../docs/TESTING.md).

## 5. Results and known issues

The [actual saved-resource acceptance](evidence/compiled-verification.jsonc) passed for `dist/ddrhw-transition-four-variants-native-01`. It binds this complete DAT and its 99 resources to the current production sources. Independent checks cover 36,808 indexed model triangles, all five zooms, the combined preview, four complete lane journeys, eight directed native boundary members, all four proper rotations, complete pavement and barriers, 14 closed support solids, and the 2.5 m × 3.8 m car corridor. The complete retained original and mirrored DATs are byte-identical to their accepted installed baselines. This build has one actual original-anchor menu button with four alternatives; a pre-grouping construction count of four roots does not mean four visible buttons.

The [saved marking verification](evidence/native-markings-verification.jsonc) binds the actual model, PATH, atlas, and native texture inputs. Across the four-type package, all 48 measured cross-sections put yellow on the driver’s left; separate deliberately reversed native and authored-atlas texture-coordinate controls fail as required. These are measured pixel samples, rather than a claim about every rendered pixel or moving game traffic. The generated checklist below retains the exact scoped software observations and pending human cases.

The [documentation and artwork capture](evidence/documentation-artwork-verification.jsonc) records the checked source DAT, extracted connector contract, final image hashes, and contributor inspection. Both 1600 × 1200 standalone views, the 360 × 270 thumbnail, and the 2000 × 8136 connection overview are current. The two new types’ connector freshness checks pass, and selected document validation covers all four guide files. The contributor inspected the actual PNGs for complete models, readable full titles and cards, correct handedness, and unclipped content. This contributor inspection does not approve the separate human preview-review or game cases.

The retained pair's earlier human acceptance does not pass this new identity. The [retained mirrored transition's close-placement report](../ddrhw-l1-l2-to-rhw-l0-transition-orthogonal-6tile-mirrored/evidence/game-close-placement-20261103.jsonc) motivates the explicit flat-base controls but does not establish that this new type fails or that its runtime terrain behavior is fixed. Test the three construction conditions separately.

The compact lane slopes are experimental game geometry, rather than structural or traffic-capacity standards. The canonical pictures show the native-to-authored asphalt blend with the audited textures; its appearance and ground transparency still need an in-game review with the active textures. The declared car envelope does not cover every replacement automaton. Native automatic placement, dragging, all four rotations, moving traffic, redraw, demolition, and save/reload remain this new type's own human checks. Four proper rotations are supported; eight cursor states do not supply extra reflections or another grid alignment.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-14cef02b25edc692f2e1">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-14cef02b25edc692f2e1"></a>

**General: unverified** — `software_resources-14cef02b25edc692f2e1`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-14cef02b25edc692f2e1">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-14cef02b25edc692f2e1"></a>

**General: unverified** — `software_connectivity-14cef02b25edc692f2e1`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-d512f2ed9261176981c6">[ ] unverified</a> | <a href="#case-in_game_render-0956a761c762fecccc2b">[ ] unverified</a> | <a href="#case-in_game_render-4734f4d0b48f54e4acf5">[ ] unverified</a> | <a href="#case-in_game_render-0bfc8aa1fe240c9b4e77">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-d512f2ed9261176981c6"></a>

**0° CCW: unverified** — `in_game_render-d512f2ed9261176981c6`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0956a761c762fecccc2b"></a>

**90° CCW: unverified** — `in_game_render-0956a761c762fecccc2b`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-4734f4d0b48f54e4acf5"></a>

**180° CCW: unverified** — `in_game_render-4734f4d0b48f54e4acf5`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0bfc8aa1fe240c9b4e77"></a>

**270° CCW: unverified** — `in_game_render-0bfc8aa1fe240c9b4e77`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-d512f2ed9261176981c6">[ ] unverified</a> | <a href="#case-in_game_placement-0956a761c762fecccc2b">[ ] unverified</a> | <a href="#case-in_game_placement-4734f4d0b48f54e4acf5">[ ] unverified</a> | <a href="#case-in_game_placement-0bfc8aa1fe240c9b4e77">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-d512f2ed9261176981c6"></a>

**0° CCW: unverified** — `in_game_placement-d512f2ed9261176981c6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0956a761c762fecccc2b"></a>

**90° CCW: unverified** — `in_game_placement-0956a761c762fecccc2b`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-4734f4d0b48f54e4acf5"></a>

**180° CCW: unverified** — `in_game_placement-4734f4d0b48f54e4acf5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0bfc8aa1fe240c9b4e77"></a>

**270° CCW: unverified** — `in_game_placement-0bfc8aa1fe240c9b4e77`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-d512f2ed9261176981c6">[ ] unverified</a> | <a href="#case-in_game_demolition-0956a761c762fecccc2b">[ ] unverified</a> | <a href="#case-in_game_demolition-4734f4d0b48f54e4acf5">[ ] unverified</a> | <a href="#case-in_game_demolition-0bfc8aa1fe240c9b4e77">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-d512f2ed9261176981c6"></a>

**0° CCW: unverified** — `in_game_demolition-d512f2ed9261176981c6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0956a761c762fecccc2b"></a>

**90° CCW: unverified** — `in_game_demolition-0956a761c762fecccc2b`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-4734f4d0b48f54e4acf5"></a>

**180° CCW: unverified** — `in_game_demolition-4734f4d0b48f54e4acf5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0bfc8aa1fe240c9b4e77"></a>

**270° CCW: unverified** — `in_game_demolition-0bfc8aa1fe240c9b4e77`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-d512f2ed9261176981c6">[ ] unverified</a> | <a href="#case-in_game_save_reload-0956a761c762fecccc2b">[ ] unverified</a> | <a href="#case-in_game_save_reload-4734f4d0b48f54e4acf5">[ ] unverified</a> | <a href="#case-in_game_save_reload-0bfc8aa1fe240c9b4e77">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-d512f2ed9261176981c6"></a>

**0° CCW: unverified** — `in_game_save_reload-d512f2ed9261176981c6`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0956a761c762fecccc2b"></a>

**90° CCW: unverified** — `in_game_save_reload-0956a761c762fecccc2b`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-4734f4d0b48f54e4acf5"></a>

**180° CCW: unverified** — `in_game_save_reload-4734f4d0b48f54e4acf5`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0bfc8aa1fe240c9b4e77"></a>

**270° CCW: unverified** — `in_game_save_reload-0bfc8aa1fe240c9b4e77`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_route_query-bc936e9fa4bd401f4912">[ ] unverified</a> | <a href="#case-in_game_route_query-a450b25284187bf91ed9">[ ] unverified</a> | <a href="#case-in_game_route_query-6b17d1338c044bbb5a8b">[ ] unverified</a> | <a href="#case-in_game_route_query-bb3900c4cc46dd95c376">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_route_query-3d36d0f415afc22ef2e1">[ ] unverified</a> | <a href="#case-in_game_route_query-472740762f5b29d4e286">[ ] unverified</a> | <a href="#case-in_game_route_query-513926c5ed02268eebff">[ ] unverified</a> | <a href="#case-in_game_route_query-c5a93e9c629f1661cad9">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_route_query-de35e69f8c4464692463">[ ] unverified</a> | <a href="#case-in_game_route_query-c8501f937a547313a216">[ ] unverified</a> | <a href="#case-in_game_route_query-933c85f41da6b9d83809">[ ] unverified</a> | <a href="#case-in_game_route_query-73fa3b074e9130c22804">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_route_query-d716764ef5e9ce15362f">[ ] unverified</a> | <a href="#case-in_game_route_query-076ea3fd3ecaef430087">[ ] unverified</a> | <a href="#case-in_game_route_query-f41d798d9f1079534058">[ ] unverified</a> | <a href="#case-in_game_route_query-26a5bb36291f1860a418">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_route_query-bc936e9fa4bd401f4912"></a>

**0° CCW: unverified** — `in_game_route_query-bc936e9fa4bd401f4912`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-a450b25284187bf91ed9"></a>

**90° CCW: unverified** — `in_game_route_query-a450b25284187bf91ed9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-6b17d1338c044bbb5a8b"></a>

**180° CCW: unverified** — `in_game_route_query-6b17d1338c044bbb5a8b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-bb3900c4cc46dd95c376"></a>

**270° CCW: unverified** — `in_game_route_query-bb3900c4cc46dd95c376`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_route_query-3d36d0f415afc22ef2e1"></a>

**0° CCW: unverified** — `in_game_route_query-3d36d0f415afc22ef2e1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-472740762f5b29d4e286"></a>

**90° CCW: unverified** — `in_game_route_query-472740762f5b29d4e286`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-513926c5ed02268eebff"></a>

**180° CCW: unverified** — `in_game_route_query-513926c5ed02268eebff`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-c5a93e9c629f1661cad9"></a>

**270° CCW: unverified** — `in_game_route_query-c5a93e9c629f1661cad9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_route_query-de35e69f8c4464692463"></a>

**0° CCW: unverified** — `in_game_route_query-de35e69f8c4464692463`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-c8501f937a547313a216"></a>

**90° CCW: unverified** — `in_game_route_query-c8501f937a547313a216`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-933c85f41da6b9d83809"></a>

**180° CCW: unverified** — `in_game_route_query-933c85f41da6b9d83809`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-73fa3b074e9130c22804"></a>

**270° CCW: unverified** — `in_game_route_query-73fa3b074e9130c22804`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_route_query-d716764ef5e9ce15362f"></a>

**0° CCW: unverified** — `in_game_route_query-d716764ef5e9ce15362f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-076ea3fd3ecaef430087"></a>

**90° CCW: unverified** — `in_game_route_query-076ea3fd3ecaef430087`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-f41d798d9f1079534058"></a>

**180° CCW: unverified** — `in_game_route_query-f41d798d9f1079534058`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-26a5bb36291f1860a418"></a>

**270° CCW: unverified** — `in_game_route_query-26a5bb36291f1860a418`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_visible_travel-bc936e9fa4bd401f4912">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a450b25284187bf91ed9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6b17d1338c044bbb5a8b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bb3900c4cc46dd95c376">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_visible_travel-3d36d0f415afc22ef2e1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-472740762f5b29d4e286">[ ] unverified</a> | <a href="#case-in_game_visible_travel-513926c5ed02268eebff">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c5a93e9c629f1661cad9">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_visible_travel-de35e69f8c4464692463">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c8501f937a547313a216">[ ] unverified</a> | <a href="#case-in_game_visible_travel-933c85f41da6b9d83809">[ ] unverified</a> | <a href="#case-in_game_visible_travel-73fa3b074e9130c22804">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_visible_travel-d716764ef5e9ce15362f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-076ea3fd3ecaef430087">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f41d798d9f1079534058">[ ] unverified</a> | <a href="#case-in_game_visible_travel-26a5bb36291f1860a418">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_visible_travel-bc936e9fa4bd401f4912"></a>

**0° CCW: unverified** — `in_game_visible_travel-bc936e9fa4bd401f4912`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-a450b25284187bf91ed9"></a>

**90° CCW: unverified** — `in_game_visible_travel-a450b25284187bf91ed9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-6b17d1338c044bbb5a8b"></a>

**180° CCW: unverified** — `in_game_visible_travel-6b17d1338c044bbb5a8b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-bb3900c4cc46dd95c376"></a>

**270° CCW: unverified** — `in_game_visible_travel-bb3900c4cc46dd95c376`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_visible_travel-3d36d0f415afc22ef2e1"></a>

**0° CCW: unverified** — `in_game_visible_travel-3d36d0f415afc22ef2e1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-472740762f5b29d4e286"></a>

**90° CCW: unverified** — `in_game_visible_travel-472740762f5b29d4e286`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-513926c5ed02268eebff"></a>

**180° CCW: unverified** — `in_game_visible_travel-513926c5ed02268eebff`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-c5a93e9c629f1661cad9"></a>

**270° CCW: unverified** — `in_game_visible_travel-c5a93e9c629f1661cad9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_visible_travel-de35e69f8c4464692463"></a>

**0° CCW: unverified** — `in_game_visible_travel-de35e69f8c4464692463`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-c8501f937a547313a216"></a>

**90° CCW: unverified** — `in_game_visible_travel-c8501f937a547313a216`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-933c85f41da6b9d83809"></a>

**180° CCW: unverified** — `in_game_visible_travel-933c85f41da6b9d83809`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-73fa3b074e9130c22804"></a>

**270° CCW: unverified** — `in_game_visible_travel-73fa3b074e9130c22804`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_visible_travel-d716764ef5e9ce15362f"></a>

**0° CCW: unverified** — `in_game_visible_travel-d716764ef5e9ce15362f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-076ea3fd3ecaef430087"></a>

**90° CCW: unverified** — `in_game_visible_travel-076ea3fd3ecaef430087`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-f41d798d9f1079534058"></a>

**180° CCW: unverified** — `in_game_visible_travel-f41d798d9f1079534058`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-26a5bb36291f1860a418"></a>

**270° CCW: unverified** — `in_game_visible_travel-26a5bb36291f1860a418`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-414fbb9e32147c21e44c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9754acca26590cf88129">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41399b1ba6032b340b0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5237da17ff85db786bab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32ed042affefff80b0ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c12ec8b2fefa3e77465">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1301b4fa9230b570511">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3c38933b92caa7570b1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ad97c92b114ce634b646">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a22ccca988557d7e0071">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86424916902e21d88f7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb5f870ef21eef21cd23">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b2b554cb78fd942b2331">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ca0bc2cf35235045a54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a3cd2a8663722f6c79c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b813a8b6c44a4916ffdf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7a77ef628769838ac10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b9d009a0a8ebcf95bf1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-161f9da1e80cfc8c4fdc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65046877cd5861c78c14">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-143071746d36358a5d1d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56ddfd6207da9cb54f14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67d243932021e59cfe8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e75cf5f2657685150766">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c6ad4103531c99a40d2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9c3f8332320908c6e18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2e0dc109ff89b11ea92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8f0d9d89f2bab53eb80">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b5c094d6be27f43670aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f00b31abfb7485cb803">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e70554a244189b398869">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a845fa353edaa731a3ab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-65ddedcfa8b0070e50bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6902b6795df7bdf8e3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4d862faeeb7304d4ded">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a699678190f80763a02">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a499225bf953afef6e88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fddcd892401f96439646">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9343c5ed76ebb1903ca8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed71bbf0926bcaf3763c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f11821c53137bf10d48b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d73bb5ac7e8f37949bfd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c68618d3cf6004851506">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0de9510ff9621f9891a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-008827395ce07395192b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a32b4875e5d0a4e1d81d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0042de3701e78219071">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09891c7a1af2daf6aff6">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-414fbb9e32147c21e44c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-414fbb9e32147c21e44c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9754acca26590cf88129"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9754acca26590cf88129`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41399b1ba6032b340b0c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-41399b1ba6032b340b0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5237da17ff85db786bab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5237da17ff85db786bab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32ed042affefff80b0ff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32ed042affefff80b0ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c12ec8b2fefa3e77465"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9c12ec8b2fefa3e77465`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1301b4fa9230b570511"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e1301b4fa9230b570511`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3c38933b92caa7570b1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d3c38933b92caa7570b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ad97c92b114ce634b646"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad97c92b114ce634b646`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a22ccca988557d7e0071"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a22ccca988557d7e0071`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86424916902e21d88f7d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-86424916902e21d88f7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb5f870ef21eef21cd23"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cb5f870ef21eef21cd23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b2b554cb78fd942b2331"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b2b554cb78fd942b2331`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ca0bc2cf35235045a54"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8ca0bc2cf35235045a54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a3cd2a8663722f6c79c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2a3cd2a8663722f6c79c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b813a8b6c44a4916ffdf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b813a8b6c44a4916ffdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7a77ef628769838ac10"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7a77ef628769838ac10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b9d009a0a8ebcf95bf1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1b9d009a0a8ebcf95bf1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-161f9da1e80cfc8c4fdc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-161f9da1e80cfc8c4fdc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65046877cd5861c78c14"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-65046877cd5861c78c14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-143071746d36358a5d1d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-143071746d36358a5d1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56ddfd6207da9cb54f14"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-56ddfd6207da9cb54f14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67d243932021e59cfe8a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67d243932021e59cfe8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e75cf5f2657685150766"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e75cf5f2657685150766`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c6ad4103531c99a40d2a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c6ad4103531c99a40d2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9c3f8332320908c6e18"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b9c3f8332320908c6e18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2e0dc109ff89b11ea92"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2e0dc109ff89b11ea92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8f0d9d89f2bab53eb80"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a8f0d9d89f2bab53eb80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b5c094d6be27f43670aa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b5c094d6be27f43670aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f00b31abfb7485cb803"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9f00b31abfb7485cb803`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e70554a244189b398869"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e70554a244189b398869`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a845fa353edaa731a3ab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a845fa353edaa731a3ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-65ddedcfa8b0070e50bd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-65ddedcfa8b0070e50bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6902b6795df7bdf8e3e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d6902b6795df7bdf8e3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4d862faeeb7304d4ded"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a4d862faeeb7304d4ded`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a699678190f80763a02"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1a699678190f80763a02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a499225bf953afef6e88"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a499225bf953afef6e88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fddcd892401f96439646"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fddcd892401f96439646`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9343c5ed76ebb1903ca8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9343c5ed76ebb1903ca8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed71bbf0926bcaf3763c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ed71bbf0926bcaf3763c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f11821c53137bf10d48b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f11821c53137bf10d48b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d73bb5ac7e8f37949bfd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d73bb5ac7e8f37949bfd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c68618d3cf6004851506"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c68618d3cf6004851506`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0de9510ff9621f9891a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f0de9510ff9621f9891a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-008827395ce07395192b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-008827395ce07395192b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a32b4875e5d0a4e1d81d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a32b4875e5d0a4e1d81d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0042de3701e78219071"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c0042de3701e78219071`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09891c7a1af2daf6aff6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-09891c7a1af2daf6aff6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored:canonical-southeast | <a href="#case-preview_review-2053d4ddbda6f8f21500">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored:canonical-top | <a href="#case-preview_review-df6d36c8518037d49114">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored:connection-overview | <a href="#case-preview_review-78985f747b2f606cccbc">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored:canonical-southeast</summary>

<a id="case-preview_review-2053d4ddbda6f8f21500"></a>

**General: unverified** — `preview_review-2053d4ddbda6f8f21500`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored:canonical-top</summary>

<a id="case-preview_review-df6d36c8518037d49114"></a>

**General: unverified** — `preview_review-df6d36c8518037d49114`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored:connection-overview</summary>

<a id="case-preview_review-78985f747b2f606cccbc"></a>

**General: unverified** — `preview_review-78985f747b2f606cccbc`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested one additional opposite-upper-side choice for each of the two existing six-tile transitions, preserving both retained types. This new identity keeps its base's DD traffic phase, moves the upper road to the opposite side of the straight lower carriageway, and preserves two native lanes in each direction with yellow on the driver's left. The source treats physical reflection, traffic phase, native cross-section phase, and native lane classes separately.

Keep actual saved-resource, documentation, installation, and human game evidence separate. Follow [the shared observation procedure](../../../../docs/TESTING.md), copy an exact current case ID, and record only the behavior explicitly observed. Source checks, previews, and filesystem installation do not create human game passes.
