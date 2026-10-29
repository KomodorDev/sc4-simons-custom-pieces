<a id="one-way-l4-merge-90deg-left-wide"></a>

# HSR Level 4 (30.5 m) — Merge 90° Left to Single-Track One-Way Mainline — Wide

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `interchange-l4-merge-90-wide-left` → `hsr-l4-single-track-oneway-merge-90deg-left-wide`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

A left-hand split or merge on the centered one-way 30.5 m track. No opposing mainline track is crossed. Use matching one-way L4 fillers and level adapters. The L4 mainline and branch are both one-way single tracks.

Exact reusable identifier: `hsr-l4-single-track-oneway-merge-90deg-left-wide`.

Footprint: **6 × 6 tiles**. Exact menu name: **HSR Level 4 (30.5 m) — Merge 90° Left to Single-Track One-Way Mainline — Wide**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

### Design review

**REVIEW NEEDED** — Closely spaced pillars need a support-consolidation review.

- Separate 1.3 m-square pillar foundations have centres less than 2.6 m apart near shared rail geometry. The foundations do not overlap, but the close pair should be reviewed and consolidated to address the reported duplicate-pillar appearance. The 2.6 m review cutoff is an authoring convention, not a structural or game collision threshold.

[Design-review evidence](../../junction-design-review.json).

![HSR Level 4 (30.5 m) — Merge 90° Left to Single-Track One-Way Mainline — Wide](previews/preview.png)

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
| `Bin` | hsr / 7 / primary | in | [-8.0, -80.0, 30.5]; [1.0, 0.0]; 0.0 | `path-interface-a11c9f8debd0ee1c3a94` |
| `Sin` | hsr / 7 / primary | in | [80.0, -88.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |
| `Nout` | hsr / 7 / primary | out | [80.0, 8.0, 30.5]; [0.0, 1.0]; 0.0 | `path-interface-90a5bcd3e5d324374d48` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Bin` → `Nout` | primary |
| hsr | `Sin` → `Nout` | primary |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-l4-single-track-oneway-merge-90deg-left-wide/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-l4-single-track-oneway-merge-90deg-left-wide/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-2e1138d347abc48e3c19">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-2e1138d347abc48e3c19"></a>

**General: unverified** — `software_resources-2e1138d347abc48e3c19`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-2e1138d347abc48e3c19">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-2e1138d347abc48e3c19"></a>

**General: unverified** — `software_connectivity-2e1138d347abc48e3c19`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-l4-merge-90-wide-left:canonical-southeast | <a href="#case-preview_review-9f91e53ba8561b3d0ae4">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-l4-merge-90-wide-left:canonical-southeast</summary>

<a id="case-preview_review-9f91e53ba8561b3d0ae4"></a>

**General: unverified** — `preview_review-9f91e53ba8561b3d0ae4`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-l4-merge-90-wide-left:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-c04ac4cc85864d444985">[ ] unverified</a> | <a href="#case-in_game_render-5f443c9c69e02b8eb4ab">[ ] unverified</a> | <a href="#case-in_game_render-da1ce710bb19591f6ee3">[ ] unverified</a> | <a href="#case-in_game_render-d025d5d6462aa90b9816">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-c04ac4cc85864d444985"></a>

**0° CCW: unverified** — `in_game_render-c04ac4cc85864d444985`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5f443c9c69e02b8eb4ab"></a>

**90° CCW: unverified** — `in_game_render-5f443c9c69e02b8eb4ab`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-da1ce710bb19591f6ee3"></a>

**180° CCW: unverified** — `in_game_render-da1ce710bb19591f6ee3`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-d025d5d6462aa90b9816"></a>

**270° CCW: unverified** — `in_game_render-d025d5d6462aa90b9816`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-c04ac4cc85864d444985">[ ] unverified</a> | <a href="#case-in_game_placement-5f443c9c69e02b8eb4ab">[ ] unverified</a> | <a href="#case-in_game_placement-da1ce710bb19591f6ee3">[ ] unverified</a> | <a href="#case-in_game_placement-d025d5d6462aa90b9816">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-c04ac4cc85864d444985"></a>

**0° CCW: unverified** — `in_game_placement-c04ac4cc85864d444985`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5f443c9c69e02b8eb4ab"></a>

**90° CCW: unverified** — `in_game_placement-5f443c9c69e02b8eb4ab`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-da1ce710bb19591f6ee3"></a>

**180° CCW: unverified** — `in_game_placement-da1ce710bb19591f6ee3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-d025d5d6462aa90b9816"></a>

**270° CCW: unverified** — `in_game_placement-d025d5d6462aa90b9816`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-c04ac4cc85864d444985">[ ] unverified</a> | <a href="#case-in_game_demolition-5f443c9c69e02b8eb4ab">[ ] unverified</a> | <a href="#case-in_game_demolition-da1ce710bb19591f6ee3">[ ] unverified</a> | <a href="#case-in_game_demolition-d025d5d6462aa90b9816">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-c04ac4cc85864d444985"></a>

**0° CCW: unverified** — `in_game_demolition-c04ac4cc85864d444985`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5f443c9c69e02b8eb4ab"></a>

**90° CCW: unverified** — `in_game_demolition-5f443c9c69e02b8eb4ab`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-da1ce710bb19591f6ee3"></a>

**180° CCW: unverified** — `in_game_demolition-da1ce710bb19591f6ee3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-d025d5d6462aa90b9816"></a>

**270° CCW: unverified** — `in_game_demolition-d025d5d6462aa90b9816`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-c04ac4cc85864d444985">[ ] unverified</a> | <a href="#case-in_game_save_reload-5f443c9c69e02b8eb4ab">[ ] unverified</a> | <a href="#case-in_game_save_reload-da1ce710bb19591f6ee3">[ ] unverified</a> | <a href="#case-in_game_save_reload-d025d5d6462aa90b9816">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-c04ac4cc85864d444985"></a>

**0° CCW: unverified** — `in_game_save_reload-c04ac4cc85864d444985`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5f443c9c69e02b8eb4ab"></a>

**90° CCW: unverified** — `in_game_save_reload-5f443c9c69e02b8eb4ab`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-da1ce710bb19591f6ee3"></a>

**180° CCW: unverified** — `in_game_save_reload-da1ce710bb19591f6ee3`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-d025d5d6462aa90b9816"></a>

**270° CCW: unverified** — `in_game_save_reload-d025d5d6462aa90b9816`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout | — | <a href="#case-in_game_journey-490445633ab6848ae63f">[ ] unverified</a> | <a href="#case-in_game_journey-c1aecca680a36bcefa1d">[ ] unverified</a> | <a href="#case-in_game_journey-331d03c573572f857b1a">[ ] unverified</a> | <a href="#case-in_game_journey-7251aa2344fe4c283a01">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-8a4e5dd600b5365b4d5c">[ ] unverified</a> | <a href="#case-in_game_journey-d0a89e8860397b296a27">[ ] unverified</a> | <a href="#case-in_game_journey-cbdf52b4907be2caf10a">[ ] unverified</a> | <a href="#case-in_game_journey-f19b5089c15304d55771">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout</summary>

<a id="case-in_game_journey-490445633ab6848ae63f"></a>

**0° CCW: unverified** — `in_game_journey-490445633ab6848ae63f`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-c1aecca680a36bcefa1d"></a>

**90° CCW: unverified** — `in_game_journey-c1aecca680a36bcefa1d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-331d03c573572f857b1a"></a>

**180° CCW: unverified** — `in_game_journey-331d03c573572f857b1a`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-7251aa2344fe4c283a01"></a>

**270° CCW: unverified** — `in_game_journey-7251aa2344fe4c283a01`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Bin>Nout; entry: Bin; exit: Nout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-8a4e5dd600b5365b4d5c"></a>

**0° CCW: unverified** — `in_game_journey-8a4e5dd600b5365b4d5c`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-d0a89e8860397b296a27"></a>

**90° CCW: unverified** — `in_game_journey-d0a89e8860397b296a27`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-cbdf52b4907be2caf10a"></a>

**180° CCW: unverified** — `in_game_journey-cbdf52b4907be2caf10a`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-f19b5089c15304d55771"></a>

**270° CCW: unverified** — `in_game_journey-f19b5089c15304d55771`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
