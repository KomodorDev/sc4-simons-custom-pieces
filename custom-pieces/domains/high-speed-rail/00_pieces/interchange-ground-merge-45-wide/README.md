# GHSR Merge 45 Degree Wide

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

GHSR Merge 45 Degree Wide. Fixed click-to-place piece in a 6 by 9 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `interchange-ground-merge-45-wide`.

Footprint: **6 × 9 tiles**. Exact menu name: **GHSR Merge 45 Degree Wide**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![GHSR Merge 45 Degree Wide](previews/preview.png)

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

Generated from [connections.json](connections.json). Coordinates are canonical east, north and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.json) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sout` | ghsr / 7 / primary | out | [-2.0, -104.0, 1.0]; [0.0, -1.0]; 0.0 | `path-interface-c78c5ac4b558d84b46f2` |
| `Nin` | ghsr / 7 / primary | in | [-2.0, 8.0, 1.0]; [0.0, -1.0]; 0.0 | `path-interface-c78c5ac4b558d84b46f2` |
| `Sin` | ghsr / 7 / primary | in | [2.0, -104.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-fab587419de6b5848d74` |
| `Nout` | ghsr / 7 / primary | out | [2.0, 8.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-fab587419de6b5848d74` |
| `Bin` | ghsr / 7 / primary | in | [88.0, -128.0, 1.0]; [-0.7071067811865475, 0.7071067811865475]; 0.0 | `path-interface-6c94c39b4abd67a7479e` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| ghsr | `Nin` → `Sout` | primary |
| ghsr | `Sin` → `Nout` | primary |
| ghsr | `Bin` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| ghsr / `Nin` | ghsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Sin` | ghsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Bin` | ghsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-ground-merge-45-wide/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-ground-merge-45-wide/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-f724a3c2b304a0007d54">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-f724a3c2b304a0007d54"></a>

**General: unverified** — `software_resources-f724a3c2b304a0007d54`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-f724a3c2b304a0007d54">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-f724a3c2b304a0007d54"></a>

**General: unverified** — `software_connectivity-f724a3c2b304a0007d54`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-ground-merge-45-wide:canonical-southeast | <a href="#case-preview_review-09298a8f4edf37c7a0ca">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-ground-merge-45-wide:canonical-southeast</summary>

<a id="case-preview_review-09298a8f4edf37c7a0ca"></a>

**General: unverified** — `preview_review-09298a8f4edf37c7a0ca`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-ground-merge-45-wide:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-ba76969d5adab5f81e76">[ ] unverified</a> | <a href="#case-in_game_render-1ada711132527d7b4a1f">[ ] unverified</a> | <a href="#case-in_game_render-a072d4af8eaad2fe301d">[ ] unverified</a> | <a href="#case-in_game_render-8f12eac7f49b314ee086">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-ba76969d5adab5f81e76"></a>

**0° CCW: unverified** — `in_game_render-ba76969d5adab5f81e76`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1ada711132527d7b4a1f"></a>

**90° CCW: unverified** — `in_game_render-1ada711132527d7b4a1f`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a072d4af8eaad2fe301d"></a>

**180° CCW: unverified** — `in_game_render-a072d4af8eaad2fe301d`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8f12eac7f49b314ee086"></a>

**270° CCW: unverified** — `in_game_render-8f12eac7f49b314ee086`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-ba76969d5adab5f81e76">[ ] unverified</a> | <a href="#case-in_game_placement-1ada711132527d7b4a1f">[ ] unverified</a> | <a href="#case-in_game_placement-a072d4af8eaad2fe301d">[ ] unverified</a> | <a href="#case-in_game_placement-8f12eac7f49b314ee086">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-ba76969d5adab5f81e76"></a>

**0° CCW: unverified** — `in_game_placement-ba76969d5adab5f81e76`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1ada711132527d7b4a1f"></a>

**90° CCW: unverified** — `in_game_placement-1ada711132527d7b4a1f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a072d4af8eaad2fe301d"></a>

**180° CCW: unverified** — `in_game_placement-a072d4af8eaad2fe301d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8f12eac7f49b314ee086"></a>

**270° CCW: unverified** — `in_game_placement-8f12eac7f49b314ee086`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-ba76969d5adab5f81e76">[ ] unverified</a> | <a href="#case-in_game_demolition-1ada711132527d7b4a1f">[ ] unverified</a> | <a href="#case-in_game_demolition-a072d4af8eaad2fe301d">[ ] unverified</a> | <a href="#case-in_game_demolition-8f12eac7f49b314ee086">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-ba76969d5adab5f81e76"></a>

**0° CCW: unverified** — `in_game_demolition-ba76969d5adab5f81e76`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1ada711132527d7b4a1f"></a>

**90° CCW: unverified** — `in_game_demolition-1ada711132527d7b4a1f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a072d4af8eaad2fe301d"></a>

**180° CCW: unverified** — `in_game_demolition-a072d4af8eaad2fe301d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8f12eac7f49b314ee086"></a>

**270° CCW: unverified** — `in_game_demolition-8f12eac7f49b314ee086`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-ba76969d5adab5f81e76">[ ] unverified</a> | <a href="#case-in_game_save_reload-1ada711132527d7b4a1f">[ ] unverified</a> | <a href="#case-in_game_save_reload-a072d4af8eaad2fe301d">[ ] unverified</a> | <a href="#case-in_game_save_reload-8f12eac7f49b314ee086">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-ba76969d5adab5f81e76"></a>

**0° CCW: unverified** — `in_game_save_reload-ba76969d5adab5f81e76`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1ada711132527d7b4a1f"></a>

**90° CCW: unverified** — `in_game_save_reload-1ada711132527d7b4a1f`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a072d4af8eaad2fe301d"></a>

**180° CCW: unverified** — `in_game_save_reload-a072d4af8eaad2fe301d`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8f12eac7f49b314ee086"></a>

**270° CCW: unverified** — `in_game_save_reload-8f12eac7f49b314ee086`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-aa99153b4de89a6f5fba">[ ] unverified</a> | <a href="#case-in_game_journey-8fb4199d3ae082ca19d9">[ ] unverified</a> | <a href="#case-in_game_journey-abb2883246470f981e4a">[ ] unverified</a> | <a href="#case-in_game_journey-5b04946ca1fe5338b49e">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-994ce250b32efd439998">[ ] unverified</a> | <a href="#case-in_game_journey-47bb5b4662d56ba9870e">[ ] unverified</a> | <a href="#case-in_game_journey-4ffa06406a0158d1acef">[ ] unverified</a> | <a href="#case-in_game_journey-89f5b99d7ad977605be6">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout | — | <a href="#case-in_game_journey-fbdd31967c763af2781b">[ ] unverified</a> | <a href="#case-in_game_journey-c7ef22bd8dd9543f0240">[ ] unverified</a> | <a href="#case-in_game_journey-dfb621c8e9e823f7a5ff">[ ] unverified</a> | <a href="#case-in_game_journey-845be83fa46683915e60">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-aa99153b4de89a6f5fba"></a>

**0° CCW: unverified** — `in_game_journey-aa99153b4de89a6f5fba`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-8fb4199d3ae082ca19d9"></a>

**90° CCW: unverified** — `in_game_journey-8fb4199d3ae082ca19d9`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-abb2883246470f981e4a"></a>

**180° CCW: unverified** — `in_game_journey-abb2883246470f981e4a`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-5b04946ca1fe5338b49e"></a>

**270° CCW: unverified** — `in_game_journey-5b04946ca1fe5338b49e`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-994ce250b32efd439998"></a>

**0° CCW: unverified** — `in_game_journey-994ce250b32efd439998`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-47bb5b4662d56ba9870e"></a>

**90° CCW: unverified** — `in_game_journey-47bb5b4662d56ba9870e`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-4ffa06406a0158d1acef"></a>

**180° CCW: unverified** — `in_game_journey-4ffa06406a0158d1acef`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-89f5b99d7ad977605be6"></a>

**270° CCW: unverified** — `in_game_journey-89f5b99d7ad977605be6`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout</summary>

<a id="case-in_game_journey-fbdd31967c763af2781b"></a>

**0° CCW: unverified** — `in_game_journey-fbdd31967c763af2781b`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-c7ef22bd8dd9543f0240"></a>

**90° CCW: unverified** — `in_game_journey-c7ef22bd8dd9543f0240`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-dfb621c8e9e823f7a5ff"></a>

**180° CCW: unverified** — `in_game_journey-dfb621c8e9e823f7a5ff`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-845be83fa46683915e60"></a>

**270° CCW: unverified** — `in_game_journey-845be83fa46683915e60`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → ghsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a294ff5ba2348ef7d08a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10fabc10cdec2ab34902">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca8e9d00ca3496d66350">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe449ac94a0a2326f76c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3c78b211d477d4a10fe4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14c6b0da0c8e4d037505">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-676dbff9b5a21be6f1d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58768e3cd2dabae88d58">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a58aac218caf6bfd38f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9e4ae3abd0946a1bf07">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74f447748595a49ac45f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51f8c1125416eba7c6ee">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a294ff5ba2348ef7d08a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a294ff5ba2348ef7d08a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10fabc10cdec2ab34902"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-10fabc10cdec2ab34902`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca8e9d00ca3496d66350"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ca8e9d00ca3496d66350`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe449ac94a0a2326f76c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe449ac94a0a2326f76c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3c78b211d477d4a10fe4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3c78b211d477d4a10fe4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14c6b0da0c8e4d037505"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-14c6b0da0c8e4d037505`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-676dbff9b5a21be6f1d4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-676dbff9b5a21be6f1d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58768e3cd2dabae88d58"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-58768e3cd2dabae88d58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a58aac218caf6bfd38f5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a58aac218caf6bfd38f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9e4ae3abd0946a1bf07"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a9e4ae3abd0946a1bf07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74f447748595a49ac45f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-74f447748595a49ac45f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51f8c1125416eba7c6ee"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-51f8c1125416eba7c6ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Bin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
