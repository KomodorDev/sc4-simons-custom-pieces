<a id="rail-l4-merge-45-degree-compact"></a>

# HSR Level 4 (30.5 m) — Merge 45° Right to Single-Track One-Way Mainline — Compact

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `interchange-l4-merge-45-compact` → `hsr-l4-single-track-oneway-merge-45deg-right-compact`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

HSR Level 4 (30.5 m) — Merge 45° Right to Single-Track One-Way Mainline — Compact. Fixed click-to-place piece in a 3 by 4 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The L4 mainline and branch are both one-way single tracks.

Exact reusable identifier: `hsr-l4-single-track-oneway-merge-45deg-right-compact`.

Footprint: **3 × 4 tiles**. Exact menu name: **HSR Level 4 (30.5 m) — Merge 45° Right to Single-Track One-Way Mainline — Compact**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR Level 4 (30.5 m) — Merge 45° Right to Single-Track One-Way Mainline — Compact](previews/preview.png)

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

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `Sin` | hsr / 7 / primary | in | [0.0, -56.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Nout` | hsr / 7 / primary | out | [0.0, 8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Bin` | hsr / 7 / primary | in | [40.0, -48.0, 30.5]; [-0.7071067811865475, 0.7071067811865475]; 0.0 | `path-interface-a70e777e6354823bc5c5` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Sin` → `Nout` | primary |
| hsr | `Bin` → `Nout` | primary |

### Forbidden transfers

No additional forbidden-transfer cases are declared beyond the directed graph; no extra transfers are implied.

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 27, passed: 0, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-l4-single-track-oneway-merge-45deg-right-compact/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-l4-single-track-oneway-merge-45deg-right-compact/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-304e83fe57855ab46699">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-304e83fe57855ab46699"></a>

**General: unverified** — `software_resources-304e83fe57855ab46699`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-304e83fe57855ab46699">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-304e83fe57855ab46699"></a>

**General: unverified** — `software_connectivity-304e83fe57855ab46699`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-l4-merge-45-compact:canonical-southeast | <a href="#case-preview_review-0828d69c0734613fb3f9">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-l4-merge-45-compact:canonical-southeast</summary>

<a id="case-preview_review-0828d69c0734613fb3f9"></a>

**General: unverified** — `preview_review-0828d69c0734613fb3f9`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-l4-merge-45-compact:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-c97ee25342b68e9d3b14">[ ] unverified</a> | <a href="#case-in_game_render-42cce471fbc6767667c4">[ ] unverified</a> | <a href="#case-in_game_render-585164cb7bfa2f63579d">[ ] unverified</a> | <a href="#case-in_game_render-6a16bab0955c16f087e8">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-c97ee25342b68e9d3b14"></a>

**0° CCW: unverified** — `in_game_render-c97ee25342b68e9d3b14`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-42cce471fbc6767667c4"></a>

**90° CCW: unverified** — `in_game_render-42cce471fbc6767667c4`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-585164cb7bfa2f63579d"></a>

**180° CCW: unverified** — `in_game_render-585164cb7bfa2f63579d`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-6a16bab0955c16f087e8"></a>

**270° CCW: unverified** — `in_game_render-6a16bab0955c16f087e8`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-c97ee25342b68e9d3b14">[ ] unverified</a> | <a href="#case-in_game_placement-42cce471fbc6767667c4">[ ] unverified</a> | <a href="#case-in_game_placement-585164cb7bfa2f63579d">[ ] unverified</a> | <a href="#case-in_game_placement-6a16bab0955c16f087e8">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-c97ee25342b68e9d3b14"></a>

**0° CCW: unverified** — `in_game_placement-c97ee25342b68e9d3b14`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-42cce471fbc6767667c4"></a>

**90° CCW: unverified** — `in_game_placement-42cce471fbc6767667c4`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-585164cb7bfa2f63579d"></a>

**180° CCW: unverified** — `in_game_placement-585164cb7bfa2f63579d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-6a16bab0955c16f087e8"></a>

**270° CCW: unverified** — `in_game_placement-6a16bab0955c16f087e8`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-c97ee25342b68e9d3b14">[ ] unverified</a> | <a href="#case-in_game_demolition-42cce471fbc6767667c4">[ ] unverified</a> | <a href="#case-in_game_demolition-585164cb7bfa2f63579d">[ ] unverified</a> | <a href="#case-in_game_demolition-6a16bab0955c16f087e8">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-c97ee25342b68e9d3b14"></a>

**0° CCW: unverified** — `in_game_demolition-c97ee25342b68e9d3b14`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-42cce471fbc6767667c4"></a>

**90° CCW: unverified** — `in_game_demolition-42cce471fbc6767667c4`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-585164cb7bfa2f63579d"></a>

**180° CCW: unverified** — `in_game_demolition-585164cb7bfa2f63579d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-6a16bab0955c16f087e8"></a>

**270° CCW: unverified** — `in_game_demolition-6a16bab0955c16f087e8`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-c97ee25342b68e9d3b14">[ ] unverified</a> | <a href="#case-in_game_save_reload-42cce471fbc6767667c4">[ ] unverified</a> | <a href="#case-in_game_save_reload-585164cb7bfa2f63579d">[ ] unverified</a> | <a href="#case-in_game_save_reload-6a16bab0955c16f087e8">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-c97ee25342b68e9d3b14"></a>

**0° CCW: unverified** — `in_game_save_reload-c97ee25342b68e9d3b14`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-42cce471fbc6767667c4"></a>

**90° CCW: unverified** — `in_game_save_reload-42cce471fbc6767667c4`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-585164cb7bfa2f63579d"></a>

**180° CCW: unverified** — `in_game_save_reload-585164cb7bfa2f63579d`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-6a16bab0955c16f087e8"></a>

**270° CCW: unverified** — `in_game_save_reload-6a16bab0955c16f087e8`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-75c3ec5791a25c8025fb">[ ] unverified</a> | <a href="#case-in_game_journey-509d0b598c02f8c94803">[ ] unverified</a> | <a href="#case-in_game_journey-ffbf420cbd2ce4cd4d37">[ ] unverified</a> | <a href="#case-in_game_journey-53e5d9b68eac5c3da5ce">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout | — | <a href="#case-in_game_journey-916065ee4d41ef9d33a7">[ ] unverified</a> | <a href="#case-in_game_journey-ae06534ae27ebe82f916">[ ] unverified</a> | <a href="#case-in_game_journey-316f438444209de8f97a">[ ] unverified</a> | <a href="#case-in_game_journey-f4ea59d3237a958076b1">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-75c3ec5791a25c8025fb"></a>

**0° CCW: unverified** — `in_game_journey-75c3ec5791a25c8025fb`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-509d0b598c02f8c94803"></a>

**90° CCW: unverified** — `in_game_journey-509d0b598c02f8c94803`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-ffbf420cbd2ce4cd4d37"></a>

**180° CCW: unverified** — `in_game_journey-ffbf420cbd2ce4cd4d37`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-53e5d9b68eac5c3da5ce"></a>

**270° CCW: unverified** — `in_game_journey-53e5d9b68eac5c3da5ce`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout</summary>

<a id="case-in_game_journey-916065ee4d41ef9d33a7"></a>

**0° CCW: unverified** — `in_game_journey-916065ee4d41ef9d33a7`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-ae06534ae27ebe82f916"></a>

**90° CCW: unverified** — `in_game_journey-ae06534ae27ebe82f916`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-316f438444209de8f97a"></a>

**180° CCW: unverified** — `in_game_journey-316f438444209de8f97a`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-f4ea59d3237a958076b1"></a>

**270° CCW: unverified** — `in_game_journey-f4ea59d3237a958076b1`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
