---
title: "Highway"
summary: "Reserve a separate home for future highway pieces and assemblies without confusing train branches with road ramps."
audience: "Future highway authors and players"
document_type: "guide"
---

# Highway

No highway piece is implemented in Simon's Custom Pieces. The existing ramp-like pieces carry trains; open the [high-speed rail player guide](../high-speed-rail/README.md) for those.

<!-- BEGIN COLLECTIONS -->

## Inventories and collections

- [Individual pieces: 0 menu types](00_pieces/INVENTORY.md).
- [Assembly blueprints: 0 designs](01_assemblies/INVENTORY.md).

<details>
<summary>Named build collections</summary>

A collection selects existing piece types; it is not an additional piece or a one-click assembly.

No named piece collections are registered in this domain.

</details>

<!-- END COLLECTIONS -->

A future highway piece belongs in `00_pieces/<piece-id>/` with one README, its definition and its artwork. A documented combination belongs in `01_assemblies/<assembly-id>/` with a README and TESTING reference. Creating an empty domain or a blueprint does not create a game button; a button requires an implemented, selected piece.

Use the [shared design workflow](../../skills/network-assembly-design/SKILL.md) and [build/install guide](../../docs/BUILD_AND_INSTALL.md) for development. Define the actual highway network, width, traffic side, level and compatible native connections before authoring a piece. Rail heights and train paths are not highway contracts.
