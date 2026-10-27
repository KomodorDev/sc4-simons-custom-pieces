# HSR L2 Compact Fan Diverge

Purpose: Explain this reusable three-tile split, its ordinary mainline connections, matched curved branch and current test coverage.

This piece carries opposite-direction HSR through a **3 × 1 tile** core at a train-path height of **15.5 m**. At its default orientation the mainline runs west–east. Westbound trains arriving from the east can continue west or leave on the north-facing curved branch. No reverse journey from that branch is provided.

Both mainline ends have the ordinary **15 m-wide paired HSR profile**. Use the existing **[HSR L2 Two-Track Straight](../hsr-component-lower-paired-straight/README.md)**, rotated 270° for an east–west line. This type does not contain extra ordinary approach tiles.

The branch is an angled custom connection, even though it leaves through the northern tile edge. Join it to the matching incoming curve on **[HSR L2 Compact Paired Fan Join](../hsr-component-l2-paired-fan-compact-join/README.md)**. A normal north–south straight does not match that branch's position or heading.

The compact shape includes a smooth internal branch lead-in and a fitted outer platform corner. Its straight connections are checked from actual saved models and train routes. Placement, moving trains, rotation controls and save/reload still require tests inside SimCity 4.

Both views show the same complete compiled piece at its default **0° orientation**. Their local southwest tile centre is **(X0, Y0)**; the top view keeps north upward. These software pictures do not establish operation inside the game.

[Angled view](previews/preview.png) · [North-up top view](previews/preview-top.png)

Definition: [piece.json](piece.json). Independent geometry: [geometry.json](geometry.json). The generated connection overview and exact test cases below describe the current saved resources.

<!-- BEGIN PIECE OVERVIEW -->

Three-tile native two-track mainline with a one-way departure into the matching Compact Paired Fan Join. Both mainline ends accept ordinary L2 two-track HSR.

Exact reusable identifier: `hsr-component-l2-compact-fan-diverge`.

Footprint: **3 × 1 tiles**. Exact menu name: **HSR L2 Compact Fan Diverge**.

Choose this exact name in Transportation → Rail. Press Home or End to rotate; use only the supported states listed below. Join each end to a matching port profile and direction.

- [Connections and journeys](#connections-and-journeys)
- [Test checklist](#test-checklist)

![HSR L2 Compact Fan Diverge](previews/preview.png)

![HSR L2 Compact Fan Diverge — top view](previews/preview-top.png)

<!-- END PIECE OVERVIEW -->

<!-- BEGIN MANUAL SUMMARY -->

## Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
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
| `Win` | hsr / 7 / primary | in | [-8.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Wout` | hsr / 7 / primary | out | [-8.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |
| `Nout` | hsr / 7 / primary | out | [-0.562689, 8.0, 15.5]; [-0.9121771234450041, 0.4097961633100019]; 0.0 | `path-interface-187e749c1d9d220c3c88` |
| `Eout` | hsr / 7 / primary | out | [40.0, -2.0, 15.5]; [1.0, 0.0]; 0.0 | `path-interface-12d12be31d2057c5763d` |
| `Ein` | hsr / 7 / primary | in | [40.0, 2.0, 15.5]; [-1.0, 0.0]; 0.0 | `path-interface-fba09fbeb87ad95c667a` |

### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| hsr | `Win` → `Eout` | primary |
| hsr | `Ein` → `Wout` | primary |
| hsr | `Ein` → `Nout` | primary |

### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| hsr / `Win` | hsr / `Wout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Win` | hsr / `Nout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| hsr / `Ein` | hsr / `Eout` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

<!-- BEGIN MANUAL CHECKS -->

## Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 42, passed: 2, failed: 0, stale: 0, not_applicable: 0.

### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-compact-fan-diverge/checks/manual-tests.json --observation custom-pieces/domains/high-speed-rail/00_pieces/hsr-component-l2-compact-fan-diverge/checks/observation.json
```

### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-8ec62c84113dcb4cb29d">[x] passed</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-8ec62c84113dcb4cb29d"></a>

**General: passed** — `software_resources-8ec62c84113dcb4cb29d`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus current compiled-resource checks; confirmed at: 2026-10-20T11:45:51.381642+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: 

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; passed: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-8ec62c84113dcb4cb29d">[x] passed</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-8ec62c84113dcb4cb29d"></a>

**General: passed** — `software_connectivity-8ec62c84113dcb4cb29d`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

Recorded observations (chronological; the state above checks the relevant dependency snapshot):

- result: passed; authority: software; reviewer: verify_hsr_trumpet_v4.py plus current compiled-resource checks; confirmed at: 2026-10-20T11:45:51.386815+00:00; evidence: [../../01_assemblies/straight-stem-trumpet-v4/evidence/validation.json]; environment: 

</details>

</details>

<details>
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:hsr-component-l2-compact-fan-diverge:canonical-southeast | <a href="#case-preview_review-f019a73987882a50ce10">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:hsr-component-l2-compact-fan-diverge:canonical-top | <a href="#case-preview_review-c31482d969a25e75d4e5">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:hsr-component-l2-compact-fan-diverge:canonical-southeast</summary>

<a id="case-preview_review-f019a73987882a50ce10"></a>

**General: unverified** — `preview_review-f019a73987882a50ce10`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-l2-compact-fan-diverge:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:hsr-component-l2-compact-fan-diverge:canonical-top</summary>

<a id="case-preview_review-c31482d969a25e75d4e5"></a>

**General: unverified** — `preview_review-c31482d969a25e75d4e5`.

Inspect this exact preview for tracks, walls, piers, seams and shadows.

Scope: Image: image:hsr-component-l2-compact-fan-diverge:canonical-top.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-b15982836e4af5476616">[ ] unverified</a> | <a href="#case-in_game_render-8dc51edd2cade606129f">[ ] unverified</a> | <a href="#case-in_game_render-72f9b61cafbe593b9cfa">[ ] unverified</a> | <a href="#case-in_game_render-67792913095a38645245">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-b15982836e4af5476616"></a>

**0° CCW: unverified** — `in_game_render-b15982836e4af5476616`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8dc51edd2cade606129f"></a>

**90° CCW: unverified** — `in_game_render-8dc51edd2cade606129f`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-72f9b61cafbe593b9cfa"></a>

**180° CCW: unverified** — `in_game_render-72f9b61cafbe593b9cfa`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-67792913095a38645245"></a>

**270° CCW: unverified** — `in_game_render-67792913095a38645245`.

Inspect the placed tracks, walls, piers, seams and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-b15982836e4af5476616">[ ] unverified</a> | <a href="#case-in_game_placement-8dc51edd2cade606129f">[ ] unverified</a> | <a href="#case-in_game_placement-72f9b61cafbe593b9cfa">[ ] unverified</a> | <a href="#case-in_game_placement-67792913095a38645245">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-b15982836e4af5476616"></a>

**0° CCW: unverified** — `in_game_placement-b15982836e4af5476616`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8dc51edd2cade606129f"></a>

**90° CCW: unverified** — `in_game_placement-8dc51edd2cade606129f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-72f9b61cafbe593b9cfa"></a>

**180° CCW: unverified** — `in_game_placement-72f9b61cafbe593b9cfa`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-67792913095a38645245"></a>

**270° CCW: unverified** — `in_game_placement-67792913095a38645245`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-b15982836e4af5476616">[ ] unverified</a> | <a href="#case-in_game_demolition-8dc51edd2cade606129f">[ ] unverified</a> | <a href="#case-in_game_demolition-72f9b61cafbe593b9cfa">[ ] unverified</a> | <a href="#case-in_game_demolition-67792913095a38645245">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-b15982836e4af5476616"></a>

**0° CCW: unverified** — `in_game_demolition-b15982836e4af5476616`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8dc51edd2cade606129f"></a>

**90° CCW: unverified** — `in_game_demolition-8dc51edd2cade606129f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-72f9b61cafbe593b9cfa"></a>

**180° CCW: unverified** — `in_game_demolition-72f9b61cafbe593b9cfa`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-67792913095a38645245"></a>

**270° CCW: unverified** — `in_game_demolition-67792913095a38645245`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-b15982836e4af5476616">[ ] unverified</a> | <a href="#case-in_game_save_reload-8dc51edd2cade606129f">[ ] unverified</a> | <a href="#case-in_game_save_reload-72f9b61cafbe593b9cfa">[ ] unverified</a> | <a href="#case-in_game_save_reload-67792913095a38645245">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-b15982836e4af5476616"></a>

**0° CCW: unverified** — `in_game_save_reload-b15982836e4af5476616`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8dc51edd2cade606129f"></a>

**90° CCW: unverified** — `in_game_save_reload-8dc51edd2cade606129f`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-72f9b61cafbe593b9cfa"></a>

**180° CCW: unverified** — `in_game_save_reload-72f9b61cafbe593b9cfa`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-67792913095a38645245"></a>

**270° CCW: unverified** — `in_game_save_reload-67792913095a38645245`.

Save, quit, reload and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Journey — hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout | — | <a href="#case-in_game_journey-b6429b406727f01aa01c">[ ] unverified</a> | <a href="#case-in_game_journey-0f861568bfb3fd6a224b">[ ] unverified</a> | <a href="#case-in_game_journey-0aeb89b464e19cfe8b66">[ ] unverified</a> | <a href="#case-in_game_journey-8b93ddce9b231c9e7c11">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout | — | <a href="#case-in_game_journey-f884dff7ea3cee420f0d">[ ] unverified</a> | <a href="#case-in_game_journey-353e6125f24050588cc7">[ ] unverified</a> | <a href="#case-in_game_journey-d329b84c809327a16cc8">[ ] unverified</a> | <a href="#case-in_game_journey-ba90c531b86546395739">[ ] unverified</a> |
| **Journey**<br>Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout | — | <a href="#case-in_game_journey-8fd9e34cff996f9db0ef">[ ] unverified</a> | <a href="#case-in_game_journey-c4f1f98f15b4ac7d6b56">[ ] unverified</a> | <a href="#case-in_game_journey-cb30dda5630e8251e7f4">[ ] unverified</a> | <a href="#case-in_game_journey-eb2090134246d86faa59">[ ] unverified</a> |


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout</summary>

<a id="case-in_game_journey-b6429b406727f01aa01c"></a>

**0° CCW: unverified** — `in_game_journey-b6429b406727f01aa01c`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-0f861568bfb3fd6a224b"></a>

**90° CCW: unverified** — `in_game_journey-0f861568bfb3fd6a224b`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-0aeb89b464e19cfe8b66"></a>

**180° CCW: unverified** — `in_game_journey-0aeb89b464e19cfe8b66`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

<a id="case-in_game_journey-8b93ddce9b231c9e7c11"></a>

**270° CCW: unverified** — `in_game_journey-8b93ddce9b231c9e7c11`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Win>Eout; entry: Win; exit: Eout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout</summary>

<a id="case-in_game_journey-f884dff7ea3cee420f0d"></a>

**0° CCW: unverified** — `in_game_journey-f884dff7ea3cee420f0d`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-353e6125f24050588cc7"></a>

**90° CCW: unverified** — `in_game_journey-353e6125f24050588cc7`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-d329b84c809327a16cc8"></a>

**180° CCW: unverified** — `in_game_journey-d329b84c809327a16cc8`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

<a id="case-in_game_journey-ba90c531b86546395739"></a>

**270° CCW: unverified** — `in_game_journey-ba90c531b86546395739`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Wout; entry: Ein; exit: Wout.

No observation recorded.

</details>


<details>
<summary>Journey — Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout</summary>

<a id="case-in_game_journey-8fd9e34cff996f9db0ef"></a>

**0° CCW: unverified** — `in_game_journey-8fd9e34cff996f9db0ef`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-c4f1f98f15b4ac7d6b56"></a>

**90° CCW: unverified** — `in_game_journey-c4f1f98f15b4ac7d6b56`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-cb30dda5630e8251e7f4"></a>

**180° CCW: unverified** — `in_game_journey-cb30dda5630e8251e7f4`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

<a id="case-in_game_journey-eb2090134246d86faa59"></a>

**270° CCW: unverified** — `in_game_journey-eb2090134246d86faa59`.

Run the declared journey in this direction using its service network.

Scope: Service: hsr; role: primary; journey: 7:Ein>Nout; entry: Ein; exit: Nout.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — hsr → hsr — 12 cases; unverified: 12</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4eeb68533cad2fae0a5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-390c51450274fbfa9e11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a410575a2edbd42f214">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46ac4f8fec749870da83">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b8196d84e3e4e09c0c7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4179518c44200851417">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cb6399782cfcc48caef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a87aeace03527ea748d1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-159f9430cceecc3ec58a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d73bc62a67289cc94d43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4149b08e91539ef056d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bd916bcea3814ccc8f9">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4eeb68533cad2fae0a5e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4eeb68533cad2fae0a5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-390c51450274fbfa9e11"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-390c51450274fbfa9e11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a410575a2edbd42f214"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8a410575a2edbd42f214`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46ac4f8fec749870da83"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-46ac4f8fec749870da83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Wout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b8196d84e3e4e09c0c7d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8196d84e3e4e09c0c7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4179518c44200851417"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b4179518c44200851417`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cb6399782cfcc48caef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9cb6399782cfcc48caef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a87aeace03527ea748d1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a87aeace03527ea748d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Win; to port: Nout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-159f9430cceecc3ec58a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-159f9430cceecc3ec58a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d73bc62a67289cc94d43"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d73bc62a67289cc94d43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4149b08e91539ef056d0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4149b08e91539ef056d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bd916bcea3814ccc8f9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6bd916bcea3814ccc8f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: Ein; to port: Eout; from service: hsr; to service: hsr; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->
