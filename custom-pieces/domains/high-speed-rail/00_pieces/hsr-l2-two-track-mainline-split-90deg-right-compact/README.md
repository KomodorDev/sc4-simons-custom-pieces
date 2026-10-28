<a id="hsr-l2-split-90-degree-compact"></a>

# HSR Level 2 (15.5 m) — Split 90° Right from Two-Track Mainline — Compact

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `interchange-hsr-split-90-compact` → `hsr-l2-two-track-mainline-split-90deg-right-compact`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

HSR Level 2 (15.5 m) — Split 90° Right from Two-Track Mainline — Compact. Fixed click-to-place piece in a 2 by 2 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `hsr-l2-two-track-mainline-split-90deg-right-compact`.

Footprint: **2 × 2 tiles**. Exact menu name: **HSR Level 2 (15.5 m) — Split 90° Right from Two-Track Mainline — Compact**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR Level 2 (15.5 m) — Split 90° Right from Two-Track Mainline — Compact](previews/preview.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/1 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/12 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN CONNECTIONS -->

## Connections and journeys

Purpose: describe intrinsic directional interfaces and permitted service journeys.

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sout` | hsr / 7 / primary | out | [-2.0, -24.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [2.0, -24.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Bout` | hsr / 7 / primary | out | [24.0, 0.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-365752af76285c80cd0b` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Sin` → `Bout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Nin` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Nin` | hsr / `Bout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 43, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-two-track-mainline-split-90deg-right-compact/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-two-track-mainline-split-90deg-right-compact/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-d185667b388de3eceec8">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-d185667b388de3eceec8"></a>

**General: unverified** — `software_resources-d185667b388de3eceec8`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-d185667b388de3eceec8">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-d185667b388de3eceec8"></a>

**General: unverified** — `software_connectivity-d185667b388de3eceec8`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-hsr-split-90-compact:canonical-southeast | <a href="#case-preview_review-35b733e073b23610029e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-hsr-split-90-compact:canonical-southeast</summary>

<a id="case-preview_review-35b733e073b23610029e"></a>

**General: unverified** — `preview_review-35b733e073b23610029e`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-hsr-split-90-compact:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-18a95bfc79a5339d4c9c">[ ] unverified</a> | <a href="#case-in_game_render-f45f8c8699197027784e">[ ] unverified</a> | <a href="#case-in_game_render-a2320ba51d5502fe4caa">[ ] unverified</a> | <a href="#case-in_game_render-53d23755ddfc9a9c452f">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-18a95bfc79a5339d4c9c"></a>

**0° CCW: unverified** — `in_game_render-18a95bfc79a5339d4c9c`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-f45f8c8699197027784e"></a>

**90° CCW: unverified** — `in_game_render-f45f8c8699197027784e`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a2320ba51d5502fe4caa"></a>

**180° CCW: unverified** — `in_game_render-a2320ba51d5502fe4caa`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-53d23755ddfc9a9c452f"></a>

**270° CCW: unverified** — `in_game_render-53d23755ddfc9a9c452f`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-18a95bfc79a5339d4c9c">[ ] unverified</a> | <a href="#case-in_game_placement-f45f8c8699197027784e">[ ] unverified</a> | <a href="#case-in_game_placement-a2320ba51d5502fe4caa">[ ] unverified</a> | <a href="#case-in_game_placement-53d23755ddfc9a9c452f">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-18a95bfc79a5339d4c9c"></a>

**0° CCW: unverified** — `in_game_placement-18a95bfc79a5339d4c9c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-f45f8c8699197027784e"></a>

**90° CCW: unverified** — `in_game_placement-f45f8c8699197027784e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a2320ba51d5502fe4caa"></a>

**180° CCW: unverified** — `in_game_placement-a2320ba51d5502fe4caa`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-53d23755ddfc9a9c452f"></a>

**270° CCW: unverified** — `in_game_placement-53d23755ddfc9a9c452f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-18a95bfc79a5339d4c9c">[ ] unverified</a> | <a href="#case-in_game_demolition-f45f8c8699197027784e">[ ] unverified</a> | <a href="#case-in_game_demolition-a2320ba51d5502fe4caa">[ ] unverified</a> | <a href="#case-in_game_demolition-53d23755ddfc9a9c452f">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-18a95bfc79a5339d4c9c"></a>

**0° CCW: unverified** — `in_game_demolition-18a95bfc79a5339d4c9c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-f45f8c8699197027784e"></a>

**90° CCW: unverified** — `in_game_demolition-f45f8c8699197027784e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a2320ba51d5502fe4caa"></a>

**180° CCW: unverified** — `in_game_demolition-a2320ba51d5502fe4caa`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-53d23755ddfc9a9c452f"></a>

**270° CCW: unverified** — `in_game_demolition-53d23755ddfc9a9c452f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-18a95bfc79a5339d4c9c">[ ] unverified</a> | <a href="#case-in_game_save_reload-f45f8c8699197027784e">[ ] unverified</a> | <a href="#case-in_game_save_reload-a2320ba51d5502fe4caa">[ ] unverified</a> | <a href="#case-in_game_save_reload-53d23755ddfc9a9c452f">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-18a95bfc79a5339d4c9c"></a>

**0° CCW: unverified** — `in_game_save_reload-18a95bfc79a5339d4c9c`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-f45f8c8699197027784e"></a>

**90° CCW: unverified** — `in_game_save_reload-f45f8c8699197027784e`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a2320ba51d5502fe4caa"></a>

**180° CCW: unverified** — `in_game_save_reload-a2320ba51d5502fe4caa`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-53d23755ddfc9a9c452f"></a>

**270° CCW: unverified** — `in_game_save_reload-53d23755ddfc9a9c452f`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-40c782c9e8fd38990c7d">[ ] unverified</a> | <a href="#case-in_game_journey-d2491ee164a82a865cb7">[ ] unverified</a> | <a href="#case-in_game_journey-6735d372e70c5502354b">[ ] unverified</a> | <a href="#case-in_game_journey-37ecd72be9c3d37e6dd2">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-70cd512e4530ec06bb85">[ ] unverified</a> | <a href="#case-in_game_journey-92f8bf9b983d8e0c43c6">[ ] unverified</a> | <a href="#case-in_game_journey-d1249aa8f2d9dce046af">[ ] unverified</a> | <a href="#case-in_game_journey-d6007fa8a9b0be72e54f">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout | — | <a href="#case-in_game_journey-af027b82719604e7157b">[ ] unverified</a> | <a href="#case-in_game_journey-d1c5f88bed67ba37242b">[ ] unverified</a> | <a href="#case-in_game_journey-4f07881fcfbc3074efd1">[ ] unverified</a> | <a href="#case-in_game_journey-72e0c61d1ab7e4d8bef8">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-40c782c9e8fd38990c7d"></a>

**0° CCW: unverified** — `in_game_journey-40c782c9e8fd38990c7d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-d2491ee164a82a865cb7"></a>

**90° CCW: unverified** — `in_game_journey-d2491ee164a82a865cb7`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-6735d372e70c5502354b"></a>

**180° CCW: unverified** — `in_game_journey-6735d372e70c5502354b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-37ecd72be9c3d37e6dd2"></a>

**270° CCW: unverified** — `in_game_journey-37ecd72be9c3d37e6dd2`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-70cd512e4530ec06bb85"></a>

**0° CCW: unverified** — `in_game_journey-70cd512e4530ec06bb85`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-92f8bf9b983d8e0c43c6"></a>

**90° CCW: unverified** — `in_game_journey-92f8bf9b983d8e0c43c6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-d1249aa8f2d9dce046af"></a>

**180° CCW: unverified** — `in_game_journey-d1249aa8f2d9dce046af`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-d6007fa8a9b0be72e54f"></a>

**270° CCW: unverified** — `in_game_journey-d6007fa8a9b0be72e54f`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout</summary>

<a id="case-in_game_journey-af027b82719604e7157b"></a>

**0° CCW: unverified** — `in_game_journey-af027b82719604e7157b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-d1c5f88bed67ba37242b"></a>

**90° CCW: unverified** — `in_game_journey-d1c5f88bed67ba37242b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-4f07881fcfbc3074efd1"></a>

**180° CCW: unverified** — `in_game_journey-4f07881fcfbc3074efd1`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-72e0c61d1ab7e4d8bef8"></a>

**270° CCW: unverified** — `in_game_journey-72e0c61d1ab7e4d8bef8`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c6eb62250443fe5a7269">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4319b6deb149dd74744a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58293225a9d79a7e4f8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c58c2df04ec189c3bee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f16fdba01efb3cb655fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ac521f72324961521d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-046b9cdd42941c94c8a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd7d222e48a4adb7f3c5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-31a69710ea5226f58568">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89e4a44aad7de4acce3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11040f1e4058ca97a207">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-204aaad3d485b0a8735e">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c6eb62250443fe5a7269"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c6eb62250443fe5a7269`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4319b6deb149dd74744a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4319b6deb149dd74744a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58293225a9d79a7e4f8e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-58293225a9d79a7e4f8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c58c2df04ec189c3bee"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c58c2df04ec189c3bee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f16fdba01efb3cb655fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f16fdba01efb3cb655fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ac521f72324961521d3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8ac521f72324961521d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-046b9cdd42941c94c8a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-046b9cdd42941c94c8a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd7d222e48a4adb7f3c5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dd7d222e48a4adb7f3c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-31a69710ea5226f58568"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-31a69710ea5226f58568`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89e4a44aad7de4acce3f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-89e4a44aad7de4acce3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11040f1e4058ca97a207"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-11040f1e4058ca97a207`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-204aaad3d485b0a8735e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-204aaad3d485b0a8735e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
