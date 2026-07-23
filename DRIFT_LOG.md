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
