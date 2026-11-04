---
title: "Testing: DD RHW-4 \u2014 L1/L2 \u2194 RHW-4 L0 \u2014 Orthogonal Transition \u2014 Opposite Upper Descent \u2014 6 Tiles"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Orthogonal Transition — Opposite Upper Descent — 6 Tiles

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Check this new type independently of the retained transition pair. It owns twelve cells in a 2 × 6 core, has one model-only cell at (1,0), and requests three unowned native sockets. Require four complete same-lane car journeys, eight exterior directed members, all four proper rotations, complete saved pavement and supports, driver-left yellow markings, and a flat constrained terrain base. These are opposite-upper-side choices within the existing orthogonal grid, rather than another relative grid alignment.

In source pose 0°, the DD socket is in the west column, with upper southbound into the adapter at 15 m and lower northbound out at 7.5 m. West ground: lower-deck traffic northbound into the adapter. East ground: upper-deck traffic southbound out. Actual upper travel is southbound, and lower travel is northbound. The full player sequence is in the [README](README.md#2-piece-and-placement).

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `lower-lane-02-in` | road / 1 / primary | in | [-2.5, -88.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-d977a84d7a911bc0048d` |
| `lower-lane-02-out` | road / 1 / primary | out | [-2.5, 8.0, 7.5]; [0.0, 1.0]; 0.0 | `path-interface-00480ef66d1c683adb2c` |
| `upper-lane-01-in` | road / 1 / primary | in | [-2.5, 8.0, 15.0]; [0.0, -1.0]; 0.0 | `path-interface-aef756dec28195473947` |
| `lower-lane-01-in` | road / 1 / primary | in | [2.5, -88.0, 0.0]; [0.0, 1.0]; 0.0 | `path-interface-57700a60d1579dc24dce` |
| `lower-lane-01-out` | road / 1 / primary | out | [2.5, 8.0, 7.5]; [0.0, 1.0]; 0.0 | `path-interface-28cd03e10e6e40a3c0fa` |
| `upper-lane-02-in` | road / 1 / primary | in | [2.5, 8.0, 15.0]; [0.0, -1.0]; 0.0 | `path-interface-c5c8334a7156c02c488c` |
| `upper-lane-01-out` | road / 1 / primary | out | [13.5, -88.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-a980347eab2bc32dd576` |
| `upper-lane-02-out` | road / 1 / primary | out | [18.5, -88.0, 0.0]; [0.0, -1.0]; 0.0 | `path-interface-3cd860990d731c95fb5e` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `lower-lane-02-in` → `lower-lane-02-out` | primary |
| road | `upper-lane-01-in` → `upper-lane-01-out` | primary |
| road | `lower-lane-01-in` → `lower-lane-01-out` | primary |
| road | `upper-lane-02-in` → `upper-lane-02-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `lower-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-in` | road / `upper-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `lower-lane-02-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `lower-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-in` | road / `upper-lane-01-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 Deluxe 1.1.641 and the audited NAM 50 right-hand-traffic profile; record whether Windows runs directly or through Wine/CrossOver. Use a disposable flat city and a verified candidate containing the exact type. Close the game before changing Plugins, restart afterward, and place a fresh adapter on clean flat ground. Keep the two existing transition types and their observations separate. A small development build is not a complete replacement for a larger managed installation.

The source frame has north DD boundary at north = 8 m and south ground boundaries at north = −88 m. The common core is x = −8 to 24 m, two columns centred at x = 0 and 16 m, and six rows with centres at north = 0, −16, −32, −48, −64, and −80 m. Leave the README's 2 × 8 connection arrangement clear, plus at least three native continuation tiles beyond each socket. Test outward dragging, inward dragging from working controls, and direct placement beside completed approaches separately.

| Native boundary | Joining core cell | Unowned socket | Original NAM model / pose | Required service |
| --- | --- | --- | --- | --- |
| North DD | [0,0] | [0,−1] | `57530000` / 0 | Two upper southbound lanes at 15 m and two lower northbound lanes at 7.5 m |
| South upper carriageway | [1,5] | [1,6] | `57030000` / 0 | Two upper-linked southbound lanes at 0 m |
| South lower carriageway | [0,5] | [0,6] | `57030000` / 2 | Two lower-linked northbound lanes at 0 m |

The dimensions above describe construction ownership. The native profile has an approximately 1 mm origin overhang whose faded model continuation may cross the **east long edge** when the upper road is on x = 16 m. This follows the native DD pose and traffic phase, independently of physical plan reflection. Measure the complete saved projection and source-profile coverage, rather than copying the opposite existing shape's overhang allowance. The core still owns twelve cells, and the native check arrangement still spans 2 × 8 cells.

A donor pose is an internal clockwise quarter-turn count; pose 0 is unchanged, and pose 2 is 180°. Whole-piece placements use their separately labelled rotation convention. Both native decks must agree together at the DD boundary; one matching lane or similar-looking picture is insufficient.

## 3. Software checks

### 3.1 Build and inspect actual saved resources

From the repository root, use the [Python setup](../../../../docs/BUILD_AND_INSTALL.md#31-python-setup-for-a-checkout-or-source-zip), replace `BUILD_NAME` with an unused directory name, and run the following commands. They compile the two new types only; building does not install them.

```sh
python3 -B custom-pieces/scp.py build --include ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile --include ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile-mirrored --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/BUILD_NAME
python3 -B custom-pieces/domains/highway/tools/freeze_orthogonal_transition_connectors.py custom-pieces/dist/BUILD_NAME --piece ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile
python3 -B -m scp_highway.connections --root custom-pieces --build custom-pieces/dist/BUILD_NAME --piece ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile
```

The acceptance checks must decode every saved lane and indexed triangle. Require native endpoint positions, classes, directions, flat collars, and all four proper rotations; `UseElevation=1`; all five zoom models and the combined preview; 14 complete support solids; the 2.5 m × 3.8 m car corridor; complete deck and barrier geometry; and exact native materials, winding, texture coordinates, and bounded original overhang. Ground native lane classes 1 and 2 are distinct from DD classes 0 and 1. The model-only cell must keep an intentionally empty PATH. A source curve or metadata table does not establish these saved-resource results.

The construction layout must retain twelve `#` core cells, with all three helpers unowned and unconstrained by the core mask. The measured engine mechanism ties all 21 core ground vertices into one common-height group. Check it in every proper rotation, while preserving each modeled road height. It selects no absolute world altitude. Compare the retained two types' actual model, PATH, and texture bytes against their accepted baseline rather than silently rebuilding a different original.

### 3.2 Generate and inspect selected documentation artifacts

After the accepted connector contract and saved-resource extraction are current, author this type's source-bound physical connector groups:

```sh
python3 -B - <<'PYDOC'
from pathlib import Path
from scp_highway.connections import write_connector_groups
write_connector_groups(Path('custom-pieces'), ['ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile'])
PYDOC
```

Replace `/path/to/SimCity 4/Plugins` below with the existing audited texture folder, retaining the quotation marks. The folder is read only. The piece's authored asphalt atlas must come from its own checked DAT before external NAM textures are resolved.

```sh
python3 -B custom-pieces/scp.py connectors refresh --domain highway --piece ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile --build dist/BUILD_NAME --plugins '/path/to/SimCity 4/Plugins'
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile --build dist/BUILD_NAME --plugins '/path/to/SimCity 4/Plugins'
python3 -B -m scp.preview --catalog --root custom-pieces --output custom-pieces/dist/BUILD_NAME --plugins '/path/to/SimCity 4/Plugins' --include ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile --views angled top
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile
python3 -B -m unittest discover -s custom-pieces/domains/highway/tests -p 'test_orthogonal_transition*.py' -v
python3 -B tools/run_tests.py
```

Inspect the actual angled, top, thumbnail, and connection-overview PNGs. Require complete models, readable names and cards, correct native directions, correctly phased yellow lines, and matching input/output fingerprints. Only accepted saved models may supply production artwork. Report skipped proprietary-input checks separately from passing configured native tests. Packaging and installation remain separate captures.

## 4. Game checks

### 4.1 Menu, fresh placement, and terrain

1. Open the original family button under **Transportation → Highways → SCP → Pieces** when its anchor is installed. Use **Tab** or **Shift+Tab** until the query names **DD RHW-4 — L1/L2 ↔ RHW-4 L0 — Orthogonal Transition — Opposite Upper Descent — 6 Tiles**. Check the two retained shapes still work as separate selections, and that a click places only this complete adapter.
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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-5e0346b1e42cc8c25363">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-5e0346b1e42cc8c25363"></a>

**General: unverified** — `software_resources-5e0346b1e42cc8c25363`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-5e0346b1e42cc8c25363">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-5e0346b1e42cc8c25363"></a>

**General: unverified** — `software_connectivity-5e0346b1e42cc8c25363`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-dbaae4136a1c7fd5ebbe">[ ] unverified</a> | <a href="#case-in_game_render-a9759d2164a6dec47e70">[ ] unverified</a> | <a href="#case-in_game_render-5d18d5255912c6574610">[ ] unverified</a> | <a href="#case-in_game_render-ce46786cd802fbc45eb6">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-dbaae4136a1c7fd5ebbe"></a>

**0° CCW: unverified** — `in_game_render-dbaae4136a1c7fd5ebbe`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a9759d2164a6dec47e70"></a>

**90° CCW: unverified** — `in_game_render-a9759d2164a6dec47e70`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5d18d5255912c6574610"></a>

**180° CCW: unverified** — `in_game_render-5d18d5255912c6574610`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ce46786cd802fbc45eb6"></a>

**270° CCW: unverified** — `in_game_render-ce46786cd802fbc45eb6`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-dbaae4136a1c7fd5ebbe">[ ] unverified</a> | <a href="#case-in_game_placement-a9759d2164a6dec47e70">[ ] unverified</a> | <a href="#case-in_game_placement-5d18d5255912c6574610">[ ] unverified</a> | <a href="#case-in_game_placement-ce46786cd802fbc45eb6">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-dbaae4136a1c7fd5ebbe"></a>

**0° CCW: unverified** — `in_game_placement-dbaae4136a1c7fd5ebbe`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a9759d2164a6dec47e70"></a>

**90° CCW: unverified** — `in_game_placement-a9759d2164a6dec47e70`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5d18d5255912c6574610"></a>

**180° CCW: unverified** — `in_game_placement-5d18d5255912c6574610`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ce46786cd802fbc45eb6"></a>

**270° CCW: unverified** — `in_game_placement-ce46786cd802fbc45eb6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-dbaae4136a1c7fd5ebbe">[ ] unverified</a> | <a href="#case-in_game_demolition-a9759d2164a6dec47e70">[ ] unverified</a> | <a href="#case-in_game_demolition-5d18d5255912c6574610">[ ] unverified</a> | <a href="#case-in_game_demolition-ce46786cd802fbc45eb6">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-dbaae4136a1c7fd5ebbe"></a>

**0° CCW: unverified** — `in_game_demolition-dbaae4136a1c7fd5ebbe`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a9759d2164a6dec47e70"></a>

**90° CCW: unverified** — `in_game_demolition-a9759d2164a6dec47e70`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5d18d5255912c6574610"></a>

**180° CCW: unverified** — `in_game_demolition-5d18d5255912c6574610`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ce46786cd802fbc45eb6"></a>

**270° CCW: unverified** — `in_game_demolition-ce46786cd802fbc45eb6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-dbaae4136a1c7fd5ebbe">[ ] unverified</a> | <a href="#case-in_game_save_reload-a9759d2164a6dec47e70">[ ] unverified</a> | <a href="#case-in_game_save_reload-5d18d5255912c6574610">[ ] unverified</a> | <a href="#case-in_game_save_reload-ce46786cd802fbc45eb6">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-dbaae4136a1c7fd5ebbe"></a>

**0° CCW: unverified** — `in_game_save_reload-dbaae4136a1c7fd5ebbe`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a9759d2164a6dec47e70"></a>

**90° CCW: unverified** — `in_game_save_reload-a9759d2164a6dec47e70`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5d18d5255912c6574610"></a>

**180° CCW: unverified** — `in_game_save_reload-5d18d5255912c6574610`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ce46786cd802fbc45eb6"></a>

**270° CCW: unverified** — `in_game_save_reload-ce46786cd802fbc45eb6`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_route_query-2a0839a4ea38753a0444">[ ] unverified</a> | <a href="#case-in_game_route_query-526cc77b7d61f99157da">[ ] unverified</a> | <a href="#case-in_game_route_query-bf8a821c5df29ba3857f">[ ] unverified</a> | <a href="#case-in_game_route_query-ecd6c8ff1fd762ad8f95">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_route_query-7d361d66bc52769b1743">[ ] unverified</a> | <a href="#case-in_game_route_query-effb4042e1faf3e6278e">[ ] unverified</a> | <a href="#case-in_game_route_query-a787563df23fb0a595f5">[ ] unverified</a> | <a href="#case-in_game_route_query-e7face372bb963f9db73">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_route_query-f8b88b319c2cb36f4112">[ ] unverified</a> | <a href="#case-in_game_route_query-9731f5b66cb5654b6758">[ ] unverified</a> | <a href="#case-in_game_route_query-7734f52108c20bf1dbc6">[ ] unverified</a> | <a href="#case-in_game_route_query-c4bd2914838a64bf3b48">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_route_query-e9f7ec18b37ad92d4386">[ ] unverified</a> | <a href="#case-in_game_route_query-1d57c4702c094e52322e">[ ] unverified</a> | <a href="#case-in_game_route_query-838052ccf84121955206">[ ] unverified</a> | <a href="#case-in_game_route_query-092f287a7bc46f6f665c">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_route_query-2a0839a4ea38753a0444"></a>

**0° CCW: unverified** — `in_game_route_query-2a0839a4ea38753a0444`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-526cc77b7d61f99157da"></a>

**90° CCW: unverified** — `in_game_route_query-526cc77b7d61f99157da`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-bf8a821c5df29ba3857f"></a>

**180° CCW: unverified** — `in_game_route_query-bf8a821c5df29ba3857f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-ecd6c8ff1fd762ad8f95"></a>

**270° CCW: unverified** — `in_game_route_query-ecd6c8ff1fd762ad8f95`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_route_query-7d361d66bc52769b1743"></a>

**0° CCW: unverified** — `in_game_route_query-7d361d66bc52769b1743`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-effb4042e1faf3e6278e"></a>

**90° CCW: unverified** — `in_game_route_query-effb4042e1faf3e6278e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-a787563df23fb0a595f5"></a>

**180° CCW: unverified** — `in_game_route_query-a787563df23fb0a595f5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-e7face372bb963f9db73"></a>

**270° CCW: unverified** — `in_game_route_query-e7face372bb963f9db73`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_route_query-f8b88b319c2cb36f4112"></a>

**0° CCW: unverified** — `in_game_route_query-f8b88b319c2cb36f4112`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-9731f5b66cb5654b6758"></a>

**90° CCW: unverified** — `in_game_route_query-9731f5b66cb5654b6758`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-7734f52108c20bf1dbc6"></a>

**180° CCW: unverified** — `in_game_route_query-7734f52108c20bf1dbc6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_route_query-c4bd2914838a64bf3b48"></a>

**270° CCW: unverified** — `in_game_route_query-c4bd2914838a64bf3b48`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_route_query-e9f7ec18b37ad92d4386"></a>

**0° CCW: unverified** — `in_game_route_query-e9f7ec18b37ad92d4386`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-1d57c4702c094e52322e"></a>

**90° CCW: unverified** — `in_game_route_query-1d57c4702c094e52322e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-838052ccf84121955206"></a>

**180° CCW: unverified** — `in_game_route_query-838052ccf84121955206`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_route_query-092f287a7bc46f6f665c"></a>

**270° CCW: unverified** — `in_game_route_query-092f287a7bc46f6f665c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 16 cases; unverified: 16</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out | — | <a href="#case-in_game_visible_travel-2a0839a4ea38753a0444">[ ] unverified</a> | <a href="#case-in_game_visible_travel-526cc77b7d61f99157da">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bf8a821c5df29ba3857f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ecd6c8ff1fd762ad8f95">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out | — | <a href="#case-in_game_visible_travel-7d361d66bc52769b1743">[ ] unverified</a> | <a href="#case-in_game_visible_travel-effb4042e1faf3e6278e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a787563df23fb0a595f5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e7face372bb963f9db73">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out | — | <a href="#case-in_game_visible_travel-f8b88b319c2cb36f4112">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9731f5b66cb5654b6758">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7734f52108c20bf1dbc6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c4bd2914838a64bf3b48">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out | — | <a href="#case-in_game_visible_travel-e9f7ec18b37ad92d4386">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1d57c4702c094e52322e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-838052ccf84121955206">[ ] unverified</a> | <a href="#case-in_game_visible_travel-092f287a7bc46f6f665c">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out</summary>

<a id="case-in_game_visible_travel-2a0839a4ea38753a0444"></a>

**0° CCW: unverified** — `in_game_visible_travel-2a0839a4ea38753a0444`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-526cc77b7d61f99157da"></a>

**90° CCW: unverified** — `in_game_visible_travel-526cc77b7d61f99157da`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-bf8a821c5df29ba3857f"></a>

**180° CCW: unverified** — `in_game_visible_travel-bf8a821c5df29ba3857f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-ecd6c8ff1fd762ad8f95"></a>

**270° CCW: unverified** — `in_game_visible_travel-ecd6c8ff1fd762ad8f95`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-in>lower-lane-02-out; entry: lower-lane-02-in; exit: lower-lane-02-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out</summary>

<a id="case-in_game_visible_travel-7d361d66bc52769b1743"></a>

**0° CCW: unverified** — `in_game_visible_travel-7d361d66bc52769b1743`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-effb4042e1faf3e6278e"></a>

**90° CCW: unverified** — `in_game_visible_travel-effb4042e1faf3e6278e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-a787563df23fb0a595f5"></a>

**180° CCW: unverified** — `in_game_visible_travel-a787563df23fb0a595f5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-e7face372bb963f9db73"></a>

**270° CCW: unverified** — `in_game_visible_travel-e7face372bb963f9db73`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-in>upper-lane-01-out; entry: upper-lane-01-in; exit: upper-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out</summary>

<a id="case-in_game_visible_travel-f8b88b319c2cb36f4112"></a>

**0° CCW: unverified** — `in_game_visible_travel-f8b88b319c2cb36f4112`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-9731f5b66cb5654b6758"></a>

**90° CCW: unverified** — `in_game_visible_travel-9731f5b66cb5654b6758`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-7734f52108c20bf1dbc6"></a>

**180° CCW: unverified** — `in_game_visible_travel-7734f52108c20bf1dbc6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

<a id="case-in_game_visible_travel-c4bd2914838a64bf3b48"></a>

**270° CCW: unverified** — `in_game_visible_travel-c4bd2914838a64bf3b48`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-in>lower-lane-01-out; entry: lower-lane-01-in; exit: lower-lane-01-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out</summary>

<a id="case-in_game_visible_travel-e9f7ec18b37ad92d4386"></a>

**0° CCW: unverified** — `in_game_visible_travel-e9f7ec18b37ad92d4386`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-1d57c4702c094e52322e"></a>

**90° CCW: unverified** — `in_game_visible_travel-1d57c4702c094e52322e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-838052ccf84121955206"></a>

**180° CCW: unverified** — `in_game_visible_travel-838052ccf84121955206`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

<a id="case-in_game_visible_travel-092f287a7bc46f6f665c"></a>

**270° CCW: unverified** — `in_game_visible_travel-092f287a7bc46f6f665c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-in>upper-lane-02-out; entry: upper-lane-02-in; exit: upper-lane-02-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-76e83cfcd41ac6e18391">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1a51a5a66f7bed24644">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc2be51f97bd2498e564">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fcde71606b5dc174aed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8e9c002e4667c7b54aaa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62d101e94eee42cb64bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7607780b9511bd488ea8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b35b85d76eb4244c08c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d7d7c272a0b8ca388570">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04785fb80704adba6b09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbcb942a964e522c70ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb582b41914c3b772704">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ad610c5725f193a5a48f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9474476b8dfa8ef4dc6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99628d557573e0119f4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c08e6b75e859fb290846">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2c3b6b8b3e54f7d8933a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83fbc1fbfdc50de78039">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c71a7fdcb32717b308a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65690deaeee8f5c5dda5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-79cdec3277e377e8a11f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6b5b7ba16de2b8b7614">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b82ab9270650589803b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5368a6ff0e1396e6d4e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7945488292ea9580c3f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a5cc2dbf2ceab4d06dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-441d3f96577d55f60fd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9b991d16364d36445dd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0b374f03390cdf489853">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74f8c3f9fd485d7f38c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55ce624d1b72c190057c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92476301c9f6d404a9e6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a5cdaf7fd19e014d8d80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f356bfecf7aaf4d267f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-607fa4cf5ceaf093bcf9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-249fc18017f58bba7df6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8866e00d90e977bca8cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72e9a72b9168fe83505d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26cd3364ac599a191204">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b4b8d413bae2a0c6aa8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a4da1e3a61fe7ea49a33">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0770888db94187f11f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53e81b04d0575ac67d59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b937e2995b178946fda">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c84d4421e165846a2acd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-169cff8ae7b92bc28053">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99946c217a7c36426df0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-420c5f1726c66b718fbe">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-76e83cfcd41ac6e18391"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-76e83cfcd41ac6e18391`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1a51a5a66f7bed24644"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f1a51a5a66f7bed24644`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc2be51f97bd2498e564"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cc2be51f97bd2498e564`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fcde71606b5dc174aed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9fcde71606b5dc174aed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8e9c002e4667c7b54aaa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8e9c002e4667c7b54aaa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62d101e94eee42cb64bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-62d101e94eee42cb64bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7607780b9511bd488ea8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7607780b9511bd488ea8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b35b85d76eb4244c08c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b35b85d76eb4244c08c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d7d7c272a0b8ca388570"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d7d7c272a0b8ca388570`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04785fb80704adba6b09"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-04785fb80704adba6b09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbcb942a964e522c70ca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bbcb942a964e522c70ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb582b41914c3b772704"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bb582b41914c3b772704`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ad610c5725f193a5a48f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad610c5725f193a5a48f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9474476b8dfa8ef4dc6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b9474476b8dfa8ef4dc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99628d557573e0119f4b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-99628d557573e0119f4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c08e6b75e859fb290846"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c08e6b75e859fb290846`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2c3b6b8b3e54f7d8933a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2c3b6b8b3e54f7d8933a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83fbc1fbfdc50de78039"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-83fbc1fbfdc50de78039`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c71a7fdcb32717b308a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c71a7fdcb32717b308a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65690deaeee8f5c5dda5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-65690deaeee8f5c5dda5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-79cdec3277e377e8a11f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-79cdec3277e377e8a11f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6b5b7ba16de2b8b7614"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a6b5b7ba16de2b8b7614`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b82ab9270650589803b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6b82ab9270650589803b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5368a6ff0e1396e6d4e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a5368a6ff0e1396e6d4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7945488292ea9580c3f3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7945488292ea9580c3f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a5cc2dbf2ceab4d06dd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4a5cc2dbf2ceab4d06dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-441d3f96577d55f60fd1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-441d3f96577d55f60fd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9b991d16364d36445dd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a9b991d16364d36445dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0b374f03390cdf489853"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0b374f03390cdf489853`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74f8c3f9fd485d7f38c5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74f8c3f9fd485d7f38c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55ce624d1b72c190057c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-55ce624d1b72c190057c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92476301c9f6d404a9e6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92476301c9f6d404a9e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a5cdaf7fd19e014d8d80"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a5cdaf7fd19e014d8d80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f356bfecf7aaf4d267f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4f356bfecf7aaf4d267f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-607fa4cf5ceaf093bcf9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-607fa4cf5ceaf093bcf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-249fc18017f58bba7df6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-249fc18017f58bba7df6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-in; to port: upper-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8866e00d90e977bca8cc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8866e00d90e977bca8cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72e9a72b9168fe83505d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-72e9a72b9168fe83505d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26cd3364ac599a191204"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-26cd3364ac599a191204`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b4b8d413bae2a0c6aa8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b4b8d413bae2a0c6aa8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-02-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a4da1e3a61fe7ea49a33"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a4da1e3a61fe7ea49a33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0770888db94187f11f0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0770888db94187f11f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53e81b04d0575ac67d59"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-53e81b04d0575ac67d59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b937e2995b178946fda"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2b937e2995b178946fda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: lower-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c84d4421e165846a2acd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c84d4421e165846a2acd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-169cff8ae7b92bc28053"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-169cff8ae7b92bc28053`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99946c217a7c36426df0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-99946c217a7c36426df0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-420c5f1726c66b718fbe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-420c5f1726c66b718fbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-in; to port: upper-lane-01-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile:canonical-southeast | <a href="#case-preview_review-49320e663f8366acedf9">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile:canonical-top | <a href="#case-preview_review-568202b2e331874668c8">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile:connection-overview | <a href="#case-preview_review-dcb14410c1ca47b4765e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile:canonical-southeast</summary>

<a id="case-preview_review-49320e663f8366acedf9"></a>

**General: unverified** — `preview_review-49320e663f8366acedf9`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile:canonical-top</summary>

<a id="case-preview_review-568202b2e331874668c8"></a>

**General: unverified** — `preview_review-568202b2e331874668c8`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile:connection-overview</summary>

<a id="case-preview_review-dcb14410c1ca47b4765e"></a>

**General: unverified** — `preview_review-dcb14410c1ca47b4765e`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-l2-to-rhw-l0-transition-opposite-6tile:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The user requested one additional opposite-upper-side choice for each of the two existing six-tile transitions, preserving both retained types. This new identity keeps its base's DD traffic phase, moves the upper road to the opposite side of the straight lower carriageway, and preserves two native lanes in each direction with yellow on the driver's left. The source treats physical reflection, traffic phase, native cross-section phase, and native lane classes separately.

Keep actual saved-resource, documentation, installation, and human game evidence separate. Follow [the shared observation procedure](../../../../docs/TESTING.md), copy an exact current case ID, and record only the behavior explicitly observed. Source checks, previews, and filesystem installation do not create human game passes.
