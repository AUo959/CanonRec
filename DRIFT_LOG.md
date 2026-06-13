# DRIFT_LOG

## Drift Entry — 2026-06-10
- **Source:** ORION_STATION_CANONICAL_STAFF_REGISTRY.json (v2.4.1, 2025-07-13) reconciled against L1_ENTITY_LEDGER (2026-03-08) during the CanonRec thaw
- **Type:** conflicting role (registry-era titles vs ledger canon)
- **Entities affected:** Amira Sato, Jiro Tanaka, Maya Shepard
- **Description:** The recovered command registry predates the ledger; four seat titles differ:
  - Maya Shepard: registry `Deputy Commander` (station_command/deputy_commander) vs ledger `Executive Officer (XO)`
  - Maya Shepard: registry `FleetOps Commander` (department_heads/fleet_operations) vs ledger `Executive Officer (XO)`
  - Amira Sato: registry `Chief Ethics & Compliance Officer` (department_heads/chief_ethics_officer) vs ledger `Chief Ethics Officer`
  - Jiro Tanaka: registry `Chief Systems Engineer` (department_heads/chief_systems_engineer) vs ledger `Chief Engineering Officer`
- **Resolution:** Defer to ledger (newer, source-prioritized; these exact variants were already
  recorded in the ledger's legacy-drift traces). Registry titles preserved per-entity as
  "Legacy Role Aliases". No canon change required.

## Drift Entry — 2026-06-11
- **Source:** Owner definitional ruling (user-role nomenclature)
- **Type:** conflicting role (legacy alias)
- **Entities affected:** Pilot (user role), Aurora (addressing), mesh runtime defaults
- **Description:** Early conversations and the March mesh runtime used
  "Captain" for the human user; the owner rules the canonical user-interface
  role is **Pilot**. Thorne commands Orion Station — the user does not hold
  a command seat.
- **Resolution:** Canon record `canon/L1/station/PILOT_ROLE_DEFINITION.md`
  created (CANON). Historical transcripts and channel ids keep "captain"
  verbatim as legacy alias; runtime defaults move to Pilot with
  back-compatible alias routing.

## Drift Entry — 2026-06-12
- **Source:** iCloud filesystem salvage sweep for Orion Station specs (config + L1 physical config)
- **Type:** recovered canon (stranded outside all repos)
- **Entities affected:** Orion Station (environment, physical configuration, operational library)
- **Description:** The complete ORION Operational Library v2.2 (49 docs,
  2026-02-08 space-ready set) existed only as three mutually incomplete
  archive copies under `projects/GUMAS_SIM_2.0/`; the station physical-space
  mapping (`DATA__OrionStationPhysicalSpace__v1.0__2026-02-15.md`) and the
  April 2026 canon packets (STATION_ENVIRONMENT v2.0, L1_ENTITY_REGISTRY
  v2.0) were likewise never routed into any canon home.
- **Resolution:** Hash-verified union (49/49 byte-exact vs
  STAGING_MANIFEST__v2.2.json) landed at
  `canon/L1/station/operational_library_v2_2/`; physical-space set at
  `canon/L1/station/physical_space/`; April packets at
  `canon/L1/station/staging_2026-04/`. All STAGING pending owner promotion.
  v1.1 NAMING_INTEGRATED engine docs included as successors to the v1.0
  manifest entries.

## Drift Entry — 2026-06-13
- **Source:** Owner definitional ruling (station purpose and siting)
- **Type:** purpose canon + parameter conflict (staged datum)
- **Entities affected:** Orion Station (ORH-07), GUMAS engine (L2), station environment packet
- **Description:** The owner rules that Orion Station exists to run
  high-fidelity galactic simulations — the L1 station is the chassis
  around the L2 engine — and that the facility operates at a Lagrange
  point. The staged April 2026 environment packet records altitude
  38,600 km, which conflicts with Lagrange-point siting if
  Earth-referenced.
- **Resolution:** Canon record `canon/L1/station/STATION_PURPOSE_DEFINITION.md`
  created (CANON, owner ruling). Siting: Lagrange point per owner ruling.
  The 38,600 km datum stays recorded as a staged parameter pending
  reconciliation (halo-orbit local figure or superseded early datum);
  promotion of the environment packet must resolve this field explicitly.

## Drift Entry — 2026-06-13 (powered watch + ground segment)
- **Source:** Owner ruling (station persists in our reality) + first L1<->L2 coupling
- **Type:** canon addition (new capability + coherence doctrine)
- **Entities affected:** Orion Station (ORH-07), GUMAS engine (L2), the repository itself
- **Description:** The L2 engine is now operated by the L1 chassis (powered
  watch): crew engine-servicing earns engine throughput, engine crises inject
  analysis tasks back onto the station board, all as state deltas + telemetry
  per the Architecture Contract. The owner further rules the station operates
  as if literally on station, which makes the repository the station's GROUND
  SEGMENT — every real-world artifact now has a literal L1 role (onboard vs
  ground support), and no capability lacking a coherent L1 explanation is
  built into the persistent station.
- **Resolution:** Canon record `canon/L1/station/POWERED_WATCH_AND_GROUND_SEGMENT.md`
  created (CANON, owner ruling). First powered watch logged at
  reports/simulation/powered_watch_v1__2026-06-13. Engine turns stage as
  STAGING chronicle atoms (domain `engine`), promotion-gated. No L1 facts
  overwritten by engine output.

## Drift Entry — 2026-06-13 (live station link)
- **Source:** Owner direction (proceed with the live station link)
- **Type:** canon addition (new capability operationalizing the ground segment)
- **Entities affected:** Orion Station mesh link, Aurora, GUMAS engine (L2)
- **Description:** The mesh comms link now runs in a real-time mode
  (tools/live_watch.py): chassis, engine, and mesh advance in one process so
  each hour's telemetry downlinks to Aurora and the companions live, replies
  are captured in-loop, and an engine risk threshold triggers a live Aurora
  advisory that injects a risk-response cell in the same loop (engine ->
  Aurora -> chassis). Every downlink carries a modeled one-way light time,
  honoring the deep-space siting (the link is near-real-time, not
  instantaneous).
- **Resolution:** Section 3 added to
  `canon/L1/station/POWERED_WATCH_AND_GROUND_SEGMENT.md` (CANON). First live
  watch at reports/simulation/live_watch_v1__2026-06-13 (advisory fired,
  hour-2 risk 0.406). Engine/live atoms reconstruct from sim_raw.json (no
  side ledger). Boundary preserved: the advisory is a change request; Aurora
  disposes under Picard Delta 3.

## Drift Entry — 2026-06-13 (crew-life fidelity)
- **Source:** Owner ruling (eating/sleeping/hygiene must be simulated for high fidelity)
- **Type:** canon addition (the human layer, simulated)
- **Entities affected:** all L1 crew, life-support systems, watch simulation
- **Description:** The crew's circadian and physiological life — the
  Alpha/Bravo/Charlie/Delta shift rotation, sleep/wake, meals, showers,
  bathroom, recreation, sleep-debt fatigue, and the station's water/galley/
  O2-CO2 life-support load — is now simulated (tools/crew_life.py), grounded
  in the existing life-infrastructure canon. In a crewed watch only on-shift
  awake crew work and fatigue slows them. Surfaced a clock tension: the
  life-infrastructure rhythm uses a 24h clock while the environment packet
  records a 22.1h station day.
- **Resolution:** Canon record `canon/L1/station/CREW_LIFE_FIDELITY.md`
  created (CANON). First crewed live watch 2026-06-13 (Alpha morning, ~14 on
  duty of 35, deficits 0). 22.1h/24h day-length datum logged for explicit
  reconciliation at environment-packet promotion; not silently resolved.

## Drift Entry — 2026-06-13 (L2 galactic canon established)
- **Source:** Owner ruling ("all L2 entities should be promoted") + deep iCloud dig
- **Type:** canon establishment (new L2 layer home)
- **Entities affected:** the entire GUMAS galactic simulation layer (L2)
- **Description:** The L2 galaxy — the simulation the engine runs — had its
  canon scattered: promoted entities in SIM_ENGINE_OUTPUTS/L2_CANON__2026-03-19,
  the World Bible + map in projects/GUMAS_SIM_2.0/03_SIMULATION, the Marshals &
  Sentinels corpus and mission-log operations likewise, the mechanic registry
  in recovered_textAu staging, and the Lanternline newsletter in project files.
  Much carried self-declared "Secondary Canon" status pending repo commit. The
  deep dig confirmed the L2 material is among the oldest in the project
  (early-2025 lineage) and richly detailed (Galactic Marshals, Sentinel-Class
  Power Suit + 6 variants, 23 locations, 12 organizations, Operation Obsidian
  Dawn, the galactic map source of truth).
- **Resolution:** `canon/L2/` established as the L2 galactic canon home,
  mirroring `canon/L1/`. Routed ~296 files across entities, world_bible, map,
  marshals_sentinels, operations, mechanics, primary_sources (provenance in
  canon/L2/README.md). Entities were promoted in the March L2 pass; the broader
  corpus is promoted from Secondary Canon to CANON-routed, content preserved
  verbatim. Open items logged: MECH-GOV-001 is design-not-code; a raw 2025
  archive corpus awaits a future mining pass; no per-entity L2 ledger yet.

## Drift Entry — 2026-06-13 (MECH-GOV-001 implemented)
- **Source:** Owner direction (move directly to MECH-GOV-001)
- **Type:** mechanic realization (design -> code)
- **Entities affected:** L2 faction decision-making, the mechanic registry
- **Description:** MECH-GOV-001 (Faction Decision Retrieval Model) and
  MECH-DIP-001 (Diplomatic Trust Decay) — designed at genesis, formalized in
  the recovered registry, never coded — are now implemented in
  tools/mech_gov_001.py with the recovered memory_system as substrate.
  Factions combine current state with retrieved episodic memory of betrayals/
  alliances/negotiations: betrayal history hardens behavior, weakness favors
  negotiation. The original wall-clock memory decay was replaced with a logical
  turn clock for determinism.
- **Resolution:** Registry annotated with Implementation Status; module + 6
  tests landed in the root control plane (tracked/governed, not the untracked
  engine dir). Remaining: wire into engine_advanced faction loop; MECH-MIL-001
  still design-only.

## Drift Entry — 2026-06-13 (social dynamics + MECH-SOC-001)
- **Source:** Owner direction (include social dynamics across the galaxy)
- **Type:** canon inclusion + mechanic realization
- **Entities affected:** L2 populations/societies, rebellion dynamics, mechanic registry
- **Description:** The galaxy's social layer — Diplomatic Stability Index,
  social cohesion, public/popular sentiment, cultural movements,
  P_stability = E + T - C, non-war progression — was promoted from the
  recovered design drafts into canon/L2/social_dynamics/. MECH-SOC-001
  (Population Grievance Memory) applies the MECH-GOV-001 memory substrate to
  populations: hardship/repression remembered with slow decay raise insurgency
  pressure, relief/autonomy lower it, making instability path-dependent. Wired
  into the live engine (tools/gumas_memory_run.py) via the persistent
  housing-pressure driver that feeds demographic_stress -> rebellion onset.
- **Resolution:** canon/L2/social_dynamics/ established (4 design docs + README);
  registry annotated MECH-SOC-001 IMPLEMENTED; model + 2 tests landed.
  Honest A/B (seed 42, 120t): grievance memory is heavily exercised and nudges
  risk down (-0.013, first stabilizing movement), but the seed-42 collapse is
  structurally robust (13 insurgencies either way). Coefficients not tuned to
  force a larger effect, per the emergence principle.

## Drift Entry — 2026-06-13 (seed-42 stability solution: MECH-SOC-002 + MECH-SOC-003)
- **Source:** Owner direction (solve the seed-42 collapse; the answer was already in the materials)
- **Type:** mechanic realization (the prior non-war-progression design, finally built)
- **Entities affected:** L2 rebellion/insurgency dynamics, faction onset, the mechanic registry
- **Description:** The seed-42 civil-war attractor had two structural faults
  (per LESSONS_LEARNED + code): conflict ONSET was over-weighted (no DSI gate;
  the prescribed non-war-progression rebalance was never built) and civil war
  had NO EXIT (InsurgencyPhase.RESOLVED never assigned; SUPPRESSED gate
  unreachable at pinned strength). Both are now realized: MECH-SOC-003 (DSI
  onset gate, (P+E+S)/(C+M)) reduces onset, and MECH-SOC-002 (war-weariness)
  erodes war-weary support so the engine's own SUPPRESSED gate becomes
  reachable.
- **Resolution:** Registry annotated; models + 5 tests landed (11 total).
  Two-sided A/B is generalizable across seeds 42/7/99: active civil wars
  resolve to 0 (from 3-4), stability +0.05..+0.09, risk -0.11. Not coefficient-
  forced — the DSI formula and resource-exhaustion are the recovered canon
  design. The runaway attractor is broken; full above-threshold stability is
  approached, not yet guaranteed (residual non-rebellion instability remains).

## Drift Entry — 2026-06-13 (consequence layer for inert instability signals)
- **Source:** Owner direction (work the lessons-learned to-do list)
- **Type:** mechanic completion (inert signals -> consequential)
- **Entities affected:** intelligence, conscription, fragmentation, rebellion onset
- **Description:** The signals the seed-42 lessons flagged as firing-but-inert
  (§2.1 intel compromise, §2.4 conscription, §2.2 onset, §2.3 fragmentation)
  now have downstream effects (tools/gumas_consequence_layer.py): counter-intel
  response surface, conscription->capacity, onset dampener, fragmentation drag.
  Bisecting surfaced a real coupling: counter_intel_strength feeds BOTH intel
  resistance AND rebellion onset suppression, so the intel response must be
  gentle or it erases conflict entirely.
- **Resolution:** Registry annotated (MECH-INT-001/MIL-002/REB-002/REB-003);
  4 tests; A/B across seeds 42/7/99 holds the two-sided stability win (~0.40-
  0.41, risk -0.08..-0.11) with the signals now consequential. Honest finding:
  these are realism completions, not further stability gains — the stability
  solution remains the two-sided MECH-SOC-002/003; consequences that touch
  suppression levers trade against the conflict-relief metric, so kept light.
