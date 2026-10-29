<a id="rail-l4-merge-135-degree-compact"></a>

# HSR Level 4 (30.5 m) — Merge 135° Right to Single-Track One-Way Mainline — Compact

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `interchange-l4-merge-135-compact` → `hsr-l4-single-track-oneway-merge-135deg-right-compact`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

HSR Level 4 (30.5 m) — Merge 135° Right to Single-Track One-Way Mainline — Compact. Fixed click-to-place piece in a 6 by 6 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The L4 mainline and branch are both one-way single tracks.

Exact reusable identifier: `hsr-l4-single-track-oneway-merge-135deg-right-compact`.

Footprint: **6 × 6 tiles**. Exact menu name: **HSR Level 4 (30.5 m) — Merge 135° Right to Single-Track One-Way Mainline — Compact**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

### Design review

**REVIEW NEEDED** — Closely spaced pillars need a support-consolidation review.

- Separate 1.3 m-square pillar foundations have centres less than 2.6 m apart near shared rail geometry. The foundations do not overlap, but the close pair should be reviewed and consolidated to address the reported duplicate-pillar appearance. The 2.6 m review cutoff is an authoring convention, not a structural or game collision threshold.

[Design-review evidence](../../junction-design-review.jsonc).

![HSR Level 4 (30.5 m) — Merge 135° Right to Single-Track One-Way Mainline — Compact](previews/preview.png)

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
| `Sin` | hsr / 7 / primary | in | [0.0, -88.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Nout` | hsr / 7 / primary | out | [0.0, 8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Bin` | hsr / 7 / primary | in | [88.0, -64.0, 30.5]; [-0.7071067811865475, -0.7071067811865475]; 0.0 | `path-interface-13a0d20884fd73110dea` |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-l4-single-track-oneway-merge-135deg-right-compact/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-l4-single-track-oneway-merge-135deg-right-compact/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-11e6863666e113a19d4e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-11e6863666e113a19d4e"></a>

**General: unverified** — `software_resources-11e6863666e113a19d4e`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-11e6863666e113a19d4e">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-11e6863666e113a19d4e"></a>

**General: unverified** — `software_connectivity-11e6863666e113a19d4e`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-l4-merge-135-compact:canonical-southeast | <a href="#case-preview_review-ea808113d48278a16c8d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-l4-merge-135-compact:canonical-southeast</summary>

<a id="case-preview_review-ea808113d48278a16c8d"></a>

**General: unverified** — `preview_review-ea808113d48278a16c8d`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-l4-merge-135-compact:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-43a1f98d9f1c82a23cf1">[ ] unverified</a> | <a href="#case-in_game_render-6a075ddd3a9bd6e0b7aa">[ ] unverified</a> | <a href="#case-in_game_render-7781b17ab2d10a285d39">[ ] unverified</a> | <a href="#case-in_game_render-78311931541bdbbbacc6">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-43a1f98d9f1c82a23cf1"></a>

**0° CCW: unverified** — `in_game_render-43a1f98d9f1c82a23cf1`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-6a075ddd3a9bd6e0b7aa"></a>

**90° CCW: unverified** — `in_game_render-6a075ddd3a9bd6e0b7aa`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-7781b17ab2d10a285d39"></a>

**180° CCW: unverified** — `in_game_render-7781b17ab2d10a285d39`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-78311931541bdbbbacc6"></a>

**270° CCW: unverified** — `in_game_render-78311931541bdbbbacc6`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-43a1f98d9f1c82a23cf1">[ ] unverified</a> | <a href="#case-in_game_placement-6a075ddd3a9bd6e0b7aa">[ ] unverified</a> | <a href="#case-in_game_placement-7781b17ab2d10a285d39">[ ] unverified</a> | <a href="#case-in_game_placement-78311931541bdbbbacc6">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-43a1f98d9f1c82a23cf1"></a>

**0° CCW: unverified** — `in_game_placement-43a1f98d9f1c82a23cf1`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-6a075ddd3a9bd6e0b7aa"></a>

**90° CCW: unverified** — `in_game_placement-6a075ddd3a9bd6e0b7aa`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-7781b17ab2d10a285d39"></a>

**180° CCW: unverified** — `in_game_placement-7781b17ab2d10a285d39`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-78311931541bdbbbacc6"></a>

**270° CCW: unverified** — `in_game_placement-78311931541bdbbbacc6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-43a1f98d9f1c82a23cf1">[ ] unverified</a> | <a href="#case-in_game_demolition-6a075ddd3a9bd6e0b7aa">[ ] unverified</a> | <a href="#case-in_game_demolition-7781b17ab2d10a285d39">[ ] unverified</a> | <a href="#case-in_game_demolition-78311931541bdbbbacc6">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-43a1f98d9f1c82a23cf1"></a>

**0° CCW: unverified** — `in_game_demolition-43a1f98d9f1c82a23cf1`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-6a075ddd3a9bd6e0b7aa"></a>

**90° CCW: unverified** — `in_game_demolition-6a075ddd3a9bd6e0b7aa`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-7781b17ab2d10a285d39"></a>

**180° CCW: unverified** — `in_game_demolition-7781b17ab2d10a285d39`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-78311931541bdbbbacc6"></a>

**270° CCW: unverified** — `in_game_demolition-78311931541bdbbbacc6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-43a1f98d9f1c82a23cf1">[ ] unverified</a> | <a href="#case-in_game_save_reload-6a075ddd3a9bd6e0b7aa">[ ] unverified</a> | <a href="#case-in_game_save_reload-7781b17ab2d10a285d39">[ ] unverified</a> | <a href="#case-in_game_save_reload-78311931541bdbbbacc6">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-43a1f98d9f1c82a23cf1"></a>

**0° CCW: unverified** — `in_game_save_reload-43a1f98d9f1c82a23cf1`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-6a075ddd3a9bd6e0b7aa"></a>

**90° CCW: unverified** — `in_game_save_reload-6a075ddd3a9bd6e0b7aa`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-7781b17ab2d10a285d39"></a>

**180° CCW: unverified** — `in_game_save_reload-7781b17ab2d10a285d39`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-78311931541bdbbbacc6"></a>

**270° CCW: unverified** — `in_game_save_reload-78311931541bdbbbacc6`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-eb7ae00c7bf77f420d9b">[ ] unverified</a> | <a href="#case-in_game_journey-291db2b96384531c9a2c">[ ] unverified</a> | <a href="#case-in_game_journey-7dc28a50c2356b9b613d">[ ] unverified</a> | <a href="#case-in_game_journey-4122fb3b8c90e70c25fa">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout | — | <a href="#case-in_game_journey-0e65ee57764d088c3788">[ ] unverified</a> | <a href="#case-in_game_journey-7e1ca437bc02295fc252">[ ] unverified</a> | <a href="#case-in_game_journey-c48a1f95236748fe3112">[ ] unverified</a> | <a href="#case-in_game_journey-c061233aacb2e8f77ba6">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-eb7ae00c7bf77f420d9b"></a>

**0° CCW: unverified** — `in_game_journey-eb7ae00c7bf77f420d9b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-291db2b96384531c9a2c"></a>

**90° CCW: unverified** — `in_game_journey-291db2b96384531c9a2c`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-7dc28a50c2356b9b613d"></a>

**180° CCW: unverified** — `in_game_journey-7dc28a50c2356b9b613d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-4122fb3b8c90e70c25fa"></a>

**270° CCW: unverified** — `in_game_journey-4122fb3b8c90e70c25fa`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout</summary>

<a id="case-in_game_journey-0e65ee57764d088c3788"></a>

**0° CCW: unverified** — `in_game_journey-0e65ee57764d088c3788`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-7e1ca437bc02295fc252"></a>

**90° CCW: unverified** — `in_game_journey-7e1ca437bc02295fc252`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-c48a1f95236748fe3112"></a>

**180° CCW: unverified** — `in_game_journey-c48a1f95236748fe3112`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-c061233aacb2e8f77ba6"></a>

**270° CCW: unverified** — `in_game_journey-c061233aacb2e8f77ba6`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
