# Hospital archive audit — 7 September 2026

Read-only inspection of the three SC4Evermore subset ZIPs already staged in `setup/cam-install/content-downloads`. No active game files or staged lot payloads were changed.

## Verified values in the actual building exemplars

| Building | Lot size | Patient capacity | Coverage radius | Budget Item: Cost | Plop cost |
|---|---|---:|---:|---:|---:|
| Mattb325 Large Modern Hospital | 10×10 | 32,000 | 2,440 | 2,400 + 400 = 2,800 | 7,400 |
| Mattb325 Large Modern Hospital (Urban) | 7×6 | 32,000 | 2,440 | 2,400 + 400 = 2,800 | 7,400 |
| Mattb325 Disease Research Center | 8×6 | 62,500 | 5,800 | 187 | 29,050 |

The Large Modern Hospital has a conflicting **Catalog Monthly Cost** display value of **6,400**. Its actual two Budget Item: Cost entries are **2,400 and 400**. Report the budget entries as the underlying costs; do not claim the archive is internally consistent or silently change the author's file. Actual city budget display is not tested.

Disease Research's health radius/capacity and monthly 187 also match the author page. It has no radiation: its Pollution at center values are 4,3,20,0. Its Budget Department/Line/Purpose arrays each contain two values, but its Budget Item: Cost array contains only one (187). This is how the official staged file is authored; runtime interpretation is not established by this file audit.

Full values and property representations: `hospital-exemplar-audit.json`.

## Models

Both Modern Hospital building exemplars reference resource `5ad0e817-a7ec6a9e-00030000`, which exists in the Modern Hospital model in the same subset ZIP. Its complete family contains twenty S3D entries across the five zoom levels and four rotations.

Disease Research references resource `5ad0e817-1d2d3ba3-00030000`, which exists in its separately staged model ZIP. That model also contains twenty S3D entries across the five zoom levels and four rotations.

The models contain embedded FSH texture entries as well: 168 for Modern Hospital and 96 for Disease Research. This audit confirmed the building-to-model resource references; it did not trace every decorative prop or texture dependency on the lots. Those dependency packs remain necessary.

Exact model file hashes, resource references and S3D instance lists: `hospital-model-references.json`.

## Disease Research Mac Fix

The staged SC4Evermore Disease Research lot still has two Float32 properties encoded as one-element arrays (key type 0x0080, repetition count 1):

- Transit Switch Entry Cost, 0xe90e25a2: 0.0.
- Transit Switch Traffic Capacity, 0xe90e25a3: 100.0.

These are the two properties associated with the documented native Mac transit-enabled-lot bug. Therefore, do **not** claim the SC4Evermore lot is already equivalent to the STEX Mac Fix. That fix is still unavailable for byte-for-byte or property-by-property comparison.

The actual installed game is Windows 641 under Wine, not the native Aspyr game. The native Mac parser issue does not by itself establish a problem in this Windows setup. The original Windows lot remains an official-source alternative, but its distinct provenance and difference from sc4pac's expected Mac-fix asset must be documented if it is substituted.

Current sc4pac metadata deliberately takes only the model from its original asset and the PLOP lot from the separate Mac-fix asset. It does not include the optional growable IHT lot.

## Sources and reusable inspection helper

- [Disease Research author page and Mac-fix instructions](https://community.simtropolis.com/files/file/28014-disease-research-center/)
- [Disease Research sc4pac metadata](https://github.com/memo33/sc4pac/blob/main/src/yaml/mattb325/civic/miscellaneous/disease-research-center.yaml)
- [Modern Hospital sc4pac metadata](https://github.com/memo33/sc4pac/blob/main/src/yaml/mattb325/civic/health/large-modern-hospital.yaml)
- [Original community investigation of the native Mac Float32/repetition problem](https://community.simtropolis.com/forums/topic/759206-mysterious-glitch-for-simcity-4-mac/)

`read_dbpf.py` is a reusable read-only helper for DBPF indexes, QFS decompression and binary exemplar inspection. It validates sizes and fails on unsupported formats instead of modifying files.
