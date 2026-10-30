---
title: "Highway"
summary: "Find the experimental DD RHW-4 and Avenue pieces, their compact assembly, and the separate game-testing requirements."
audience: "Highway authors and players"
document_type: "guide"
---

# Highway

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Inventories and collections](#1-inventories-and-collections) · [2. Design prototypes](#2-design-prototypes)
<!-- END DOCUMENT NAVIGATION -->

The experimental highway provider builds a diagonal NAM DD RHW-4 over a ground diagonal avenue, including a compact four-ramp assembly. DD RHW-4 has two opposing stacked decks: the lower deck is 7.5 m high, and the upper deck is 15 m high. This implementation uses the exact NAM 50 right-hand-traffic profile. Its game placement and traffic behaviour remain unverified.

<!-- BEGIN COLLECTIONS -->

<a id="inventories-and-collections"></a>

## 1. Inventories and collections

- [Individual pieces: 14 menu types](00_pieces/INVENTORY.md).
- [Assembly blueprints: 1 design](01_assemblies/INVENTORY.md).

<details>
<summary>Named build collections</summary>

A collection selects existing piece types; it is not an additional piece or a one-click assembly.

- `ddrhw-diagonal-avenue-crossing`: 1 piece types.
- `ddrhw-compact-diagonal-diamond`: 13 piece types.

</details>

<!-- END COLLECTIONS -->

Each highway type belongs in `00_pieces/<piece-id>/` with its JSONC definition, README, TESTING document, and artwork. A documented combination belongs in `01_assemblies/<assembly-id>/` with a README and TESTING reference. Creating an empty domain or a blueprint does not create a game button; a button requires an implemented, selected piece. Select the highway components and their assembly cycle button under **Transportation → Highways**. The ordinary Avenue construction tool remains under **Transportation → Roads → Avenue**.

Use the [piece and assembly design skill](../../skills/network-piece-and-assembly-design/SKILL.md) and [build/install guide](../../docs/BUILD_AND_INSTALL.md) for development. Define the actual highway network, width, traffic side, level, and compatible native connections before authoring a piece. Rail heights and train paths are not highway contracts.

## 2. Design prototypes

The [compact diagonal avenue diamond](01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md) uses 13 reusable component types and 15 placements, owning 53 construction tiles inside a 10 × 10-tile rectangle. All four highway joins now have actual shoulder-lane driving paths, progressive tapers, short parallel sections, and native-material markings. Both through lanes on each deck remain available. Ramp access permits only adjacent-carriageway right turns. Complete driving curves are approximately 70.33 m lower and 102.21 m upper, including their new flat approaches; active height transitions remain approximately 35.08 m lower and 52.66 m upper. The 30% software grade limit is an experimental bound for this compact layout. The assembly guide explains the intended external Avenue joins, the adaptive-ground implementation, and the separate game checks that remain unverified. The [network specification](NETWORK_SPEC.md) separates measured native facts, authored geometry, and verification limits.
