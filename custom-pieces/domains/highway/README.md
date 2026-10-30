---
title: "Highway"
summary: "Find the diagonal double-decker highway design prototype and distinguish it from implemented highway game pieces."
audience: "Future highway authors and players"
document_type: "guide"
---

# Highway

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Inventories and collections](#1-inventories-and-collections) · [2. Design prototypes](#2-design-prototypes)
<!-- END DOCUMENT NAVIGATION -->

No highway piece is implemented in Simon's Custom Pieces. The existing ramp-like pieces carry trains; open the [high-speed rail player guide](../high-speed-rail/README.md) for those.

<!-- BEGIN COLLECTIONS -->

<a id="inventories-and-collections"></a>

## 1. Inventories and collections

- [Individual pieces: 0 menu types](00_pieces/INVENTORY.md).
- [Assembly blueprints: 0 designs](01_assemblies/INVENTORY.md).

<details>
<summary>Named build collections</summary>

A collection selects existing piece types; it is not an additional piece or a one-click assembly.

No named piece collections are registered in this domain.

</details>

<!-- END COLLECTIONS -->

A future highway piece belongs in `00_pieces/<piece-id>/` with one README, its definition and its artwork. A documented combination belongs in `01_assemblies/<assembly-id>/` with a README and TESTING reference. Creating an empty domain or a blueprint does not create a game button; a button requires an implemented, selected piece.

Use the [piece and assembly design skill](../../skills/network-piece-and-assembly-design/SKILL.md) and [build/install guide](../../docs/BUILD_AND_INSTALL.md) for development. Define the actual highway network, width, traffic side, level, and compatible native connections before authoring a piece. Rail heights and train paths are not highway contracts.

## 2. Design prototypes

The [DD RHW-4 — Diagonal Avenue Diamond](01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md) explores a diagonal stacked highway over a ground diagonal avenue, with four ramps. It contains a reproducible geometric model, top and opposite angled schematics, native-donor measurements, and numerical checks. It is unregistered and has no game menu button, compiled DAT, or recorded game tests. The [network specification](NETWORK_SPEC.md) separates measured native facts from the design assumptions and missing implementation stages.
