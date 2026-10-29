---
title: "Highway agent additions"
summary: "Apply future highway requirements alongside the selected shared workflow without importing rail geometry assumptions."
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

No highway piece or network specification is implemented. Establish actual network, width, traffic side, height, and donor contracts in this domain’s `NETWORK_SPEC.md` when implementing it; do not infer RHW compatibility from a ramp-shaped train preview. Use that specification for highway engineering facts. Shared artwork and document procedures live in [documentation generation](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md). New subjects and guides deliberately migrated to the split layout use README plus TESTING; a piece has three README chapters and the shared six TESTING chapters. Preserve legacy combined guides until deliberately migrated, and record human observations through the [shared testing guide](../../docs/TESTING.md).
