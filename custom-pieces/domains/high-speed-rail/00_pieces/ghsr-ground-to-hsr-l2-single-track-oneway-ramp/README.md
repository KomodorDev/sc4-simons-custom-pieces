<a id="one-way-ghsr-to-hsr-l2-ramp"></a>

# GHSR Ground (1 m) → HSR Level 2 (15.5 m) — Single-Track One-Way Ramp

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `interchange-oneway-grade-ground-to-hsr` → `ghsr-ground-to-hsr-l2-single-track-oneway-ramp`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

GHSR Ground (1 m) → HSR Level 2 (15.5 m) — Single-Track One-Way Ramp. Fixed click-to-place piece in a 1 by 8 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending.

Exact reusable identifier: `ghsr-ground-to-hsr-l2-single-track-oneway-ramp`.

Footprint: **1 × 8 tiles**. Exact menu name: **GHSR Ground (1 m) → HSR Level 2 (15.5 m) — Single-Track One-Way Ramp**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![GHSR Ground (1 m) → HSR Level 2 (15.5 m) — Single-Track One-Way Ramp](previews/preview.png)

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
| `in` | ghsr / 7 / primary | in | [0.0, -120.0, 1.0]; [0.0, 1.0]; 0.0 | `path-interface-459a3d38a8ff1501aa51` |
| `out` | hsr / 7 / primary | out | [0.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-ac60d237d23f01143255` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| ghsr+hsr | `in` → `out` | primary |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/ghsr-ground-to-hsr-l2-single-track-oneway-ramp/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/ghsr-ground-to-hsr-l2-single-track-oneway-ramp/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-ceacdcded600fb2be244">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-ceacdcded600fb2be244"></a>

**General: unverified** — `software_resources-ceacdcded600fb2be244`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-ceacdcded600fb2be244">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-ceacdcded600fb2be244"></a>

**General: unverified** — `software_connectivity-ceacdcded600fb2be244`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-oneway-grade-ground-to-hsr:canonical-southeast | <a href="#case-preview_review-e217c95c2190699f99f2">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-oneway-grade-ground-to-hsr:canonical-southeast</summary>

<a id="case-preview_review-e217c95c2190699f99f2"></a>

**General: unverified** — `preview_review-e217c95c2190699f99f2`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-oneway-grade-ground-to-hsr:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-23431c52ee9094d6aa78">[ ] unverified</a> | <a href="#case-in_game_render-d913fbf698e835d6f131">[ ] unverified</a> | <a href="#case-in_game_render-c84c2ba7ae1c8f50896e">[ ] unverified</a> | <a href="#case-in_game_render-cebd7d15dd789defe13d">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-23431c52ee9094d6aa78"></a>

**0° CCW: unverified** — `in_game_render-23431c52ee9094d6aa78`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-d913fbf698e835d6f131"></a>

**90° CCW: unverified** — `in_game_render-d913fbf698e835d6f131`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-c84c2ba7ae1c8f50896e"></a>

**180° CCW: unverified** — `in_game_render-c84c2ba7ae1c8f50896e`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-cebd7d15dd789defe13d"></a>

**270° CCW: unverified** — `in_game_render-cebd7d15dd789defe13d`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-23431c52ee9094d6aa78">[ ] unverified</a> | <a href="#case-in_game_placement-d913fbf698e835d6f131">[ ] unverified</a> | <a href="#case-in_game_placement-c84c2ba7ae1c8f50896e">[ ] unverified</a> | <a href="#case-in_game_placement-cebd7d15dd789defe13d">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-23431c52ee9094d6aa78"></a>

**0° CCW: unverified** — `in_game_placement-23431c52ee9094d6aa78`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-d913fbf698e835d6f131"></a>

**90° CCW: unverified** — `in_game_placement-d913fbf698e835d6f131`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-c84c2ba7ae1c8f50896e"></a>

**180° CCW: unverified** — `in_game_placement-c84c2ba7ae1c8f50896e`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-cebd7d15dd789defe13d"></a>

**270° CCW: unverified** — `in_game_placement-cebd7d15dd789defe13d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-23431c52ee9094d6aa78">[ ] unverified</a> | <a href="#case-in_game_demolition-d913fbf698e835d6f131">[ ] unverified</a> | <a href="#case-in_game_demolition-c84c2ba7ae1c8f50896e">[ ] unverified</a> | <a href="#case-in_game_demolition-cebd7d15dd789defe13d">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-23431c52ee9094d6aa78"></a>

**0° CCW: unverified** — `in_game_demolition-23431c52ee9094d6aa78`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-d913fbf698e835d6f131"></a>

**90° CCW: unverified** — `in_game_demolition-d913fbf698e835d6f131`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-c84c2ba7ae1c8f50896e"></a>

**180° CCW: unverified** — `in_game_demolition-c84c2ba7ae1c8f50896e`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-cebd7d15dd789defe13d"></a>

**270° CCW: unverified** — `in_game_demolition-cebd7d15dd789defe13d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-23431c52ee9094d6aa78">[ ] unverified</a> | <a href="#case-in_game_save_reload-d913fbf698e835d6f131">[ ] unverified</a> | <a href="#case-in_game_save_reload-c84c2ba7ae1c8f50896e">[ ] unverified</a> | <a href="#case-in_game_save_reload-cebd7d15dd789defe13d">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-23431c52ee9094d6aa78"></a>

**0° CCW: unverified** — `in_game_save_reload-23431c52ee9094d6aa78`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-d913fbf698e835d6f131"></a>

**90° CCW: unverified** — `in_game_save_reload-d913fbf698e835d6f131`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-c84c2ba7ae1c8f50896e"></a>

**180° CCW: unverified** — `in_game_save_reload-c84c2ba7ae1c8f50896e`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-cebd7d15dd789defe13d"></a>

**270° CCW: unverified** — `in_game_save_reload-cebd7d15dd789defe13d`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr+hsr — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr+hsr; role: primary; journey: 7:in>out; entry: in; exit: out | — | <a href="#case-in_game_journey-cc1e3b6f824a7aaef88e">[ ] unverified</a> | <a href="#case-in_game_journey-0c22ee87d4b06af495c4">[ ] unverified</a> | <a href="#case-in_game_journey-de12d6937433d1239db1">[ ] unverified</a> | <a href="#case-in_game_journey-7e3f9d8ce4e99fc2c381">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr+hsr; role: primary; journey: 7:in>out; entry: in; exit: out</summary>

<a id="case-in_game_journey-cc1e3b6f824a7aaef88e"></a>

**0° CCW: unverified** — `in_game_journey-cc1e3b6f824a7aaef88e`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr+hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-0c22ee87d4b06af495c4"></a>

**90° CCW: unverified** — `in_game_journey-0c22ee87d4b06af495c4`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr+hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-de12d6937433d1239db1"></a>

**180° CCW: unverified** — `in_game_journey-de12d6937433d1239db1`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr+hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

<a id="case-in_game_journey-7e3f9d8ce4e99fc2c381"></a>

**270° CCW: unverified** — `in_game_journey-7e3f9d8ce4e99fc2c381`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr+hsr; role: primary; journey: 7:in>out; entry: in; exit: out.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
