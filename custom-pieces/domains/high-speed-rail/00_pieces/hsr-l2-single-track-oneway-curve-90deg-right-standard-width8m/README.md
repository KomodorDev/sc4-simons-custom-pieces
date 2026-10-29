<a id="one-way-hsr-l2-standard-90-degree-curve-right"></a>

# HSR Level 2 (15.5 m) — Single-Track One-Way Curve 90° Right — Standard, 8 m Deck Width

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `hsr-component-lower-oneway-curve90-right` → `hsr-l2-single-track-oneway-curve-90deg-right-standard-width8m`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

A centred lower one-way track turns right through 90 degrees with 104 m cardinal displacement, smooth curvature and eight-metre flat collars.

Exact reusable identifier: `hsr-l2-single-track-oneway-curve-90deg-right-standard-width8m`.

Footprint: **7 × 7 tiles**. Exact menu name: **HSR Level 2 (15.5 m) — Single-Track One-Way Curve 90° Right — Standard, 8 m Deck Width**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR Level 2 (15.5 m) — Single-Track One-Way Curve 90° Right — Standard, 8 m Deck Width](previews/preview.png)

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

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sin` | hsr / 7 / primary | in | [0.0, -104.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-ac60d237d23f01143255` |
| `Eout` | hsr / 7 / primary | out | [104.0, 0.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-365752af76285c80cd0b` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Sin` → `Eout` | primary |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-single-track-oneway-curve-90deg-right-standard-width8m/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-single-track-oneway-curve-90deg-right-standard-width8m/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b7afd1073067a15e45ef">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b7afd1073067a15e45ef"></a>

**General: unverified** — `software_resources-b7afd1073067a15e45ef`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b7afd1073067a15e45ef">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b7afd1073067a15e45ef"></a>

**General: unverified** — `software_connectivity-b7afd1073067a15e45ef`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-lower-oneway-curve90-right:canonical-southeast | <a href="#case-preview_review-04e2c8bb6e8d9417b28f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-lower-oneway-curve90-right:canonical-southeast</summary>

<a id="case-preview_review-04e2c8bb6e8d9417b28f"></a>

**General: unverified** — `preview_review-04e2c8bb6e8d9417b28f`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-lower-oneway-curve90-right:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-d023a489c9ab24f243f6">[ ] unverified</a> | <a href="#case-in_game_render-cd6a0716b73d6ba317cd">[ ] unverified</a> | <a href="#case-in_game_render-fb0badf7c585b7167046">[ ] unverified</a> | <a href="#case-in_game_render-c773a09326d64b2d3435">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-d023a489c9ab24f243f6"></a>

**0° CCW: unverified** — `in_game_render-d023a489c9ab24f243f6`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-cd6a0716b73d6ba317cd"></a>

**90° CCW: unverified** — `in_game_render-cd6a0716b73d6ba317cd`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-fb0badf7c585b7167046"></a>

**180° CCW: unverified** — `in_game_render-fb0badf7c585b7167046`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c773a09326d64b2d3435"></a>

**270° CCW: unverified** — `in_game_render-c773a09326d64b2d3435`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-d023a489c9ab24f243f6">[ ] unverified</a> | <a href="#case-in_game_placement-cd6a0716b73d6ba317cd">[ ] unverified</a> | <a href="#case-in_game_placement-fb0badf7c585b7167046">[ ] unverified</a> | <a href="#case-in_game_placement-c773a09326d64b2d3435">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-d023a489c9ab24f243f6"></a>

**0° CCW: unverified** — `in_game_placement-d023a489c9ab24f243f6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-cd6a0716b73d6ba317cd"></a>

**90° CCW: unverified** — `in_game_placement-cd6a0716b73d6ba317cd`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-fb0badf7c585b7167046"></a>

**180° CCW: unverified** — `in_game_placement-fb0badf7c585b7167046`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c773a09326d64b2d3435"></a>

**270° CCW: unverified** — `in_game_placement-c773a09326d64b2d3435`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-d023a489c9ab24f243f6">[ ] unverified</a> | <a href="#case-in_game_demolition-cd6a0716b73d6ba317cd">[ ] unverified</a> | <a href="#case-in_game_demolition-fb0badf7c585b7167046">[ ] unverified</a> | <a href="#case-in_game_demolition-c773a09326d64b2d3435">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-d023a489c9ab24f243f6"></a>

**0° CCW: unverified** — `in_game_demolition-d023a489c9ab24f243f6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-cd6a0716b73d6ba317cd"></a>

**90° CCW: unverified** — `in_game_demolition-cd6a0716b73d6ba317cd`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-fb0badf7c585b7167046"></a>

**180° CCW: unverified** — `in_game_demolition-fb0badf7c585b7167046`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c773a09326d64b2d3435"></a>

**270° CCW: unverified** — `in_game_demolition-c773a09326d64b2d3435`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-d023a489c9ab24f243f6">[ ] unverified</a> | <a href="#case-in_game_save_reload-cd6a0716b73d6ba317cd">[ ] unverified</a> | <a href="#case-in_game_save_reload-fb0badf7c585b7167046">[ ] unverified</a> | <a href="#case-in_game_save_reload-c773a09326d64b2d3435">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-d023a489c9ab24f243f6"></a>

**0° CCW: unverified** — `in_game_save_reload-d023a489c9ab24f243f6`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-cd6a0716b73d6ba317cd"></a>

**90° CCW: unverified** — `in_game_save_reload-cd6a0716b73d6ba317cd`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-fb0badf7c585b7167046"></a>

**180° CCW: unverified** — `in_game_save_reload-fb0badf7c585b7167046`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c773a09326d64b2d3435"></a>

**270° CCW: unverified** — `in_game_save_reload-c773a09326d64b2d3435`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_journey-83c5bc9dd0ca7bf17664">[ ] unverified</a> | <a href="#case-in_game_journey-7860aaa9f63cd94a8724">[ ] unverified</a> | <a href="#case-in_game_journey-f899b068644d728032f0">[ ] unverified</a> | <a href="#case-in_game_journey-1323ce189fa8f6fd4e0c">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_journey-83c5bc9dd0ca7bf17664"></a>

**0° CCW: unverified** — `in_game_journey-83c5bc9dd0ca7bf17664`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-7860aaa9f63cd94a8724"></a>

**90° CCW: unverified** — `in_game_journey-7860aaa9f63cd94a8724`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-f899b068644d728032f0"></a>

**180° CCW: unverified** — `in_game_journey-f899b068644d728032f0`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-1323ce189fa8f6fd4e0c"></a>

**270° CCW: unverified** — `in_game_journey-1323ce189fa8f6fd4e0c`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## Engineering contract

This standard lower one-way 90° curve occupies a 7 × 7 rectangle, with 15 occupied cells and ten mirrored supports. Its cardinal displacement is 104 m, its flat collars are 8 m, and its path height remains 15.5 m. This source defines one-way movement; a physical single track is not inherently one-way in the general connector model.

Use the [independent source contract](../../implementation/scp_hsr/hsr_components_verify.py) and this type's [definition](piece.json) for exact expectations. Shared HSR/GHSR facts remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). These authored notes supplement generated source views; they do not change geometry, reset observations, or establish game operation.
