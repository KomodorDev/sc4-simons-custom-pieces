# Toranomon Hills Station Tower dependency audit

Audit date: 2026-09-13. Original archive: `downloads/Toranomon Hills Station Tower.zip`.

The 13×5 lot references exactly three unique prop exemplars and three unique lot textures. Its building model is supplied by its own archive. Standard retaining-wall, foundation and query resources were found in the original game files.

| Resource | Supplier | Result |
|---|---|---|
| Prop `6534284a-98b1856b-199a6a85` — ML street planter 16m | `Moonlight/ML JPN street chg SAM1 prop.dat` | Staged; matching model group `f91d286c` included (20 model entries) |
| Prop `6534284a-200b5863-35a34d09` — RDQ_PROPS_Tree_09 | `RDQ/RDQ_HD_PROPS_Trees.dat` | Staged; matching model group `643b1761` included (20 model entries) |
| Prop `6534284a-200b5863-15a34ce2` — RDQ_PROPS_Tree_05 | `RDQ/RDQ_HD_PROPS_Trees.dat` | Staged; matching model group `c3eb4631` included (20 model entries) |
| Texture `7ab50e44-0986135e-4689e780` | Installed `BSC Textures Vol02.dat` | Already available |
| Texture `7ab50e44-0986135e-1da44650` | Installed `PEG-SUPER_TEXTURES.dat` | Available after PEG MTP installation |
| Texture `7ab50e44-0986135e-1da4466a` | Installed `PEG-SUPER_TEXTURES.dat` | Available after PEG MTP installation |

## Exact staged files

These are untouched original files extracted from the author archives, under `staging/dependencies/`:

- `Moonlight/ML JPN street chg SAM1 prop.dat`: 161,290 bytes; SHA-256 `6d3d05d5052ce2e2cd8c87741fbf0b954afcdc9e0bca8ad36a08bf7c4e863c44`. Source: Moonlight compilation → `ML JPN Street overwrite SAM1/z ML JPN Street MOD chg SAM1.zip` → `z ML JPN Street MOD chg SAM1/ML JPN street chg SAM1 prop.dat`.
- `RDQ/RDQ_HD_PROPS_Trees.dat`: 6,226,681 bytes; SHA-256 `cea6f53ed65971d144476d76830b0b82bb3324516b3dc909058b52330f3eafdb`. Source: RDQ Maxis Night compilation → `SC4D_LEX_LEGACY_RDQ_Collection_MaxisNite_V2.jar` → `installation/RedDonQuixote/RDQ Props/HD Prop Pack#/Tree Props/RDQ_HD_PROPS_Trees.dat`.

The two files contained no resource-ID collisions with the existing live Plugins during the pre-copy audit, excluding the standard compression-directory record. No additional broad BSC pack is required by this lot.

Only the Moonlight prop DAT is selected: the Street Addon Mod network replacement and its other files were not extracted. The SAM9 prop DAT was not selected because it additionally repeats unrelated Maxis and CP exemplars. No RDQ building lots or building model packages were selected.

This audit verifies resource presence and the referenced props' model availability. It is not an in-game visual or traffic simulation test. All live installation is handled by the parent task; this audit subtask only writes staging and records.
