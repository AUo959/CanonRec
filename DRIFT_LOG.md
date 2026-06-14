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

## Drift Entry — 2026-06-13 (post-war recovery: stability components)
- **Source:** Owner direction (take care of the remaining stability-index components)
- **Type:** mechanic completion (population + legitimacy recovery)
- **Entities affected:** faction population_stability, leader legitimacy, demographic drivers
- **Description:** The stability index is 0.35*population + 0.30*legitimacy +
  0.25*trust + 0.10*peace. The lessons found population floored at ~0.09 (§1.5)
  and legitimacy the weakest contributor (§1.6) because the engine only ever
  drags these down and never restores them. MECH-SOC-005 (Post-War
  Reconstruction) lets a faction at peace rebuild population stability and
  legitimacy and ease its stress drivers. War-weariness (MECH-SOC-002) was
  extended to cede insurgent territory so the lingering minor-insurgency swarm
  clears (it chronically drags population via the engine's per-insurgency drag).
- **Resolution:** Registry annotated MECH-SOC-005; 2 tests (16 total). A/B
  across seeds 42/7/99: stability lifts to ~0.45-0.49 (+0.09..+0.13) and risk
  clears its 0.540 threshold (0.465-0.505). Stability now straddles the 0.480
  threshold (seed 7 over; 42/99 just under). Honest tension recorded: the
  metric rewards high population = few insurgencies, but realism wants some
  conflict — so onset is not suppressed further to force all seeds over. The
  components are recovered; full above-threshold stability is reached on some
  seeds, approached on others.

## Drift Entry — 2026-06-13 (living galaxy: complacency cycle, MECH-SOC-006)
- **Source:** Owner correction — "if we have over-solved the problem to make
  conflict impossible then we have a serious issue and we're not done."
- **Type:** mechanic completion (break the permanent-peace fixed point)
- **Entities affected:** faction legitimacy, demographic drivers, insurgency
  support/grievance; the global conflict trajectory
- **Description:** The stabilizers (MECH-SOC-002/003/005) all ratcheted up
  monotonically, replacing the seed-42 permanent-civil-war attractor with the
  opposite degeneracy — permanent peace (conflict happened once then flatlined,
  e.g. seed 42 civil-wars/era [0,0,17,6,0,0]). A galaxy where conflict is
  impossible is as unreal as one where it never ends. MECH-SOC-006 (Complacency
  Cycle) models canon's non-war destabilizer: long peace breeds complacency
  (creeping corruption in DSI = (P+E+S)/(C+M)) that erodes legitimacy, worsens
  living conditions, and fuels insurgent support/grievance until conflict recurs;
  serious war purges it. Closes the limit cycle peace→complacency→conflict→renewal.
- **Resolution:** Registry annotated MECH-SOC-006; 1 test (17 total). A/B across
  seeds 42/7/99 (120t): conflict now recurs every era and waxes/wanes (rises,
  peaks mid-run ~90-100, subsides to single digits); stability moves in response
  (~0.46-0.49 final), risk clears 0.540 on 7/99. Honest long-run finding (240t):
  conflict keeps recurring in successive waves but stability drifts to a
  turbulent ~0.38 plateau — never collapsing, never freezing; a realistic
  large-galaxy steady state where localized conflict is always present somewhere.
  Per the emergence principle the cycle is left as an emergent dynamic and its
  full behavior documented, not coefficient-forced to a target number. Both
  degeneracies (permanent war, permanent peace) are now gone.

## Drift Entry — 2026-06-14 (dynamic galaxy: insurgency resolution, MECH-REB-004)
- **Source:** Owner direction — "a galaxy with control dynamics but not yet a
  dynamic galaxy ... war is not the only off-ramp to conflict." Grounded in the
  prebuilt-systems inventory + conflict-machine deep read (reports/analysis).
- **Type:** mechanic completion (give civil wars a resolution off-ramp)
- **Entities affected:** insurgencies (lifecycle/removal), host demographic
  drivers, leader legitimacy, the conflict trajectory
- **Description:** The galaxy ran two parallel conflict systems. Inter-faction
  ConflictState always had a full de-escalation ladder ending in RESOLUTION
  (calc_deescalation_probability, mediation, treaty collapse); the intra-faction
  insurgency layer (rebellion.py) had only military suppression —
  InsurgencyPhase.RESOLVED was declared but never assigned, suppressed movements
  lingered with grievance intact, and the same ~13 wounds reopened forever
  (Observatory roundtable, 2026-06-14). MECH-REB-004 grafts the engine's own
  de-escalation rule onto insurgencies: a grinding, costly, stalemated civil war
  under domestic pressure reaches a negotiated settlement that retires the
  movement and spends its grievance (eased stress + restored legitimacy — a
  peaceful renewal path). Self-limiting; mediation bonus reserved for MECH-DIP-002.
  Also adds D1, an honest internal-conflict-aware stability metric in the
  Observatory (the engine's conflict-relief term is blind to civil war).
- **Resolution:** Registry annotated MECH-REB-004; tests 28 total (mech 14 +
  consequence 4 + observatory 10). Observatory 240-cycle now **DYNAMIC GALAXY —
  CERTIFIED** on seeds 42/7/99: 60-68 negotiated settlements per run, conflict
  cast rotates (distinct insurgencies 13 → 71/74/76), civil wars no longer pile
  up (per-era ~0.5-3.75, 3 waves), honest stability plateau ~0.29-0.33 (below the
  engine's masked ~0.38). De-escalation uses the engine's own formula, not a new
  coefficient set — reuse over reinvention, per the emergence principle. Open
  follow-ups logged: re-derive COLLAPSE_FLOOR against the honest metric (D9),
  minor-insurgency swarm, engine-side RESOLVED removal path (owner clearance).

## Drift Entry — 2026-06-14 (diplomacy off-ramp: mediated settlement, MECH-DIP-002)
- **Source:** Owner direction — "diplomacy and cultural exchange exist as
  meaningful systems"; Phase 1 of the dynamic-galaxy action plan.
- **Type:** mechanic completion (diplomacy as a distinct conflict off-ramp)
- **Entities affected:** insurgencies (mediation_available/mediator_id), host
  legitimacy + demographic drivers (mediated-settlement bonus)
- **Description:** MECH-REB-004 gave civil wars a single generic off-ramp
  (grind to exhaustion). MECH-DIP-002 makes diplomacy a distinct, faster path
  tied to the galaxy's relationships: an insurgency becomes mediation-available
  when its host has a credible third-party broker — a peaceful neighbour it
  mutually trusts (read from the live trust_scores network MECH-GOV-001/DIP-001
  maintain; a faction in its own serious war can't broker). Brokering feeds the
  de-escalation mediation bonus so a well-connected regime gets a faster, more
  durable peace, while an isolated/distrusted one must bleed to exhaustion.
  Emergent, not scripted. Also adds D9: collapse is now gated on sustained
  civil-war load, not a stability scalar (calibration showed the honest scalar
  can't tell health from collapse — both ~0.30 — because conflict is 10% of the
  index).
- **Resolution:** Registry annotated MECH-DIP-002; tests 29 (mech 15 +
  consequence 4 + observatory 10). Observatory 240-cycle stays DYNAMIC GALAXY —
  CERTIFIED on seeds 42/7/99: ~40-56% of settlements now brokered by a trusted
  neighbour (the rest grind), share varying by each seed's trust network;
  living/dynamic invariants all hold (load < 3.0 reference). TRUST_FLOOR=0.58
  calibrated for meaning (both paths present), not a target. De-escalation still
  uses the engine's own formula — mediation only flips its mediation_available
  input. Follow-up: MECH-DIP-003 treaty-enforcement consequences on broken
  settlements (calc_treaty_breach_score already exists).

## Drift Entry — 2026-06-14 (treaty enforcement: peace binds, MECH-DIP-003)
- **Source:** Pillar B finish, dynamic-galaxy action plan.
- **Type:** mechanic completion (give the diplomacy off-ramp stakes)
- **Entities affected:** peace accords (new), host stress + legitimacy, the
  host↔mediator trust edge
- **Description:** A settled peace (MECH-REB-004/DIP-002) was a free, permanent
  win. MECH-DIP-003 makes it bind and break, reusing the engine's own treaty
  machinery (calc_treaty_breach_score/is_treaty_breach). Each settlement registers
  an accord against the stress floor it set; as the complacency cycle rebuilds
  stress above that floor, a heavy backslide breaks the accord — grievance
  resurges (renewed conflict) and a broken brokered peace collapses host↔mediator
  trust, burning the broker's credibility. Repeated breaches compound.
- **Resolution:** Registry annotated MECH-DIP-003; tests 30 (mech 16 +
  consequence 4 + observatory 10). Observatory 240-cycle stays DYNAMIC GALAXY —
  CERTIFIED on seeds 42/7/99: ~5-7 of ~60-70 accords break per run (~10%); living/
  dynamic invariants hold. Honest finding recorded: mediation buys *speed*, not
  guaranteed *durability* — mediated accords break at a similar/higher rate than
  exhaustion ones because the hosts that get brokers are the contested core powers
  whose conditions churn more; this was NOT forced to a durability advantage with
  a resistance coefficient (emergence principle). Breach scoring is the engine's
  own formula; only BACKSLIDE_WEIGHT is calibrated, to the measured backslide
  range. Pillar B (off-ramps) substantially complete: war, exhaustion-settlement,
  brokered diplomacy, binding/breakable treaties all live.

## Drift Entry — 2026-06-14 (authentic decisions: culture-weighted, MECH-GOV-002)
- **Source:** Owner direction — "civilizations make authentic decisions based on
  culture, tradition, internal politics." Pillar C, dynamic-galaxy action plan.
- **Type:** mechanic completion (express culture in behaviour)
- **Entities affected:** the settle-or-grind decision on every faction's civil
  wars; reads each leader's dominant_bias (from charforge traits.json)
- **Description:** Leaders carried distinct dominant_bias labels (zero-sum,
  hyper-rational, fear-based, sunk-cost, survivorship, status-quo, ...) but the
  engine's behavioural knobs were uniform (~0.5), so culture was cosmetic —
  identical conditions yielded identical choices. MECH-GOV-002 (CultureModel)
  translates dominant_bias into a settlement lean applied to de-escalation: a
  zero-sum clan or sunk-cost attritionist grinds on, a hyper-rational or
  survivalist order takes the off-ramp. Accepts both the engine's BiasType.X form
  and the traits.json text form; unknown bias is neutral.
- **Resolution:** Registry annotated MECH-GOV-002; tests 32 (mech 17 +
  consequence 4 + observatory 11). A/B (seeds 42/7/99, culture off vs on):
  settlement rate by bias is uniform (~12-19%) with culture off and tracks the
  cultural lean monotonically with it on — a ~3x spread (zero-sum ~7% vs
  rational ~20%) on the same kind of civil war (n~350+ for major biases). The
  Observatory now reports settlement_rate_by_culture and gates a cultures_diverge
  verdict (spread >=5%; observed 11-13%); 240-cycle stays DYNAMIC GALAXY —
  CERTIFIED. First of Pillar C; escalation_lean exposed but not yet wired. Bias
  labels are the engine's own — authentic decisions from canon culture, not
  invented coefficients.

## Drift Entry — 2026-06-14 (internal politics & succession, MECH-GOV-003)
- **Source:** Owner direction ("internal politics") + look-first sweep of iCloud
  project docs. Canon §13 (Senate_Elections vs Military_Coups), Public_Opinion
  form from text_early_sim_logic.txt, org_union_senate.
- **Type:** mechanic completion (leadership turnover + political consequence)
- **Entities affected:** leader dominant_bias / public_legitimacy / scandals;
  host demographic stress (coup shock)
- **Description:** Leaders could not lose power — no turnover, political
  stagnation. MECH-GOV-003 (SuccessionModel) computes a leader's grip
  (legitimacy minus scandal + war-pressure drag; built on the live signals since
  elite_support/institutional_control are inert ~0.5). When grip collapses past a
  honeymoon, the regime falls — by coup in a militarized polity (hard-line
  successor, shaky legitimacy, a destabilizing stress bump) or election in an
  economic one (pragmatic successor, fresh mandate). Founding character is locked
  at first sight so war-economy drift doesn't make everyone a coup. The successor
  clears scandals and takes a new dominant_bias (a real engine BiasType), which
  flows into MECH-GOV-002 — so a regime change visibly shifts the faction's
  trajectory.
- **Resolution:** Registry annotated MECH-GOV-003; tests 34 (mech 18 +
  consequence 4 + observatory 12). Observatory 240-cycle stays DYNAMIC GALAXY —
  CERTIFIED on seeds 42/7/99: ~8-9 successions/run (coup/election split holds:
  5/3, 7/1, 6/3), 5-7 factions change ruling culture; living/dynamic invariants
  hold. Gates leadership_turns_over. Engine-side leader replacement remains an
  owner-clearance follow-up; Legacy_System / Fame_and_Notoriety from §13 not yet
  modelled. Pillar C: GOV-002 + GOV-003 done; POW-001 remains.
