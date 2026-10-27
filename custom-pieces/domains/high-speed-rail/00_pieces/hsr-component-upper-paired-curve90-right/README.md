# HSR L4 Two-Track 90 Degree Curve Right

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

Close opposite-direction tracks on one native-width upper 90 degree slab, with flat cardinal connection collars.

Exact reusable identifier: `hsr-component-upper-paired-curve90-right`.

Footprint: **7 × 7 tiles**. Exact menu name: **HSR L4 Two-Track 90 Degree Curve Right**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR L4 Two-Track 90 Degree Curve Right](previews/preview.png)

<!-- END PIECE OVERVIEW -->

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
| `Sout` | hsr / 7 / primary | out | [-2.0, -104.0, 30.5]; [0.0, -1.0]; 0.0 | `path-interface-ce3ccdc10e5e243d11ae` |
| `Sin` | hsr / 7 / primary | in | [2.0, -104.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-9b897a8bacb659f807fe` |
| `Eout` | hsr / 7 / primary | out | [104.0, -2.0, 30.5]; [1.0, 0.0]; 0.0 | `path-interface-ce3ccdc10e5e243d11ae` |
| `Ein` | hsr / 7 / primary | in | [104.0, 2.0, 30.5]; [-1.0, -0.0]; 0.0 | `path-interface-ce3ccdc10e5e243d11ae` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Sin` → `Eout` | primary |
| hsr | `Ein` → `Sout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Sin` | hsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-upper-paired-curve90-right/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-upper-paired-curve90-right/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-178900e17deb5321a950">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-178900e17deb5321a950"></a>

**General: unverified** — `software_resources-178900e17deb5321a950`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-178900e17deb5321a950">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-178900e17deb5321a950"></a>

**General: unverified** — `software_connectivity-178900e17deb5321a950`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-upper-paired-curve90-right:canonical-southeast | <a href="#case-preview_review-ff2be2842d0a5e55d639">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-upper-paired-curve90-right:canonical-southeast</summary>

<a id="case-preview_review-ff2be2842d0a5e55d639"></a>

**General: unverified** — `preview_review-ff2be2842d0a5e55d639`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-upper-paired-curve90-right:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-bbdf11c78976adc03b3e">[ ] unverified</a> | <a href="#case-in_game_render-7d0cf1ae4bc8b78df7b0">[ ] unverified</a> | <a href="#case-in_game_render-3c3201a436411e65df06">[ ] unverified</a> | <a href="#case-in_game_render-8a711a2762ef42ae87fd">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-bbdf11c78976adc03b3e"></a>

**0° CCW: unverified** — `in_game_render-bbdf11c78976adc03b3e`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7d0cf1ae4bc8b78df7b0"></a>

**90° CCW: unverified** — `in_game_render-7d0cf1ae4bc8b78df7b0`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3c3201a436411e65df06"></a>

**180° CCW: unverified** — `in_game_render-3c3201a436411e65df06`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8a711a2762ef42ae87fd"></a>

**270° CCW: unverified** — `in_game_render-8a711a2762ef42ae87fd`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-bbdf11c78976adc03b3e">[ ] unverified</a> | <a href="#case-in_game_placement-7d0cf1ae4bc8b78df7b0">[ ] unverified</a> | <a href="#case-in_game_placement-3c3201a436411e65df06">[ ] unverified</a> | <a href="#case-in_game_placement-8a711a2762ef42ae87fd">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-bbdf11c78976adc03b3e"></a>

**0° CCW: unverified** — `in_game_placement-bbdf11c78976adc03b3e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7d0cf1ae4bc8b78df7b0"></a>

**90° CCW: unverified** — `in_game_placement-7d0cf1ae4bc8b78df7b0`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3c3201a436411e65df06"></a>

**180° CCW: unverified** — `in_game_placement-3c3201a436411e65df06`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8a711a2762ef42ae87fd"></a>

**270° CCW: unverified** — `in_game_placement-8a711a2762ef42ae87fd`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-bbdf11c78976adc03b3e">[ ] unverified</a> | <a href="#case-in_game_demolition-7d0cf1ae4bc8b78df7b0">[ ] unverified</a> | <a href="#case-in_game_demolition-3c3201a436411e65df06">[ ] unverified</a> | <a href="#case-in_game_demolition-8a711a2762ef42ae87fd">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-bbdf11c78976adc03b3e"></a>

**0° CCW: unverified** — `in_game_demolition-bbdf11c78976adc03b3e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7d0cf1ae4bc8b78df7b0"></a>

**90° CCW: unverified** — `in_game_demolition-7d0cf1ae4bc8b78df7b0`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3c3201a436411e65df06"></a>

**180° CCW: unverified** — `in_game_demolition-3c3201a436411e65df06`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8a711a2762ef42ae87fd"></a>

**270° CCW: unverified** — `in_game_demolition-8a711a2762ef42ae87fd`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-bbdf11c78976adc03b3e">[ ] unverified</a> | <a href="#case-in_game_save_reload-7d0cf1ae4bc8b78df7b0">[ ] unverified</a> | <a href="#case-in_game_save_reload-3c3201a436411e65df06">[ ] unverified</a> | <a href="#case-in_game_save_reload-8a711a2762ef42ae87fd">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-bbdf11c78976adc03b3e"></a>

**0° CCW: unverified** — `in_game_save_reload-bbdf11c78976adc03b3e`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7d0cf1ae4bc8b78df7b0"></a>

**90° CCW: unverified** — `in_game_save_reload-7d0cf1ae4bc8b78df7b0`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3c3201a436411e65df06"></a>

**180° CCW: unverified** — `in_game_save_reload-3c3201a436411e65df06`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8a711a2762ef42ae87fd"></a>

**270° CCW: unverified** — `in_game_save_reload-8a711a2762ef42ae87fd`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_journey-d814c7168f1a22e00c79">[ ] unverified</a> | <a href="#case-in_game_journey-27408fe05e655efd195e">[ ] unverified</a> | <a href="#case-in_game_journey-a33d078dd5fb7b94bdc2">[ ] unverified</a> | <a href="#case-in_game_journey-8a22d3e6dbe518861eb9">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout | — | <a href="#case-in_game_journey-73d0a9bc9f5d0aee2994">[ ] unverified</a> | <a href="#case-in_game_journey-bdcd899bfe580e60b4d9">[ ] unverified</a> | <a href="#case-in_game_journey-8427d59089170d6a0a49">[ ] unverified</a> | <a href="#case-in_game_journey-66e4da5d5f13622a92e5">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_journey-d814c7168f1a22e00c79"></a>

**0° CCW: unverified** — `in_game_journey-d814c7168f1a22e00c79`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-27408fe05e655efd195e"></a>

**90° CCW: unverified** — `in_game_journey-27408fe05e655efd195e`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-a33d078dd5fb7b94bdc2"></a>

**180° CCW: unverified** — `in_game_journey-a33d078dd5fb7b94bdc2`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-8a22d3e6dbe518861eb9"></a>

**270° CCW: unverified** — `in_game_journey-8a22d3e6dbe518861eb9`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout</summary>

<a id="case-in_game_journey-73d0a9bc9f5d0aee2994"></a>

**0° CCW: unverified** — `in_game_journey-73d0a9bc9f5d0aee2994`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-bdcd899bfe580e60b4d9"></a>

**90° CCW: unverified** — `in_game_journey-bdcd899bfe580e60b4d9`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-8427d59089170d6a0a49"></a>

**180° CCW: unverified** — `in_game_journey-8427d59089170d6a0a49`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-66e4da5d5f13622a92e5"></a>

**270° CCW: unverified** — `in_game_journey-66e4da5d5f13622a92e5`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3eda211cc0d1455e8872">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-485e0260c7affa6e0511">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e27ae58aec2bb554170c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e774d8e0ffc6e7a0c99">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-717c977b6e8947166b58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-213d6e9933c32b4d2af2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19fd0c5a1b2f7473f9a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dde6f8fec103aac805c8">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3eda211cc0d1455e8872"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3eda211cc0d1455e8872`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-485e0260c7affa6e0511"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-485e0260c7affa6e0511`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e27ae58aec2bb554170c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e27ae58aec2bb554170c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e774d8e0ffc6e7a0c99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3e774d8e0ffc6e7a0c99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-717c977b6e8947166b58"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-717c977b6e8947166b58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-213d6e9933c32b4d2af2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-213d6e9933c32b4d2af2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19fd0c5a1b2f7473f9a6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-19fd0c5a1b2f7473f9a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dde6f8fec103aac805c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dde6f8fec103aac805c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## Engineering contract

This paired quarter-turn reserves a complete 7 × 7 rectangle and 20 occupied cells, including seven structural cells. Its paired deck is one 15 m physical sheet, rather than two overlapping single decks. Reserve the full mitered slab footprint, rather than only cells crossed by PATH centrelines. Structural cells have the audited native empty PATH, a declared top-level `structural_cells` entry, and independent construction checks. The sampled minimum radius exceeds 53 m, and the fixed cardinal collars are 8 m long.

Use the [independent source contract](../../implementation/scp_hsr/hsr_components_verify.py) and this type's [definition](piece.json) for exact expectations. Shared HSR/GHSR facts remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). These authored notes supplement generated source views; they do not change geometry, reset observations, or establish game operation.
