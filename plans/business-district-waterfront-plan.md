# Business district and waterfront build plan

> **Superseded design:** you subsequently chose to keep the HSR circle and extend the tram south. Use the [current HSR circle and south-park tram plan](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/plans/hsr-loop-south-park-tram.md). The earlier removal proposal below is retained only as design history.

Prepared 16 September 2026 from your screenshot. You confirmed that HSR should connect this district to other districts or neighbouring cities.

This is a proposed design, not a modification to your saved city. For the directions below, **north means the top of the screenshot**. The actual compass direction, elevations, map-square counts and connections outside the screenshot have not been measured. The coloured overlay is conceptual; its edges are not exact earthworks boundaries.

![Proposed district layout](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/plans/business-district-waterfront-concept.png)

## The layout

1. **Western transport entrance:** retain a regional HSR connection and one useful station near the existing western approaches. Put a small plaza outside the station, with a connected road and nearby local tram stop. The precise track arrangement needs a wider view of the western approaches before any demolition.
2. **Upper business district:** keep the central roundabout and existing internal streets as the starting framework. Concentrate the tallest offices around the centre and station side. Use shorter buildings and trees toward the parks. Fill awkward triangular leftovers with small plazas rather than forcing large building lots into them.
3. **Northern lower park:** a quieter waterfront with grass, groups of trees and the NBVC stone seawall. A terrace means a relatively flat shelf of land at one height.
4. **Southern lower park:** a more formal leisure area with a plaza, park lawns and viewpoints. Use the same stone seawall for continuity, or your installed Marina Seawall for a short paved section.
5. **Eastern coastal walk:** reserve a continuous strip between the business district and the coast to connect the two parks. A promenade means a walkway along the waterfront. The dotted line in the concept shows its approximate corridor, not a specific network already built.

The intended sequence from inland toward the water is:

**Upper business district → landscaped slope → lower park → promenade → stone seawall → water.**

Initially use a grass/tree slope between upper and lower land. An inland retaining wall (a wall against a change in ground height) can be a later detail. Shoreline seawall stairs are not a general kit for connecting arbitrary inland cliff heights.

## HSR: retain the connection, simplify the route

My design recommendation is to remove the elevated circuit around the centre instead of enlarging it toward the waterfront. Its current shape is not inherently invalid in the game; the issue is how much land and visual space it occupies around a relatively compact district.

**Do not delete both incoming railway legs before checking where they go.** If the loop connects two external routes, first plan a replacement connection near the western edge. If this district is the end of the line, use a station layout verified to work as a terminal. The screenshot does not establish whether the current station can simply be cut off at one end.

NAM HSR uses the game's Monorail network, so the station must support HSR/Monorail traffic. Your installed catalogue contains **HSRP Transit Hub by 3ddz**, searchable with `HSRP`; this is an available asset, not a verified terminal replacement. Ordinary passenger rail stations are not automatically compatible. [Official NAM HSR guide](https://www.sc4nam.com/docs/feature-guides/high-speed-rail/)

Keep the apparent local tram/ground-light-rail routes within the business district as the local transport framework. This division gives regional rail a useful destination and local transit access to the surrounding blocks. [NAM tram guide](https://www.sc4nam.com/docs/feature-guides/light-rail-tram/)

## Start with one small waterfront section

Do this before terraforming the whole peninsula. It establishes a wall height and terrain treatment you can repeat.

1. Pause the city with the pause control beside the simulation speed controls.
2. Choose an empty stretch of northern shoreline, away from the tunnel mouths and their immediate slopes. Aim for about **6–8 map squares along the shore** for the first sample. This is a suggested work area, not a required seawall dimension.
3. Press **O**, click **Buildings & Lots**, and click **Clear filters** so an old selection does not hide the wall pieces.
4. Click the search field and type **Riprap**.
5. Select **Riprap Seawall** in the upper list, select its lot in the lower list, then click **Plop**. A lot is the complete placeable object together with its occupied plot.
6. Move the preview onto the shore. On your Mac keyboard, rotate with **fn + left arrow** or **fn + right arrow**. The rock face should point toward the water.
7. Place one piece if the preview allows it. Inspect it from more than one camera angle: its upper edge should meet the dry land and the rocks should cover the sloping bank. The author does not specify one universal shoreline elevation.
8. If it floats or disappears into the ground, adjust only the small trial area and try again. Do not extend the entire wall until one section fits.
9. Once it fits, place several matching pieces beside it. Use **Riprap Seawall Diagonal** or corner pieces when the shoreline turns.
10. Reserve space immediately behind the wall for the promenade, then add a small lawn or plaza inland of it. This completed sample determines the look of the rest of the waterfront.

The detailed installation and placement reference is in [Riprap Seawalls](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity%204%20-%20Riprap%20Seawalls.md). [Author's wall set](https://community.simtropolis.com/files/file/26175-riprap-seawall/)

## Form the lower terraces

Use the elevation that works in the shoreline sample. **The earlier 15 m tunnel suggestion does not establish the right park height.** A trial drop of 7.5 m can be useful where the land is high enough, but the screenshot does not show whether that is suitable here. Keep the terrace above the water.

For a controlled test of a height change:

1. Open **Transportation → Roads** or **Highways** and find **Hole Diggers and Raisers** near the top.
2. Select it and press **Tab** to cycle the available height changes. Read the displayed height before placing.
3. Use **fn + left/right arrow** to switch between the blue raiser and red digger. A digger lowers land; a raiser raises it. You run the Windows edition through Wine, so use ordinary Tab rather than the special native-Mac shortcut in some NAM documentation.
4. Click once on an empty test square, away from roads, structures and tunnel entrances. The tool changes that square's height and then disappears.
5. To extend a suitable flat level, choose the ordinary **Road** tool and place a single-square road stub on the adjusted ground. Place adjacent single-square stubs outward, inspecting the terrain after each one. Stop before the waterfront slope or protected tunnel terrain. Bulldoze these temporary road stubs afterward.

This is the NAM-documented levelling method. [Hole Diggers and Raisers](https://www.sc4nam.com/docs/feature-guides/hole-diggers-and-raisers/)

Keep the existing north–south tunnel and preserve the land immediately around its openings. Let the park shape bend around those locations. The green concept areas do not mean every square inside them should be lowered uniformly.

Give each lower park one ordinary **Road** connection descending from the upper road system, preferably near its western side. Drag along a sufficiently long gradual slope and use the permitted preview as the guide; the required length depends on the chosen height and terrain. Build that connection before filling its corridor with park lots.

**Riprap Seawall Stairs** and **Riprap Seawall Stairs Small** are decorative. Inspection of the installed files found no functional pedestrian transit connection. They do not replace the road ramp or a properly connected NAM pedestrian network.

## Add the business district after the terrain works

1. Choose two or three candidate office buildings in **O → Buildings & Lots**. Read each lot's size before changing the streets; the lot includes the building and its surroundings.
2. Try one large building near the centre as a scale reference. Keep its road access, power and water available. Manual placement does not guarantee occupancy or prevent abandonment.
3. Fit a few rectangular plots along the internal roads. Use the footprint of the chosen lots rather than assuming all skyscrapers fit a standard block.
4. As a first composition, aim for **4–6 tower sites**, with smaller buildings and open space between them. This number is a design suggestion, not a game requirement.
5. Use **Small Plaza** for awkward corners and the station forecourt. Use **Small Park Green**, **Medium Park Green** or **Large Park Green** where their footprints fit. These names are verified in your installed search catalogue.
6. Leave a clear public route from the station area into the centre and toward each park. Decorative park paths alone do not establish a functional transit network.

Complete one northern waterfront sample and one office block before repeating them elsewhere. This makes the remaining decisions concrete: wall height, park width, building scale and the amount of open space.

## Image provenance

The concept overlay was produced with the built-in image-generation tool using your screenshot. It is an illustration, not measured surveying or a tested rail construction plan. The final image was checked visually; an invented scale bar and uncertain tunnel labels were removed. The prompt history is saved beside this guide.
