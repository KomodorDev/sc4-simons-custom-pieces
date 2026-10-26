# CAM content dependency audit — 7 September 2026

This is a read-only audit of current official sc4pac metadata and author download pages. No active game files, package profiles, or shared download cache were changed. The full metadata snapshot is in `content-package-audit.json`.

## Installation choices

- `CAM=yes`: install the building lots that use CAM growth stages.
- `nightmode=standard`: select Maxis night lighting, matching the existing game.
- `config:sc4-edition:edition=Windows-digital`: this game is the Windows GOG edition running through Wine, even though the computer uses macOS.

These choices do not install CAM itself. The parent installation task separately selects CAM Controller, SIM, and Ordinances.

## Requested content packages

| Package ID | Current version | What the package installs |
|---|---|---|
| `mattb325:large-modern-hospital` | 1.0 | Both the 7×6 and 10×10 hospitals with the same 32,000-patient capacity. |
| `mattb325:disease-research-center` | 1.0 | The fixed ploppable medical reward and model. The sc4pac selection excludes the bonus growable industrial lot. |
| `cobb:collection-pack` | 1.0.0 | Residential and commercial sets; their child packages select the CAM lots when `CAM=yes`. |
| `cerulean:cerulean-rci-collection` | 1.0.0 | 38 residential, commercial, and industrial component packages; CAM variants are selected in the individual packages. |
| `ulisse-wolf:andisart-cam-building-pack` | 3.0.0 | CAM lots plus their building models, props, and textures. The CAM asset is omitted entirely if `CAM=no`. |

## Seven additional explicit selections

Add these exact package IDs:

```text
ulisse-wolf:building-style-art-deco
ulisse-wolf:building-style-neo-futurism
bsc:mega-props-cp-vol01
bsc:mega-props-cp-vol02
bsc:textures-vol01
bsc:textures-vol02
bsc:textures-vol03
```

The [AndisArt author page](https://community.simtropolis.com/files/file/35516-andisart-cam-building-pack/) lists both architectural styles as dependencies. The package's current sc4pac metadata has the reverse dependency relationship instead: installing AndisArt alone does not bring in these styles. Explicitly selecting them resolves this. Each style depends on `null-45:allow-more-building-styles-dll`, `null-45:sc4-resource-loading-hooks`, and the AndisArt package. Both style packages are currently version 2.0.1.

The [Large Modern Hospital author page](https://community.simtropolis.com/files/file/33034-large-modern-hospital/) requires the five BSC packages listed above, but the hospital's sc4pac metadata omits them. AndisArt already brings in all five. Selecting them explicitly also protects the hospital from losing its dependencies if the AndisArt package is removed later.

These IDs are also recorded one per line in `recommended-extra-package-ids.txt`.

## Sources and checks

- [Large Modern Hospital package source](https://github.com/memo33/sc4pac/blob/main/src/yaml/mattb325/civic/health/large-modern-hospital.yaml)
- [Disease Research Center package source](https://github.com/memo33/sc4pac/blob/main/src/yaml/mattb325/civic/miscellaneous/disease-research-center.yaml)
- [Cobb package source](https://github.com/SC4Evermore/sc4pac-channel/blob/main/src/yaml/Cobb/cobb32118-campatible-residental-lots.yaml)
- [Cerulean package source](https://github.com/SC4Evermore/sc4pac-channel/blob/main/src/yaml/Cerulean/rci-and-cam-compilation.yaml)
- [AndisArt package source](https://github.com/sebamarynissen/simtropolis-channel/blob/main/src/yaml/ulisse-wolf/35516-andisart-cam-building-pack.yaml)
- [Art Deco author page](https://community.simtropolis.com/files/file/36970-building-style-art-deco/)
- [Neo Futurism author page](https://community.simtropolis.com/files/file/36965-building-style-neo-futurism/)

The recursive metadata audit covered 92 packages using the three configured official channels. All referenced package IDs resolved. After selecting the three settings above, there were no unresolved variant choices within this content dependency graph. This count is not the final installation count: it excludes the separate full CAM/SIM dependency graph and includes packages that may already exist in the new profile.

This verifies package choices and dependency declarations. It does not establish that all newly required DLLs work with the exact Wine environment, or that every lot appears correctly in a city. The parent task must perform installation and runtime verification.
