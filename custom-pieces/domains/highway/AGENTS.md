---
title: "Highway agent entry point"
summary: "Route future highway work without importing rail geometry assumptions."
audience: "Coding agents"
document_type: "agent-instructions"
---

# Highway agent entry point

Use the [framework router](../../AGENTS.md), [domain README](README.md), and [assembly-design skill](../../skills/network-assembly-design/SKILL.md) to select the shared workflow. No highway piece or network specification is implemented. Establish actual network, width, traffic side, height, and donor contracts in this domain’s `NETWORK_SPEC.md` when implementing it; do not infer RHW compatibility from a ramp-shaped train preview. Shared artwork and document procedures live in [documentation generation](../../docs/WORKFLOW_DOCUMENTATION_GENERATION.md). New or intentionally refreshed pieces and assemblies use README plus TESTING; a piece has three README chapters and the shared six TESTING chapters. Preserve legacy combined guides until deliberately migrated, and record human observations through the [shared testing guide](../../docs/TESTING.md).
