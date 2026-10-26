# Tram beneath HSR — NAM 50 investigation

Checked on 17 September 2026 against the installed Windows game setup and official NAM documentation/source. **An installed legacy tram underpass provides a route beneath HSR.** A visible ground-level tram can also be investigated using a short ordinary Monorail crossing within the HSR route, with a change in the upper track's appearance.

The earlier blanket answer that a tram cannot pass under HSR was too broad. What remains unsupported in this audit is a direct surface-tram crossing with the existing HSR bridge appearance continuing across the crossing tile.

**Verification boundary:** menu names, construction rules, models and traffic paths were inspected. None of these layouts was constructed or traffic-tested in the running game. Game plugins and city saves were not changed.

| Arrangement | Finding | Visual result |
|---|---|---|
| Ground-level tram directly under the existing HSR-style span | No working native crossing found in installed resources/controller | No verified all-HSR-looking surface solution |
| Legacy tram FLUP tunnel under HSR | Crossing, matching ramps and connecting traffic paths are installed | HSR stays elevated; tram disappears into a short tunnel |
| GLR × Monorail puzzle piece between HSR approaches | Crossing exists and its upper paths match the HSR paths after rotation; complete assembly still needs an in-game check | Tram remains visible; upper crossing tile looks like ordinary Monorail |
| Tram-to-subway transitions and a subway connection | Installed alternative using a change of transport type | Tram enters a subway connection |
| L2 Hybrid Railway over GLR | Some unused path records exist, but required construction rules/models were not found | Not a verified construction option |

**The confirmed installed underpass pieces**

Ground Light Rail (GLR) is NAM's name for a tram on separate ground-level tracks. FLUP means Flexible Underpass. Here it refers to the **old puzzle-piece system**, whose pieces must be placed individually. NAM's glossary explicitly includes tram support in that system. The newer draggable road-underpass system has different capabilities. [NAM glossary](https://www.sc4nam.com/docs/reference/glossary/).

The required crossing's exact installed description is **Straight underground route under HSR (no pillar)**. Its traffic paths contain HSR at **15.5 m above ground** and tram traffic at **10 m below ground**, crossing at a right angle. Both have paths in both directions. The tram keeps its light-rail transport type through this underpass; this is not a tram-to-subway conversion.

The matching **Ramp for underground tram** is three map tiles long and one wide. Its three pieces carry the tram from ground level through −3 m and −7 m to −10 m. A matching reversed ramp brings it back up.

The compact arrangement follows from those footprints:

`ground tram → 3-tile ramp down → 1 crossing tile beneath HSR → 3-tile ramp up → ground tram`

This requires a straight seven-tile corridor along the tram route, plus whatever approach tracks your city needs. Seven tiles is the sum of the installed footprints, not an in-game-tested clearance guarantee.

**How to try the legacy underpass**

1. Use a flat test area with a straight HSR section. Make the proposed tram route cross HSR at 90 degrees. This avoids unsupported curve and diagonal combinations.
2. Open **Transportation → Rail** and select the **High Speed Rail** starter/puzzle-piece button.
3. Press **Tab** until the preview description is **Straight underground route under HSR (no pillar)**. The installed controller also puts this five **Shift+Tab** presses backward from the initial HSR starter. Use the displayed description as the check, since reselecting a button can reset its current piece.
4. Rotate using **Home/End**, which on your Mac keyboard are **fn + left arrow / fn + right arrow**. Align the upper HSR track with the existing HSR. Place the piece on that straight section. The underground route must point across the HSR toward the two intended tram approaches.
5. In the **Rail** menu, select **Tram-FLUPs - Flexible UnderPasses**. Its initial piece is **Ramp for underground tram**.
6. Place one ramp on each side of the crossing. The low, underground ends face the crossing; the surface track ends face outward. For the compact arrangement, each ramp's underground end meets the crossing tile directly.
7. Connect normal GLR tracks to both outside ends. Use a **Draggable Ground Light Rail (Tram)** starter and the ordinary **Elevated Rail** drawing tool for the surface GLR approaches. The starter is the small piece that changes the drawn elevated-rail network into ground tram tracks.
8. If you leave extra space between a ramp and the HSR crossing, fill **every** intervening underground tile. The old **Flexible Underpasses (FLUPs) under various surfaces** button includes **Straight underground route under Grass** and **Straight underground route under transparent surface**, both with compatible tram paths at −10 m. Blank land alone does not connect the tunnel.
9. Use **Route Query** after the line has actual commuters to check that traffic traverses the crossing. An empty route-query result on a line with no travel demand is inconclusive. Also check that trains still traverse the upper HSR line.

The similarly named **with pillar** HSR underpass variant has underground paths running **parallel** to the HSR in the inspected definition. For this perpendicular crossing, select **no pillar**.

Use the old tram FLUP pieces throughout this tunnel. Do not fill its gap using the Subway tool or the newer Highway-menu road FLUP portals. The newer portals support road vehicles and have different HSR restrictions. [NAM FLUP guide](https://www.sc4nam.com/docs/feature-guides/flexible-underpasses/).

**Keeping the tram visible at ground level**

An installed **Ground Light Rail x Monorail Puzzle Piece** contains ground-level tram paths and elevated Monorail paths. HSR is itself based on Monorail. The inspected crossing's upper path endpoints match the straight HSR path endpoints after a 90-degree rotation, including their 15.5 m height. Thus a candidate layout is **HSR → Monorail crossing → HSR**. This conclusion is based on network/path compatibility; placement and actual traffic remain untested. [HSR network definition](https://www.sc4nam.com/docs/feature-guides/high-speed-rail/).

To try it in a test area:

1. Open **Transportation → Miscellaneous Transportation**. If the tools are grouped, open **Ground Lightrail**.
2. Select **Ground Light Rail (Tram)**, the legacy puzzle-piece button, rather than the similarly named draggable starter button.
3. Press **Tab** until **Ground Light Rail x Monorail Puzzle Piece** appears. Rotate it to the intended right-angle crossing and place it.
4. Connect the ground tram ends to GLR approaches. Use GLR starters where necessary to join draggable track to the static piece.
5. Connect the upper track ends to the HSR approaches with the **Monorail** drawing tool, ending at the crossing piece rather than drawing through and replacing it. Use an HSR starter on each approach if the HSR appearance does not continue there.
6. Expect the crossing tile itself to retain an ordinary Monorail beam. Check actual commuter routes on both lines before using this in the city.

NAM officially lists the Monorail crossing. It does not list a corresponding HSR crossing. [Ground Light Rail puzzle-piece list](https://www.sc4nam.com/docs/feature-guides/base-network-additions/#ground-light-rail-puzzle-pieces).

For the original tram-in-avenue question, the analogous **Tram-Avenue under Monorail** pieces are also installed. Accepting a Monorail-looking upper span may therefore avoid separating the tram from the avenue, but that full assembly also remains untested. The standalone tram FLUP crossing above does not by itself preserve an additional surface avenue on the same tile.

**Technical evidence retained**

The relevant extracted paths are saved in [installed-path-evidence.json](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/research/tram-under-hsr-2026-09-17/installed-path-evidence.json). Resource IDs below identify particular records inside NAM's DAT archives; no knowledge of these IDs is needed to build the route.

| Resource ID | Finding |
|---|---|
| `53e67c00` | HSR +15.5 m; crossing tram −10 m; controller puzzle `C017` |
| `53e67e00` | HSR +15.5 m; underground route parallel to HSR |
| `584b3e00`, `584b3e10`, `584b3e20` | Three parts of the standalone tram tunnel ramp, controller puzzle `B400` |
| `53e61400`, `53e61000` | Grass/transparent-surface tunnel fillers carrying tram traffic |
| `580e0700` | GLR at 0 m beneath Monorail at +15.5 m; static puzzle `B12F` |
| `5dd31500` | Ordinary straight HSR path used for the endpoint comparison |

All 221 paths in the installed **High Speed Rail.dat** were parsed. None provides ground-level tram below elevated HSR. A broader scan inspected 71,985 path records across 350 NAM archives; all relevant HSR, GLR and Hybrid Railway path records parsed successfully. No installed HSR model override for the standard GLR × Monorail piece was found.

Four apparently promising L2 Hybrid Railway/tram path records were found in a left-hand-traffic archive, but the matching models, right-hand-traffic paths and construction rules were absent. Those isolated records do not establish a usable crossing.

Historical cleanup lists refer to old HSR-over-GLR patch filenames. They do not establish compatibility with the current installed NAM. No current compatible download was verified during this investigation.
