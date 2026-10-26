# HSR L2 Two-Track Straight

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

Native-width two-track HSR at 15.5 m with opposite-direction paths; an individually selectable lower straight.

Exact reusable identifier: `hsr-component-lower-paired-straight`.

Footprint: **1 × 1 tiles**. Exact menu name: **HSR L2 Two-Track Straight**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR L2 Two-Track Straight](preview.png)

<!-- END PIECE OVERVIEW -->

**Open demolition defect, reported 2026-10-23:** the user placed three copies of this piece end to end and bulldozed the middle tile; both connected survivors appeared as Monorail. The [failure record](../../01_assemblies/straight-stem-trumpet-v4/evidence/demolition-regression-20261023.json) retains the exact confirmation, installed menu-trial context, and unreported conditions. No fix has been verified. Existing whole-placement demolition cases do not cover this partial-deletion result; use the [focused regression procedure](../../../../docs/TESTING.md#investigate-single-tile-demolition-and-connected-survivors).

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/1 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/8 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN CONNECTIONS -->

## Connections and journeys

Purpose: describe intrinsic directional interfaces and permitted service journeys.

Generated from [connections.json](connections.json). Coordinates are canonical east, north and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sout` | hsr / 7 / primary | out | [-2.0, -8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [2.0, -8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 35, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-lower-paired-straight/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-lower-paired-straight/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-ce9d7f87faa8cf15c8fc">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-ce9d7f87faa8cf15c8fc"></a>

**General: unverified** — `software_resources-ce9d7f87faa8cf15c8fc`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-ce9d7f87faa8cf15c8fc">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-ce9d7f87faa8cf15c8fc"></a>

**General: unverified** — `software_connectivity-ce9d7f87faa8cf15c8fc`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-lower-paired-straight:canonical-southeast | <a href="#case-preview_review-02941c608575aef5939c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-lower-paired-straight:canonical-southeast</summary>

<a id="case-preview_review-02941c608575aef5939c"></a>

**General: unverified** — `preview_review-02941c608575aef5939c`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-lower-paired-straight:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-33b06929a6d90240c7ca">[ ] unverified</a> | <a href="#case-in_game_render-cc1af715d656b28f54bb">[ ] unverified</a> | <a href="#case-in_game_render-568b1caaf435a32ff291">[ ] unverified</a> | <a href="#case-in_game_render-9873412f9f8be0255400">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-33b06929a6d90240c7ca"></a>

**0° CCW: unverified** — `in_game_render-33b06929a6d90240c7ca`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-cc1af715d656b28f54bb"></a>

**90° CCW: unverified** — `in_game_render-cc1af715d656b28f54bb`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-568b1caaf435a32ff291"></a>

**180° CCW: unverified** — `in_game_render-568b1caaf435a32ff291`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9873412f9f8be0255400"></a>

**270° CCW: unverified** — `in_game_render-9873412f9f8be0255400`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-33b06929a6d90240c7ca">[ ] unverified</a> | <a href="#case-in_game_placement-cc1af715d656b28f54bb">[ ] unverified</a> | <a href="#case-in_game_placement-568b1caaf435a32ff291">[ ] unverified</a> | <a href="#case-in_game_placement-9873412f9f8be0255400">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-33b06929a6d90240c7ca"></a>

**0° CCW: unverified** — `in_game_placement-33b06929a6d90240c7ca`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-cc1af715d656b28f54bb"></a>

**90° CCW: unverified** — `in_game_placement-cc1af715d656b28f54bb`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-568b1caaf435a32ff291"></a>

**180° CCW: unverified** — `in_game_placement-568b1caaf435a32ff291`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9873412f9f8be0255400"></a>

**270° CCW: unverified** — `in_game_placement-9873412f9f8be0255400`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-33b06929a6d90240c7ca">[ ] unverified</a> | <a href="#case-in_game_demolition-cc1af715d656b28f54bb">[ ] unverified</a> | <a href="#case-in_game_demolition-568b1caaf435a32ff291">[ ] unverified</a> | <a href="#case-in_game_demolition-9873412f9f8be0255400">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-33b06929a6d90240c7ca"></a>

**0° CCW: unverified** — `in_game_demolition-33b06929a6d90240c7ca`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-cc1af715d656b28f54bb"></a>

**90° CCW: unverified** — `in_game_demolition-cc1af715d656b28f54bb`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-568b1caaf435a32ff291"></a>

**180° CCW: unverified** — `in_game_demolition-568b1caaf435a32ff291`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9873412f9f8be0255400"></a>

**270° CCW: unverified** — `in_game_demolition-9873412f9f8be0255400`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-33b06929a6d90240c7ca">[ ] unverified</a> | <a href="#case-in_game_save_reload-cc1af715d656b28f54bb">[ ] unverified</a> | <a href="#case-in_game_save_reload-568b1caaf435a32ff291">[ ] unverified</a> | <a href="#case-in_game_save_reload-9873412f9f8be0255400">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-33b06929a6d90240c7ca"></a>

**0° CCW: unverified** — `in_game_save_reload-33b06929a6d90240c7ca`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-cc1af715d656b28f54bb"></a>

**90° CCW: unverified** — `in_game_save_reload-cc1af715d656b28f54bb`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-568b1caaf435a32ff291"></a>

**180° CCW: unverified** — `in_game_save_reload-568b1caaf435a32ff291`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9873412f9f8be0255400"></a>

**270° CCW: unverified** — `in_game_save_reload-9873412f9f8be0255400`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-06466a17ee6b6d84dab0">[ ] unverified</a> | <a href="#case-in_game_journey-8b92b636a69df8add9aa">[ ] unverified</a> | <a href="#case-in_game_journey-7498b67eef5ca59e0d27">[ ] unverified</a> | <a href="#case-in_game_journey-a25f075c170c5d9de330">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-359af6bdd34b9eca0d1f">[ ] unverified</a> | <a href="#case-in_game_journey-eddd6f88b43b05d0af0c">[ ] unverified</a> | <a href="#case-in_game_journey-7fd9e7def85f452e4cbc">[ ] unverified</a> | <a href="#case-in_game_journey-32b3a4420c6ca4c0e61e">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-06466a17ee6b6d84dab0"></a>

**0° CCW: unverified** — `in_game_journey-06466a17ee6b6d84dab0`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-8b92b636a69df8add9aa"></a>

**90° CCW: unverified** — `in_game_journey-8b92b636a69df8add9aa`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-7498b67eef5ca59e0d27"></a>

**180° CCW: unverified** — `in_game_journey-7498b67eef5ca59e0d27`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-a25f075c170c5d9de330"></a>

**270° CCW: unverified** — `in_game_journey-a25f075c170c5d9de330`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-359af6bdd34b9eca0d1f"></a>

**0° CCW: unverified** — `in_game_journey-359af6bdd34b9eca0d1f`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-eddd6f88b43b05d0af0c"></a>

**90° CCW: unverified** — `in_game_journey-eddd6f88b43b05d0af0c`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-7fd9e7def85f452e4cbc"></a>

**180° CCW: unverified** — `in_game_journey-7fd9e7def85f452e4cbc`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-32b3a4420c6ca4c0e61e"></a>

**270° CCW: unverified** — `in_game_journey-32b3a4420c6ca4c0e61e`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5d0dc3294a3cb0b46b9a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-750498f3078855da1e30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9590c0a02a015da93fde">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13b6927e1c86c3e658de">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c05123841250d6afc043">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d9df2f38511df6690f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7aad55b31d38731c7d4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4097acdd5d4ac75fc53">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5d0dc3294a3cb0b46b9a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5d0dc3294a3cb0b46b9a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-750498f3078855da1e30"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-750498f3078855da1e30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9590c0a02a015da93fde"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9590c0a02a015da93fde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13b6927e1c86c3e658de"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-13b6927e1c86c3e658de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c05123841250d6afc043"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c05123841250d6afc043`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d9df2f38511df6690f7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3d9df2f38511df6690f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7aad55b31d38731c7d4b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7aad55b31d38731c7d4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4097acdd5d4ac75fc53"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4097acdd5d4ac75fc53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
