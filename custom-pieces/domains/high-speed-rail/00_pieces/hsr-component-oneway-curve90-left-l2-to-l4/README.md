# One-Way HSR 90 Degree Left L2 to L4 Ramp

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

One centred track turns 90 degrees while changing height, with flat matching-level cardinal ends.

Exact reusable identifier: `hsr-component-oneway-curve90-left-l2-to-l4`.

Footprint: **7 × 7 tiles**. Exact menu name: **One-Way HSR 90 Degree Left L2 to L4 Ramp**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![One-Way HSR 90 Degree Left L2 to L4 Ramp](previews/preview.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/1 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Directed journeys: 0/4 applicable cases passed; 0 failed, 0 stale.

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
| `Wout` | hsr / 7 / primary | out | [-8.0, 0.0, 30.5]; [-1.0, 0.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Sin` | hsr / 7 / primary | in | [96.0, -104.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-ac60d237d23f01143255` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Sin` → `Wout` | primary |

### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 23, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-oneway-curve90-left-l2-to-l4/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-oneway-curve90-left-l2-to-l4/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-6c38b9b869ab5513b545">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-6c38b9b869ab5513b545"></a>

**General: unverified** — `software_resources-6c38b9b869ab5513b545`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-6c38b9b869ab5513b545">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-6c38b9b869ab5513b545"></a>

**General: unverified** — `software_connectivity-6c38b9b869ab5513b545`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-oneway-curve90-left-l2-to-l4:canonical-southeast | <a href="#case-preview_review-92149b919e857f9f2a6b">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-oneway-curve90-left-l2-to-l4:canonical-southeast</summary>

<a id="case-preview_review-92149b919e857f9f2a6b"></a>

**General: unverified** — `preview_review-92149b919e857f9f2a6b`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-oneway-curve90-left-l2-to-l4:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-b869e9f29821b1114b28">[ ] unverified</a> | <a href="#case-in_game_render-2a831add414a66c36d92">[ ] unverified</a> | <a href="#case-in_game_render-723f66d9864af7922402">[ ] unverified</a> | <a href="#case-in_game_render-d501ea8ba14a01d6648c">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-b869e9f29821b1114b28"></a>

**0° CCW: unverified** — `in_game_render-b869e9f29821b1114b28`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2a831add414a66c36d92"></a>

**90° CCW: unverified** — `in_game_render-2a831add414a66c36d92`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-723f66d9864af7922402"></a>

**180° CCW: unverified** — `in_game_render-723f66d9864af7922402`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-d501ea8ba14a01d6648c"></a>

**270° CCW: unverified** — `in_game_render-d501ea8ba14a01d6648c`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-b869e9f29821b1114b28">[ ] unverified</a> | <a href="#case-in_game_placement-2a831add414a66c36d92">[ ] unverified</a> | <a href="#case-in_game_placement-723f66d9864af7922402">[ ] unverified</a> | <a href="#case-in_game_placement-d501ea8ba14a01d6648c">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-b869e9f29821b1114b28"></a>

**0° CCW: unverified** — `in_game_placement-b869e9f29821b1114b28`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2a831add414a66c36d92"></a>

**90° CCW: unverified** — `in_game_placement-2a831add414a66c36d92`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-723f66d9864af7922402"></a>

**180° CCW: unverified** — `in_game_placement-723f66d9864af7922402`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-d501ea8ba14a01d6648c"></a>

**270° CCW: unverified** — `in_game_placement-d501ea8ba14a01d6648c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-b869e9f29821b1114b28">[ ] unverified</a> | <a href="#case-in_game_demolition-2a831add414a66c36d92">[ ] unverified</a> | <a href="#case-in_game_demolition-723f66d9864af7922402">[ ] unverified</a> | <a href="#case-in_game_demolition-d501ea8ba14a01d6648c">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-b869e9f29821b1114b28"></a>

**0° CCW: unverified** — `in_game_demolition-b869e9f29821b1114b28`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2a831add414a66c36d92"></a>

**90° CCW: unverified** — `in_game_demolition-2a831add414a66c36d92`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-723f66d9864af7922402"></a>

**180° CCW: unverified** — `in_game_demolition-723f66d9864af7922402`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-d501ea8ba14a01d6648c"></a>

**270° CCW: unverified** — `in_game_demolition-d501ea8ba14a01d6648c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-b869e9f29821b1114b28">[ ] unverified</a> | <a href="#case-in_game_save_reload-2a831add414a66c36d92">[ ] unverified</a> | <a href="#case-in_game_save_reload-723f66d9864af7922402">[ ] unverified</a> | <a href="#case-in_game_save_reload-d501ea8ba14a01d6648c">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-b869e9f29821b1114b28"></a>

**0° CCW: unverified** — `in_game_save_reload-b869e9f29821b1114b28`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2a831add414a66c36d92"></a>

**90° CCW: unverified** — `in_game_save_reload-2a831add414a66c36d92`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-723f66d9864af7922402"></a>

**180° CCW: unverified** — `in_game_save_reload-723f66d9864af7922402`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-d501ea8ba14a01d6648c"></a>

**270° CCW: unverified** — `in_game_save_reload-d501ea8ba14a01d6648c`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Wout; entry: Sin; exit: Wout | — | <a href="#case-in_game_journey-705d6b98de14891b7c5e">[ ] unverified</a> | <a href="#case-in_game_journey-25a7919c59819c25b859">[ ] unverified</a> | <a href="#case-in_game_journey-f9806b98f12511e9c4f1">[ ] unverified</a> | <a href="#case-in_game_journey-fb1046a454621017de42">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Wout; entry: Sin; exit: Wout</summary>

<a id="case-in_game_journey-705d6b98de14891b7c5e"></a>

**0° CCW: unverified** — `in_game_journey-705d6b98de14891b7c5e`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Wout; entry: Sin; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-25a7919c59819c25b859"></a>

**90° CCW: unverified** — `in_game_journey-25a7919c59819c25b859`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Wout; entry: Sin; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-f9806b98f12511e9c4f1"></a>

**180° CCW: unverified** — `in_game_journey-f9806b98f12511e9c4f1`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Wout; entry: Sin; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-fb1046a454621017de42"></a>

**270° CCW: unverified** — `in_game_journey-fb1046a454621017de42`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Wout; entry: Sin; exit: Wout.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## Engineering contract

This single curved height ramp reserves a complete 7 × 7 rectangle and 15 occupied cells, including two structural cells. Its left/right and climb/descent identities remain separately authored. Reserve the full mitered slab footprint, rather than only cells crossed by PATH centrelines. Structural cells have the audited native empty PATH, a declared top-level `structural_cells` entry, and independent construction checks. The sampled minimum radius exceeds 53 m, and the fixed cardinal collars are 8 m long.

Use the [independent source contract](../../implementation/scp_hsr/hsr_components_verify.py) and this type's [definition](piece.json) for exact expectations. Shared HSR/GHSR facts remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). These authored notes supplement generated source views; they do not change geometry, reset observations, or establish game operation.
