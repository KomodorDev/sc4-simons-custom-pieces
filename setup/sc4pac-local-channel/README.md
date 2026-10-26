# Local sc4pac additions

This folder is an active sc4pac channel used by the SimCity 4 Windows profile. Keep this whole folder, including `assets`, `yaml`, and `json`, for package information and reinstall support.

Black Hole Waste Management v2 by gshmails is registered as `local-gshmails:black-hole-waste-management-v2`. The source page lists version 1.0; the title identifies the building as v2. The downloaded ZIP has a lot filename containing v3. Original payload names and bytes are preserved. This local package can be managed and removed through sc4pac. Upstream updates are not automatic: this local metadata and preserved ZIP must be refreshed for a new release.

Scoty Walls Sets is registered as `local-scoty:walls-sets` version `1.2.0`. It includes the current wall lots and submenu patches, plus the original `MGB_UBprop_ScotyWalls.dat` recovered from the author's version 1.1 ZIP because the current archive omits it. The package includes all author-listed mandatory dependencies and the additional `girafe:wheat` dependency identified by resource inspection. `local-mas71:japanese-walls-props` installs only the required All-Design prop DAT from the Japanese Walls Set, without its separate wall lots or conflicting One-Design alternative.

Five unidentified small prop references on ten wall variants remain unavailable in both wall archives and the complete listed dependency packs. Standard concrete straight walls and stairs have no unresolved lot references. Detailed findings and installation verification are in `../scoty-walls/`.
