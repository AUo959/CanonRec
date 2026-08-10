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

## Drift Entry — 2026-06-14 (galactic power dynamics, MECH-POW-001 — Pillar C complete)
- **Source:** dynamic-galaxy action plan, Pillar C; canon §10 (Alliance_System =
  shifting trust; threat-based response).
- **Type:** mechanic completion (power politics; completes authentic decisions)
- **Entities affected:** the inter-faction trust network (realignment toward/away
  from the hegemon)
- **Description:** Factions ignored the galactic balance of power. MECH-POW-001
  (PowerDynamicsModel) reads the balance each turn (power = 0.45*mil + 0.40*eco +
  0.15*tech), finds the hegemon, and has every other faction realign its trust by
  how threatened it is and by its culture: balancers (zero-sum/fear/sunk-cost/
  confirmation) pull trust away from the hegemon and toward each other,
  bandwagoners (survivorship/status-quo/moral-licensing/rational) pull toward it.
  Operates on the live trust network, so it feeds mediation and disposition.
- **Resolution:** Registry annotated MECH-POW-001; tests 36 (mech 19 +
  consequence 4 + observatory 13). A/B (seeds 42/7/99): bandwagoners end ~0.25-
  0.31 more trusting of the hegemon than balancers, vs ~0 without the mechanic —
  power politics decided by culture. Run-averaged against the current hegemon
  (robust to hegemon shifting); trust bounded. Observatory gates
  power_politics_active; 240-cycle stays DYNAMIC GALAXY — CERTIFIED. REALIGN_RATE=
  0.10 the only knob; stance is the culture's own (GOV-002). Threat-based military
  readiness / deterrence (§10) not yet modelled. **Pillar C (authentic decisions)
  complete: GOV-002 culture + GOV-003 succession + POW-001 power, all driven by
  the same canon dominant_bias.**

## Drift Entry — 2026-06-14 (territorial consequence, MECH-TER-001 — Pillar A begins)
- **Source:** dynamic-galaxy action plan, Pillar A (emergent consequence);
  preceded by an engine-version audit confirming GUMASAdvancedEngine (Forge v3.0)
  is current and exposes the economy this builds on.
- **Type:** mechanic completion (a war's outcome reshapes the world)
- **Entities affected:** faction territory (new), economic_potential ceiling,
  and — downstream — galactic power
- **Description:** Conflict was a self-contained scalar — a war ended and the
  world was unchanged. MECH-TER-001 makes a faction's mature civil wars
  permanently scar its territory (half seceded for good, half reclaimable at
  peace; a ~45% core always held), and the territory still held caps its
  economic_potential (the engine's economic ceiling, which it never lowered).
  Because MECH-POW-001 reads economy, the loss propagates: war-torn factions are
  permanently poorer and weaker, shifting the balance of power. Built on the
  engine's own economy, not invented scalars.
- **Resolution:** Registry annotated MECH-TER-001; tests 38 (mech 20 +
  consequence 4 + observatory 14). A/B (seeds 42/7/99): without it every economic
  ceiling stays 1.0; with it ceilings diverge by war history (spread 0.12-0.37),
  ~4 factions permanently shrink per run, and the war-torn end +0.08-0.16 weaker
  in power than the spared — map -> economy -> power, causal depth > 1. Observatory
  gates consequences_propagate; 240-cycle stays DYNAMIC GALAXY — CERTIFIED.
  Magnitude moderate by design (12-37% loss, core preserved). Pillar A begun;
  ECO-001 (war economy / tech_economic_multipliers) and CUL-002 (assimilation vs
  tradition) remain; l2_state spatial deepening + DIP-005 reintegration noted.

## Drift Entry — 2026-06-14 (war economy & market flux, MECH-ECO-001 — Pillar A)
- **Source:** dynamic-galaxy action plan, Pillar A; canon Public_Opinion =
  Policy_Success - Scandals + Economic_Stability (text_early_sim_logic.txt).
- **Type:** mechanic completion (transient war economy + economy->unrest loop)
- **Entities affected:** faction economic_strength (war scarcity / peace boom);
  population demographic_stress (the feedback)
- **Description:** TER-001 made war's economic damage permanent (the ceiling);
  ECO-001 adds the transient cycle and a feedback loop. War scarcity suppresses a
  faction's output while it fights; peace drives a reconstruction boom back toward
  the territory-capped ceiling; and a depressed economy deepens demographic stress
  -> unrest while a booming one eases it, closing the loop war -> economic
  depression -> grievance -> war.
- **Resolution:** Registry annotated MECH-ECO-001; tests 40 (mech 21 +
  consequence 4 + observatory 15). A/B (seeds 42/7/99): the economy busts in war
  and booms in peace (at-war health ~0.18-0.37 of potential vs at-peace
  ~0.70-0.81, gap +0.44-0.54; peacetime health lifts from ~0.58 without ECO-001 to
  ~0.70-0.81 with it). The feedback loop turns without runaway (mean civil-war load
  unchanged). Observatory gates war_economy_active; 240-cycle stays DYNAMIC GALAXY
  — CERTIFIED. Gentle magnitudes by design. Pillar A: TER-001 + ECO-001 done;
  CUL-002 remains.

## Drift Entry — 2026-06-14 (assimilation vs tradition, MECH-CUL-002 — Pillar A complete)
- **Source:** dynamic-galaxy action plan, Pillar A; canon §12 (Cultural_Identity =
  Assimilation vs Local_Traditions).
- **Type:** mechanic completion (culture-dependent cost of holding conquered ground)
- **Entities affected:** population demographic_stress (identity grievance under
  assimilation); leader legitimacy (accommodation under tolerance)
- **Description:** Holding restive, recently-reconquered ground (TER-001's
  contested territory) is a cultural choice keyed to dominant_bias: assimilationist
  cultures impose identity (control now, identity grievance -> separatist unrest
  later); tolerant cultures preserve local tradition (civic peace, a little
  legitimacy). So conquest costs differently depending on who holds it.
- **Resolution:** Registry annotated MECH-CUL-002; tests 42 (mech 22 + consequence
  4 + observatory 16). A/B (seeds 42/7/99): the cost is real and culture-split
  (both policies exercised every run; ~115-238 assimilations vs ~52-190
  tolerations); civil-war load stays under the 3.0 collapse reference (2.08/1.32/
  1.90). Observatory gates cultural_cost_active; 240-cycle stays DYNAMIC GALAXY —
  CERTIFIED. Honest finding recorded: gentle by design (IDENTITY_GRIEVANCE 0.06) —
  an A/B isolating the mechanic showed its galaxy-level outcome is small/noisy and
  a stronger setting mildly amplified conflict, so it is certified at the
  mechanism level (the policy split), not forced to a measurable outcome. Weakest-
  impact of the three Pillar-A mechanics, stated plainly. **Pillar A complete:
  TER-001 (map->economy->power) + ECO-001 (war/peace economy + feedback) + CUL-002
  (cultural cost of conquest). All three of the dynamic-galaxy clauses now live.**

## Drift Entry — 2026-06-15 (Phase 4: dynamic-galaxy integration certified)
- **Source:** dynamic-galaxy action plan, Phase 4 (integration + roundtable).
- **Type:** program milestone (integration certification) + honest weakness
- **Entities affected:** the whole L2 galactic simulation (11 mechanics, Pillars A/B/C)
- **Description:** Ran the complete dynamic-galaxy loop as one integrated system and
  convened the senior-staff roundtable. All twelve pillar gates pass simultaneously
  on seeds 42/7/99 in one run, determinism confirmed, and the causal loop closes
  end-to-end: culture (GOV-002/POW-001/CUL-002) -> decisions -> conflict ->
  consequence (TER-001 map/economy/power, ECO-001 war economy) -> new conditions
  (weaker factions, shifted hegemon, economic grievance) -> GOV-003 installs a new
  culture -> loop. The galaxy's turn-240 state is the product of its own history,
  not its initial conditions — it acts rather than merely settling.
- **Resolution:** DYNAMIC GALAXY — CERTIFIED at the canonical 240-turn horizon.
  Honest integration finding logged (not buried): a 360-turn stress run shows the
  coupled feedback loops (complacency + economic hardship + territorial decline)
  **compound into a slow conflict-amplifying drift** — cw_load rises from ~1.3-2.1
  at 240t to ~1.9-2.9 at 360t, approaching (not reaching) the 3.0 pinned-conflict
  reference on the most volatile seed; honest stability still plateaus ~0.30 (no
  collapse). Diagnosis: a missing **homeostatic damper** (no counter-force that
  strengthens as conflict rises). Routed as the priority follow-up, to be
  re-certified at the 360-turn horizon; not coefficient-patched under the
  integration banner. The Observatory 240-cycle remains the standing regression
  gate; the 360-turn run is the new long-horizon check. Roundtable receipt:
  reports/simulation/observatory_240_cycle__2026-06-15/integration_roundtable.md.

## Drift Entry — 2026-07-20
- **Source:** April-2025 raw-archive mining, Marshals domain (`archives/session_archives/Au_Archive_323_41/`, "MAS - Glactic Union" + "Team Dev_GUMAS" threads); reconciliation: `_staging/marshals_archive_mining__2026-07-20/RECONCILIATION_REPORT.md`
- **Type:** conflicting role
- **Entities affected:** kael_durn, vael_saros, org_union_marshals
- **Description:** Mar-2025 draft has Kael Durn as "Director of the Galactic Marshals" ("The Iron Sentinel"); locked canon has Vael Saros as Chief Marshal, Durn as Supreme Military Commander.
- **Resolution:** RESOLVED (owner, 2026-07-20) — retconned as prior era: Durn led the Marshals as Director before rising to Supreme Military Commander; office retitled Chief Marshal, succeeded by Saros. Recorded in ARCHIVE_MINING_ADDENDUM__2026-07-20.md (LEDGER-MARSHALS-0005).

## Drift Entry — 2026-07-20
- **Source:** Same
- **Type:** duplicate name / superseded surname
- **Entities affected:** zylox_rhaegos
- **Description:** Early-draft surname "Zylox Verrin" vs canonical "Zylox Rhaegos"; early "Galactic Security Bureau" vs canonical Union Intelligence Bureau.
- **Resolution:** RESOLVED — deferred to canon; superseded names recorded as draft-era artifacts in the addendum.

## Drift Entry — 2026-07-20
- **Source:** Same
- **Type:** ghost entity
- **Entities affected:** org_judicial_council (new), org_union_senate
- **Description:** Marshals oversight model references a "Judicial Council" absent from promoted orgs; "Galactic Senate" used for Union Senate.
- **Resolution:** RESOLVED (owner, 2026-07-20) — org_judicial_council created at STAGING; "Galactic Senate" treated as Union Senate alias.

## Drift Entry — 2026-07-20
- **Source:** Same
- **Type:** schema drift / taxonomy collision
- **Entities affected:** Phantom-Class Stealth Frigate (Marshal fleet classes)
- **Description:** Draft "Sentinel-Class Hunter Vessel" absent from the canonical 6-class fleet table; extended the Sentinel-Class suit-vs-ship naming collision.
- **Resolution:** RESOLVED (owner, 2026-07-20) — ruled an early alias of the Phantom-Class Stealth Frigate; fleet remains six classes; alias registered in Marshal_Starship_Classes.csv.

## Drift Entry — 2026-07-20 (second sweep)
- **Source:** Charter-detail review of April-2025 archives (same mining corpus)
- **Type:** conflicting role / intra-source contradiction
- **Entities affected:** org_union_marshals, zylox_rhaegos
- **Description:** A governance-overview passage states the Chancellor "has direct oversight over the Marshalls Division," contradicting the owner-approved oversight model (reports to Judicial Council; no chancellor direct orders in investigations).
- **Resolution:** RESOLVED — approved model prevails; contradicting line held as LEGEND_CONTESTED (in-world misreading of appointment/budget influence as direct control). ARCHIVE_MINING_ADDENDUM Part II, LEDGER-DRIFT-NOTE.

## Drift Entry — 2026-07-20 (second sweep)
- **Type:** naming inconsistency (origin correction)
- **Entities affected:** org_union_marshals
- **Description:** The "Marshalls" double-L misspelling, previously recorded as appearing only in two 2026 prose files, is now traced to the Mar-2025 source conversations (45 instances, incl. "Marshalls Division"). The misspelling is source-era, carried forward into later prose.
- **Resolution:** RESOLVED — canonical spelling remains "Union Marshals"; l2_state.py normalization unaffected; dossier corrected.

## Drift Entry — 2026-07-20 (CL-13 rulings)
- **Source:** CL-13 owner rulings over second-sweep finds (April-2025 archives)
- **Type:** conflicting role → resolved as distinct offices
- **Entities affected:** org_sentinel_high_command (new), org_union_marshals
- **Description:** Archive "Grand Marshal" (Sentinel High Command) vs canon "Chief Marshal" (Union Marshals) office ambiguity.
- **Resolution:** RESOLVED (owner, 2026-07-20) — distinct offices: Grand Marshal commands the Sentinel program (SHC, STAGING entity created); Chief Marshal heads the Marshals service. Side effect: GUMAS_Factions.json "Sentinels as parallel substructure" anomaly now coherent. ARCHIVE_MINING_ADDENDUM Part III, LEDGER-MARSHALS-0006.

## Drift Entry — 2026-07-20 (CL-13 rulings)
- **Type:** schema drift / variant-list extension
- **Entities affected:** Sentinel variant taxonomy (LEDGER-SENTINEL-0003)
- **Description:** Diplomatic-Class Sentinel adopted in 2025-03-15 thread conflicts with canonical six-variant list.
- **Resolution:** RESOLVED (owner, 2026-07-20) — admitted as seventh variant "Sentinel-Diplomat" at STAGING (explicit 2025 adoption memo = documented intent); six-variant CANON list unchanged; active-service count unknown, not invented. LEDGER-SENTINEL-0005.

## Drift Entry — 2026-07-20 (Marshals Charter Promotion Pass)
- **Source:** Owner-approved promotion of sim-derived Marshal Charter v0.1
- **Type:** promotion receipt
- **Entities affected:** org_union_marshals (charter fields CANON), org_judicial_council (STAGING→CANON), org_sentinel_high_command (STAGING→CANON; Grand Marshal Aric Thal CANON)
- **Description:** Charter Articles I (three-tier override), II (official-acts immunity), III (9-jurist Judicial Council), V (Grand Marshal incumbent) promoted to CANON. Article IV chronology remains APPROX by design. Derivation grounded in GUMASAdvancedEngine runs, seeds 42/7/99 × 40 turns, findings F1–F8 with receipts.
- **Resolution:** LOCKED at commit. Charter open-question queue LEDGER-CHARTER-0001..0004 closed (0004 as APPROX). Remaining STAGING: Sentinel-Diplomat variant. Remaining UNCONFIRMED: Judicator Prime "supercarrier" gloss.

## Drift Entry — 2026-07-21 (Marshals Closeout Pass)
- **Source:** Owner-approved closeout of the three remaining Marshals-domain holds
- **Type:** promotion receipt
- **Entities affected:** timeline (UFC-E3..E5 added), addendum LEDGER-SENTINEL-0005, vessel_gu_001
- **Description:** (1) Charter Art. IV chronology anchored to the canonical timeline's "~N years ago" convention by deterministic rule (minimal constraint-satisfying timeline; 1 cycle = 1 standard year): pact ~8 ya, first cohort ~4 ya, leadership transition ~2 ya — consistency-checked against Union founding (~75 ya), Rise of AI Warlords (~50–20 ya), and World Bible "recent actions". (2) Sentinel-Diplomat seventh variant promoted STAGING→CANON; service count remains unknown by precedent. (3) "Supercarrier" resolved as CANON hull-type descriptor of CLASS-JUDICATOR-01 — class ID unchanged, no rename.
- **Resolution:** LOCKED at commit. Marshals domain: zero open holds. Claim ledger CL-04c, CL-16 closed.

## Drift Entry — 2026-07-21 (L2 Corpus Audit)
- **Source:** Full audit of canon/L2 vs local corpus (550 source files), all 12 session archives, and registered repos. Report: reports/analysis/l2_corpus_audit__2026-07-21.md (root repo).
- **Type:** audit receipt / schema drift / ghost entities
- **Entities affected:** vessel_gu_013, vessel_gu_014 (invalid tag STAGING_CONFIRMED → STAGING), org_union_intelligence_bureau + org_sentinel_high_command (aliases), org_diplomatic_corps, org_hardliner_warlords, org_imperial_loyalists, org_republican_reformists, org_outer_colony_warlords (new, STAGING)
- **Description:** Raw-archive corpus verified fully mined (323_326 = duplicates; 62_619 = false positive). 7 faction substructures in canonical GUMAS_Factions.json lacked entity records. Xelvani-3/Torix-7 SUPERSEDED tag flagged (outside approved vocabulary) — content untouched, owner ruling queued. No canon-vs-source contradictions found corpus-wide.
- **Resolution:** Hygiene fixes applied; 5 orgs staged; go-forward queue in audit report (Velar + AI-Warlord domain passes, SUPERSEDED ruling, alias enrichment, cloudbank skim).

## Drift Entry — 2026-07-21 (L2 Audit Ruling Batch)
- **Type:** promotion receipt / vocabulary ratification
- **Entities affected:** org_diplomatic_corps, org_hardliner_warlords, org_imperial_loyalists, org_republican_reformists, org_outer_colony_warlords (STAGING→CANON); Xelvani-3/Torix-7 (tag ratified)
- **Description:** Owner rulings: (1) all five audit-staged substructure orgs promoted (names pre-canon in GUMAS_Factions.json; enrichment deferred to domain passes). (2) SUPERSEDED admitted to the certainty vocabulary as a terminal retired-record state — CERTAINTY_TAGS.md created as authoritative vocabulary. (3) Fabric-invariants spec v0.1 ratified in scope (T1-T4/P1-P4/C1-C4) at STAGING; Velar domain pass designated the verification test case, including the aurora-cloudbank-symbolic enforcement trace.
- **Resolution:** LOCKED at commit. Next: Velar pass per FABRIC_INVARIANTS spec §Velar test-case plan.

## Drift Entry — 2026-07-21 (Velar Fabric Pass)
- **Source:** Velar Imperium domain pass per FABRIC_INVARIANTS spec v0.1 §Velar test-case plan (queue item velar-fabric-pass). Receipts: root reports/analysis/velar_fabric_pass__2026-07-21.md; canon/L2/velar/VELAR_FABRIC_PASS__2026-07-21.md (LEDGER-VELAR-0001..0006).
- **Type:** invariant verification receipt / placement contradiction / enforcement-gap audit
- **Entities affected:** loc_vel_surak, loc_vel_surak_megacity_infrastructure_gravity_atmosphere_districts (P1 contradiction, unmodified); virex_talvaren (C1 gap, unmodified)
- **Description:** Static check (new tools/fabric_invariants_check.py, deterministic): T1/T2/C2/C3/C4 PASS; **P1 VIOLATION ×2** — both Vel-Surak location records claim canonical placement while the map authority table (P1 source of truth) holds them at STAGING/"placement TBD"; P3 gaps (null region_id ×2; unexecuted megacity collapse-into-parent). Symbolic-layer trace: aurora-cloudbank-symbolic enforces no fabric invariant semantically (ethics=operational rules, drift responder=generic runbooks, file_lock=write atomicity, sensors=layer provenance). Engine run (GUMASAdvancedEngine, seed 42 × 40 turns, 1,349 events / 153 Velar): T1/T4/C4 PASS; P4 gap — migration events cite no canonical drive/route; turn-1 tech-unlock backfill noted for T4 promotion discipline.
- **Resolution:** OPEN — five owner rulings queued: RULING-VELAR-P1 (placement), RULING-VELAR-P3 (adjacency/collapse), RULING-FABRIC-SCHEMA (placement_rule + character location binding), RULING-FABRIC-WIRING (checker→DriftAlert→DriftResponder), RULING-ENGINE-P4 (route citation). No canon records modified; spec remains STAGING.

## Drift Entry — 2026-07-21 (Velar Fabric Pass — Ruling Batch)
- **Source:** Owner rulings over LEDGER-VELAR-0001..0006 (queue item velar-fabric-owner-rulings)
- **Type:** ruling batch / P1 resolution / record collapse / schema extension
- **Entities affected:** loc_vel_surak (position status canon→staging, prev preserved), loc_vel_surak_megacity_infrastructure_gravity_atmosphere_districts (CANON→SUPERSEDED, alias-forward to loc_vel_surak), 16 mobile-asset records (+placement_rule)
- **Description:** RULING-VELAR-P1 resolved by downgrade — map authority table (P1 source of truth) governs; both Vel-Surak rows remain STAGING/placement TBD, entity records no longer overstate. RULING-VELAR-P3 executed the documented megacity collapse (Xelvani-3 SUPERSEDED precedent); region_id deferred until placement. RULING-FABRIC-SCHEMA: placement_rule on all mobile assets; capsule location_binding approved but queued (sha256-manifested capsules require rebuild). RULING-ENGINE-P4: promotion-gate model — engine flows acceptable, route citation required at promotion (reconciler checklist addition queued). RULING-FABRIC-WIRING: checker→DriftAlert→DriftResponder approved, implementation queued.
- **Resolution:** LOCKED at commit. P1 violations closed; Velar fabric linter exit now clean (gaps documented by design). Open by design: Vel-Surak placement ruling, region anchoring, capsule rebuild, reconciler checks, cloudbank wiring.

## Drift Entry — 2026-07-21 (Vel-Surak Placement Ruling)
- **Source:** Owner ruling RULING-VELAR-PLACEMENT (Velar fabric pass residual)
- **Type:** faction-binding drift correction / placement promotion / zone-entity creation
- **Entities affected:** loc_vel_surak (velar_imperium→galactic_union, region_id=loc_zone_inner_mid_disk_core, position staging→canon); 7 new loc_zone_* macro-zone entities (STAGING); map source-of-truth (§2.1 occupant + §8.7 GU-ECON-01); authority table rows 44/54 (both copies)
- **Description:** Placement review surfaced that primary sources (Physical Galaxy Packet §3.2 CANON; knowledge bundle) define Vel-Surak as the UNION economic capital ("Engine of the Union", Trade Coalition HQ, core world with Prime Ascendancy). The 2026-03-19 velar_imperium binding was name-prefix drift; "Vel-" reflects Velari settlement heritage. Owner ruled: Inner Mid-Disk Core Zone placement, binding corrected with prev preserved, authority row CANON, megacity row SUPERSEDED, seven macro-zone entities created at STAGING for P3 adjacency resolution.
- **Resolution:** LOCKED at commit. Open follow-up queued: Velar Crescent anchor entities (VEL-CORE-01/VEL-BORDER-01 + Ruin/Outer-Colony nodes) so the Imperium's own map anchors have records.

## Drift Entry — 2026-07-21 (Velar Crescent Anchor Pass)
- **Source:** Owner-directed follow-up to RULING-VELAR-PLACEMENT (queue item velar-crescent-anchor-entities)
- **Type:** anchor-record creation / staged interpretive note
- **Entities affected:** loc_vel_core_01, loc_vel_border_01, loc_velar_ruin_worlds, loc_velar_outer_colony_nodes (new, STAGING); loc_vel_surak (heritage_lineage_note, STAGING/INFERENCE_PENDING_SOURCE); authority table (4 rows, both copies)
- **Description:** The Velar Imperium's four map §4 anchor requirements now have entity records: two derived from placed systems (VEL-CORE-01 §8.6, VEL-BORDER-01 §8.5 — position canon) and two anchor-class placeholders (Ruin Worlds, Outer Colony Nodes — position staging, no placed system; placement deferred to future map §8 entries per the epistemic rule). All anchored to loc_zone_velar_crescent. Vel-Surak's Union-entry-via-reformist-founding hypothesis recorded as an explicitly non-citable staged inference.
- **Resolution:** LOCKED at commit. Records remain STAGING pending owner promotion review. Open: system-name ratification for VEL-CORE-01/VEL-BORDER-01; Ruin/Outer placed-system discovery; lineage-note sourcing.

## Drift Entry — 2026-07-21 (Spatha Promotion Pass)
- **Source:** Owner-authorized promotion per reports/analysis/spatha_context_report__2026-07-21.md ("Cross and Vorn Narrative is essential records"); ratifies owner "canon locked" declarations from the 2026-02-01/03 design thread and the L2 sim capture's sec.9 promotion claim.
- **Type:** promotion receipt / roster closure / duplicate consolidation
- **Entities affected:** char_cross, char_vorn, char_roake, char_kade (new, CANON); SPATHA_MODERNA__KIT_DETAIL__2026-07-21.md (new); L2_SIM_CAPTURE__MARSHALS_RANGER_SENTINEL__v1.0.md (landed in canon/L2/operations/); canon/L2/marshals_sentinels/Marshal_Standard_Kit.md (SUPERSEDED pointer)
- **Description:** (G1) Spatha Moderna design canon promoted — three-layer naming (Spatha Moderna/spade), etymology, katana-like powered single-edge profile with sword-and-board doctrine, "worn not brandished" authority register, kit linguistic asymmetry (Spade/Iron/Viper). (G2) L2 sim capture landed in CanonRec honoring its L1-promotion claim. (G3) Roster closure (C4): all four capture-instantiated actors now have records — Cross (field agent, helmet-imaging documentation, data-core access), Vorn (field agent, female per owner correction, bracer repulsion device), Roake (logistics officer/primary pilot, resupply + drone picture), Kade (Sentinel task force). Unestablished details explicitly marked do-not-invent. (G4) Stale marshals_sentinels kit copy converted to SUPERSEDED pointer; operations/ copy canonical. Validator: all four records pass (sole WARN = pre-commit CANON tag, resolved at this commit).
- **Resolution:** LOCKED at commit. Open (G5, optional): equipment-class records for Spade/Iron/Viper; capsule builds for the four characters if engine instantiation is desired.

## Drift Entry — 2026-07-21 (G5 — Equipment Records & Crew Capsules)
- **Source:** Owner-approved G5 completion of the Spatha Promotion Pass
- **Type:** entity creation / capsule build / schema first-rollout
- **Entities affected:** eq_spatha_moderna, eq_mr6_service_revolver, eq_mfr9_viper_rifle, eq_marshal_energy_shield (new, CANON); vessel_gu_015 (new, CANON); char_cross/char_vorn/char_roake/char_kade capsules (new, charforge-capsule-v1.0)
- **Description:** Equipment-class records close G5: each kit weapon/shield now has a linter-checkable entity carrying its established mechanics (MR-6 dual-cell clank, Viper modularity/anti-armor, spade sword-and-board pairing) with do-not-invent guards. Ranger gunboat recorded as vessel_gu_015 (3-crew, twin 360-degree human-AI quad turrets, not cloaked/rapid-concealment, drone platform; name pending ratification) with the P2 placement_rule. Four CharForge capsules built and verified through tools/character_capsule_adapter.py (33 capsules total, all four valid, zero missing/mismatched files); evidence-fact extraction returns promotable established facts. Capsules carry the FIRST location_binding fields (C1 rollout per RULING-FABRIC-SCHEMA): Cross/Vorn/Roake -> vessel_gu_015, Kade -> org_sentinel_high_command. State vectors derived by documented deterministic rule (0.5 baseline, evidence-only deltas <=0.2, big-endian float32).
- **Resolution:** LOCKED at commit. Cross's crew is now engine-instantiable. Open: ship-name ratification for vessel_gu_015; C1 linter check extension to validate location_binding (queue item capsule-location-binding-rebuild now partially satisfied — pattern established, remaining 29 legacy capsules unbound).

## Drift Entry — 2026-07-21 (Roster Closure Pass)
- **Source:** Owner-directed sweep after the union-domain fabric linter flagged Grand Marshal Aric Thal as CANON with no entity record. Full method + findings: root reports/analysis/roster_closure_audit__2026-07-21.md
- **Type:** ghost entity / roster closure (C4)
- **Entities affected:** char_aric_thal, char_lior_serath, char_veyna_koris, char_kael_voss, char_darek_voss (new, CANON)
- **Description:** Deterministic sweep of all canon (L1+L2+L3) for named actors lacking records found two gap classes: (1) Aric Thal — Marshal Charter Article V CANON incumbent (Grand Marshal, SHC) with no record, dual-role career with his Operation Silent Dagger command (LEDGER-MISSIONS-0001) which the Charter's own selection rule cited; (2) the complete Silent Dagger Sentinel team — Lior Serath (Phantom), Veyna Koris (Striker), Kael Voss (Stalker), Darek Voss (Vanguard, KIA) — all named in the canon ledger with no records. All five created from ledger/Charter/SRC-0005 facts only; unestablished detail explicitly marked. Darek Voss recorded status=deceased per C2 terminal-status rule. Kael Voss/Darek Voss shared surname flagged as NOT-established relationship (no kinship inferred); Kael Voss disambiguated from Kael Durn. False positives (role strings, doc titles) excluded and encoded as C4 linter stopwords.
- **Resolution:** LOCKED at commit. Post-closure verification: 0 true roster gaps canon-wide; fabric linter union domain 0 violations across 78 entities (was 1), velar regression clean. Open (optional): capsule builds for the Sentinel five; Sentinel-variant equipment cross-links.

## Drift Entry — 2026-07-21 (Sentinel Team Capsule Build)
- **Source:** Owner-approved follow-on to the Roster Closure Pass (queue item sentinel-team-capsules)
- **Type:** capsule build / lifecycle handling
- **Entities affected:** char_aric_thal, char_lior_serath, char_veyna_koris, char_kael_voss, char_darek_voss (capsules, charforge-capsule-v1.0)
- **Description:** Five CharForge capsules built following the Cross-crew pattern; adapter verification clean (38 capsules workspace-wide, zero missing/mismatched). location_binding: the four living operatives bind to org_sentinel_high_command — deliberately NOT to a vessel, because Silent Dagger's Phantom-Class Stealth Frigate insertion platform has no named hull in canon and one was not invented. Darek Voss (KIA) carries a TERMINAL location binding to loc_blackreach_station with explicit not-a-live-placement basis; his capsule, runtime stub, cns lifecycle_status, and BUILD_RECEIPT all mark the terminal state and record that it is a historical artifact not intended for live instantiation (C2: death terminal absent a canonical revival mechanism). State vectors follow the documented deterministic rule (0.5 baseline, evidence-only deltas <=0.2, big-endian float32) with per-capsule basis in each receipt. Kael Voss/Darek Voss surname ambiguity restated as NOT established in both capsules.
- **Resolution:** LOCKED at commit. Linter extended with a C2 cross-check (active assets may not list deceased personnel on crew rosters) — passes: union 0 violations/83 entities, velar clean.

## Drift Entry — 2026-07-21 (Judicator Prime Promotion Pass)
- **Source:** Owner rulings over the Judicator Prime context report (reports/analysis/judicator_prime_context_report__2026-07-21.md). Receipt: canon/L2/fleet/JUDICATOR_PRIME_PROMOTION__2026-07-21.md
- **Type:** promotion receipt / conflict resolution / registry landing / class-record creation
- **Entities affected:** vessel_gu_001 (specs + crew_ids + class link); 12 new ship_class records (cls_*); 13 vessels (class_entity_id linked); vessel_gu_013/014 (class_open_item flagged); 8 officer capsules rebuilt with location_binding (alric_tann, lyra_voss, elias_radek, adrienne_kovas, nia_veran, rhen_kailo, arin_tavos, elias_drayen)
- **Description:** J1 specifications promoted from two mutually corroborating sources (World Bible sec.4.2 + Ship Registry v1.0). J5 crew-count conflict RESOLVED: vessel figure ~12,000 governs; registry class baseline 2,500 marked SUPERSEDED and retained on cls_judicator for lineage only. J2 senior staff linked both ways — vessel crew_ids plus capsule location_binding (Drayen distinguished as EMBARKED, not ship's company). J3 Ship Registry v1.0 landed in CanonRec canon/L2/fleet/. J4 all 12 ship classes recorded; class references now resolve fleet-wide. Capsules rebuilt with re-derived manifest hashes; no state or behavioral changes. C1 gaps reduced 17 -> 9 workspace-wide.
- **Resolution:** LOCKED at commit. NEW FINDING queued (not repaired): anaya_ral_seyr capsule state.bin is 0 bytes since original promotion commit e34ec16 — state vector never written, capsule fails manifest verification. Flagged rather than re-hashed to avoid laundering a build defect. Also open: Kharon/Sablewake class assignment (Registry sec.5.1 P2).

## Drift Entry — 2026-07-21 (L2 Character Salvage Pass)
- **Source:** Filesystem-wide L2 named-character sweep (5,711 files, all repos + archives + note dumps). Report: root reports/analysis/l2_character_salvage_audit__2026-07-21.md. Owner rulings 2026-07-21.
- **Type:** ghost-entity salvage / alias drift / disambiguation
- **Entities affected:** char_eriana_vos, char_selia_trask (new, STAGING, +capsules); char_haden_korr (new, UNCONFIRMED, no capsule); lirian_vael_torin (alias "Lirian Vos"/"Vos"), rhaegon_torr_kai (alias "Rhaegon Voss")
- **Description:** Sweep of GUMAS character-profile blocks across the whole workspace surfaced three well-defined L2 characters recorded nowhere in canon, each filling a faction-leadership slot: Eriana Vos (PMC Syndicate Intelligence Chief), Selia Trask (Separatist Confederation political leader), Haden Korr (Union Navy Fleet Admiral). RULING-CHAR-NEW: Vos + Trask promoted STAGING with capsules; Korr recorded UNCONFIRMED (his profile sits under an archive header literally titled "AI-Generated Character", framed as an on-demand generation demo — not standing canon), no capsule. RULING-CHAR-ALIAS: registered drift aliases "Lirian Vos"/"Vos" -> lirian_vael_torin and "Rhaegon Voss" -> rhaegon_torr_kai (same DRIFT-002-b class as Lyra Voss/Veylan); their capsule manifests re-hashed. Vos/Voss cluster now disambiguated (4 distinct: Lyra Voss, Lirian Vael-Torin, Eriana Vos, Rhaegon Torr-Kai). Note dumps carried zero GUMAS character content. Two new capsules adapter-verified (40 total, only pre-existing anaya defect failing).
- **Resolution:** LOCKED at commit. Open: Haden Korr affirmation (UNCONFIRMED -> STAGING) is an owner call; Eriana Vos org binding uses org_the_black_hand (nearest PMC covert org) pending a dedicated PMC intelligence-division record; Selia Trask faction-level only (no Separatist civil-government record exists).

## Drift Entry — 2026-07-21 (L2 Character Salvage Supplement — v2.2.6b tail)
- **Source:** Owner follow-up ("what about the pirate queen"). Report: root reports/analysis/l2_character_salvage_supplement__2026-07-21.md. Owner rulings 2026-07-21: v2.2.6b = early generation, salvage selectively; run now.
- **Type:** ghost-entity salvage (prose/mixed-source tail) / alias drift / continuity reconciliation
- **Entities affected:** 14 new characters (12 STAGING, 2 UNCONFIRMED); zylox_rhaegos + renn_valcor alias enrichment
- **Description:** The Pirate Queen (Theryn Kael'Vakar) was already canon (theryn_kaelvakar) — the question exposed a method gap: the main pass's Name/Role/Allegiance block-scan missed characters described in relationship prose and in the mixed-content v2.2.6b knowledge core (interleaved with real-world news noise). Salvaged 12 established GUMAS characters as STAGING: Jaxx Tyren (Outer Colonies warlord), Talyx Velkonn (exiled Velar Grand Duke), Orin Vex (Union Vice Chancellor), Sarina Vael (GSB Director), Deyan Orros (Envoy-Captain), Mara Velthis (Captain), Saela Corven (Fleet Admiral), Selene Rho (Vice Admiral, Judicator fleet — distinct from Selene Arcturus/Ark), Aria Lenix (fighter-wing Commander), Joran Malik (Commander, G.U.S. Umbra Stalker vessel_gu_002), Thalen Rynn (Republican Reformist voice), Karn Vos (Separatist Admiral — DECEASED, KIA Operation Phantom Eclipse, C2 terminal). Recorded UNCONFIRMED: Iskar Veyr and Vaxtan Rhel (both design-menu / generative "Option" proposals, not standing actors). Continuity reconciled: "High Chancellor Valcor" = existing renn_valcor (bare "Valcor" alias registered); "Zylox Verrin"/"Zylox Kryon" = zylox_rhaegos (aliases registered, manifest re-hashed). Vos/Voss cluster grows to 5 (added Karn Vos) — disambiguation noted. Entity records only; capsules deferred (source is title/role-only — baseline capsules would be over-fabrication). No new linter violations.
- **Resolution:** LOCKED at commit. Open: optional capsule builds if any of the 12 are wanted engine-ready; broader prose/relationship sweep across other mixed-content exports (deferred); owner affirmation of the 2 UNCONFIRMED; anchor for Sarina Vael pending a GSB org record.

## Drift Entry — 2026-07-21 (Chronicle Reconciliation — Zylox & Durn rich detail)
- **Source:** Owner directive — treat name differences as historical/chronicler churn; where a chronicle carries rich detail, record and reconcile it into the character. Rich source: projects GUI_Cloudhub v2.2.6b knowledge core ("Grand Council" leadership sourcebook). Dossier: canon/L2/entities/zylox_rhaegos/DOSSIER__reconciled__2026-07-21.md
- **Type:** biographical reconciliation / detail enrichment (no canon overwrite)
- **Entities affected:** zylox_rhaegos, kael_durn (capsule knowledge.jsonl enriched, manifests re-hashed)
- **Description:** A workspace-wide rich-profile sweep (Official Title + Species + Age format, 40 source files) converged on exactly two deeply-detailed figures, both already recorded: Zylox and Kael Durn. ZYLOX: added species (Xenon), age (~54 cycles), full rise-to-power (Xenon mercantile dynasty -> hyperlane corporate empire -> Trade Minister/Free Trade Zone -> Chancellor via Trade Coalition+AI Vanguard alliance), epithets (Merchant Chancellor / the Pragmatist / Corporate Tyrant), doctrine and standing tensions. Title variance 'High Chancellor / Supreme Overseer of Trade' reconciled to canonical 'Supreme Chancellor' (distinct from renn_valcor); surname Verrin/Kryon = churn (aliased earlier). DURN: added species (Human), age (~62), background (frontier pirate-raid origin, Special Forces Supreme Commander, Battle of Teraxis Prime -> 'Iron Sentinel', refused a military chancellor candidate), epithets, doctrine, and a ROLE reconciliation — v2.2.6b's 'Director of the Galactic Marshals' is his EARLIER office, superseded by the Marshal Charter succession (Durn -> Supreme Military Command; Saros -> Chief Marshal, ~2 ya); historical progression, not conflict. All additions are enrichment; mechanical capsule state vectors and prior identity unchanged; both capsules re-verify clean.
- **Resolution:** LOCKED at commit. The rich-profile format covers only these two; other v2.2.6b characters remain title/role-only (the 14 salvaged records stand). Open: broaden churn-aware prose sweep to any remaining mixed-content exports (v226b-prose-sweep-widen).

## Drift Entry — 2026-07-21 (L2 Location Salvage Pass)
- **Source:** Owner directive "keep doing salvage passes". Named-place sweep across rich sources vs 34 loc_ records.
- **Type:** ghost-entity salvage (locations)
- **Entities affected:** loc_teraxis_prime, loc_nyros_expanse, loc_thalor_sector, loc_eltari_nebula, loc_nethari_expanse, loc_hollen_expanse, loc_daeryth_enclave (new, STAGING)
- **Description:** Seven named L2 places attested in sources but unrecorded, each cross-referenced to a salvaged character or event: Teraxis Prime (Durn's "Iron Sentinel" battle), Nyros Expanse (Velar restorationist fleet reactivation — Talyx Velkonn arc), Thalor Sector (Deyan Orros separatist-informant extraction), Eltari Nebula (site of the "Eltari Nexus" quantum anomaly), Nethari Expanse (Saela Corven's Siege of Nethari), Hollen Expanse (AI-Warlord annihilation of a Union forward base), Daeryth Enclave (Reformist Capital of the Velar Republican Movement — full base profile; org_republican_reformists). Map-primacy discipline: all recorded canonical_position_status=unplaced (not on the map placed-systems list; placement deferred to a future map §8 entry — detail discovered, not invented). All carry recovered_source naming_exemptions and pass the naming-admission gate.
- **Resolution:** LOCKED at commit. Open: map placement for any of the seven (owner/map-authority call); Garen/Orison Expanse deferred (insufficient context); "System"-suffix candidates too noisy for automated salvage (star-system vs software-system ambiguity).

## Drift Entry — 2026-07-21 (Precursor / Dyson Sphere Salvage Pass)
- **Source:** Owner directive "keep going" + "one region with massive precursor megastructures (Dyson Spheres)". Sources: map §2.5 Dyson Sphere Frontier + v2.2.6b precursor codex.
- **Type:** ghost-entity salvage (precursor megastructures + builder civilizations)
- **Entities affected:** loc_dyson_twin_spheres (new, STAGING); polity_orak_thuun, polity_sythrex_conclave, polity_vorthan_imperium (new, STAGING), polity_shroudborn (new, UNCONFIRMED) — first canon/L2/entities/precursors/ records; loc_xyphos_prime_ruins + loc_hollow_expanse (Orak-Thuun builder attribution)
- **Description:** The Dyson Sphere Frontier's two abandoned Dyson spheres (twin systems) now have a location record (loc_dyson_twin_spheres, precursor_site) anchored to loc_zone_dyson_sphere_frontier — the galaxy's foremost precursor megastructures, "Forbidden prize", contested by scavengers/pirates, built by the Orak-Thuun. Recorded the four canonical precursor civilizations (schema-named Orak'Thuun/Vorthan/Sythrex/Shroudborn): Orak-Thuun (Celestial Engineers, Dyson/ringworld builders — the Dyson-sphere makers; their tech still runs in the Hollow Expanse + Xyphos Prime ruins), Sythrex Conclave (Bio-Ascendants, seed vaults), Vorthan Imperium (Great Tyranny, earliest interstellar empire felled by an AI revolt — a cautionary tale still shaping AI policy) all STAGING/extinct; Shroudborn (Mysterious Transcendents) UNCONFIRMED/unknown status (myth-only, matches the map's open Shroudborn question). Existing Xyphos Prime ruins + Hollow Expanse enriched with builder_polity_id=polity_orak_thuun. All recovered_source; naming gate PASS.
- **Resolution:** LOCKED at commit. Map-primacy: Dyson twin systems zone-attested (§2.5) but not §8-placed — canonical_position_status=staging pending a map §8 entry. Open: §8 placement for the Dyson systems; Sythrex/Vorthan site records (seed vaults, Vorthan worlds) if attested elsewhere.

## Drift Entry — 2026-07-21 (Major Polity Salvage Pass)
- **Source:** Owner directive "keep going". v2.2.6b Major Civilizations codex + canonical timeline. The precursor pass surfaced the "seven major civilizations" list; three had no records.
- **Type:** ghost-entity salvage (major polities / species)
- **Entities affected:** polity_zyphari_compact, polity_nythran_ascendancy, polity_harkon_sovereignty (new, STAGING) — first canon/L2/entities/polities/ records
- **Description:** Of the seven major galactic civilizations, three lacked entity records: Zyphari Compact (Corporate Oligarchy; Zyphari insectoid communal species; Trade Lords/Guild Alliances hierarchy; holds the Primary Trade Nexus; engine faction zyphari_compact), Nythran Ascendancy (Post-Singularity AI-symbiotic culture; Nythran cyber-enhanced species; organic+AI equal-vote council; Cyber-Symbiotes vs Traditionalists; timeline-attested via the Nythran Cyber Uprising), Harkon Sovereignty (Martial isolationist state; Harkoni reptilian species; High Strategos meritocracy; timeline-attested via the Velar-Harkon Wars). All entity_kind polity, subtype major_civilization, STAGING/active, with species + government detail. The other four majors already have records (Galactic Union, Velar Imperium, Prime Construct, Shroudborn). All recovered_source; naming gate PASS.
- **Resolution:** LOCKED at commit. Open: dedicated species records (Zyphari/Nythran/Harkoni/Xenon/Velari) if a species entity_kind pass is wanted; polity leadership characters (Harkon High Strategos, Zyphari Trade Lords) not yet named in sources.

## Drift Entry — 2026-07-21 (Species Salvage Pass)
- **Source:** Owner directive "keep going". Species surfaced during the major-polity and Zylox passes; no species records existed.
- **Type:** ghost-entity salvage (species)
- **Entities affected:** species_velari, species_xenon, species_human, species_nythran, species_harkoni, species_zyphari (new, STAGING) — first canon/L2/entities/species/ records
- **Description:** Six named L2 species recorded, each cross-referenced to a polity and/or established character: Velari (ancient long-lived humanoids, high brain plasticity, Velar Imperium founders, Vel-Surak namesake), Xenon (heightened-cognition humanoids; Zylox's species), Human (baseline; Kael Durn's species), Nythran (cybernetically enhanced, Nythran Ascendancy), Harkoni (reptilian martial, Harkon Sovereignty), Zyphari (insectoid communal economists, Zyphari Compact). entity_kind species, STAGING/extant. Reciprocal links added: polity_{zyphari,nythran,harkon}.primary_species_id → species record. All recovered_source; naming gate PASS.
- **Resolution:** LOCKED at commit. Open: additional minor species if attested (e.g., precursor biomechanical forms); species→character back-links.

## Drift Entry — 2026-07-21 (Vessel check + Anomaly Salvage)
- **Source:** Owner directive "keep going". Vessel-registry diff + anomaly sweep.
- **Type:** coverage confirmation (vessels) + ghost-entity salvage (anomaly)
- **Entities affected:** anomaly_eltari_nexus (new, STAGING); loc_eltari_nebula (anomaly back-link)
- **Description:** VESSELS: all 16 Ship Registry v1.0 named vessels + all source-mentioned G.U.S. ships already have records (12 GU classes bound, Nemesis Prime, Khar'Thyrix, plus owner-added Watchfire/Shieldwake/Continuance/Third Measure/Crown Dark/Dark Star). Vessel domain is closed — no salvage gap. ANOMALIES: most "Nexus/Anomaly/Surge/Uprising" hits are generic descriptors or already-recorded timeline events (Celestial Surge, Cyber Uprising); "Sovereign Nexus" is a simulation-scenario label, not in-world. One genuine named anomaly recorded: the Eltari Nexus (anomaly_eltari_nexus) — a quantum-astroengineering breakthrough in the Eltari Nebula (loc_eltari_nebula), discovered by Dr. Adrienne Kovas (adrienne_kovas) with the Prime Construct and an AI/human coalition; nebula back-linked. recovered_source; naming gate PASS.
- **Resolution:** LOCKED at commit. The major salvage seams (characters, polities, species, precursors, megastructures, locations, vessels, this anomaly) are now substantially mined. Remaining thin/lower-yield: org sub-factions (Trade Lords/Guild Alliances/GSB), mechanics registry (MECH ids), minor anomalies, widened prose sweep — pursue on request.

## Drift Entry — 2026-07-21 (Widened Prose Sweep)
- **Source:** Owner directive. Roster rebuilt post-salvage (329 names); swept 30 mixed-content knowledge/memory/conversation exports for titled named characters.
- **Type:** ghost-entity salvage (prose tail) / alias drift
- **Entities affected:** char_idris_vale, char_syrr_velkonn (new, STAGING); char_selia_trask (alias "Selia Tren-Voss"/"Selia Tren")
- **Description:** The widened sweep ran against heavy contamination — the exports interleave scraped real-world news (world leaders, US politicians) and an L1 development-team "expert panel" of Dr.-titled personas (Emily Tran/Leo Nakamura/Sasha Ilyanova/Amelia Rivers = Simulation Architect / AI Specialist / Performance Engineer — meta roles, correctly excluded). Two genuine new L2 characters surfaced: Colonel Idris Vale (Marshal Intelligence Directorate, Sentinel strike-team commander; boarded an enemy shipyard to destroy AI war-production cores) and Dr. Syrr Velkonn (Velar anthropologist, potential reformist; Velkonn-name kin to char_talyx_velkonn, relationship NOT established). "Selia Tren-Voss"/"Selia Tren" resolved as chronicler variants of char_selia_trask (same Separatist political-leader office) and registered as aliases. All recovered_source; naming gate PASS.
- **Resolution:** LOCKED at commit. The prose tail is now substantially mined; residual single-file GUMAS-flavored one-offs are low-confidence (likely generative examples), left unrecorded pending stronger attestation. Real-world-news and L1-dev-persona noise dominate the remaining matches.

## Drift Entry — 2026-07-21 (Identity De-flattening Pass)
- **Source:** Owner concern — political entities don't inherently describe a whole people; avoid flattening national/factional, cultural, and species identity.
- **Type:** modeling correction (de-conflation)
- **Entities affected:** 6 species records, 3 polity records; new canon/L2/mechanics/IDENTITY_DIMENSIONS__v0.1
- **Description:** The Major-Polity and Species passes had flattened polity↔species into a 1:1 map (polity.species field; species.primary_polity_id). Corrected to four orthogonal dimensions — species(people)/polity(state)/culture(heritage)/region(place). Species: dropped primary_polity_id; added origin_polity_id + member_polities(plural, non-exhaustive) + distribution. species_human now spans Union/Separatist/PMC; species_velari spans Imperium/Union with a cultural_note that Velari heritage ≠ the Imperium state (Vel-Surak precedent); species_xenon spans Union/Zyphari sphere. Polities: dropped the species field (implied polity==people); added founding/dominant_species_id + multispecies flag + peoplehood_note. Nythran Ascendancy marked a TWO-peoples polity (organic Nythrans + AI co-citizens); Zyphari Compact explicitly multispecies. Verified character records keep faction (allegiance) orthogonal to species — no species-as-faction conflation. Established IDENTITY_DIMENSIONS__v0.1 with anti-flattening rules for future passes/reconciler.
- **Resolution:** LOCKED at commit. Linter clean (only pre-existing selene_ark). Certainty of the modeling doc: STAGING pending owner ratification.

## Drift Entry — 2026-07-21 (Major Promotion Pass)
- **Source:** Owner directive — promote anything staged that does not conflict with canon. Receipt: canon/L2/MAJOR_PROMOTION_PASS__2026-07-21.md
- **Type:** batch promotion receipt (STAGING -> CANON)
- **Entities affected:** 50 STAGING entity records promoted to CANON (19 location, 16 character, 6 polity, 6 species, 2 mobile_asset [Kharon/Sablewake], 1 anomaly [Eltari Nexus]) + 2 capsule identities (eriana_vos, selia_trask) re-promoted/re-hashed
- **Description:** Deterministic conflict scan found ZERO conflicts (no name collisions vs different canon entities; no C3 office/incumbency collisions; fabric linter clean; identity-dimensions honored). Promoted all 50 non-conflicting STAGING entity records, each preserving prev_certainty=STAGING + a promotion_to_canon audit block. Position axis preserved: 10 promoted locations stay unplaced/staging on the map axis (certainty and placement are orthogonal — nothing auto-placed; map §8 placement still pending). HELD by design: 4 UNCONFIRMED (Haden Korr, Iskar Veyr, Vaxtan Rhel = generative; Shroudborn = myth-only) and 3 SUPERSEDED alias-forwards. Naming gate: 11 pre-gate map-derived records retrofitted with recovered_source exemptions; gate passes on the promoted set; pre-2026-03-19 original canon + owner records remain grandfathered.
- **Resolution:** LOCKED at commit. The L2 salvage corpus is now substantially CANON. Open: UNCONFIRMED affirmations (owner), owner records' naming exemptions (naming-gate-owner-records), map §8 placement for unplaced canonical locations, anaya state.bin defect.

## Drift Entry — 2026-07-21 (Filesystem Artifact Audit + Active-Faction Salvage)
- **Source:** Owner conviction that key L2 artifacts exist only in the filesystem. Audited structured L2 source docs + extracted the never-opened GUMAS_Unified_Registry zip (gumas_lore_db.json: 27 factions, 24 characters).
- **Type:** major coverage gap (active engine factions) + ghost-entity salvage
- **Entities affected:** polity_separatist_confederation, polity_ai_warlord_collective, polity_pmc_syndicate, polity_crimson_pact (new, STAGING); char_overseer_theta_9 (new, STAGING)
- **Description:** BIG FINDING — the four MAJOR ACTIVE-SIMULATION factions had NO polity/org records despite characters binding to them and the engine running on them: Separatist Confederation (separatist_confed; leaders Selia Trask + Rhaegon Torr-Kai already recorded, but the faction itself was not), AI-Warlord Collective (ai_warlord; Nemesis Core flagship), PMC Syndicate (pmc_syndicate; Vailen Rix + Eriana Vos), Crimson Pact (crimson_pact; cult/extremist). My earlier "seven major civilizations" pass worked from the LORE list and missed the ENGINE faction set. All four recorded as entity_kind polity subtype active_faction with engine_faction_id, identity-model peoplehood_note (faction≠people). Plus Overseer Theta-9 — AI-Diplomatic Representative of a MODERATE AI-Warlord splinter (AI recognition talks, attempted AI-Union ceasefire; opposed by Nemesis Core, potential Prime Construct ally) — showing the AI-Warlord Collective is not monolithic. Sources: canon GUMAS_Factions.json + the extracted gumas_lore_db.json. All recovered_source; gate PASS; linter clean.
- **Resolution:** LOCKED at commit. STILL UNMINED (owner was right): AURORA_GUMAS_STAFF_REGISTRY_SSOT zip, machine-readable reference packet (L2 mechanics library — leadership bias/diplomacy/treaty-reputation systems not yet landed as canon), L2 Staging Dossier v0.6 (process-control doc), and other session-archive zips. Queued for continued filesystem mining.

## Drift Entry — 2026-07-21 (Peoples & Cultural Tapestry Pass)
- **Source:** Continued filesystem mining of the machine-readable L2 reference packet (mechanics library + §2 Cultural Tapestry), cross-corroborated by engine scenarios.py faction archetypes.
- **Type:** major coverage gap (secondary peoples) + cultural-dimension salvage
- **Entities affected:** polity_elari_ascendancy, polity_vorran_clans, polity_kaelar_orders, polity_tharaxian_nomads (new, STAGING); new canon/L2/culture/L2_CULTURAL_TAPESTRY__v0.1
- **Description:** MECHANICS: canon already has 23 MECH ids — the core mechanics library is substantially landed; not a gap. CULTURAL TAPESTRY: no canon record existed for L2 art movements, philosophy/doctrine, or entertainment/media — landed as canon/L2/culture/L2_CULTURAL_TAPESTRY__v0.1 (culture as a first-class dimension per IDENTITY_DIMENSIONS, each tradition attributed to a people not a state). This surfaced FOUR more engine peoples with no records: Elari Ascendancy (cultural/spiritual; Celestial Abstraction art; Symmetry Doctrine), Vorran Clans (clan confederation; Resonance Sculpture; Symmetry Doctrine), Kaelar Monastic Orders (monastic; Organic Ink Histories; Doctrine of Perfect Uncertainty), Tharaxian Nomads (nomadic diaspora; Silent Poetry). All recorded with faction_type + dominant_bias + cultural_traditions + engine_faction_id. Engine cross-corroboration: scenarios.py encodes the tapestry's own alliances (Elari↔Vorran "Symmetry Doctrine allies" 0.20; Kaelar↔Tharaxian "philosophical alignment" 0.10). ALL 13 ENGINE FACTIONS NOW HAVE RECORDS (was: only ~7 lore civilizations). Held UNCONFIRMED: Shroud Phenomenon (myth, Shroudborn-adjacent). recovered_source; gate PASS; linter clean.
- **Resolution:** LOCKED at commit. Engine faction coverage complete. Open: dedicated species records for Elari/Vorran/Kaelar/Tharaxian peoples; cultural-movement entity records if a culture entity_kind is wanted; Staff Registry SSOT zip still unmined.

## Drift Entry — 2026-07-22 (Dark Star Unified Manuscript and Translation Improvement Pass)
- **Source:** Owner-directed full narrative improvement pass following review of Shadow-captain translation behavior.
- **Type:** narrative supersession / translation-recording correction / continuity consolidation
- **Entities affected:** event_dark_star_incident_4718_224; unified Dark Star narrative; prior Third Silence chapter source
- **Description:** Committed a unified three-chapter v1.1 manuscript covering The Dark Star, Valkyrie, and Third Silence. Revised Shadow communications so speaker intelligence and professional cadence remain intact while uncertainty appears through delayed live translation, substitutions, confidence warnings, competing terms, and later corrections. Applied a general prose, rhythm, viewpoint, repetition, and evidentiary-clarity improvement pass without changing the locked event outcome.
- **Resolution:** Unified v1.1 manuscript is the governing narrative source. The prior chapter-three file remains in place as superseded provenance. Translation output is an evidentiary instrument record, not an omniscient narrator.

## Drift Entry — 2026-07-25 (Lineage Reconciliation — Cultural Tapestry × Dark Star)
- **Source:** Two independent L2 promotions landed on divergent refs: local `bacd3e6` (Peoples & Cultural Tapestry, 2026-07-21) and `origin/main` `9764708` (Dark Star unified manuscript v1.1, 2026-07-22). Both appended to this log, which is the only file they contended.
- **Type:** lineage divergence (no content conflict)
- **Entities affected:** none. The two promotions touch disjoint canon — `canon/L2/culture/` + `canon/L2/entities/polities/` on one side, `canon/L2/narratives/` + `canon/L2/events/` on the other.
- **Description:** Neither promotion contradicts, supersedes, or renames anything in the other; the collision was structural, caused by both appending to the tail of this file rather than by any disagreement about canon. Verified before resolution: no shared entity ids, no shared canon paths, and both entries internally complete.
- **Resolution:** Both entries retained verbatim in chronological order (07-21 then 07-22), matching this file's oldest-first convention. Nothing was dropped, rewritten, or superseded — the conflict is retconned into the record rather than resolved destructively. Entry count 58 + 58 with 57 shared → 59, confirming one entry contributed by each lineage. Pre-merge state tagged `pre-reconcile-2026-07-25` for rollback.

## Drift Entry — 2026-07-21 (Staff Registry SSOT check + Peoples-species records)
- **Source:** Continued filesystem mining. Extracted AURORA_GUMAS_STAFF_REGISTRY_SSOT zip (27 profiles).
- **Type:** coverage confirmation (L1 staff) + species salvage (L2 peoples)
- **Entities affected:** species_elari, species_vorran, species_kaelar, species_tharaxian (new, STAGING); 4 polity records (dominant_species_id links)
- **Description:** STAFF REGISTRY SSOT is an L1 Orion Station staff registry (Alex Thorne, Tobias Qin, Amina Velin, etc.), not L2 — and essentially complete (41 L1 canon character records superset the 27 SSOT profiles). One SSOT profile unmatched: amelia-rivers (previously identified as an L1 dev/expert-panel persona, not in-world) — flagged for owner, L1 domain, not actioned. L2 DELIVERABLE: created species records for the four peoples surfaced by the cultural tapestry (Elari, Vorran, Kaelar, Tharaxian), completing the species dimension for the engine faction set. Each recorded per the de-flattened identity model (origin_polity_id + member_polities + cultural_note as a distinct dimension; biology marked not-established/do-not-invent). Reciprocal dominant_species_id links added to the 4 polities. recovered_source; gate PASS; linter clean.
- **Resolution:** LOCKED at commit. Species dimension now covers all major peoples (10 species). Open (L1, owner): amelia-rivers L1 roster question. L2 salvage seams substantially exhausted.

## Drift Entry — 2026-07-21 (Engine-Authoritative Audit + Geopolitics + Process Reframe)
- **Source:** Owner critique — stop stacking process-resolvable details as owner decisions; use the existing resolution processes. Plus "not convinced everything is found." Audited against authoritative ground-truth sources.
- **Type:** authoritative-source completeness audit + conflict salvage + process correction
- **Entities affected:** conflict_union_imperium_border, conflict_ai_sovereignty_crisis, conflict_separatist_tension (new, STAGING); new canon/L2/RESOLUTION_ROUTING doc
- **Description:** Diffed canon against TWO authoritative ground-truth sources instead of documents: (1) the ENGINE runtime — all 21 instantiated leaders recorded, all 13 factions recorded; (2) the formal 2026-03-13 promotion-candidate set — all 10 chars + 6 polities landed (old CHAR-GU-*/POL-* ID scheme maps 1:1 to normalized canonical_ids, verified via canonical_name). Both come back fully covered. GAP FOUND + FILLED: the engine's 3 scenario-defined "canonical tension points" had no records — recorded conflict_union_imperium_border (Union↔Velar, TENSION), conflict_ai_sovereignty_crisis (Union↔Prime Construct↔AI-Warlord, ESCALATION), conflict_separatist_tension (Union↔Separatist, TENSION) using SCENARIO-level stable facts only. The 5 run treaties and all per-run conflict dynamics (war_cost, turns_active, de-escalation prob) held as TERTIARY/instance-local (Canon Protocol §5) — NOT canon. PROCESS CORRECTION: authored RESOLUTION_ROUTING to stop mislabeling process-resolvable items as owner decisions — placement routes to the §4.5 Reconciliation Workflow + §4.6 Claim Ledger (evidence→placement, not eyeballing coordinates); names route to the NameService/naming protocol; simulation outcomes to the engine; UNCONFIRMED awaits source evidence. Owner is the promotion GATE, not the value generator.
- **Resolution:** LOCKED at commit. gate PASS; linter clean. Coverage validated against authoritative sources. Open items reframed to their processes.

## Drift Entry — 2026-07-21 (Prime Construct + Kaelor's Rift Pass)
- **Source:** Owner spot-check.
- **Type:** consistency fix (Prime Construct polity parity) + stub enrichment (Kaelor's Rift)
- **Entities affected:** polity_prime_construct (new, STAGING); loc_kaelor_s_rift (enriched from empty stub)
- **Description:** PRIME CONSTRUCT was recorded only as org_prime_construct_polity (organization) + prime_construct_leader (character) — the ONLY engine faction lacking a polity record, inconsistent with the other 12. Added polity_prime_construct (sovereign AI civilization: a network of evolving consciousnesses, originally an AI war strategist that gained autonomy, nearly triggered war, negotiated peace, now a recognized sovereign life form within the Union; former AI-Warlord member since allied). Cross-linked to org_prime_construct_polity and prime_construct_leader; identity-model note (the AI collective is both people and polity); legacy_canonical exemption. Now ALL 13 engine factions have polity records. KAELOR'S RIFT was CANON (position=canon, "anomaly region") but a bare stub with EMPTY notes despite being a major recurring site. Enriched with established canon only (no invention): FTL-disruption anomaly region + navigation hazard (World Bible CANON); the "event scar" of the Battle/Victory at Kaelor's Rift (map §7); related_character_ids alric_tann (led the victory), lyra_voss (crew readiness), arin_tavos (ship-to-ship combat). gate PASS; linter clean.
- **Resolution:** LOCKED at commit. Engine-faction polity coverage now complete (13/13). Note: placement of Kaelor's Rift and other locations still routes through the §4.5 reconciliation workflow per RESOLUTION_ROUTING (Kaelor's Rift already position=canon from prior canon).

## Drift Entry — 2026-07-21 (L2 Stub Audit)
- **Source:** Owner — "there's a lot more like [Kaelor's Rift] out there, find it all." Built a deterministic thinness scorer over all canon L2 entity records.
- **Type:** completeness/quality audit (hollow records)
- **Entities affected:** loc_marshal_academy (enriched); loc_kaelor_s_rift (prior). 7 owner Dark Star records flagged (NOT touched); 8 vessel_gu_* noted thin-as-source.
- **Description:** 16 stub records found (present but hollow: <40-char description). Category A (safe, unowned original canon): loc_marshal_academy back-filled from the Marshals Ledger (training/selection pipeline); loc_kaelor_s_rift done in the prior pass. Category B (owner active-arc, NOT modified): 7 Dark Star / Third Silence records (place_lethan_system, place_kallis_foundry, place_kharis_sector, artifact_third_silence, fleet_shadow_fleet, vessel_shadow_001, vessel_unknown_dark_star_001) — their detail already exists in committed canon (Dark Star narrative v1.1 + AAR + event_dark_star_incident hub), just never back-filled into the entity records; I prepared an additive back-fill then REVERTED it to avoid editing the owner's in-flight work, flagging it for owner authorization instead (respecting the earlier don't-overstep guidance). Category C (thin-as-source, no action): 8 registry vessels whose Ship Registry v1.0 source only gave name/class/allegiance — enriching would be invention. Report: root reports/analysis/l2_stub_audit__2026-07-21.md.
- **Resolution:** LOCKED at commit. loc_marshal_academy enriched (grandfathered, additive, gate-permitted). Owner Dark Star back-fill available on request. Stub scorer re-runnable for future audits.

## Drift Entry — 2026-07-21 (Stub Reconciliation — corrected approach)
- **Source:** Owner correction — the simulation's purpose is to extrapolate truth from established canon; follow the reconciliation process, stop the revert-and-ask non-linear workflow; the ship detail DOES exist.
- **Type:** reconciliation (derivation from established canon)
- **Entities affected:** 17 mobile_assets (derived_capabilities from class); 7 Dark Star records (reconciled from committed narrative)
- **Description:** Corrected two errors. (1) SHIPS: my "thin-as-source, would be invention" conclusion was WRONG. A vessel's capabilities ARE its canonical class's established role/features/complement — reconciling each vessel with its class (cls_* records + ship registry) is derivation from established canon, not invention. Added derived_capabilities to all 17 classed vessels (class role, key_features, typical_complement, with basis note). (2) DARK STAR: reverting the earlier additive reconciliation left valid work on the floor. Re-applied it — the detail is committed canon (Dark Star narrative v1.1 + AAR + event_dark_star_incident hub); reconciling it into the entity records (description + doc_sources + event_refs) is the process, and editing existing canon records is grandfathered against the naming gate per policy. RESULT: 0 remaining thin records (was 16); linter clean.
- **Resolution:** LOCKED at commit. Stub problem fully resolved by reconciliation, not menus. Process note: derivation from established canonical detail is the core simulation mechanism, not overstepping.

## Drift Entry — 2026-08-01 (Strict Integrity Recovery)
- **Source:** Public-readiness integrity audit; committed capsule manifest, CANON lock record, Marshals ledger, and adjacent locked Marshal sub-unit records.
- **Type:** artifact recovery / zero-byte record reconstruction
- **Entities affected:** `anaya_ral_seyr` capsule state; `org_tactical_enforcement_officers`
- **Description:** Restored Anaya Ral-Seyr's 42-byte `state.bin` with the exact object required by her locked capsule manifest (`1571a3933d7f344c8facd70a26620283268d2cdc34f569f21b1c06cb1a6afb73`). The object is independently present in eight intact peer capsules. Reconstructed the Tactical Enforcement Officers record from its 2026-03-19 CANON lock and the Marshals ledger entry at line 125, following the adjacent locked Marshal sub-unit schema.
- **Resolution:** RECOVERED without promotion or authority change. Removed the three temporary baseline findings after strict validation passed. Detailed receipt: `reports/CANON_INTEGRITY_RECOVERY__2026-08-01.md`.

## Drift Entry — 2026-08-09 (duplicate: Prime Construct)
- **Source:** STAGING closure reconciliation (aurora-canon-reconciler conflict scan over all 21 STAGING/UNCONFIRMED records)
- **Type:** duplicate name / ghost entity
- **Entities affected:** `org_prime_construct_polity` (CANON), `polity_prime_construct` (STAGING)
- **Description:** Two records described the same referent and cross-aliased each other — the organization record was named "Prime Construct Polity" with alias "Prime Construct"; the polity record was named "Prime Construct" with alias "Prime Construct Polity". The organization record was already CANON but carried **no doc_sources**; the polity record carried provenance (Major Civilizations codex) and held more inbound references from live records (Obsidian Dawn event, Omega-Veil, Sovereign Nexus).
- **Resolution:** RESOLVED. `polity_prime_construct` retained as canonical — it models the correct identity dimension (a state, not an organization, per IDENTITY_DIMENSIONS v0.1), has provenance, and is more referenced. `org_prime_construct_polity` set to `certainty: SUPERSEDED`, `status: alias_forward_only`, `superseded_by: polity_prime_construct`, so existing references keep resolving. No content lost.

## Drift Entry — 2026-08-09 (certainty precision: Shroudborn)
- **Source:** same reconciliation pass
- **Type:** certainty mis-tag
- **Entities affected:** `polity_shroudborn`
- **Description:** Held at UNCONFIRMED, but the record is in-world legend material ("Some believe the Shroudborn are a surviving precursor race…"), not unvalidated speculation about the setting. UNCONFIRMED conflated "we lack evidence" with "the in-world account is disputed".
- **Resolution:** RESOLVED — retagged `LEGEND_CONTESTED`, the approved tag for in-universe rumor/myth/disputed account. The legend's existence is canon; its truth remains contested. Not a promotion to fact.

## Drift Entry — 2026-08-09 (P1 placement drift: 19 records overstating placement)
- **Source:** aurora-canon-reconciler FABRIC P1 check, newly wired 2026-08-09
- **Type:** invariant violation (P1 — map primacy)
- **Entities affected:** 19 locations, incl. loc_khalrix_3, loc_veil_nebula, loc_hollow_expanse, loc_xyphos_prime_ruins, loc_draskor_9, loc_vaelos_iv, loc_silent_bastion, loc_torix_7_crimson_abyss, loc_shadow_reef_nebula, loc_rethos_iv, loc_viridian_sanctum, loc_prime_ascendancy, loc_velkaris_v, loc_xelvani_3_silent_plains, loc_deep_space_listening_posts, loc_xyphos_precursor_research_center, and (no map row) loc_kaelor_s_rift, loc_marshal_academy, loc_blackreach_station.
- **Description:** 16 records claimed `canonical_position_status: canon` while their Location Authority Table row stood at STAGING/TBD; 3 claimed canonical placement with no LAT row at all. P1 holds that the map is the source of truth and an entity's position status must not exceed its map row. These were invisible until now because `tools/fabric_invariants_check.py` is Velar-domain-scoped (16 of 158 entities) — the drift sat outside its scan window.
- **Resolution:** RESOLVED by downgrade, per the RULING-VELAR-P1 precedent (2026-07-21, "resolved by downgrade — entity records no longer overstate"). Position status set to `staging` where a STAGING row exists and `unplaced` where no row exists; each record carries a `p1_downgrade` block with the map row, its status, and the basis. **Scope: the placement claim only** — every entity remains CANON and its attributes are untouched. Placement re-promotes when the map-authority / Reconciliation Workflow §4.5 process supplies evidence (precedent: loc_vel_surak was downgraded, then legitimately re-promoted once its map row was promoted). No coordinates were invented.

## Drift Entry — 2026-08-09 (P4 was unsatisfiable as first implemented)
- **Source:** same pass — self-review of the newly added P4 gate
- **Type:** governance defect (unsatisfiable exit condition)
- **Entities affected:** event_dark_star_incident_4718_224, fleet_shadow_fleet (both correctly identified as movement events lacking route citation)
- **Description:** P4 requires a canon promotion citing a movement/cross-region event to cite a canonical route or drive. Canon contains **no route, corridor, lane or drive entity at all**, so a hard BLOCK made every movement event permanently unpromotable with no compliant action available — a gate that can never be satisfied.
- **Resolution:** RESOLVED. P4 now self-activates: it reports WARN (`FABRIC_P4_NO_ROUTE_REGISTRY`) while no route registry exists, and escalates to BLOCK automatically once one does. Mirrors the P1 degradation when the map authority table is absent. Building the route registry is queued as `l2-route-registry` — that is the work that makes P4 enforceable.

## Drift Entry — 2026-08-09 (P4 made enforceable and satisfiable)
- **Source:** l2-route-registry pass, following the P4 self-activation fix
- **Type:** governance gap closure
- **Entities affected:** event_dark_star_incident_4718_224, fleet_shadow_fleet; new canon/L2/map/ROUTE_REGISTRY__v0.1__2026-08-09.md
- **Description:** P4 requires movement promotions to cite a route or drive. Canon names no corridor anywhere — it attests movements between named *places* only. The registry detector was also too narrow: it looked at `subtype` alone and so missed the Hollow Expanse, which is typed `region / lawless corridor` and is a genuine corridor referent.
- **Resolution:** RESOLVED. (1) Detector widened to consider `location_type`, so the Hollow Expanse registers and P4 escalates from WARN to a live BLOCK. (2) P4 is now satisfiable two ways — cite a route, or record an explicit `route_exemption` giving the canonical endpoints that define the transit, the basis, and what would resolve it. The gate demands the route question be *answered*, not fabricated; this mirrors `naming_exemption` and `canonical_position_status: unplaced`. (3) Both waiting records carry exemptions citing canonical endpoints. **No route name was minted** — naming belongs to NameService, not to a validator's convenience. Notably, the Hollow Expanse would be a plausible citation for the Shadow Fleet, but canon establishes no link between them, so it was NOT cited: plausible is not attested.

## Drift Entry — 2026-08-09 (C1 rollout completed: 22 capsules bound)
- **Source:** capsule-location-binding-rebuild (RULING-FABRIC-SCHEMA part b)
- **Type:** invariant closure / schema extension
- **Entities affected:** 22 charforge capsules (all remaining unbound), incl. zylox_rhaegos, vael_saros, selene_arcturus, renn_valcor, kael_durn, virex_talvaren, nemesis_core, prime_construct_leader and the polity leaders.
- **Description:** 19 capsules received `location_binding` in the 2026-07-21 Judicator crew rollout; 22 remained unbound, so C1 (one body, one place) was unenforceable for them. All 22 are institutional office-holders — Chancellor, Chief Marshal, Admiral, Ministers, Directors, polity leaders. **Canon establishes their offices but names no seat, vessel or world for any of them**: the Union capital appears only as "the capital planet" in the Marshal Academy charter and has no location entity, and no polity seat entities exist.
- **Resolution:** RESOLVED. All 22 carry an explicit `location_binding` of type `undetermined`, each with a basis naming the office and stating that canon establishes no place, plus why a target was not invented and what resolves it. Capsules were **rebuilt, not hand-edited** — they are sha256-manifested, so every record hash was re-derived; all 40 manifests verify. The C1 check now distinguishes an explicit undetermined binding (INFO — question answered) from a missing one (GAP — nobody looked), and still rejects an undetermined binding that gives no basis. Establishing seats of government is queued as `l2-seat-of-government-locations`; bindings fill in when it lands.
- **Also found:** all 23 `mobile_asset` records key their identity as `canonical_id` while the rest of canon uses `entity_id`. Any tool indexing only `entity_id` silently skips every vessel — this had been hiding the vessels from full-canon validation runs. Queued as `canon-identity-key-unification`.

## Drift Entry — 2026-08-09 (split identity key: entity_id vs canonical_id)
- **Source:** canon-identity-key-unification, found during the C1 capsule rollout
- **Type:** schema drift / silent partial coverage
- **Entities affected:** all 23 `mobile_asset` records (every vessel in canon)
- **Description:** Vessels keyed identity as `canonical_id`; the other 166 canon entity records use `entity_id`. **Zero overlap.** Six of the seven tools that walk the canon tree index on exactly one key, so each was operating on a partial corpus without knowing it. Two concrete wrong results in one session: a full-canon validation sweep reported 166 records (real count 189) and was read as complete coverage; and capsule `location_binding` targets pointing at `vessel_gu_001` appeared to be ghost destinations because the resolver's id index contained no vessels at all. Silent partial coverage is worse than a crash — the tool reports success.
- **Resolution:** RESOLVED additively. All 23 vessels gained `entity_id` carrying the same value, and **kept** `canonical_id` for back-compat with readers that depend on it (`tools/character_capsule_adapter.py`). Nothing was removed, so no working consumer breaks. Each record carries an `identity_key_note` explaining the history. Guard tests (`tests/test_canon_identity_keys.py`) now pin: every entity record has `entity_id`, the keys never disagree, ids are unique, and an `entity_id`-only index covers the whole corpus — the exact failure that reported 166/189 as clean.

## Drift Entry — 2026-08-09 (C2 status vocabulary: flat set applied to every kind)
- **Source:** selene-ark-status-vocab
- **Type:** schema design error / unenforceable invariant
- **Entities affected:** 25 records across species, polities, events, characters, vessels, places, equipment, organizations and reports
- **Description:** `STATUS_VOCAB` was one flat set (`active/deceased/destroyed/retired/inactive/unknown/alias_forward_only`) applied to every entity kind. It is body-oriented — C2 is "one body, one place", and the dead do not act — but canon also holds species, events and reports, whose lifecycles are different words. A species is not "active", it is **extant**; an event is **concluded**; a report is **submitted**. 25 of 189 records therefore sat outside the vocabulary and C2 was effectively unenforced for all of them. Separately, 11 records packed lifecycle *and* situation into a single string (`alive_in_union_medical_custody`, `withdrawn_from_lethan_active_strength_unknown`, `active_but_covertly_reoccupied`) — real canon that a naive vocabulary fix would have deleted.
- **Resolution:** RESOLVED two ways. (1) `STATUS_VOCAB_BY_KIND` gives each entity kind its own lifecycle vocabulary, with a generic fallback so an undefined kind fails loudly rather than passing silently. (2) The 11 composite statuses were split: `status` now carries lifecycle only (the part an invariant can reason about), while the situational canon is preserved **verbatim** in `status_detail`, with the original string kept in `prev_status`. **No canon detail was traded for linter cleanliness** — a test asserts every split record retains its detail, and specifically that Selene Ark reads `active` with her medical custody still recorded. All 189 records now sit inside their kind's vocabulary; C2 is enforceable for the first time.

## Drift Entry — 2026-08-09 (archive ship profiles reconciled; flag-officer/captain distinction)
- **Source:** `archives/unzipped/Complete Archive 4_19 copy/galactic_union_core_ships_module (1).py`, surfaced by the archive content triage
- **Type:** recovered canon / apparent conflict resolved by role distinction
- **Entities affected:** vessel_gu_001, vessel_gu_011, vessel_gu_012, vessel_ai_001, cls_sentinel, char_saela_corven, char_mara_velthis, char_deyan_orros
- **Description:** An archived module classified as code turned out to be **L2 canon data** — five detailed ship profiles (traits, reputation, crew complement, weapons, defence, propulsion, embarked craft, cyberwarfare, recent actions, directives, adaptive behaviour). The three named officers were already canon from earlier salvage passes, but the **ship↔officer linkage and the specifications had never landed**. Valiant Spear and Resolute Dawn had *no commanding officer at all* in canon.
- **Apparent conflict:** the profile names **Fleet Admiral Saela Corven** as commanding officer of the Judicator Prime, while canon sets `commanding_officer_id = alric_tann` (a **Captain**).
- **Resolution:** RESOLVED by role distinction, not by overwrite. On a flagship an embarked flag officer commands the *formation* while the ship's captain commands the *vessel* — both are true simultaneously. Corven is recorded in a new `embarked_flag_officer` field with the reasoning; `commanding_officer_id` was left untouched. Canon corroborates rather than contradicts: `loc_nethari_expanse` already records Corven suppressing a Separatist Armada at the Siege of Nethari Expanse, which this profile lists as a recent action. Judicator Prime's existing `specifications` block was also left intact, with the recovered profile kept alongside it so neither source is lost.
- **NOT merged:** the profile names **WRATH-09 (Prime AI Core)** commanding the AI Leviathan Dreadnought, where canon records `nemesis_core` (aliases *Nemesis Core*, *The Nemesis*) in that office aboard that vessel. Same office, same ship, different designation — most plausibly naming churn, but merging two AI identities on a plausible inference is not a reconciliation. The designation is recorded verbatim with `identity_status: UNDETERMINED`; resolution routed to the naming gate (`wrath-09-naming-gate`).
- **Still absent from canon** (new referents, recorded in the triage report, not minted here): Battle of Tevrak's Gate, Kaelor Shadow Ring, VALR-99, Sentinel Ghost v3.7.

## Drift Entry — 2026-08-09 (29 characters had capsules but no entity record)
- **Source:** archive JSON-tier extraction (Galactic Union character master lists)
- **Type:** structural gap / dangling references from the entity graph
- **Entities affected:** 29 characters — the entire Judicator Prime command crew (alric_tann, lyra_voss, elias_radek, adrienne_kovas, nia_veran, rhen_kailo, arin_tavos, elias_drayen), Union leadership (zylox_rhaegos, vael_saros, kael_durn, selene_arcturus, renn_valcor, anaya_ral_seyr, callan_deyrus, varek_norr, lirian_vael_torin) and faction leaders (nemesis_core, prime_construct_leader, malrik_voska, qellan_vyss, drenn_korvath, virex_talvaren, theryn_kaelvakar, sivaen_the_driftcaller, thessa_nai_oruun, vailen_rix, rhaegon_torr_kai, aelindra_voss_aurai).
- **Description:** These characters existed **only as charforge capsules**, with no entity record — while being **referenced by entity records** (`vessel_gu_001.commanding_officer_id = alric_tann`; its `crew_ids` listed eight of them). From the entity graph's perspective those references dangled, the same defect class as the Velar Imperium referent. Every tool that indexes entity records silently omitted all 29, including the validation sweeps that reported "189 records clean". Not a design choice: 11 other characters carry both forms.
- **Resolution:** RESOLVED. 29 entity records created, deriving core fields (name, aliases, certainty, status, role, faction) from the capsule — the authoritative existing canon — with a `capsule_ref` backlink. 15 were additionally enriched from the archived master lists (allegiance, traits, reputation, relationships, recent actions, decision style, personality insight). Canon record count 189 → 218; capsule-only count 29 → **0**; all 8 Judicator crew references and the commanding-officer reference now resolve to entity records. Validation clean at 218/218; fabric linter clean; 47 guard tests green.
- **Method note — a matching error caught before it landed:** a surname fallback was tried to widen archive enrichment. It gave the Elari Luminary **Aelindra Voss-Aurai** the profile of **Lyra Voss** (Judicator XO), and matched **Lirian Vael-Torin** against **Vael Saros**. Shared name fragments are common in this setting, so a partial match is not evidence of identity. The fallback was removed and enrichment restricted to exact rank-stripped name matches; the two contaminated profiles were dropped. 15 of 29 enriched rather than a falsely-confident 17+.

## Drift Entry — 2026-08-09 (three dangling faction referents closed)
- **Source:** archive JSON mega-blob extraction (`deep_filtered_galactic_union_simulation_conversations`)
- **Type:** dangling referent / missing entity record
- **Entities affected:** new `polity_outer_colonies`, `org_trade_coalition`, `org_ai_vanguard`
- **Description:** `outer_colonies` was in use as a **faction binding by 5 canonical records** (cls_dreadraider, char_jaxx_tyren, char_vaxtan_rhel, char_theryn_kaelvakar and its capsule) with **no entity record behind it** — the same defect as the Velar Imperium referent. Separately, the **Trade Coalition** and **AI Vanguard** are named power blocs attested repeatedly in committed canon — together they are the alliance that carried Chancellor Zylox to the chancellorship, "narrowly defeating a military-backed candidate" — yet neither had a record. The Trade Coalition additionally holds HQ on the Union capital ("Engine of the Union") and brokered the ceasefire trade zones; the AI Vanguard is recorded as "growing beyond his full control".
- **Resolution:** RESOLVED. Three records created, every attribute recovered from committed canon. `polity_outer_colonies` is modelled as a **bloc, not a unified state** — canon calls it volatile and conditionally neutral "unless debts unpaid" — and is explicitly distinguished from `org_outer_colony_warlords`, which is a Velar-Imperium internal faction, not this bloc. `org_ai_vanguard` is explicitly distinguished from the adversarial AI-Warlord Collective and from the Prime Construct: it is Union-aligned and politically embedded. Its internal structure, leadership and membership are **not** established in canon and were not invented. Dangling faction referents now: **zero**. Canon 218 → 221 records, all validating clean.

## Drift Entry — 2026-08-09 (name collision: Sovereign Nexus — AI or place?)
- **Source:** prose-claim salvage (`tools/prose_claim_extractor.py`) over early-project conversations
- **Type:** name collision / unresolved referent identity
- **Entities affected:** `org_sovereign_nexus`
- **Description:** `org_sovereign_nexus` was created earlier the same day from the Operation Obsidian Dawn outcome file, as a **rogue AI intelligence** ("another rogue AI entity… a more powerful intelligence guiding the AI rebellion from the shadows"). Early-project prose describes the same name as a **place**: *"Union Intelligence intercepts communications revealing that Separatist hardliners are amassing forces in Sovereign Nexus, a hyperlane chokepoint."*
- **Resolution:** UNRESOLVED by design, routed to the conflict scan. Three readings are open — two distinct referents sharing a name; one referent with the AI named for or operating from the chokepoint; or naming churn across project eras — and canon settles none of them. The record now carries `conflict_flags: [name_collision_sovereign_nexus]` and a `name_collision` block recording both sources and all three readings. **Nothing was merged or overwritten**, the same restraint applied to WRATH-09 / nemesis_core. Queued as `sovereign-nexus-name-collision` (high).
- **Method note:** this collision was found only because prose mining continued. An earlier recommendation to stop mining prose in favour of reference-integrity sweeps was **wrong and has been retracted**: the "exhausted" reading came from a proper-noun extractor, which in this corpus returns fragments of existing names and template labels. Claim-oriented extraction over the same 9.3 MB blob yields **469 claims across 72 canon entities**. The early project lived in prose; prose salvage is a standing obligation.

## Drift Entry — 2026-08-09 (prose-claim salvage: Velar history + faction stances)
- **Source:** `tools/prose_claim_extractor.py` over the archive `.md` tier and the deep-filtered GU conversations
- **Type:** recovered canon / enrichment from prose claims
- **Entities affected:** `polity_velar_imperium`, `org_republican_reformists`, `org_imperial_loyalists`
- **Description:** Prose claims asserted the Velar Imperium's full historical arc — unification under a technocratic monarchy via the **Sahn'Darith Accord**, expansion during the **Celestial Surge**, collapse in the **Fracture War**, and the resulting three-way split. Checking those names revealed all three are **already canon in the timeline files**, while the `polity_velar_imperium` entity record — created earlier the same day — carried none of it.
- **Resolution:** RESOLVED. The history was reconciled onto the entity record **from the authoritative timeline**, not from the prose paraphrase: prose surfaced the gap, canon supplied the fact. The Fracture War outcome ties directly to the three internal factions the record already carried. Also recorded faction stances: Republican Reformists favour **Union integration**; Imperial Loyalists are **restorationists**.
- **Deliberately NOT asserted:** prose lists the Imperial Loyalists as "Led by Tal'Varen", which very likely means `virex_talvaren` (Lord Marshal Virex Tal'Varen). That is recorded as a **claim with UNCONFIRMED linkage**, not written into a leadership field — a surname is not identity evidence. Same discipline that caught the Aelindra Voss-Aurai / Lyra Voss contamination earlier the same day.
- **Method significance:** the `.md` tier had been declared "largely exhausted" hours earlier on the basis of proper-noun extraction. Claim-oriented extraction over the *same* files yields **951 claims across 85 entities**. The earlier finding was a tool artefact, and the retraction is recorded in `reports/analysis/archive_content_triage__2026-08-09.md`.

## Drift Entry — 2026-08-09 (Sovereign Nexus collision RESOLVED: two referents)
- **Source:** conflict scan over the prose-claim ledger
- **Type:** name collision resolved by evidence
- **Entities affected:** `org_sovereign_nexus` (AI), new `loc_sovereign_nexus` (region)
- **Description:** The collision flagged earlier the same day is now resolved. Early-project prose attests "Sovereign Nexus" as a **place** in three independent ways: "a strategically vital region of space", "a hyperlane chokepoint" where Union Intelligence observed Separatist hardliners massing forces, and the setting of **the Sovereign Nexus Crisis** — a high-stakes multi-faction standoff. That is consistent evidence across separate passages, not a one-off phrasing.
- **Resolution:** RESOLVED as **two distinct referents sharing a name**. `loc_sovereign_nexus` created for the hyperlane chokepoint region (unplaced — no map-authority row); `org_sovereign_nexus` remains the rogue AI intelligence from the Obsidian Dawn outcome file. Both records carry a disambiguation block pointing at the other. **Neither was merged into the other, and no relationship was inferred**: whether the AI is named for the region, operates from it, or the name was simply reused across project eras is explicitly recorded as UNDETERMINED.
- **Also surfaced, not minted:** *the Sovereign Nexus Crisis* — a named multi-faction standoff event with no canon record. Queued for the naming gate.
