# GHSR Split 90 Degree Wide

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

GHSR Split 90 Degree Wide. Fixed click-to-place piece in a 6 by 6 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `interchange-ground-split-90-wide`.

Footprint: **6 × 6 tiles**. Exact menu name: **GHSR Split 90 Degree Wide**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![GHSR Split 90 Degree Wide](previews/preview.png)

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
| `Sout` | ghsr / 7 / primary | out | [-2.0, -88.0, 1.0]; [0.0, -1.0]; 0.0 | `path-interface-c78c5ac4b558d84b46f2` |
| `Nin` | ghsr / 7 / primary | in | [-2.0, 8.0, 1.0]; [0.0, -1.0]; 0.0 | `path-interface-c78c5ac4b558d84b46f2` |
| `Sin` | ghsr / 7 / primary | in | [2.0, -88.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-fab587419de6b5848d74` |
| `Nout` | ghsr / 7 / primary | out | [2.0, 8.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-fab587419de6b5848d74` |
| `Bout` | ghsr / 7 / primary | out | [88.0, 0.0, 1.0]; [1.0, 0.0]; 0.0 | `path-interface-ab4e40517da7fa0dbd34` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| ghsr | `Nin` → `Sout` | primary |
| ghsr | `Sin` → `Bout` | primary |
| ghsr | `Sin` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| ghsr / `Nin` | ghsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Nin` | ghsr / `Bout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Sin` | ghsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/interchange-ground-split-90-wide/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/interchange-ground-split-90-wide/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-77f1afe759f3b6613344">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-77f1afe759f3b6613344"></a>

**General: unverified** — `software_resources-77f1afe759f3b6613344`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-77f1afe759f3b6613344">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-77f1afe759f3b6613344"></a>

**General: unverified** — `software_connectivity-77f1afe759f3b6613344`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-ground-split-90-wide:canonical-southeast | <a href="#case-preview_review-57c6fbadda8eed4579af">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-ground-split-90-wide:canonical-southeast</summary>

<a id="case-preview_review-57c6fbadda8eed4579af"></a>

**General: unverified** — `preview_review-57c6fbadda8eed4579af`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-ground-split-90-wide:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-a4ad8302dea1b5e1f97e">[ ] unverified</a> | <a href="#case-in_game_render-88c811d6a4ec36ff20a3">[ ] unverified</a> | <a href="#case-in_game_render-a6f5df96050d45fb22ea">[ ] unverified</a> | <a href="#case-in_game_render-345cd3ce1dcddef0c4fd">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-a4ad8302dea1b5e1f97e"></a>

**0° CCW: unverified** — `in_game_render-a4ad8302dea1b5e1f97e`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-88c811d6a4ec36ff20a3"></a>

**90° CCW: unverified** — `in_game_render-88c811d6a4ec36ff20a3`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-a6f5df96050d45fb22ea"></a>

**180° CCW: unverified** — `in_game_render-a6f5df96050d45fb22ea`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-345cd3ce1dcddef0c4fd"></a>

**270° CCW: unverified** — `in_game_render-345cd3ce1dcddef0c4fd`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-a4ad8302dea1b5e1f97e">[ ] unverified</a> | <a href="#case-in_game_placement-88c811d6a4ec36ff20a3">[ ] unverified</a> | <a href="#case-in_game_placement-a6f5df96050d45fb22ea">[ ] unverified</a> | <a href="#case-in_game_placement-345cd3ce1dcddef0c4fd">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-a4ad8302dea1b5e1f97e"></a>

**0° CCW: unverified** — `in_game_placement-a4ad8302dea1b5e1f97e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-88c811d6a4ec36ff20a3"></a>

**90° CCW: unverified** — `in_game_placement-88c811d6a4ec36ff20a3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-a6f5df96050d45fb22ea"></a>

**180° CCW: unverified** — `in_game_placement-a6f5df96050d45fb22ea`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-345cd3ce1dcddef0c4fd"></a>

**270° CCW: unverified** — `in_game_placement-345cd3ce1dcddef0c4fd`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-a4ad8302dea1b5e1f97e">[ ] unverified</a> | <a href="#case-in_game_demolition-88c811d6a4ec36ff20a3">[ ] unverified</a> | <a href="#case-in_game_demolition-a6f5df96050d45fb22ea">[ ] unverified</a> | <a href="#case-in_game_demolition-345cd3ce1dcddef0c4fd">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-a4ad8302dea1b5e1f97e"></a>

**0° CCW: unverified** — `in_game_demolition-a4ad8302dea1b5e1f97e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-88c811d6a4ec36ff20a3"></a>

**90° CCW: unverified** — `in_game_demolition-88c811d6a4ec36ff20a3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-a6f5df96050d45fb22ea"></a>

**180° CCW: unverified** — `in_game_demolition-a6f5df96050d45fb22ea`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-345cd3ce1dcddef0c4fd"></a>

**270° CCW: unverified** — `in_game_demolition-345cd3ce1dcddef0c4fd`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-a4ad8302dea1b5e1f97e">[ ] unverified</a> | <a href="#case-in_game_save_reload-88c811d6a4ec36ff20a3">[ ] unverified</a> | <a href="#case-in_game_save_reload-a6f5df96050d45fb22ea">[ ] unverified</a> | <a href="#case-in_game_save_reload-345cd3ce1dcddef0c4fd">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-a4ad8302dea1b5e1f97e"></a>

**0° CCW: unverified** — `in_game_save_reload-a4ad8302dea1b5e1f97e`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-88c811d6a4ec36ff20a3"></a>

**90° CCW: unverified** — `in_game_save_reload-88c811d6a4ec36ff20a3`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-a6f5df96050d45fb22ea"></a>

**180° CCW: unverified** — `in_game_save_reload-a6f5df96050d45fb22ea`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-345cd3ce1dcddef0c4fd"></a>

**270° CCW: unverified** — `in_game_save_reload-345cd3ce1dcddef0c4fd`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-b2854aa51ebb0224d0ef">[ ] unverified</a> | <a href="#case-in_game_journey-1ee77662da71f0522965">[ ] unverified</a> | <a href="#case-in_game_journey-c08bd2fc7b2da4586866">[ ] unverified</a> | <a href="#case-in_game_journey-fa46fc316bf2ad22c477">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout | — | <a href="#case-in_game_journey-6f7c73edc1b09acc3813">[ ] unverified</a> | <a href="#case-in_game_journey-d79786d73a98e99f396f">[ ] unverified</a> | <a href="#case-in_game_journey-3089c21aedb83890806d">[ ] unverified</a> | <a href="#case-in_game_journey-9b8c95f661f5c7aff7fd">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-e179d7cd35581effb914">[ ] unverified</a> | <a href="#case-in_game_journey-4e33ef68835547fd4d62">[ ] unverified</a> | <a href="#case-in_game_journey-ffb09a8b7ec36e5221df">[ ] unverified</a> | <a href="#case-in_game_journey-2027cde3dcd34832ad71">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-b2854aa51ebb0224d0ef"></a>

**0° CCW: unverified** — `in_game_journey-b2854aa51ebb0224d0ef`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-1ee77662da71f0522965"></a>

**90° CCW: unverified** — `in_game_journey-1ee77662da71f0522965`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-c08bd2fc7b2da4586866"></a>

**180° CCW: unverified** — `in_game_journey-c08bd2fc7b2da4586866`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-fa46fc316bf2ad22c477"></a>

**270° CCW: unverified** — `in_game_journey-fa46fc316bf2ad22c477`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout</summary>

<a id="case-in_game_journey-6f7c73edc1b09acc3813"></a>

**0° CCW: unverified** — `in_game_journey-6f7c73edc1b09acc3813`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-d79786d73a98e99f396f"></a>

**90° CCW: unverified** — `in_game_journey-d79786d73a98e99f396f`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-3089c21aedb83890806d"></a>

**180° CCW: unverified** — `in_game_journey-3089c21aedb83890806d`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-9b8c95f661f5c7aff7fd"></a>

**270° CCW: unverified** — `in_game_journey-9b8c95f661f5c7aff7fd`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-e179d7cd35581effb914"></a>

**0° CCW: unverified** — `in_game_journey-e179d7cd35581effb914`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-4e33ef68835547fd4d62"></a>

**90° CCW: unverified** — `in_game_journey-4e33ef68835547fd4d62`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-ffb09a8b7ec36e5221df"></a>

**180° CCW: unverified** — `in_game_journey-ffb09a8b7ec36e5221df`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-2027cde3dcd34832ad71"></a>

**270° CCW: unverified** — `in_game_journey-2027cde3dcd34832ad71`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → ghsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1c707ce6e23170559cc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-538924314439ef6f0d81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73b18ad952108d544713">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9754fe3bf750d6201c74">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eb97725367cf163d6e63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c05e88a510a0d101e22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5938eafae2a9e9102bbe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a172013c4ea8385d533">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-330c3ec18c9cafad1f4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afd78fcf479781c10d5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17e8f912e3cbb536a7c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4fe391601d284eb2e09f">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1c707ce6e23170559cc4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1c707ce6e23170559cc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-538924314439ef6f0d81"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-538924314439ef6f0d81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73b18ad952108d544713"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-73b18ad952108d544713`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9754fe3bf750d6201c74"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9754fe3bf750d6201c74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eb97725367cf163d6e63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eb97725367cf163d6e63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c05e88a510a0d101e22"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1c05e88a510a0d101e22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5938eafae2a9e9102bbe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5938eafae2a9e9102bbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a172013c4ea8385d533"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8a172013c4ea8385d533`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-330c3ec18c9cafad1f4b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-330c3ec18c9cafad1f4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afd78fcf479781c10d5e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-afd78fcf479781c10d5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17e8f912e3cbb536a7c5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-17e8f912e3cbb536a7c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4fe391601d284eb2e09f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4fe391601d284eb2e09f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
