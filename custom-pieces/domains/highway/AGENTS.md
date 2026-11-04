---
title: "Highway agent additions"
summary: "Apply the measured highway provider and selected shared workflow without importing rail geometry assumptions."
audience: "Coding agents"
document_type: "agent-instructions"
---

<a id="highway-agent-entry-point"></a>

# Highway agent additions

<!-- BEGIN DOCUMENT NAVIGATION -->
[1. Domain workflow](#1-domain-workflow)
<!-- END DOCUMENT NAVIGATION -->

<a id="domain-workflow"></a>

## 1. Domain workflow

Apply the parent [library instructions](../../AGENTS.md) and continue the selected shared workflow; these domain additions do not require restarting workflow selection. Consult the [domain README](README.md) for placement and menu guidance when those features are implemented.

The `scp_highway` provider builds measured native DD RHW-4 crossing channels and authored compact ramp modules. Read the [network specification](NETWORK_SPEC.md) for the exact supported inputs, actual car and pedestrian transports, zero-height pavement datum, native overhang convention, module partition, verification limits, and experimental slope bound. Preserve each retained piece’s allocated identifiers and sparse cell ownership. Do not infer highway compatibility from a rail model, a schematic, or one matching lane.

The [compact diagonal diamond](01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/README.md) uses reusable modules and one cycle button in **Transportation → Highways → SCP → Assemblies**. The pure native crossing remains separately reusable. Standalone Highway buttons go in **Transportation → Highways → SCP → Pieces** and use the **PART HWY** icon format. Shared artwork and document procedures live in [documentation generation](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md). New subjects use README plus TESTING, with measured connections and unverified human game observations generated through `scp_highway.connections`. Preserve the earlier schematic and native audit evidence with its original scope.
