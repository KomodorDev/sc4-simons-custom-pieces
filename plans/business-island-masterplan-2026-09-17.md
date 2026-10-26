# Business district island — tram research and development proposal

Prepared 17 September 2026 from the current screenshot, project installation records, the installed-NAM crossing investigation, and fresh checks of official NAM documentation and creator pages.

**Recommendation:** keep the HSR ring. Extend its interior tram to the southern park through a short legacy tram underpass. Extend the hub's light rail north using the existing raised spur, then a transition to ground tram in the open northern interior.

For this guide, north means the top of the screenshot. The screenshot does not establish actual compass direction, grid coordinates, heights, network identity at every spur, or whether existing crossings carry traffic. No city saves or game plugins were changed.

![Business island design concept](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/plans/business-island-masterplan-2026-09-17.png)

The image is an architectural and landscape illustration: it shows proposed building scale, open space and district character. It is not a tile-accurate transport blueprint or a catalogue of exact installed building models. Generated route annotations were removed because they did not accurately reproduce the required network connections. Follow the construction arrangements below for tram work.

## Terms and evidence

- **NAM:** Network Addon Mod, the installed transport expansion; your project records identify version 50.
- **HSR:** High Speed Rail. NAM implements it using the game's Monorail network.
- **GLR:** Ground Light Rail, NAM's tram track on the ground. It uses the game's Elevated Rail network underneath its changed appearance.
- **Transition:** a supplied piece or lot that connects two network forms, such as elevated light rail and ground tram.
- **FLUP:** Flexible Underpass. This proposal uses the older tram puzzle pieces: individually placed tunnel components.
- **Orthogonal:** aligned with one direction of the square game grid. A grid-aligned line appears slanted on an isometric screenshot.
- **Lot:** the whole plot occupied by a building, station or park, including its surroundings.

Official documentation establishes supported features. The earlier local investigation establishes exact installed names, footprints and hidden traffic paths. A hidden traffic path is the route the simulation can use inside a network piece. These checks do not prove that the proposed pieces fit this particular city until they are placed and carry traffic.

## 1. Right-hand tram: business district to southern park

### Options

| Option | What the evidence establishes | Recommendation |
|---|---|---|
| Legacy tram FLUP beneath straight HSR | Official menu entry and installed matching tram paths, ramps and crossing | First choice: retains the HSR structure and light-rail travel type |
| Tram → Subway → Tram | Suitable transition lots are installed; creators document the conversion | Fallback when an underground route needs more freedom |
| Ground tram × ordinary Monorail piece between HSR approaches | A real crossing piece exists and the local audit found compatible upper endpoints | Test only; the upper crossing looks like ordinary Monorail, and the assembled route is untested |
| Ground tram directly under an unchanged HSR-style span | No suitable native surface crossing established by the installed audit | Do not design around it as a proven option |

The official [HSR menu list](https://www.sc4nam.com/docs/feature-guides/high-speed-rail/#list-of-menu-items) explicitly includes underground-route crossings under straight HSR. The detailed [installed crossing investigation](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/research/tram-under-hsr-2026-09-17/Findings%20and%20building%20guide.md) identifies the exact usable tram arrangement.

### Where to put it

Continue from the existing tram corridor around the central roundabout inside the right-hand loop. Separate the tram from the avenue before reaching the railway boundary. Shift its approach toward a **straight, grid-aligned stretch of the southern HSR edge**, away from the tight southwestern curve. Keep the crossing on flat ground. Beyond the crossing, continue through the park east/right of the existing road tunnel entrance, finishing at an inland plaza.

The screenshot is not sufficient to select an exact crossing tile. If the desired straight segment is too short, adjust a short section of the HSR alignment or use the subway alternative; do not force a crossing onto a curve.

The compact tram-only arrangement is:

```text
District surface tram
        ↓
Ramp down: 3 tiles
        ↓
Under-HSR crossing: 1 tile — HSR continues above
        ↓
Ramp up: 3 tiles
        ↓
Park surface tram → flat stop and plaza
```

**3 + 1 + 3 = 7 tiles**, plus outside approaches. This is the sum of installed component footprints, not a tested minimum-clearance guarantee. The avenue is not included in this one-tile-wide tunnel.

### Build sequence

1. Pause the city. Try the crossing on spare flat land before committing buildings to its final corridor. A test prevents the later skyline or park from occupying space needed by the ramps.
2. Choose a straight HSR section and a perpendicular tram approach on the game grid. Leave three tiles on each side for the ramps, plus approach space.
3. Click **Transportation → Rail → High Speed Rail**. Press **Tab** until the tooltip reads **Straight underground route under HSR (no pillar)**. Use the tooltip rather than counting key presses.
4. Rotate with **Home/End**. On your Mac keyboard these are **fn + left arrow / fn + right arrow**. Align the elevated rails with HSR, then place the crossing. The tunnel direction must point across the HSR toward the tram approaches.
5. In **Transportation → Rail**, select **Tram-FLUPs - Flexible UnderPasses**. Find **Ramp for underground tram**.
6. Place one ramp on each side, with their low ends facing the crossing and surface ends facing away. If there is a gap underground, fill every tile with matching old FLUP underground pieces. Empty land alone does not connect this system.
7. Connect the surface ends to GLR. Place a **Draggable Ground Light Rail (Tram)** starter on a clear approach, then draw the ordinary **Elevated Rail** tool through the starter. The starter changes the drawn track to ground-level tram.
8. Connect the district tram to this approach. If it is Tram-in-Avenue, the installed **Tram-Avenue transition to straight Tram and Avenue curve** is a candidate that sends the road aside while the tram continues. Find it under **Transportation → Miscellaneous Transportation → Ground Lightrail → Tram-Avenue (GroundLightRail / Avenue) - Dual Network Pieces**, cycling with **Tab**. Fit its actual preview on flat land; relocate the split if necessary.
9. Keep the underpass flat. If the park is lower, make the terrain descent after the outside ramp, with flat track before the stop. No reliable slope length or park height can be measured from this screenshot.
10. Press **O → Buildings & Lots → Clear filters**, search **Orthogonal Tram Station by NOB**, select its **2 × 1** lot and click **Plop**. Place it on flat straight GLR. The separate-track version is appropriate here; the similarly named Tram-in-Avenue station is for a different track layout.
11. Draw **Elevated Rail** through the standalone tram station to activate its connections. Give it usable street/road or pedestrian-network access, and connect nearby commercial lots to streets.
12. When the connected districts have actual commuters, use **Route Query** on the tram and HSR approaches. Check that both routes pass through the crossing. Zero traffic before there is travel demand does not prove that the crossing is broken.

The precise crossing and ramp names above come from the installed data audit. Select **no pillar**: the inspected **with pillar** alternative routes its underground paths parallel to HSR and is not the perpendicular arrangement described here.

Do not substitute the newer Highway-menu FLEX FLUP portals. That newer system carries road traffic and its documented restrictions include HSR. The old tram system and the new road system have different construction rules. [Official FLUP guide](https://www.sc4nam.com/docs/feature-guides/flexible-underpasses/).

### Subway fallback

The installation contains **SFBT Chrisim Subway-Tram Transition**, **RTMT Tram-in-Avenue to Underground Transition**, and **RTMT Tram-in-Road to Underground Transition**. Use the version matching the surface approach, place a compatible transition on the park side, and connect their underground ports with the **Subway** tool. Check each lot's orientation and access requirements. This creates a network conversion; visible tram vehicles do not travel continuously through the underground segment.

These transitions are integrated into NAM; the old download page is useful documentation, not a reason to install duplicate files. [RTMT creator page](https://community.simtropolis.com/files/file/22714-rtmt-glr-transitions/).

## 2. Left-hand tram: hub to northern island

The best route uses the short raised spur ending in the open land above-left of the central glass-roof hub. Its identity as light rail is a visual inference. First confirm the hub name and that the spur connects to its **Elevated Rail** outlet. HSR and Elevated Rail need different tools even when their structures look similar.

The hub appears to be **HSRP Transit Hub by 3ddz**, an installed 8 × 6 station with HSR, Elevated Rail, passenger rail and bus connections. Do not apply the connection layout of the much larger Tokyo Central Station to this hub. [Hub creator description](https://community.simtropolis.com/files/file/19750-hsrp-transit-hub-by-3ddz-refurbished-by-andreas/).

```text
Hub Elevated Rail outlet
        ↓
Existing raised spur and existing approach crossing
        ↓
Elevated-to-ground tram transition in clear land
        ↓
Northern office-campus stop
        ↓
Northern square stop — woodland beyond
```

1. Confirm the hub and spur network types using the game's query information and track connections. Check the existing passage through the approach roads before relying on it.
2. Reuse the existing raised alignment out of the hub. Extend beyond the congested collection of roads and tracks before changing height. This avoids adding another crossing there.
3. Reserve a flat straight patch beyond the current raised stub for the transition. Open **Transportation → Miscellaneous Transportation → Ground Lightrail** if the submenu is present.
4. Select the legacy **Ground Light Rail (Tram)** piece button and cycle with **Tab** to **Elevated to Ground Light Rail**. NAM also supplies a transition with an attached GLR starter. Rotate so the high end faces the hub, place it, then connect the raised approach. Use the preview to establish the actual footprint.
5. Continue the ground tram through the **interior between the two long perimeter roads**. Stay east/right of the separate northern HSR structures. Aim for a simple corridor serving blocks on both sides, using straight segments and supported turns.
6. Put one stop at a central northern office square and one before the wooded cape. Add another only if the eventual blocks need it. Two initial stops are a planning recommendation, not a fixed game rule.
7. Use ordinary GLR station placement and activation as described for the park. Reserve station plots before developing the surrounding offices.

NAM documents the [elevated-to-ground transition and GLR pieces](https://www.sc4nam.com/docs/feature-guides/base-network-additions/#ground-light-rail-puzzle-pieces) and the [starter and station workflow](https://www.sc4nam.com/docs/feature-guides/light-rail-tram/).

If the apparent spur proves to be HSR, connect a new short branch to the hub's actual Elevated Rail port before using this plan. If the existing approach crossing proves unusable, a separate elevated-rail/subway transition and a ground-tram/subway transition provide a fallback to investigate. This is not evidence that the hub itself has a subway connection.

## 3. Other planning questions and proposed answers

| Question | Proposed answer and reason |
|---|---|
| Where should the skyline be tallest? | Inside the right-hand HSR ring. Reserve about 4–6 major tower sites with smaller buildings between them. The picture's heights are a composition target, not exact lot assignments. |
| What belongs in the north? | Medium-height offices, shops and a few optional residential blocks around tram stops. Keep roughly the last fifth of the northern lobe as woodland and park. This is a design allocation, not a measured area. |
| What belongs around the hub? | A recognisable station forecourt, a hotel, shops and medium-height offices. Keep all station access and rail approach space clear. |
| Will the park fill the tram with passengers? | Do not assume it will. Put functioning shops or offices by the arrival square so there can be job destinations as well as scenery. |
| Where will office workers come from? | Initially the mainland or neighbouring districts. Check that the external rail and road connections reach developed residential areas. A few island residential blocks are optional if you want local trips. |
| Do paths and stairs provide access? | Decorative paths may not. Use connected streets or functional pedestrian-network pieces. The local Riprap audit found no pedestrian transit paths in its decorative stairs. |
| Should the whole waterfront be lowered? | Choose its height from a small successful seawall sample. Preserve existing road-tunnel portals and their immediate terrain; the screenshot does not justify a universal drop such as 15 m. |
| What should happen to the red warning symbols in the north? | Query the affected objects and inspect their power/water/access status before building around them. The screenshot alone does not identify each warning. |
| Should every empty plot get a building? | Keep bridge approaches, awkward wedges, rail setbacks and the park green. Fit rectangular building lots to the streets, then use small plazas and trees in leftovers. |
| What services should be reserved? | Sites with road access for fire/police and utilities as the island grows. If adding residences, include the associated education and health coverage. Determine required capacity from the city data views. |

The recommendation about useful tram destinations follows the simulator's documented emphasis on travel between homes and jobs. Busy scenic transit is not guaranteed by station placement alone. [NAM traffic simulator](https://www.sc4nam.com/docs/feature-guides/traffic-simulator/).

For functional pedestrian routes, check the specific lots' paths rather than their visible paving. [Installed Riprap guide](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/SimCity%204%20-%20Riprap%20Seawalls.md).

## 4. Existing assets that can realise the design

These names and sizes come from project installation records, not visual identification of generated buildings. A lot's stated size includes the surrounding plot.

| Installed asset/search term | Size | Suggested use |
|---|---|---|
| Mattb325 Daiwa House Tokyo | 4 × 4 | Northern offices and blocks around the hub |
| PC Yunika Building Shinjuku | 2 × 4 | Shops at station plazas |
| Cobb Emperador Hotel | 4 × 4 | Arrival district near hub |
| Toranomon Hills Station Tower | 13 × 5 | Optional signature office site if the complete footprint fits |
| Orthogonal Tram Station by NOB | 2 × 1 | Separate-track northern and park stops |
| Small Plaza | Check selected lot | Station forecourts and awkward corners |
| Small/Medium/Large Park Green | Check selected lot | Modular park lawns |
| Riprap Seawall, Diagonal and corner pieces | Depends on piece | Rock-lined park shore |

The local Toranomon lot audit reports only **100 units of transit capacity** for its through-avenue lot. Keep the principal avenue beside it rather than using its through-lot road as the island's main traffic route. Its name does not make it an HSR station. [Installed building guide](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/Tokyo%20Hub%20-%20Installed%20Buildings.md).

To find a listed building, press **O → Buildings & Lots → Clear filters**, search the distinctive name, select the building and lot, then choose **Plop**. Look at the placement footprint before changing roads. Manually placing a building does not by itself establish demand, occupancy or working access.

If converting an ordinary road or avenue to a tram dual network later, NAM recommends laying out the ordinary network and zones before adding the tram component, since zone access can be more complicated afterward. [NAM tram guide](https://www.sc4nam.com/docs/feature-guides/light-rail-tram/).

## 5. Order of work

1. Confirm the hub's light-rail outlet and test the southern underpass.
2. Reserve both complete tram corridors, including height transitions and flat station sites.
3. Check power, water and working regional connections; resolve the queried warning icons.
4. Lay out one northern block and one office-core block around real building footprints. Verify access and useful travel destinations.
5. Build the park arrival stop and one small shoreline sample, then extend the matching promenade.
6. Add the rest of the buildings gradually, using occupancy and Route Query to check whether the transport layout works.
7. Finish decorative planting and park details after the transport corridors are secure.

## Image provenance

The final image was produced with the built-in image-generation tool from the supplied screenshot. No in-game construction was performed. The full prompt history is saved beside this guide in [business-island-masterplan-2026-09-17-prompt.md](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/plans/business-island-masterplan-2026-09-17-prompt.md). The retained source screenshot is [business-island-existing-2026-09-17.png](/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/plans/business-island-existing-2026-09-17.png).
