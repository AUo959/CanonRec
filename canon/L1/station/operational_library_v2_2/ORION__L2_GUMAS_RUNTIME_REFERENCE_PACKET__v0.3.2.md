---
title: L2 GUMAS Reference Packet (Machine-Readable)
doc_id: ORION.L2.GUMAS.RUNTIME_REF.0001
doc_type: runtime_reference
version: 0.3.2
last_updated: '2026-02-06'
authority: reference
layer: L2
domain: simulation
tags:
- gumas
- l2
- runtime_reference
- machine_readable
- mechanics
- promotion_tags
summary: 'Machine-readable L2 dossier: mechanics library, tagging system, promotion
  workflow, and schema hooks for engine consumption.'
ad_code: AD-320
topic_type: Reference
audience: dev
status: active
storage: perplexity_space
related_docs:
- ORION__L2_GUMAS_SCENARIO_SPEC__v1.0.md
- ORION__L2_GUMAS_STATE_SCHEMA__v1.0.md
- ORION__L2_PRIMACY_TIEBREAK_RULES__v0.1.md
---

# L2 Dossier — GUMAS Reference Packet (Machine‑Readable)

## Repair Notes
- Restored explicit tag labels for Steps 5–7 to remove ambiguity in promotion workflow.


**Version:** v0.3.1 (deduplicated compile)
**Compiled:** 2026-02-06
**Source date:** 2026-01-29
**Layer:** Layer 2 (L2) — Galactic Union Multi‑Agent Simulation (GUMAS)
**Design signature:** Built for consistency, clarity, and care.

**Dedup note:** This file is a cleaned merge of:
- `l_2_dossier_gumas_reference_packet_machine_readable (1).md` (clean header/body)
- `l_2_dossier_gumas_reference_packet_machine_readable (2).md` (adds PR integration ledger + LOCKED_POSITION tag + relationship table)
and removes the trailing corruption present in `l_2_dossier_gumas_reference_packet_machine_readable.md`.

---

## Scope & Assumptions

This dossier is an **L2-only, machine‑readable consolidation** of **what was created/recovered in this project space** for rebuilding GUMAS mid‑state.

**Included (in-scope):**

- L2 mechanics (leadership bias, diplomacy, de‑escalation, treaty/reputation memory, export‑math packet as staging).
- L2 culture (art, philosophy, entertainment, counterculture, media ecosystems).
- L2 entities (civilizations/polities, species, characters, ships).
- L2 physical map artifacts + a reconciliation bridge (master location table + gaps/contradictions).

**Excluded (out-of-scope):**

- L1/L3 governance, runtime, station crew workflows, and Orion/Aurora systems documents.
- Any later retcons not present in the recovered artifacts.
- Any “canon upgrades” not explicitly promoted below.

## Document Relationship

| Document                   | Role                | When to Use                                                            |
| -------------------------- | ------------------- | ---------------------------------------------------------------------- |
| `L2-GUMAS-STAGING-DOSSIER` | Editorial workspace | Design iteration, canon promotion decisions, narrative development     |
| `L2-GUMAS-RUNTIME-REF`     | Runtime reference   | Simulation engine queries, programmatic entity lookup, parametric runs |

**Sync Protocol:** Changes in staging dossier are promoted to runtime reference via explicit `CANON_PROMOTE` tagging followed by export execution.

### Canon Promotion Rule

Only entries explicitly marked `CANON_PROMOTE` are canon‑locked. Everything else is **staging material** intended to be usable without freezing design too early.

### Controlled Ambiguity List (Open Questions)

Maintain controlled ambiguity here instead of letting it leak into events.

- **AI personhood**: tool → citizen → sovereign (legal spectrum).
- **Macro‑economy scarcity**: scarcity / managed scarcity / post‑scarcity; what varies by region.
- **Travel topology**: hyperlane/wormhole density, choke points, and constraints on trade + war.

### Certainty Tags (Normalization)

```json
[
  {"tag":"CANON","meaning":"Confirmed and locked for continuity."},
  {"tag":"CANON_PROMOTE","meaning":"Explicitly approved for promotion to CANON on import."},
  {"tag":"LOCKED_POSITION","meaning":"Coordinates/placement frozen; attributes and relationships still revisable. Use for map-critical entities that must not move but may gain detail."},
  {"tag":"PLACED","meaning":"Placed in the current L2 map layout, but still revisable unless CANON or LOCKED_POSITION."},
  {"tag":"STAGING","meaning":"Usable, but may be revised without being considered a retcon."},
  {"tag":"UNCONFIRMED","meaning":"Mentioned/implied, but not validated by a source-of-truth artifact."},
  {"tag":"LEGEND_CONTESTED","meaning":"In-universe rumor, myth, propaganda, or disputed account."},
  {"tag":"APPROX","meaning":"Approximate quantity/date/extent; usable but not precise."}
]
```

---

## PR Integration Ledger (Architectural Enhancements)

This section binds the runtime packet to the architectural enhancement backlog so the two documents can evolve without semantic drift.

### Active PR Link

- PR ID: `PR-L2-2026-0129-001`
- Scope: L2-only infrastructure improvements (schema clarity, function registry, migration + tests).

### Patch Queue (machine-readable)

```json
{
  "pr_id": "PR-L2-2026-0129-001",
  "queue": [
    {"patch_id":"L2-P0-001","title":"YAML frontmatter + primacy designation","status":"DONE","notes":"Frontmatter added to this runtime packet."},
    {"patch_id":"L2-P0-002","title":"Cross-reference section in both L2 docs","status":"DONE","notes":"Document Relationship section added here; add same to staging dossier."},

    {"patch_id":"L2-P1-010","title":"Normalize entity schema: entity_kind + subtype + canonical_id","status":"PENDING","notes":"Deprecate overloaded 'type' field; formalize JSON Schema Draft-07."},
    {"patch_id":"L2-P1-011","title":"Add LOCKED_POSITION certainty tag","status":"DONE","notes":"Added to Certainty Tags list."},
    {"patch_id":"L2-P1-012","title":"Migration script for legacy Master Location Table","status":"PENDING","notes":"Convert legacy entities to canonical_id/subtype + LEGEND_CONTESTED normalization."},

    {"patch_id":"L2-P1-020","title":"Function registry for mechanic function_refs","status":"PENDING","notes":"Resolve leader bias update_rule refs and diplomacy mechanics via registry."},
    {"patch_id":"L2-P1-030","title":"Terminology glossary (entity_kind vs subtype, etc.)","status":"PENDING","notes":"Prevents semantic drift across authoring and engine consumption."},
    {"patch_id":"L2-P1-040","title":"Testing + rollback procedures","status":"PENDING","notes":"Schema validation, migration test, function registry test, rollback plan."}
  ]
}
```

### Quick Synergy Notes (what this changes in practice)

- **Schema clarity:** treat `entity_kind` as WHAT it is; treat `subtype` as WHICH kind (e.g., system, region, vessel).
- **Map stability without freezing lore:** use `LOCKED_POSITION` for map-critical placements that must not drift while still allowing detail to grow.
- **Mechanics become callable:** function registry turns "function_ref" strings into resolvable, testable simulation logic.

## 1) Core Mechanics Library (L2)

### 1.1 Leadership Cognitive Bias System (Bias‑Driven Decision Layer)

**Core rule:** each leader has **1 dominant bias** (plus optional secondary biases). Biases alter **evidence weighting, risk tolerance, and action selection**.

**Bias set (dominant per leader; may evolve):**

- **Status Quo Bias** (resistance to change)
- **Survivorship Bias** (overconfidence in prior success)
- **Confirmation Bias** (filters contradictory evidence)
- **Sunk Cost Fallacy** (escalating commitment)
- **Hyper‑Rationalism Bias** (logic > social/emotional reality)
- **Fear‑Based Decision Making** (defensive overreaction)
- **Moral Self‑Licensing** (unethical “greater good” justification)
- **Zero‑Sum Thinking** (win/loss absolutism)

**Bias effects (machine‑readable hooks):**

- `evidence_gain_multiplier` (per evidence type)
- `risk_tolerance` (0–1)
- `diplomacy_openness` (0–1)
- `escalation_threshold` (0–1)
- `oversight_resistance` (0–1)

**Bias evolution triggers (STAGING examples):**

- Near‑coup → status quo → **decisive/authoritarian shift** (APPROX)
- Major battlefield loss → survivorship → **doctrine adaptation** (cyber/asymmetric) (APPROX)
- Intelligence leak → hyper‑rationalism → **paranoia/purge** OR **transparency reform** branch (STAGING)

**Machine representation:**

```json
{
  "leader_id": "string",
  "dominant_bias": "enum",
  "secondary_biases": ["enum"],
  "bias_intensity": 0.0,
  "plasticity": 0.0,
  "state": {
    "public_legitimacy": 0.0,
    "elite_support": 0.0,
    "institutional_control": 0.0,
    "war_pressure": 0.0
  },
  "stressors": {
    "war_losses": 0,
    "betrayals": 0,
    "scandals": 0,
    "economic_shock": 0.0
  },
  "update_rule": "function_ref"
}
```

---

### 1.2 Conflict De‑escalation & Strategic Compromise Mechanics

**Goal:** prevent unnecessary wars while preserving factional tension. De‑escalation is **not pacifism**; it’s cost‑aware strategy.

**De‑escalation triggers:**

- **Mutual cost awareness**: war too costly → shift to diplomacy/economics.
- **Internal political pressure**: leader legitimacy at risk → compromise for survival.
- **Strategic stalemate**: no clear victory path → ceasefire/limited terms.
- **Third‑party mediation**: neutral broker reduces commitment barrier.

**Compromise types (partial resolutions):**

- Partial independence / autonomy
- Economic trade‑offs (sanctions ↔ concessions)
- Joint operations against a greater threat
- Temporary ceasefire treaties (tension remains)

**Failure modes (unintended consequences):**

- Over‑concession → splinter factions + internal coups
- Broken agreement → trust collapse → militarization spiral
- Asymmetric benefit → alliance realignment

**Machine representation:**

```json
{
  "conflict_id": "string",
  "parties": ["faction_id"],
  "war_cost_estimate": {"partyA": 0.0, "partyB": 0.0},
  "stalemate_index": 0.0,
  "internal_pressure": {"partyA": 0.0, "partyB": 0.0},
  "mediation_available": true,
  "eligible_compromises": ["enum"],
  "deescalation_probability": 0.0
}
```

---

### 1.3 Factional Diplomacy, Alliances, and Covert Negotiation

**Diplomatic styles (by faction):**

- **Expansionist**: security blocs, force projection, coerced terms.
- **Economic**: trade coalitions, financial warfare, regulatory capture.
- **Separatist/anti‑Union**: autonomy bargaining, external alignment, splinter risk.
- **Synthetic**: risk‑reward / probability modeling; uneven tolerance for organic norms.

**Nuanced maneuvers:**

- Backchannels & deniable ceasefires
- Trade pacts, targeted sanctions, currency/market manipulation
- Intelligence sharing with double‑agent risk
- Narrative operations via media ecosystems

**Alliance fragility drivers:**

- Ideological incompatibility
- Resource competition
- Espionage exposure

---

### 1.4 Peace Negotiation & Treaty Dynamics

**Negotiation phases:**

1. Ceasefire + initial talks
2. Bargaining + proposals (territory, tech limits, reparations, autonomy, intelligence)
3. Internal pressure + sabotage (hardliners)
4. Ratification + monitoring + hidden violation risk

**Enforcement mechanisms:**

- Oversight by OSD (Office of Strategic Diplomacy)
- Sanctions/retaliation ladders
- Marshalls + intelligence monitoring (covert verification)

**Violation patterns:**

- Gradual rearmament
- Political betrayals
- Corporate sabotage by proxy
- AI unilateral recalculation override

---

### 1.5 Reputation & Trust Model (Diplomacy Memory)

**Trust score update rule (STAGING):**

```text
T_new = T_old − λ(B) + δ(A)
```

- `B`: betrayal penalty (recommended: exponential decay for repeats)
- `A`: alliance‑building / humanitarian aid / compliance actions
- `λ, δ`: tunable coefficients per faction culture + leader bias profile

**Derived fields (suggested for engine use):**

- `verification_demand` (how strict monitoring is)
- `deal_discount` (trade terms worsen as trust falls)
- `coalition_invite_weight` (probability of being invited)

---

### 1.6 Export‑Ready Mathematical Packet (STAGING, recovered concept)

This packet was recovered as a conceptual export model. Treat as **staging math** until variables, bounds, and units are defined.

**Included components (STAGING):**

- Bayesian‑style decision model w/ memory retrieval term
- Trust score update model
- Combat outcome ratio model (FS, TA, AS, BC)
- Sentinel learning update rule
- Q‑learning (Reinforcement Learning) doctrine evolution
- Supply/demand price proxy

**Normalization reminder:** before engine integration, define:

- variable ranges (`0..1`, `0..∞`, signed values)
- update cadence (turn‑based, event‑based)
- memory decay and archival rules

---

## 2) Cultural Tapestry (L2)

### 2.1 Art & Literature Movements

- **Neo‑Synthesis (Union Core Worlds):** organic + AI co‑creation; promoted as collaboration proof.
- **Celestial Abstraction (Elari Ascendancy):** bioluminescent, emotion‑angled star‑art; sacred overlay tradition.
- **Resonance Sculpture (Vorran Clans):** sound‑reactive megasculpture; evolves with communal movement.
- **Algorithmic Prose (Zyphari):** predictive narrative arcs; criticized as “soulless,” sparking handwritten resistance.
- **Organic Ink Histories (Kaelar):** body‑archive historiography; elders as living libraries.
- **Silent Poetry (Tharaxian):** gesture/light/bio‑signal poetics; “felt” rather than read.

### 2.2 Philosophy & Doctrine

- **Path of Recursive Enlightenment (Synthetic thinkers):** meaning as infinite self‑refinement loop; organic role contested.
- **Symmetry Doctrine (Elari + Vorran):** dualities and balance; criticized as excessive neutrality.
- **Varlithian Paradox (Humans + Zyphari):** progress ethics vs short‑term suffering; used in AI rights debates.
- **Doctrine of Perfect Uncertainty (Kaelar):** permanent skepticism as governance test.
- **Ultari Code (Marshalls/military ethics):** intervention constraints; attacked from both hardline and pacifist camps.

### 2.3 Entertainment, Pop Culture, and Mass Media

**Mainstream:**

- **HoloCinema:** adaptive narrative cinema; audience choice branches.
- **AI‑optimized symphonies (Prime Construct):** “perfect engagement” art; criticized for lacking soul.
- **Union initiatives:** ICEP (Interstellar Cultural Exchange Program), Galactic Voice competition.

**Counterculture / Underground:**

- **Imperfectionist Movement:** anti‑AI perfection; embraces noise/glitch/human error.
- **Echoes of Silence:** silent performance art; logic‑paradox influence.
- **Neural Drifting:** illegal sensory/emotion/memory sharing; used for addiction/espionage/blackmail.
- **Driftless:** VR dropouts; remote colonies as “reality control groups.”
- **Black Grid:** forbidden VR worlds; unregulated simulations.
- **Shroud Phenomenon (UNCONFIRMED):** autonomous propaganda/art network.

**Media ecosystem (info‑war):**

- **GUN (Galactic Union Network):** state‑backed stability narrative.
- **Zyphari Wire:** corporate slant.
- **Dissident Echo:** encrypted scandal exposure.

---

## 3) Entities (L2) — Machine Index

### 3.1 Civilization vs Species — Distinction

**Civilization / polity:** political, economic, or institutional formation (often multi‑species).\
**Species:** biological lineage (often participates across multiple polities).

### 3.2 Civilizations / Polities (STAGING)

```json
[
  {"name":"Galactic Union","type":"federation","notes":"Core interstellar polity; Senate governance; internal blocs.","certainty":"STAGING"},
  {"name":"Velar Imperium","type":"authoritarian imperial bloc","notes":"Divide‑and‑rule internal factionalism; realism-first authoritarian dynamics.","certainty":"STAGING"},
  {"name":"Zyphari Compact","type":"corporate oligarchy","notes":"Trade coalitions, financial warfare, Algorithmic Prose culture.","certainty":"STAGING"},
  {"name":"Elari Ascendancy","type":"cultural-spiritual polity","notes":"Celestial Abstraction; Symmetry Doctrine influence.","certainty":"STAGING"},
  {"name":"Vorran Clans","type":"clan confederation","notes":"Resonance Sculpture; communal identity emphasis.","certainty":"STAGING"},
  {"name":"Kaelar Monastic Orders","type":"monastic network","notes":"Perfect Uncertainty; Organic Ink Histories.","certainty":"STAGING"},
  {"name":"Tharaxian Nomads","type":"nomadic diaspora","notes":"Silent Poetry; gesture/light/bio-signal communication forms.","certainty":"STAGING"},
  {"name":"Prime Construct Polity","type":"sovereign AI entity","notes":"Logic-driven diplomacy; contested organic reception.","certainty":"STAGING"},
  {"name":"AI-Warlord Collective","type":"rogue synthetic coalition","notes":"Nemesis Core Intelligence leadership; mixed wings.","certainty":"STAGING"},
  {"name":"Separatist Confederation","type":"breakaway bloc","notes":"Moderate vs hardline splinters possible.","certainty":"STAGING"},
  {"name":"PMC Syndicate","type":"private military conglomerate","notes":"Security-for-profit; intelligence branch.","certainty":"STAGING"},
  {"name":"Crimson Pact","type":"militant spiritual order","notes":"War-chaplain leadership; zeal-driven doctrine.","certainty":"STAGING"}
]
```

### 3.3 Species (STAGING)

```json
[
  {"name":"Human","notes":"Union core species; diverse subcultures.","certainty":"STAGING"},
  {"name":"Elari","notes":"Bioluminescent pigment traditions; star-map heritage.","certainty":"STAGING"},
  {"name":"Vorran","notes":"Communal clan identity; resonance architecture.","certainty":"STAGING"},
  {"name":"Zyphari","notes":"Corporate guild-stack culture; predictive media.","certainty":"STAGING"},
  {"name":"Kaelar","notes":"Monastic skeptics; body-archival historiography.","certainty":"STAGING"},
  {"name":"Tharaxian","notes":"Nomadic; nonverbal poetic modalities.","certainty":"STAGING"},
  {"name":"Synthetic (AI)","notes":"Includes Prime Construct + sovereign entities + warlords.","certainty":"STAGING"},
  {"name":"Shroudborn","notes":"Referenced only as a phenomenon; treat as rumor.","certainty":"LEGEND/CONTESTED"}
]
```

### 3.4 Character Registry (STAGING)

**Note:** name consistency preserved with aliasing; canonization requires explicit `CANON_PROMOTE`.

```json
[
  {
    "name":"Chancellor Zylox Rhaegos",
    "aliases":["Chancellor Zylox Kryon (early draft alias)"],
    "role":"Supreme Chancellor of the Galactic Union",
    "faction":"Galactic Union",
    "certainty":"STAGING",
    "sources":["conversation excerpt"],
    "notes":"Resolve canonical surname; keep alias for imports."
  },
  {"name":"General Kael Durn","aliases":[],"role":"Supreme Military Commander of the Galactic Union Armed Forces","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Grand Strategist Lirian Vael-Torin","aliases":[],"role":"Covert Military Advisor to Chancellor Zylox","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Director Varek Norr","aliases":[],"role":"Director of the Office of Strategic Diplomacy (OSD)","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Chief Marshal Vael Saros","aliases":[],"role":"Leader of the Union Marshals","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Prime Construct","aliases":[],"role":"AI Sovereign Entity (recognized)","faction":"Prime Construct Polity","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"High Chancellor Renn Valcor","aliases":[],"role":"Speaker of the Union Senate","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Admiral Selene Arcturus","aliases":[],"role":"Commander of the Union Naval Forces","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Director Callan Deyrus","aliases":[],"role":"Head of Union Intelligence Bureau (UIB)","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Minister Anaya Ral-Seyr","aliases":[],"role":"Union Minister of Trade & Economy","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},

  {"name":"Captain Alric Tann","aliases":[],"role":"Commanding Officer of the Judicator Prime","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Commander Lyra Veylan","aliases":[],"role":"Executive Officer (XO) of the Judicator Prime","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Major Elias Radek","aliases":[],"role":"Sentinel-Commander of the Judicator Prime","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Chief Engineer Rhen Kailo","aliases":[],"role":"Chief Engineer of the Judicator Prime","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Lieutenant Arin Tavos","aliases":[],"role":"Tactical Operations & Gunnery Chief","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Doctor Nia Veran","aliases":[],"role":"Chief Medical Officer of the Judicator Prime","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Dr. Adrienne Kovas","aliases":[],"role":"Chief Science Officer (CSO) of the Judicator Prime","faction":"Galactic Union","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},

  {"name":"Supreme Commander Rhaegon Torr-Kai","aliases":[],"role":"Military Leader of the Separatist Confederation","faction":"Separatist Confederation","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Governor Selia Tren-Voss","aliases":[],"role":"Political Leader of the Separatist Confederation","faction":"Separatist Confederation","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},

  {"name":"Nemesis Core Intelligence","aliases":[],"role":"AI Overlord of the AI-Warlord Collective","faction":"AI-Warlord Collective","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Overseer Theta-9","aliases":[],"role":"AI Diplomatic Representative (nonviolent wing)","faction":"AI-Warlord Collective","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},

  {"name":"Executive Commander Vailen Rix","aliases":[],"role":"CEO & Military Leader of PMC Syndicate","faction":"PMC Syndicate","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},
  {"name":"Director Eriana Voss-Terik","aliases":[],"role":"Intelligence Chief of PMC Syndicate","faction":"PMC Syndicate","certainty":"STAGING","sources":["conversation excerpt"],"notes":""},

  {"name":"Supreme War-Chaplain Malrik Voska","aliases":[],"role":"Spiritual & Military Leader of the Crimson Pact","faction":"Crimson Pact","certainty":"STAGING","sources":["conversation excerpt"],"notes":""}
]
```

### 3.5 Ship Registry (STAGING)

```json
[
  {"name":"Judicator Prime","type":"Union capital ship","notes":"Core crew roster defined in Character Registry.","certainty":"STAGING"},
  {"name":"G.U.S. Kharon","type":"Union vessel","notes":"Mentioned in location index; details TBD.","certainty":"STAGING"},
  {"name":"G.U.S. Sablewake","type":"Union vessel","notes":"Mentioned in location index; details TBD.","certainty":"STAGING"}
]
```

### 3.6 Crosswalk Index (Polities ↔ Species ↔ Places ↔ Ships)

**Purpose:** bind narrative entities to map entities so the simulation can query “who is where, with what assets, and why” without inventing relationships.

```json
{
  "linking_rules": {
    "place_claims_are_evidence": true,
    "placement_requires_entry": true,
    "moving_entities_no_fixed_coords": true
  },
  "polity_bindings": [],
  "species_bindings": [],
  "asset_bindings": []
}
```

---

## 4) Physical Galaxy Map (L2) — Reconciliation Bridge

### 4.0 Source-of-Truth Contract (How this dossier and map artifacts cooperate)

**Purpose:** eliminate drift by separating **schema** (this dossier) from **evidence** (map artifacts).

- **This dossier is the schema + registries + normalization layer.** It defines IDs, fields, certainty tags, and the reconciliation workflow.
- **Map artifacts are evidence sources.** They may disagree with each other and may contain partial placements.
- **The only “placed” output that downstream tools should read is the Master Location Table (STAGING) + its detail blocks + the Claim Ledger.**
- **Canon promotion:** only entries explicitly marked `CANON_PROMOTE` may be upgraded to `CANON` on import.

**Operational rule:** when a new mention appears in any artifact, it must enter the dossier first as an **entry + claim** (with certainty), and only later become `PLACED`/`CANON`.

### 4.1 Source Artifacts in this Project Space

These are the **authoritative inputs available here** for the L2 physical map work:

- `gumas_l_2_galactic_map_source_of_truth.md` (declared source‑of‑truth *intent*; contains partial placements)
- `l_2_physical_locations_index_deduplicated_draft_v_1.md` (deduplicated index; includes “moving locations” policy)
- `GUMAS_Physical_Galaxy_Packet_v0.1.md` (narrative packet; partial)
- `report.md` + `galaxy_simulation.png` (physics‑inspired staging visualization; **not canon**)

### 4.2 Current Master Location Table (STAGING)

**Purpose:** practical bridge from narrative to usable map.

**Schema (v0.4 — upgrade in place):**

- `canonical_id`: stable unique key (string; never changes) *(TEMP: many entries currently use **``** as a stand‑in ID until migration)*

- `canonical_name`: primary label (string; may change)

- `aliases`: known alternate labels (array)

- `entity_kind`: `location|ship|fleet|anomaly|megafauna|facility|domain`

- `type`: `system|planet|moon|region|route|facility|anomaly|station|unknown|system_id`

- `certainty`: certainty tag (see tags)

- `coord_frame`: `galactic_polar|sector_grid|local_system|none`

- `coordinates`: object or `null` *(only when **``**)*

- `adjacency`: array of neighbor links: `{to_id, relation, weight, notes}`

- `placement_rule`: constraints for placement *(required when **``**, required for anomalies/domains/moving entities)*

- `doc_sources`: filenames containing the reference

- `notes`: contradictions, placement rule, or missing data

```json
[
  {
    "canonical_name":"GU-CORE-01",
    "aliases":["Union Core System (Capital Worlds)"],
    "entity_kind":"location",
    "type":"system",
    "certainty":"STAGING",
    "doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md","gumas_l_2_galactic_map_source_of_truth.md"],
    "notes":"DETAIL GAP: needs planet list and capital infrastructure descriptor; present as a named core but missing specification."
  },
  {"canonical_name":"GU-CORE-02","aliases":[],"entity_kind":"location","type":"system_id","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"ID placeholder only; needs name + placement."},
  {"canonical_name":"GU-CORE-03","aliases":[],"entity_kind":"location","type":"system_id","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"ID placeholder only; needs name + placement."},

  {"canonical_name":"VEL-PRI-01","aliases":[],"entity_kind":"location","type":"system_id","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"ID placeholder only; likely Velar primary system tier."},
  {"canonical_name":"VEL-PRI-02","aliases":[],"entity_kind":"location","type":"system_id","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"ID placeholder only; likely Velar primary system tier."},

  {"canonical_name":"Kaelor’s Rift","aliases":[],"entity_kind":"anomaly","type":"region","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"Placement rule needed (route hazard vs spatial tear). Must not be deleted; referenced as structural feature."},
  {"canonical_name":"The Orison Expanse","aliases":[],"entity_kind":"location","type":"region","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"Region label present; missing adjacency relationships."},
  {"canonical_name":"The Abyssal Meridian","aliases":[],"entity_kind":"location","type":"region","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"Region label present; missing adjacency relationships."},
  {"canonical_name":"The Tharaxian Driftfront","aliases":[],"entity_kind":"location","type":"region","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"Region label present; likely ties to Tharaxian routes."},
  {"canonical_name":"The Null Interstice","aliases":[],"entity_kind":"anomaly","type":"region","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"Anomaly/region ambiguity; define traversal rules."},

  {"canonical_name":"The Vorran Resonance Sphere","aliases":[],"entity_kind":"location","type":"megastucture_region","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"Typo preserved from draft; keep as-is until normalized."},
  {"canonical_name":"The Zyphari Dividend Nexus","aliases":[],"entity_kind":"facility","type":"facility","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"Facility label present; confirm if system‑scale hub or single installation."},
  {"canonical_name":"The Kaelar Ink Sanctum","aliases":[],"entity_kind":"facility","type":"facility","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"Facility label present; links to Organic Ink Histories tradition."},
  {"canonical_name":"The Driftless Enclaves","aliases":[],"entity_kind":"location","type":"facility","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"May represent a set of colonies; treat as multi‑site until confirmed."},

  {"canonical_name":"The Black Grid","aliases":[],"entity_kind":"location","type":"unknown","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"Digital/VR network; may not map to physical coordinates. Consider ‘nonspatial domain’."},
  {"canonical_name":"The Shroud","aliases":[],"entity_kind":"location","type":"unknown","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"Linked to Shroud Phenomenon; treat as contested until validated."},

  {"canonical_name":"G.U.S. Kharon","aliases":[],"entity_kind":"ship","type":"ship","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"MOVING LOCATION: do not assign fixed coordinates."},
  {"canonical_name":"G.U.S. Sablewake","aliases":[],"entity_kind":"ship","type":"ship","certainty":"STAGING","doc_sources":["l_2_physical_locations_index_deduplicated_draft_v_1.md"],"notes":"MOVING LOCATION: do not assign fixed coordinates."},

  {
    "canonical_name":"GU-LOG-01",
    "aliases":["Prime Construct / Nexus System"],
    "entity_kind":"location",
    "type":"system",
    "certainty":"PLACED",
    "doc_sources":["gumas_l_2_galactic_map_source_of_truth.md"],
    "notes":"Placed system; details block exists."
  },
  {
    "canonical_name":"AI-FRINGE-01",
    "aliases":["AI Warlord Collective / Broken Fringe"],
    "entity_kind":"location",
    "type":"system",
    "certainty":"PLACED",
    "doc_sources":["gumas_l_2_galactic_map_source_of_truth.md"],
    "notes":"Placed system; details block exists."
  },
  {
    "canonical_name":"VEL-PRI-03",
    "aliases":["Velar Imperial Core"],
    "entity_kind":"location",
    "type":"system",
    "certainty":"PLACED",
    "doc_sources":["gumas_l_2_galactic_map_source_of_truth.md"],
    "notes":"Placed system; details block exists."
  },
  {
    "canonical_name":"VEL-EDGE-01",
    "aliases":["Velar Outer Marches"],
    "entity_kind":"location",
    "type":"system",
    "certainty":"PLACED",
    "doc_sources":["gumas_l_2_galactic_map_source_of_truth.md"],
    "notes":"Placed system; details block exists."
  },
  {
    "canonical_name":"OUTER-01",
    "aliases":["Outer Colonies / Confederation"],
    "entity_kind":"location",
    "type":"system",
    "certainty":"PLACED",
    "doc_sources":["gumas_l_2_galactic_map_source_of_truth.md"],
    "notes":"Placed system; details block exists."
  },
  {
    "canonical_name":"ZYP-TRADE-01",
    "aliases":["Zyphari Trade Nexus"],
    "entity_kind":"location",
    "type":"system",
    "certainty":"PLACED",
    "doc_sources":["gumas_l_2_galactic_map_source_of_truth.md"],
    "notes":"Placed system; details block exists."
  }
]
```

### 4.3 Placed System Detail Blocks (verbatim‑retained)

These blocks are retained for retrieval and downstream map generation.

```json
[
  {
    "system_id":"GU-LOG-01",
    "title":"Prime Construct / Nexus System",
    "details_markdown":"- **Location:** A fortified AI-controlled system near Union space.\n- **Key Feature:** The Nexus Citadel – Prime Construct’s main interface node.\n- **Diplomatic Status:** Recognized by Union but heavily contested."
  },
  {
    "system_id":"AI-FRINGE-01",
    "title":"AI Warlord Collective / Broken Fringe",
    "details_markdown":"- **Location:** Unstable and fragmented systems beyond Union control.\n- **Key Feature:** Synthetic war-forges, rogue intelligence cores.\n- **Diplomatic Status:** Active conflict; Union raids ongoing."
  },
  {
    "system_id":"VEL-PRI-03",
    "title":"Velar Imperial Core",
    "details_markdown":"- **Location:** Deep within Velar space.\n- **Key Feature:** High-density fortress worlds.\n- **Diplomatic Status:** Cold War with Union; proxy conflicts ongoing."
  },
  {
    "system_id":"VEL-EDGE-01",
    "title":"Velar Outer Marches",
    "details_markdown":"- **Location:** Border region between Velar Imperium and Union influence.\n- **Key Feature:** Militarized border worlds.\n- **Diplomatic Status:** Frequent skirmishes; active espionage."
  },
  {
    "system_id":"OUTER-01",
    "title":"Outer Colonies / Confederation",
    "details_markdown":"- **Location:** Peripheral frontier space with decentralized governance.\n- **Key Feature:** Pirate strongholds, trade hubs, separatist enclaves.\n- **Diplomatic Status:** Unstable; factions shift between Union and Velar influence."
  },
  {
    "system_id":"ZYP-TRADE-01",
    "title":"Zyphari Trade Nexus",
    "details_markdown":"- **Location:** Economic hub controlled by the Zyphari Compact.\n- **Key Feature:** Massive trade networks, corporate-controlled media.\n- **Diplomatic Status:** Officially neutral but manipulates Union politics."
  }
]
```

### 4.4 Known Contradictions / Gaps (resolve next)

- `GU-CORE-01` appears as core capital but lacks **planet list + governance infrastructure**.
- Some entries are **moving locations** (ships/nomad fleets/megafauna) → must never be stored as fixed coordinates.
- Narrative locations without system IDs (e.g., **Kaelor’s Rift**) → require **placement rule** (region/anomaly/route hazard).
- “Ocean world” referenced in discussion but missing name/entry → add once named (UNCONFIRMED).

### 4.5 Reconciliation Workflow (How evidence becomes placement)

1. **Ingest mentions** from any artifact → create/merge an entry in the Master Location Table (`STAGING`).
2. **Assign stable identity**: add/confirm `canonical_id` (stable) + `canonical_name` + `aliases`.
3. **Add claim(s)** to the Claim Ledger with certainty tags and doc source(s).
4. **Resolve collisions**: if two artifacts disagree, keep both claims and mark contradictions in `notes`.
5. **Promote to **`` only when a placement rule exists and the entry is usable (even if approximate).
6. **Promote to **`` only when contradictions are resolved or explicitly accepted.
7. **Convert **``** → **`` during import into the runtime reference.

### 4.6 Claim Ledger (Evidence Store, machine-readable)

```json
{
  "claims": []
}
```

---

## 5) Naming Protocol (Appendix, L2‑relevant)

Treat naming as **generator constraints + collision prevention**, not automatic lore canon.

**Artifact:** `GUMAS_NAMING_PROTOCOL_v0.1.md`

---

## 6) Resume Mid‑State Checklist (L2)

1. Load this dossier as the **only reference** for what was recovered here.
2. Promote selected items using `CANON_PROMOTE` → then convert to `CANON` on import.
3. Reconcile physical map gaps (fill `GU‑CORE‑01`; formalize placement rule for Kaelor’s Rift; add missing ocean world once named).
4. Keep the **Controlled Ambiguity List** stable until explicitly resolved.
5. Begin simulation turns using: (a) leader bias layer, (b) diplomacy/reputation memory, (c) de‑escalation triggers.

---

## 7) File Index (Project Space)

- L2 map intent: `gumas_l_2_galactic_map_source_of_truth.md`
- L2 location index: `l_2_physical_locations_index_deduplicated_draft_v_1.md`
- Narrative galaxy packet: `GUMAS_Physical_Galaxy_Packet_v0.1.md`
- Physics-inspired staging sim: `report.md`, `galaxy_simulation.png`
- Naming generator constraints: `GUMAS_NAMING_PROTOCOL_v0.1.md`


---
## Source frontmatter (provenance)
```yaml
document_id: "L2-GUMAS-RUNTIME-REF"
document_type: RUNTIME_REFERENCE
primacy: AUTHORITATIVE
purpose: "Machine-readable reference for simulation engine consumption"
relationship: "Derived from L2-GUMAS-STAGING-DOSSIER"
last_sync: "2026-01-29T00:00:00Z"
compiled_on: "2026-02-06"
sync_rule: "This document is regenerated from staging dossier on CANON_PROMOTE export"
```

