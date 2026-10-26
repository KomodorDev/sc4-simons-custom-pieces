# SimCity 4 regional agent: sample workflows

Draft specification · 7 September 2026

These are proposed interactions for the system described in the [regional agent plan](SimCity%204%20-%20Regional%20Agent%20Research%20and%20Plan.md). They are not demonstrations of a controller that has already been built. Every game-changing operation below depends on a tested implementation for the Windows game under Wine.

Each workflow starts with a user wish, follows the messages between the components, and states the visible result and completion conditions. Numbers, place names, route identifiers and dialogue are illustrative. They do not describe the current contents of your game.

## How to read the diagrams

Read from top to bottom: time progresses downward. Each vertical column belongs to a person or component. A solid arrow sends a request or event; a dashed arrow returns information. A **loop** repeats its enclosed steps. An **alt** box shows alternative outcomes. An **opt** box contains an optional step.

| Participant | Meaning |
|---|---|
| **You** | The person giving instructions or taking control. |
| **Agent** | The AI that interprets the wish, chooses priorities and explains decisions. |
| **Planner** | Software that calculates terrain, routes, construction order and resource requirements. |
| **Records** | The persistent map, asset catalogue, plans, action history and references to backups. |
| **Controller** | The single local program allowed to issue game-changing commands and switch cities. |
| **SC4** | The actual running game; replies are collected through a tested game bridge. |
| **Display** | The regional map and progress panel, shown alongside the real game. |

A **city tile** is one separately loaded city square. A **recipe** is a tested sequence for constructing something, including its required space and validation. A **checkpoint** is a consistent saved copy from which work can be recovered. A **revision** is a numbered version of the plan. An **operation ID** is a unique label that helps distinguish a new instruction from a repeated request.

The display receives factual progress from the controller. The agent adds short explanations. Game screenshots and observations carry capture times and city identities, so an old view is not mistaken for the current city.

## Shared example region

The examples use a fictional region called **Meridia**, with four city tiles:

| Northwest | Northeast |
|---|---|
| Westhaven: planned major centre | Eastbank: planned intermediate centre |
| **Southwest** | **Southeast** |
| Greenfields: farming and protected land | Southport: planned second major centre |

The example express corridor runs **Westhaven → Eastbank → Southport**, crossing two city borders. These names denote city tiles; urban development can extend across their boundaries. The protected hillside, coast and valley are example inputs to planning.

Unless a wish says otherwise, the examples assume the user has already selected a funding policy and defined protected land. Instructions that authorize building can proceed within those limits. A plan preview is informational unless the user asks to review it before construction. Missing essential information or an impossible constraint requires a focused question, rather than an invented answer.

## 1. A regional wish becomes a masterplan and build programme

**User wish:** “Build Meridia around public transport. Put the largest centre at A in Westhaven and another at B in Southport. Connect them by HSR through Eastbank. Preserve the marked hills and coastline. Use my funded-design settings and show me the work.”

**Inputs:** Map pins A and B; protected-area outlines; the chosen funding policy; the region and installed mod catalogue. **HSR** means high-speed rail.

```mermaid
sequenceDiagram
    autonumber
    actor U as You
    participant A as Agent
    participant R as Records
    participant P as Planner
    participant C as Controller
    participant G as SC4
    participant D as Display

    U->>A: Build Meridia from pins A and B, with HSR and protected land
    A->>R: Read region, saved preferences, map marks and available recipes
    R-->>A: Layout, observations, permissions and capability gaps
    opt Essential location or funding information is missing
        A-->>U: Ask for the specific missing decision
        U->>A: Supply the missing information
    end
    A->>C: Survey areas whose information is missing or stale
    loop Each city requiring a fresh observation
        C->>G: Load city and wait until ready
        G-->>C: Confirm city identity and return supported observations
        C->>R: Store observation with city, game date and capture time
        C->>D: Highlight surveyed city and observation coverage
    end
    A->>P: Plan centres, HSR, feeders, utilities and growth phases
    P->>R: Read terrain, assets and tested construction rules
    R-->>P: Data with units, versions and uncertainty
    P-->>A: Candidate plan, costs, dependencies and unresolved constraints
    alt A required feature has no feasible implementation
        A-->>U: Explain the blocked requirement and concrete alternatives
        Note over A,C: Hold affected construction until the requirement is resolved
    else The plan fits the brief and available capabilities
        A->>R: Store masterplan revision 1 and inherited limits
        A->>D: Show city centres, reserved routes and development phases
        A->>C: Start authorized phase 1 using revision 1
        C->>D: Show the active city, work area and next operation
        C->>G: Begin the first tested construction recipe
    end
```

**What you see:** Survey coverage fills in on the region map. Planned centres and corridors appear before physical construction. The game then loads the first work site and follows the initial operation.

**Result:** A recorded masterplan and a dependency-ordered work queue. For example, power and access precede occupied districts; station land is reserved before adjacent dense development. The region is not labelled “finished” when the planning step ends.

**When the wish is “make a plan first”:** End this sequence after showing the masterplan. Execution begins only after a later building instruction.

## 2. Build a high-speed railway across three city tiles

**User wish:** “Build the Westhaven–Eastbank–Southport HSR corridor now, including stations and local public-transport access.”

**Starting conditions:** The corridor has a feasible alignment and verified recipes for its starters, curves, crossings, stations and border connections. If a required recipe is unverified, this workflow first returns a capability gap; it cannot manufacture a supported game command.

```mermaid
sequenceDiagram
    autonumber
    actor U as You
    participant A as Agent
    participant P as Planner
    participant C as Controller
    participant G as SC4
    participant R as Records
    participant D as Display

    U->>A: Build HSR through Westhaven, Eastbank and Southport
    A->>P: Expand corridor into ordered, tested construction recipes
    P-->>A: Terrain, track, stations, feeders and paired border records
    A->>C: Execute corridor H1 under current plan and funding limits
    C->>R: Acquire exclusive ownership and record the intended stage
    C->>G: Complete pending saves at safe points
    G-->>C: Saves completed
    C->>R: Create checkpoint for all affected cities and project records
    loop Westhaven, then Eastbank, then Southport
        C->>G: Load the named city and wait for readiness
        G-->>C: Return verified identity and fresh local state
        C->>G: Pause simulation clock and move camera to the work area
        C->>D: Show city, corridor section and purpose of this work
        loop Each small construction operation
            C->>R: Record operation ID and expected starting state
            C->>G: Apply terrain, track or station operation
            G-->>C: Return result and observed local change
            C->>C: Check geometry, paths, access and observed charge
            C->>R: Record verified result or stop on mismatch
            C->>D: Update completed section and latest game image
        end
        C->>G: Save the city without leaving during the save
        G-->>C: Save completed
        C->>R: Mark this city saved and keep incomplete border pairs pending
    end
    C->>G: Revisit border pairs and verify both endpoints
    G-->>C: Return connection, height and supported route evidence
    alt Suitable housing and jobs already exist
        C->>G: Run bounded simulation visits in the affected cities
        G-->>C: Return supported passenger and station observations
        C->>R: Record usage evidence and its city and date coverage
        C->>D: Show construction and traffic verification separately
    else The corridor is built before demand exists
        C->>D: Show built with passenger test awaiting development
        C->>R: Schedule verification after the relevant districts grow
    end
    C-->>A: Return corridor results and unresolved items
    A-->>U: Explain what is built, what works and what still awaits proof
```

**What you see:** The camera follows terrain preparation, track and station work. When the controller leaves Westhaven for Eastbank, the regional map moves its active-city highlight. A border crossing stays “pending other side” until both ends have been checked.

**Completion conditions:** Correct network types and paths, activated stations, usable access, matching border endpoints and successful save/reopen checks. Passenger operation is a separate result. No claims about individual passengers completing an entire regional journey are made unless the measurements actually support that conclusion.

**Failure example:** A crossing reverts to ordinary monorail or cannot be placed. The controller stops that recipe, marks the section failed and returns the actual state for replanning. Dependent track construction does not continue across the gap.

## 3. Reshape a valley and keep terrain continuous across a border

**User wish:** “Make a gentle rail approach along this valley between Eastbank and Southport. Keep the river and protected forest. Show me the earthworks.”

**Inputs:** A marked corridor; a user-selected limit on terrain changes; protected areas; current terrain and buildings. The example assumes a permitted live-terrain method has passed the tests in the main plan.

```mermaid
sequenceDiagram
    autonumber
    actor U as You
    participant A as Agent
    participant P as Planner
    participant C as Controller
    participant G as SC4
    participant R as Records
    participant D as Display

    U->>A: Shape a gentle rail approach while preserving river and forest
    A->>C: Refresh terrain and occupied land on both sides of the border
    C->>G: Read each affected city at a safe observation point
    G-->>C: Return heights, water level, occupied cells and identity
    C->>R: Store both observations with their dates
    A->>P: Calculate a permitted terrain profile and earthworks
    P->>R: Read protected areas and tested rail slope constraints
    R-->>P: Current limits and construction rules
    P-->>A: Target heights, shared edge values and estimated cut and fill
    alt No terrain profile satisfies the limits
        A->>D: Mark the conflicting hillside, river or occupied area
        A-->>U: Explain the conflict and ask which constraint may change
    else The profile fits the wish
        A->>D: Preview the changed area and before-and-after terrain profile
        A->>C: Apply the bounded terrain stage
        C->>R: Create a consistent checkpoint for both cities
        loop Each affected city
            C->>G: Load city, verify identity and focus the camera
            loop Each small terrain patch in this city
                C->>G: Change permitted heights and allow the screen to render
                G-->>C: Return observed terrain and nearby object state
                C->>C: Compare against the expected patch and protected areas
                C->>R: Record patch result and stop the stage on mismatch
                C->>D: Highlight completed earthworks and any pending shared edge
            end
            C->>G: Save this city's edits before changing cities
            G-->>C: Confirm the save has completed
        end
        C->>G: Revisit both cities to inspect the persisted shared border
        G-->>C: Return persisted heights and affected network state
        C->>R: Commit stage only after both sides pass
        C->>D: Show terrain verified and release the next rail operation
        C-->>A: Return measured changes and estimated earthworks totals
        A-->>U: Report the completed approach and any remaining limits
    end
```

**What you see:** A map preview of the affected area, followed by actual terrain changes in the game. The terrain profile is a side-on chart of height along the route; it makes a steep approach visible before track placement.

**Completion conditions:** Heights match the target within the declared tolerance, the shared edge agrees after reload, protected areas are unchanged, and affected objects remain valid. Cut/fill estimates and in-game expenditure are reported as different measurements.

**Failure example:** The game stops after changing Eastbank but before changing Southport. The stage remains incomplete. Resume only after inspecting both sides; otherwise restore the coordinated checkpoint while the affected cities are unloaded. Do not mark a half-completed border as safe for railway construction.

## 4. Grow a station district and provide adequate services

**User wish:** “Build a dense, walkable district around Southport Central. Give it jobs, schools and a hospital that will not immediately overflow. Use the CAM buildings I installed.”

**Inputs:** Station location, allowed development area, desired density, funding policy and installed assets. **CAM** is the installed Colossus Addon Mod, which expands the development system. **Zoning** designates land where the simulation may grow buildings; it does not guarantee a particular building immediately.

```mermaid
sequenceDiagram
    autonumber
    actor U as You
    participant A as Agent
    participant P as Planner
    participant C as Controller
    participant G as SC4
    participant R as Records
    participant D as Display

    U->>A: Develop Southport Central with dense housing, jobs and services
    A->>C: Inspect population, demand, access, utilities and civic services
    C->>G: Read supported district and city measurements
    G-->>C: Return measurements and identify unavailable fields
    C-->>A: Summarize the current bottlenecks and data gaps
    A->>P: Plan the next affordable and serviceable growth phase
    P->>R: Find installed compatible lots and their capacity and cost
    R-->>P: Catalogue candidates and tested placement capabilities
    P-->>A: Street access, transit feeders, utilities, zoning and civic sites
    A->>C: Execute the next bounded district phase
    C->>R: Record plan revision and create the required checkpoint
    C->>D: Show the district boundary and reserved service sites
    C->>G: Build verified access, utilities and civic infrastructure
    G-->>C: Return placements, connectivity and charges
    C->>G: Apply the planned zones and save
    G-->>C: Confirm zone layout and save completion
    loop Until phase target or simulation budget is reached
        C->>G: Advance a bounded simulation interval
        G-->>C: Return growth, occupancy, service load and budget observations
        C->>R: Store results with the simulated date
        C->>D: Show new development and remaining bottlenecks
        C-->>A: Report measured changes
        A->>P: Evaluate whether to wait, expand services or revise the phase
        P-->>A: Recommend the next action within the user's limits
    end
    A-->>U: Report observed growth, service headroom and unmet conditions
```

**What you see:** Access and infrastructure appear first. Buildings grow as the game simulates. The district display reports actual occupancy and services, rather than treating zoned land as already populated.

**Hospital example:** The planner selects from the actual installed lots, checks placement and recurring costs, and measures effective capacity and patient demand after placement. If funding changes effective capacity, it uses the measured result. A large nominal capacity is not assumed to guarantee coverage of the entire district.

**Completion conditions:** The phase is built and persisted, observed development is reported accurately, and service demands are within the selected limits. If growth stalls, the result names the observed bottleneck or states that its cause is still uncertain. The controller never reports a requested CAM skyline as achieved simply because it placed high-density zoning.

**Loop detail:** A service expansion recommended inside the loop is a new recorded construction operation, checked and executed through the same controller. The agent does not bypass the construction rules by calling it a repair.

## 5. Improve public transport based on observed problems

**User wish:** “Too many people drive into Westhaven. Improve public transport, but preserve the existing homes.”

**Inputs:** The protected housing boundary; current station access and traffic observations; the user's spending limits. The first task is diagnosis: more track is only one possible remedy.

```mermaid
sequenceDiagram
    autonumber
    actor U as You
    participant A as Agent
    participant P as Planner
    participant C as Controller
    participant G as SC4
    participant R as Records
    participant D as Display

    U->>A: Reduce driving into Westhaven without demolishing homes
    A->>C: Refresh relevant cities and collect supported travel measurements
    C->>G: Observe roads, stations, access, housing and jobs
    G-->>C: Return evidence with measurement coverage and game dates
    C->>R: Record the baseline and protected residential lots
    C->>D: Show congestion, station access and areas lacking observations
    A->>P: Diagnose barriers and compare changes within the constraints
    P-->>A: Ranked options with expected effect, cost and uncertainty
    A->>D: Explain the selected intervention and how it will be evaluated
    A->>C: Build the selected feeder, interchange or capacity improvement
    C->>R: Record the intervention and baseline checkpoint
    C->>G: Execute and verify the required construction recipes
    G-->>C: Return physical result and observed cost
    loop Bounded follow-up simulation visits
        C->>G: Advance and observe the affected cities
        G-->>C: Return comparable observations and actual simulated dates
        C->>R: Store post-change evidence
        C->>D: Update results and their measurement coverage
    end
    C-->>A: Return the before-and-after measurements
    alt The selected indicators improved
        A-->>U: Report observed improvement and remaining weak points
    else Improvement is absent or cannot be established
        A-->>U: Explain the result, uncertainty and next diagnostic step
    end
```

**Specific diagnostic examples:** A station may lack walking access; a feeder may end too far away; a useful line may be overloaded; or the supposed regional through-route may be restricted. Each explanation needs evidence before construction is chosen.

**Completion conditions:** The intervention respects protected homes, and the final report shows comparable measurements. If a region-wide public-transport share is unavailable, report the supported city/route indicators instead. Before-and-after changes are observations; continuing population growth can also influence them, so they are not automatically proof of causation.

## 6. Change the station location while construction is running

**User wish:** “Move Eastbank Central to this new pin farther south. Keep the hill untouched and adjust the approaches and feeder routes.”

**Starting conditions:** Revision 4 is running. Some approach track may already exist. The controller must first establish what has happened before calculating revision 5.

```mermaid
sequenceDiagram
    autonumber
    actor U as You
    participant A as Agent
    participant P as Planner
    participant C as Controller
    participant G as SC4
    participant R as Records
    participant D as Display

    U->>A: Move Eastbank Central to the new pin and preserve the hill
    A->>C: Hold all new changes while revising the plan
    C->>D: Show stopping after the current operation
    C->>G: Establish the outcome of the operation already dispatched
    G-->>C: Return observed construction or an unresolved outcome
    alt The current operation remains uncertain
        C->>R: Mark the operation uncertain and retain the hold
        C->>D: Show that recovery is required before replanning
    else The current state is established
        C->>R: Record actual revision 4 work and refreshed local state
        C->>D: Show construction paused and revision 5 being prepared
        A->>P: Replan station, approaches, feeders and reserved development
        P->>R: Read actual work, protected land, limits and user pin
        R-->>P: Current geometry, assets and rebuilding policy
        P-->>A: Revised layout with retained, removed and new work
        alt The change exceeds policy or conflicts with protected land
            A->>D: Highlight the precise conflict and feasible alternatives
            A-->>U: Ask only for the unresolved location or rebuilding decision
        else The revised work fits the authorized limits
            A->>R: Store revision 5 and record why it changed
            A->>D: Preview retained, removed and new construction
            A->>C: Prepare the complete queue for revision 5
            C->>R: Invalidate obsolete work and revalidate retained operations
            C->>C: Switch to the new queue as one coordinated transition
            C->>G: Check current conditions and execute the revised work
            G-->>C: Return observed changes
            C->>D: Follow the new site and show active revision 5
        end
    end
```

**What you see:** “Stopping” changes to “Paused” only after the current operation's outcome is known. The map then shows which existing track stays, which would be removed, and where new work will occur.

**Two important cases:** If the station is unbuilt, only the plan and dependent queued work move. If it is already built, moving it is a demolition-and-rebuild operation with explicit disruption and costs. The established rebuilding policy decides whether that needs a further user decision.

**Completion conditions:** All subsequent operations use the validated revision 5 queue, including unchanged work carried forward. A late reply from revision 4 remains evidence about the old operation; it never restarts obsolete queued construction. The revision covers the station's related paths and utilities, rather than moving only its map marker. The initial design holds all new game changes during this queue transition.

## 7. Let the user take over and then preserve their edits

**User wish:** “Pause. I want to fix this bridge myself. Continue when I tell you.”

**Starting conditions:** The agent is operating the game. Manual control must be a clear handoff: construction, city changes, camera following and automated simulation advances stop before the user is told the handoff is ready.

```mermaid
sequenceDiagram
    autonumber
    actor U as You
    participant A as Agent
    participant C as Controller
    participant G as SC4
    participant R as Records
    participant D as Display

    U->>C: Take over to repair this bridge
    C->>C: Stop new operations, city changes and automatic camera movement
    C->>D: Show preparing manual control
    C->>G: Resolve the current operation and pause simulation if responsive
    G-->>C: Confirm the current city and operation outcome
    C->>R: Record work state and the observation before handoff
    C->>D: Show manual control ready in Eastbank
    U->>G: Edit the bridge and play directly
    Note over C,G: Controller observes where possible but issues no competing changes
    U->>C: Resume agent and retain my bridge
    C->>G: Verify actual region, city, simulation state and edited area
    G-->>C: Return fresh observations and any inspection gaps
    C->>R: Compare with the handoff observation and mark changed areas
    C-->>A: Report user edits and affected planned work
    A->>A: Revise the remaining plan while preserving the user's edits
    alt The manual bridge conflicts with a required connection
        A-->>U: Explain the specific conflict and request the missing decision
        C->>D: Keep construction paused
    else Remaining work can use the edited bridge
        A->>C: Resume with a revised queue and current conditions
        C->>R: Discard obsolete operations and record the retained bridge
        C->>D: Show resuming with your bridge retained
        C->>G: Continue the next verified construction operation
    end
```

**What you see:** Three distinct states: “Preparing manual control”, “Manual control ready”, and “Resuming”. The camera stays under your control during the handoff.

**Completion conditions:** The controller identifies any city you loaded, resurveys areas it could not observe, and preserves manual work in the revised plan. It does not silently overwrite your bridge using an older instruction.

**Failure example:** If a game command is hung, the controller cannot claim that manual control is ready. It shows the unresolved operation and enters recovery. Expiration of a timer does not prove that the game has stopped changing.

## 8. Recover when a command times out or the game crashes

**User wish:** “Continue building the regional HSR line.”

**Fault in this example:** The controller sends a station-placement operation but receives no reply. A missing reply does not establish whether the station was placed.

```mermaid
sequenceDiagram
    autonumber
    actor U as You
    participant A as Agent
    participant C as Controller
    participant G as SC4
    participant R as Records
    participant D as Display

    U->>A: Continue building the HSR line
    A->>C: Resume the current plan under its recovery policy
    C->>R: Record operation H1-042, city, revision and expected starting state
    C->>G: Place the station for operation H1-042
    Note over C,G: No usable reply arrives before the timeout
    C->>C: Stop dispatching further changes
    C->>R: Mark H1-042 uncertain
    C->>D: Show interrupted station placement and last confirmed work
    C->>C: Check game liveness and whether the operation is still running
    C->>G: Reconnect or restart under the selected recovery policy
    G-->>C: Confirm readiness and actual region and city
    C->>G: Inspect station site, paths, terrain and relevant budget evidence
    G-->>C: Return observed current state
    alt Complete result is proved
        C->>R: Record the operation's observed result without replaying it
        C->>G: Verify required persistence and continue with the next operation
        C->>D: Show recovered with station retained
    else No change is proved and no old operation can still execute
        C->>C: Recheck conditions and bounded retry allowance
        C->>R: Record a new attempt for the same logical operation
        C->>G: Retry placement once within the configured retry limit
    else A partial result is proved
        C-->>A: Return the actual partial construction for a repair plan
        A->>D: Show what remains and what repair would change
    else The outcome cannot be established
        C->>D: Show stopped with the missing evidence identified
        C-->>A: Keep dependent construction blocked
        A-->>U: Explain the unresolved operation and recovery options
    end
```

**What you see:** The display states the last confirmed action and marks the interrupted operation “Uncertain”. It does not keep advancing its completion bar while the connection is lost.

**Checkpoint restoration, when necessary:** First show which cities and later progress would be restored. Follow the selected recovery policy; ask if losing that progress is an unresolved decision. Ensure affected cities are unloaded and file writes have ended. Restore the entire affected-city set and matching project state, retain the audit history, then load and verify the restored state before rebuilding the queue.

**Completion conditions:** The controller proves whether the operation happened, avoids duplicates, and resumes from the state that actually exists. Previously observed work may disappear after a crash if it was never saved; the history alone is not proof of persistence. If the last branch applies, the correct outcome is a clear stop, not a claim of recovery.

## 9. Develop and maintain the region for a bounded run

**User wish:** “Keep developing the station towns for the next two hours. Prioritize public transport, keep the existing spending limits, and stop if you lose track of the game.”

**Inputs:** A two-hour real-world limit, per-city simulation limits, development priorities, budget rules and the watchable-build policy. A game month and a real-world minute are different units.

```mermaid
sequenceDiagram
    autonumber
    actor U as You
    participant A as Agent
    participant C as Controller
    participant G as SC4
    participant R as Records
    participant D as Display

    U->>A: Develop station towns for two hours within the current limits
    A->>R: Record deadline, allowed actions and stopping conditions
    A->>C: Start bounded regional development
    loop While the run is active and time remains
        C->>R: Read dependencies, oldest observations and unfinished work
        R-->>C: Next city with a reason for visiting it
        C->>G: Load the next city and wait for readiness
        G-->>C: Confirm identity and supported current measurements
        C->>D: Show active city, its game date and the visit's purpose
        C-->>A: Report growth, transport, services and funds
        A->>C: Select a permitted action or a bounded observation interval
        C->>G: Execute checked work or advance simulation
        G-->>C: Return result and actual simulation progress
        C->>R: Record evidence, costs and affected neighbors
        C->>D: Update completed work and measurement age
        alt Deadline or a stopping condition is reached
            C->>C: Stop dispatch after resolving the current operation
            C->>C: Mark the run inactive so the loop cannot load another city
            C->>D: Show stopping and the reason
        else Further regional work is permitted
            C->>G: Save and return to the region at a safe lifecycle point
            G-->>C: Confirm save and region readiness
        end
    end
    C->>G: Pause and save when responsive and the state is verified
    G-->>C: Return final save result or unresolved condition
    C->>R: Record the run's ending state and outstanding work
    C-->>A: Return measured results and persistence status
    A-->>U: Summarize built work, city dates, costs and remaining priorities
```

**What you see:** The active-city highlight moves with the game. Each city has its own last observed game date; an overview of old data is visibly different from a fresh city observation. Loading, building, simulating, saving and stopping are distinct activities.

**Stopping conditions:** The deadline, a user stop request, a breached financial/service limit, wrong city identity, uncertain command outcome, or observations becoming too old under the chosen policy. Thresholds are selected and recorded before the run; they are not silently invented during execution.

**Completion conditions:** The report distinguishes construction, observed growth, verified transport use and unfinished work. It states which cities were saved successfully. A two-hour limit stops new dispatch; a current game call or final safe save may finish later. A frozen game may prevent a final save and must be reported as such.

## Common execution rules behind every diagram

The diagrams omit some repeated plumbing to keep their main sequence readable. Every construction workflow still follows these rules:

1. **Validate before dispatch.** Check the region, city, plan revision, relevant area, installed capabilities and operation limits. Recheck immediately before the actual game change if other work has occurred since planning.
2. **Keep one writer.** The controller serializes construction, automatic simulation advances, saves and city switching. Before loading another city, establish the outgoing city's save state and finish any required save. This also applies to surveys and resumption after manual play. A manual handoff suspends automatic camera control. Reading the game must occur through safe observation points.
3. **Record before and after.** Persist an operation ID and expected starting conditions before sending a change. Record the actual result and evidence afterward. The same operation may have multiple attempts; those attempts never imply multiple intended stations.
4. **Verify at three levels.** Check physical placement, save/reopen persistence, and simulation behavior where measurable. These can finish at different times and must have separate statuses.
5. **Stop a failed dependency.** A failed terrain patch or connection blocks work that depends on it. A loop in a diagram never authorizes continuing through a failed verification.
6. **Coordinate checkpoints.** Save at safe points, wait for writes and relevant Auto Save activity to finish, and copy a coherent affected-city set. Cross-city stages retain the checkpoint until both sides are verified.
7. **Keep the picture honest.** The display shows the last observed city, operation and capture time. Under the example watchable-build policy, loss of required tracking stops new changes after the current operation is resolved. A stalled image never becomes fabricated live progress.
8. **Ask only for a needed decision.** A valid building wish already authorizes work within its limits. Ask when essential input is missing, a protected constraint must change, or a proposed recovery/rebuild exceeds the recorded policy.

| Status | Exact meaning |
|---|---|
| Planned | Exists in the design; no game change is implied. |
| Queued | Eligible to run after its dependencies pass. |
| Executing | Sent to the game; the outcome is not yet verified. |
| Physically verified | The requested objects or terrain have been observed. |
| Persisted | The required save/reopen verification passed. |
| Simulation verified | Defined behavior was observed with its measurement scope recorded. |
| Awaiting demand | Infrastructure exists, but an operational usage test needs development first. |
| Stopping | New dispatch is halted; the current operation still needs resolution. |
| Paused | New changes are suspended and no previously dispatched command can still execute. |
| Uncertain | A sent operation may have completed or partially completed; inspect before retrying. |
| Blocked | A named dependency, capability or user decision prevents further work. |

Operation status and controller status are separate. A controller can be paused with an uncertain historical result only after proving that the old command can no longer execute. If the command might still change the game, the controller remains stopping or in recovery and cannot release manual control. Even after execution has stopped, uncertain results need inspection before dependent work resumes.

## Suggested implementation order

Start by implementing **workflow 1's survey and recorded plan**, then a small supported portion of **workflow 2** with real observations and camera following. Add **workflow 8's interruption handling** before allowing a long queue. Expand to the full cross-city corridor, terrain work and user handoff. District growth, diagnosis and the two-hour regional run follow once the basic operations and recovery are dependable.

The resulting demonstration should let a user give one regional wish, see a persistent masterplan, watch the game act on it, change their mind, take control, and resume without losing the relationship between the plan and the real region.

The nine diagrams are also provided as individual Mermaid `.mmd` files in [workflow-diagrams](workflow-diagrams). Their syntax was checked with Mermaid 11.17.2; this verifies the diagram notation, not the proposed game integration. The main regional plan contains the research sources and implementation uncertainties behind these workflows.
