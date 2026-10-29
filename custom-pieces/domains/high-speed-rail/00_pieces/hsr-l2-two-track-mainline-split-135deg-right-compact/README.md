<a id="hsr-l2-split-135-degree-compact"></a>

# HSR Level 2 (15.5 m) — Split 135° Right from Two-Track Mainline — Compact

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `interchange-hsr-split-135-compact` → `hsr-l2-two-track-mainline-split-135deg-right-compact`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

HSR Level 2 (15.5 m) — Split 135° Right from Two-Track Mainline — Compact. Fixed click-to-place piece in a 6 by 6 tile area. Follow the arrows and join only matching track widths, directions, and height labels. Four proper rotations; the second four states repeat them. Experimental; game testing pending. The mainline retains both directions; only the branch is one-way.

Exact reusable identifier: `hsr-l2-two-track-mainline-split-135deg-right-compact`.

Footprint: **6 × 6 tiles**. Exact menu name: **HSR Level 2 (15.5 m) — Split 135° Right from Two-Track Mainline — Compact**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

### Design review

**REVIEW NEEDED** — Closely spaced pillars need a support-consolidation review.

- Separate 1.3 m-square pillar foundations have centres less than 2.6 m apart near shared rail geometry. The foundations do not overlap, but the close pair should be reviewed and consolidated to address the reported duplicate-pillar appearance. The 2.6 m review cutoff is an authoring convention, not a structural or game collision threshold.

[Design-review evidence](../../junction-design-review.json).

![HSR Level 2 (15.5 m) — Split 135° Right from Two-Track Mainline — Compact](previews/preview.png)

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
| `Sout` | hsr / 7 / primary | out | [-2.0, -88.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Nin` | hsr / 7 / primary | in | [-2.0, 8.0, 15.5]; [0.0, -1.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Sin` | hsr / 7 / primary | in | [2.0, -88.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [2.0, 8.0, 15.5]; [0.0, 1.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Bout` | hsr / 7 / primary | out | [88.0, -16.0, 15.5]; [0.7071067811865475, -0.7071067811865475]; 0.0 | `path-interface-e52e55553f098fa8572d` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Nin` → `Sout` | primary |
| hsr | `Sin` → `Bout` | primary |
| hsr | `Sin` → `Nout` | primary |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-two-track-mainline-split-135deg-right-compact/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-l2-two-track-mainline-split-135deg-right-compact/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-1f57928b6f6f890b1133">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-1f57928b6f6f890b1133"></a>

**General: unverified** — `software_resources-1f57928b6f6f890b1133`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-1f57928b6f6f890b1133">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-1f57928b6f6f890b1133"></a>

**General: unverified** — `software_connectivity-1f57928b6f6f890b1133`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:interchange-hsr-split-135-compact:canonical-southeast | <a href="#case-preview_review-8c40cbbef2fbc27d60ec">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:interchange-hsr-split-135-compact:canonical-southeast</summary>

<a id="case-preview_review-8c40cbbef2fbc27d60ec"></a>

**General: unverified** — `preview_review-8c40cbbef2fbc27d60ec`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:interchange-hsr-split-135-compact:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-33c9c99b0e50c97197b6">[ ] unverified</a> | <a href="#case-in_game_render-3d749f21b63cce3c06d4">[ ] unverified</a> | <a href="#case-in_game_render-8658eec3073011f396d6">[ ] unverified</a> | <a href="#case-in_game_render-450efbb97b513f3e814f">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-33c9c99b0e50c97197b6"></a>

**0° CCW: unverified** — `in_game_render-33c9c99b0e50c97197b6`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3d749f21b63cce3c06d4"></a>

**90° CCW: unverified** — `in_game_render-3d749f21b63cce3c06d4`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8658eec3073011f396d6"></a>

**180° CCW: unverified** — `in_game_render-8658eec3073011f396d6`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-450efbb97b513f3e814f"></a>

**270° CCW: unverified** — `in_game_render-450efbb97b513f3e814f`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-33c9c99b0e50c97197b6">[ ] unverified</a> | <a href="#case-in_game_placement-3d749f21b63cce3c06d4">[ ] unverified</a> | <a href="#case-in_game_placement-8658eec3073011f396d6">[ ] unverified</a> | <a href="#case-in_game_placement-450efbb97b513f3e814f">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-33c9c99b0e50c97197b6"></a>

**0° CCW: unverified** — `in_game_placement-33c9c99b0e50c97197b6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3d749f21b63cce3c06d4"></a>

**90° CCW: unverified** — `in_game_placement-3d749f21b63cce3c06d4`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8658eec3073011f396d6"></a>

**180° CCW: unverified** — `in_game_placement-8658eec3073011f396d6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-450efbb97b513f3e814f"></a>

**270° CCW: unverified** — `in_game_placement-450efbb97b513f3e814f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-33c9c99b0e50c97197b6">[ ] unverified</a> | <a href="#case-in_game_demolition-3d749f21b63cce3c06d4">[ ] unverified</a> | <a href="#case-in_game_demolition-8658eec3073011f396d6">[ ] unverified</a> | <a href="#case-in_game_demolition-450efbb97b513f3e814f">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-33c9c99b0e50c97197b6"></a>

**0° CCW: unverified** — `in_game_demolition-33c9c99b0e50c97197b6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3d749f21b63cce3c06d4"></a>

**90° CCW: unverified** — `in_game_demolition-3d749f21b63cce3c06d4`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8658eec3073011f396d6"></a>

**180° CCW: unverified** — `in_game_demolition-8658eec3073011f396d6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-450efbb97b513f3e814f"></a>

**270° CCW: unverified** — `in_game_demolition-450efbb97b513f3e814f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-33c9c99b0e50c97197b6">[ ] unverified</a> | <a href="#case-in_game_save_reload-3d749f21b63cce3c06d4">[ ] unverified</a> | <a href="#case-in_game_save_reload-8658eec3073011f396d6">[ ] unverified</a> | <a href="#case-in_game_save_reload-450efbb97b513f3e814f">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-33c9c99b0e50c97197b6"></a>

**0° CCW: unverified** — `in_game_save_reload-33c9c99b0e50c97197b6`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3d749f21b63cce3c06d4"></a>

**90° CCW: unverified** — `in_game_save_reload-3d749f21b63cce3c06d4`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8658eec3073011f396d6"></a>

**180° CCW: unverified** — `in_game_save_reload-8658eec3073011f396d6`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-450efbb97b513f3e814f"></a>

**270° CCW: unverified** — `in_game_save_reload-450efbb97b513f3e814f`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout | — | <a href="#case-in_game_journey-7211e6d9c62334cf8aee">[ ] unverified</a> | <a href="#case-in_game_journey-62150dfeac818e519042">[ ] unverified</a> | <a href="#case-in_game_journey-adf8063afe3f507b5d4e">[ ] unverified</a> | <a href="#case-in_game_journey-1ca6528cdac3c4163046">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout | — | <a href="#case-in_game_journey-0b74563bb1880e5cdf13">[ ] unverified</a> | <a href="#case-in_game_journey-6a13ffa8e56e80be2fee">[ ] unverified</a> | <a href="#case-in_game_journey-7f3faafdf13ccff97563">[ ] unverified</a> | <a href="#case-in_game_journey-3c9ddf0c838a3008042d">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout | — | <a href="#case-in_game_journey-9a80188fe2b2529c9301">[ ] unverified</a> | <a href="#case-in_game_journey-aa316fa726ed9a633d12">[ ] unverified</a> | <a href="#case-in_game_journey-8461408dbb4a03541dc8">[ ] unverified</a> | <a href="#case-in_game_journey-67ab7e33f39ef8bd6df8">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout</summary>

<a id="case-in_game_journey-7211e6d9c62334cf8aee"></a>

**0° CCW: unverified** — `in_game_journey-7211e6d9c62334cf8aee`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-62150dfeac818e519042"></a>

**90° CCW: unverified** — `in_game_journey-62150dfeac818e519042`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-adf8063afe3f507b5d4e"></a>

**180° CCW: unverified** — `in_game_journey-adf8063afe3f507b5d4e`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-1ca6528cdac3c4163046"></a>

**270° CCW: unverified** — `in_game_journey-1ca6528cdac3c4163046`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Nin>Sout; entry: Nin; exit: Sout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout</summary>

<a id="case-in_game_journey-0b74563bb1880e5cdf13"></a>

**0° CCW: unverified** — `in_game_journey-0b74563bb1880e5cdf13`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-6a13ffa8e56e80be2fee"></a>

**90° CCW: unverified** — `in_game_journey-6a13ffa8e56e80be2fee`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-7f3faafdf13ccff97563"></a>

**180° CCW: unverified** — `in_game_journey-7f3faafdf13ccff97563`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

<a id="case-in_game_journey-3c9ddf0c838a3008042d"></a>

**270° CCW: unverified** — `in_game_journey-3c9ddf0c838a3008042d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Bout; entry: Sin; exit: Bout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout</summary>

<a id="case-in_game_journey-9a80188fe2b2529c9301"></a>

**0° CCW: unverified** — `in_game_journey-9a80188fe2b2529c9301`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-aa316fa726ed9a633d12"></a>

**90° CCW: unverified** — `in_game_journey-aa316fa726ed9a633d12`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-8461408dbb4a03541dc8"></a>

**180° CCW: unverified** — `in_game_journey-8461408dbb4a03541dc8`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-67ab7e33f39ef8bd6df8"></a>

**270° CCW: unverified** — `in_game_journey-67ab7e33f39ef8bd6df8`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Sin>Nout; entry: Sin; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2671c631985f37731a5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75a1cebd542552de00cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ebd48d2d32fcd6ed471">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a51c1fdc54032891064a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fbb99b7efbac6dcb9df3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ec51f78050bb82e8308">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9affd4842f1f0da3fe8c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-781a599d83ba7dfe3fd6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-209dc7bb45750ad40475">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe7f5cdbd38c32f37d46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd054c8af212fe1b596e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebb7419be11c33d2d291">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2671c631985f37731a5d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2671c631985f37731a5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75a1cebd542552de00cf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-75a1cebd542552de00cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ebd48d2d32fcd6ed471"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9ebd48d2d32fcd6ed471`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a51c1fdc54032891064a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a51c1fdc54032891064a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fbb99b7efbac6dcb9df3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fbb99b7efbac6dcb9df3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ec51f78050bb82e8308"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0ec51f78050bb82e8308`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9affd4842f1f0da3fe8c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9affd4842f1f0da3fe8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-781a599d83ba7dfe3fd6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-781a599d83ba7dfe3fd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Nin; to port: Bout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-209dc7bb45750ad40475"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-209dc7bb45750ad40475`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe7f5cdbd38c32f37d46"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fe7f5cdbd38c32f37d46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd054c8af212fe1b596e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dd054c8af212fe1b596e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebb7419be11c33d2d291"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ebb7419be11c33d2d291`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
