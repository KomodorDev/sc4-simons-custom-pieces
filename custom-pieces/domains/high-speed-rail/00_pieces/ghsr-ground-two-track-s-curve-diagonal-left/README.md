<a id="ghsr-diagonal-s-curve-left"></a>

# GHSR Ground (1 m) — Two-Track Diagonal S-Curve Left

<!-- SUBJECT IDENTITY MIGRATION -->

Identity migration: `rail-ghsr-diagonal-s-left` → `ghsr-ground-two-track-s-curve-diagonal-left`. Earlier measurements, observations, and pictures retain their recorded names and fingerprints; they do not establish verification of the renamed build. See the [identity migration rules](../../../../docs/NAMING_CONVENTIONS.md#10-choosing-and-changing-names).

Purpose: explain this reusable piece, its matching connections and current test coverage.

<!-- BEGIN PIECE OVERVIEW -->

A two-way diagonal S-curve shifts a diagonal line sideways while preserving its entry and exit heading. Native HSR or GHSR track ends; select the matching height and handedness.

Exact reusable identifier: `ghsr-ground-two-track-s-curve-diagonal-left`.

Footprint: **3 × 3 tiles**. Exact menu name: **GHSR Ground (1 m) — Two-Track Diagonal S-Curve Left**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![GHSR Ground (1 m) — Two-Track Diagonal S-Curve Left](previews/preview.png)

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
| `Sout` | ghsr / 7 / primary | out | [13.1, -40.0, 1.0]; [-0.7071067811865471, -0.707106781186548]; 0.0 | `path-interface-2fb13cb0f06be67da5ca` |
| `Sin` | ghsr / 7 / primary | in | [18.9, -40.0, 1.0]; [0.6334396472647336, 0.7737920995158389]; 0.0 | `path-interface-f5abdc4d8e21bba0ef88` |
| `Eout` | ghsr / 7 / primary | out | [40.0, -2.8, 1.0]; [0.6045105171867364, 0.7965971595547052]; 0.0 | `path-interface-a366002602b3783f5094` |
| `Ein` | ghsr / 7 / primary | in | [40.0, 2.9, 1.0]; [-0.7071067811865482, -0.7071067811865469]; 0.0 | `path-interface-493b20c718656c56d5d7` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| ghsr | `Sin` → `Eout` | primary |
| ghsr | `Ein` → `Sout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| ghsr / `Sin` | ghsr / `Sout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| ghsr / `Ein` | ghsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

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
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/ghsr-ground-two-track-s-curve-diagonal-left/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/ghsr-ground-two-track-s-curve-diagonal-left/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-ff72785c9a05a7bedd5a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-ff72785c9a05a7bedd5a"></a>

**General: unverified** — `software_resources-ff72785c9a05a7bedd5a`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-ff72785c9a05a7bedd5a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-ff72785c9a05a7bedd5a"></a>

**General: unverified** — `software_connectivity-ff72785c9a05a7bedd5a`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:rail-ghsr-diagonal-s-left:canonical-southeast | <a href="#case-preview_review-0ec6361617168959dca8">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:rail-ghsr-diagonal-s-left:canonical-southeast</summary>

<a id="case-preview_review-0ec6361617168959dca8"></a>

**General: unverified** — `preview_review-0ec6361617168959dca8`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:rail-ghsr-diagonal-s-left:canonical-southeast.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-5c82cf93f1c8ae600207">[ ] unverified</a> | <a href="#case-in_game_render-2ffd1a8be62438d7ffb0">[ ] unverified</a> | <a href="#case-in_game_render-2e4ab61f8655338f3ecf">[ ] unverified</a> | <a href="#case-in_game_render-28c39af47b611771eaf5">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-5c82cf93f1c8ae600207"></a>

**0° CCW: unverified** — `in_game_render-5c82cf93f1c8ae600207`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2ffd1a8be62438d7ffb0"></a>

**90° CCW: unverified** — `in_game_render-2ffd1a8be62438d7ffb0`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2e4ab61f8655338f3ecf"></a>

**180° CCW: unverified** — `in_game_render-2e4ab61f8655338f3ecf`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-28c39af47b611771eaf5"></a>

**270° CCW: unverified** — `in_game_render-28c39af47b611771eaf5`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-5c82cf93f1c8ae600207">[ ] unverified</a> | <a href="#case-in_game_placement-2ffd1a8be62438d7ffb0">[ ] unverified</a> | <a href="#case-in_game_placement-2e4ab61f8655338f3ecf">[ ] unverified</a> | <a href="#case-in_game_placement-28c39af47b611771eaf5">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-5c82cf93f1c8ae600207"></a>

**0° CCW: unverified** — `in_game_placement-5c82cf93f1c8ae600207`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2ffd1a8be62438d7ffb0"></a>

**90° CCW: unverified** — `in_game_placement-2ffd1a8be62438d7ffb0`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2e4ab61f8655338f3ecf"></a>

**180° CCW: unverified** — `in_game_placement-2e4ab61f8655338f3ecf`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-28c39af47b611771eaf5"></a>

**270° CCW: unverified** — `in_game_placement-28c39af47b611771eaf5`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-5c82cf93f1c8ae600207">[ ] unverified</a> | <a href="#case-in_game_demolition-2ffd1a8be62438d7ffb0">[ ] unverified</a> | <a href="#case-in_game_demolition-2e4ab61f8655338f3ecf">[ ] unverified</a> | <a href="#case-in_game_demolition-28c39af47b611771eaf5">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-5c82cf93f1c8ae600207"></a>

**0° CCW: unverified** — `in_game_demolition-5c82cf93f1c8ae600207`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2ffd1a8be62438d7ffb0"></a>

**90° CCW: unverified** — `in_game_demolition-2ffd1a8be62438d7ffb0`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2e4ab61f8655338f3ecf"></a>

**180° CCW: unverified** — `in_game_demolition-2e4ab61f8655338f3ecf`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-28c39af47b611771eaf5"></a>

**270° CCW: unverified** — `in_game_demolition-28c39af47b611771eaf5`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-5c82cf93f1c8ae600207">[ ] unverified</a> | <a href="#case-in_game_save_reload-2ffd1a8be62438d7ffb0">[ ] unverified</a> | <a href="#case-in_game_save_reload-2e4ab61f8655338f3ecf">[ ] unverified</a> | <a href="#case-in_game_save_reload-28c39af47b611771eaf5">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-5c82cf93f1c8ae600207"></a>

**0° CCW: unverified** — `in_game_save_reload-5c82cf93f1c8ae600207`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2ffd1a8be62438d7ffb0"></a>

**90° CCW: unverified** — `in_game_save_reload-2ffd1a8be62438d7ffb0`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2e4ab61f8655338f3ecf"></a>

**180° CCW: unverified** — `in_game_save_reload-2e4ab61f8655338f3ecf`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-28c39af47b611771eaf5"></a>

**270° CCW: unverified** — `in_game_save_reload-28c39af47b611771eaf5`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — ghsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout | — | <a href="#case-in_game_journey-d215bc7458aaacc33c2b">[ ] unverified</a> | <a href="#case-in_game_journey-3cc44ba100727cfe45a6">[ ] unverified</a> | <a href="#case-in_game_journey-b3477bc4e6598e199f08">[ ] unverified</a> | <a href="#case-in_game_journey-5d315f28d2db5d9916eb">[ ] unverified</a> |
| **Journey**<br>Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout | — | <a href="#case-in_game_journey-c3092ca032cf52fab2d4">[ ] unverified</a> | <a href="#case-in_game_journey-0e0bef34ff3f9976bf2d">[ ] unverified</a> | <a href="#case-in_game_journey-3c8c0dce0d4a93d6c467">[ ] unverified</a> | <a href="#case-in_game_journey-0f3554ebd910d5298dcb">[ ] unverified</a> |


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout</summary>

<a id="case-in_game_journey-d215bc7458aaacc33c2b"></a>

**0° CCW: unverified** — `in_game_journey-d215bc7458aaacc33c2b`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-3cc44ba100727cfe45a6"></a>

**90° CCW: unverified** — `in_game_journey-3cc44ba100727cfe45a6`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-b3477bc4e6598e199f08"></a>

**180° CCW: unverified** — `in_game_journey-b3477bc4e6598e199f08`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-5d315f28d2db5d9916eb"></a>

**270° CCW: unverified** — `in_game_journey-5d315f28d2db5d9916eb`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Sin>Eout; entry: Sin; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout</summary>

<a id="case-in_game_journey-c3092ca032cf52fab2d4"></a>

**0° CCW: unverified** — `in_game_journey-c3092ca032cf52fab2d4`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-0e0bef34ff3f9976bf2d"></a>

**90° CCW: unverified** — `in_game_journey-0e0bef34ff3f9976bf2d`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-3c8c0dce0d4a93d6c467"></a>

**180° CCW: unverified** — `in_game_journey-3c8c0dce0d4a93d6c467`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

<a id="case-in_game_journey-0f3554ebd910d5298dcb"></a>

**270° CCW: unverified** — `in_game_journey-0f3554ebd910d5298dcb`.

Run the declared journey in this direction using its service network.

Scope: Service: ghsr; role: primary; journey: 7:Ein>Sout; entry: Ein; exit: Sout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — ghsr → ghsr — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7961852d91623cadee31">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-534669d0ab7d1f32ded6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7fe864565c3308f94624">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e736db633204d8b5e42">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-83f78ddad1b4b0b69e35">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45704a4a8fea41b4f5b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-175c2095b3a3b7539b38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a57ce3fa4ec2565373c4">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7961852d91623cadee31"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7961852d91623cadee31`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-534669d0ab7d1f32ded6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-534669d0ab7d1f32ded6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7fe864565c3308f94624"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7fe864565c3308f94624`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e736db633204d8b5e42"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e736db633204d8b5e42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Sin; to port: Sout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-83f78ddad1b4b0b69e35"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-83f78ddad1b4b0b69e35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45704a4a8fea41b4f5b2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-45704a4a8fea41b4f5b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-175c2095b3a3b7539b38"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-175c2095b3a3b7539b38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a57ce3fa4ec2565373c4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a57ce3fa4ec2565373c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: ghsr; to service: ghsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## Engineering contract

This diagonal S-curve has a 3 × 3 construction rectangle, four occupied cells, and an empty construction reference cell. The Left and Right geometries are separate authored types, rather than reflections inferred from a name. Empty cells do not establish construction clearance.

Use the [independent source contract](../../implementation/scp_hsr/rail_feature_verify.py) and this type's [definition](piece.json) for exact expectations. Shared HSR/GHSR facts remain in [NETWORK_SPEC.md](../../NETWORK_SPEC.md). These authored notes supplement generated source views; they do not change geometry, reset observations, or establish game operation.
