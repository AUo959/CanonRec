# L2 Mechanic Registry

Status: structured staging draft  
Reason for separate handling: the current L2 validator defines a `mechanic` type but its
`entity_kind` rules do not fully accept that path yet. This registry therefore preserves the
intended mechanic schema without forcing a bad workaround into the canonical entity kinds.

```json
[
  {
    "canonical_id": "MECH-GOV-001",
    "canonical_name": "Faction Decision Retrieval Model",
    "aliases": ["Faction Strategy Retrieval", "Bayesian Memory Strategy"],
    "entity_kind": "mechanic",
    "certainty": "STAGING",
    "doc_sources": [
      "intake/textAu.txt",
      "intake/recovered_textAu__2026-03-13/L2/03_galactic_union_mechanics_and_models.md"
    ],
    "notes": "Recovered as the main faction decision logic combining present conditions with retrieved historical context.",
    "mechanic_id": "MECH-GOV-001",
    "category": "governance",
    "description": "Factions choose actions by combining current state with remembered prior outcomes, betrayals, and negotiation history.",
    "parameters": {
      "inputs": ["current_scenario", "retrieved_memory", "action_space"],
      "design_intent": "adaptive faction behavior"
    },
    "function_ref": null
  },
  {
    "canonical_id": "MECH-DIP-001",
    "canonical_name": "Diplomatic Trust Decay Model",
    "aliases": ["Trust Score System"],
    "entity_kind": "mechanic",
    "certainty": "STAGING",
    "doc_sources": [
      "intake/textAu.txt",
      "intake/recovered_textAu__2026-03-13/L2/03_galactic_union_mechanics_and_models.md"
    ],
    "notes": "One of the most stable mechanics recovered from the source.",
    "mechanic_id": "MECH-DIP-001",
    "category": "diplomacy",
    "description": "Tracks trust as a function of betrayal penalties and alliance-building gains over time.",
    "parameters": {
      "formula": "T_new = T_old - lambda(B) + delta(A)"
    },
    "function_ref": null
  },
  {
    "canonical_id": "MECH-MIL-001",
    "canonical_name": "Weighted Combat Resolution",
    "aliases": ["Fleet Strength Ratio Model"],
    "entity_kind": "mechanic",
    "certainty": "STAGING",
    "doc_sources": [
      "intake/textAu.txt",
      "intake/recovered_textAu__2026-03-13/L2/03_galactic_union_mechanics_and_models.md"
    ],
    "notes": "Recovered as a doctrine-aware combat model emphasizing strategy and conditions over raw force.",
    "mechanic_id": "MECH-MIL-001",
    "category": "military",
    "description": "Resolves battle outcomes through fleet strength, tactical adaptation, strategic superiority, and battlefield conditions.",
    "parameters": {
      "formula": "W = (FS_U * TA_U * AS_U * BC) / (FS_E * TA_E * AS_E * BC)"
    },
    "function_ref": null
  },
  {
    "canonical_id": "MECH-MIL-002",
    "canonical_name": "Sentinel Adaptive Learning",
    "aliases": ["Sentinel Tactical Effectiveness Model"],
    "entity_kind": "mechanic",
    "certainty": "STAGING",
    "doc_sources": [
      "intake/textAu.txt",
      "intake/recovered_textAu__2026-03-13/L2/03_galactic_union_mechanics_and_models.md"
    ],
    "notes": "Recovered as the main experience-growth loop for elite Sentinel-class forces.",
    "mechanic_id": "MECH-MIL-002",
    "category": "military",
    "description": "Updates Sentinel effectiveness based on mission successes and failures.",
    "parameters": {
      "formula": "S_new = S_old + alpha(E_success) - beta(E_failure)"
    },
    "function_ref": null
  },
  {
    "canonical_id": "MECH-MIL-003",
    "canonical_name": "Doctrine Reinforcement Loop",
    "aliases": ["Q-Learning War Doctrine"],
    "entity_kind": "mechanic",
    "certainty": "STAGING",
    "doc_sources": [
      "intake/textAu.txt",
      "intake/recovered_textAu__2026-03-13/L2/03_galactic_union_mechanics_and_models.md"
    ],
    "notes": "Recovered as the mechanism that lets battle doctrine shift after repeated outcomes.",
    "mechanic_id": "MECH-MIL-003",
    "category": "military",
    "description": "Adjusts doctrine priorities through reinforcement feedback from prior victories and losses.",
    "parameters": {
      "formula": "Q(s, a) = Q(s, a) + alpha * (R + gamma * max_a'(Q(s', a')) - Q(s, a))"
    },
    "function_ref": null
  },
  {
    "canonical_id": "MECH-ECO-001",
    "canonical_name": "Supply and Demand Resource Model",
    "aliases": ["Economic Equilibrium Model"],
    "entity_kind": "mechanic",
    "certainty": "STAGING",
    "doc_sources": [
      "intake/textAu.txt",
      "intake/recovered_textAu__2026-03-13/L2/03_galactic_union_mechanics_and_models.md"
    ],
    "notes": "Recovered as the base economic model supporting war production and trade pressure.",
    "mechanic_id": "MECH-ECO-001",
    "category": "economy",
    "description": "Models resource price movement through demand divided by supply.",
    "parameters": {
      "formula": "P_eq = D / S"
    },
    "function_ref": null
  },
  {
    "canonical_id": "MECH-CUL-001",
    "canonical_name": "Non-War Event Distribution",
    "aliases": ["Peace-Weighted Event Balance"],
    "entity_kind": "mechanic",
    "certainty": "STAGING",
    "doc_sources": [
      "intake/textAu.txt",
      "intake/recovered_textAu__2026-03-13/L2/03_galactic_union_mechanics_and_models.md"
    ],
    "notes": "One of the strongest balancing recommendations in the recovery: major events should skew toward diplomacy, science, culture, and economy rather than war alone.",
    "mechanic_id": "MECH-CUL-001",
    "category": "culture",
    "description": "Biases scenario generation toward non-war event types across a simulation cycle.",
    "parameters": {
      "target_ratio": "60-70% non-war major events"
    },
    "function_ref": null
  },
  {
    "canonical_id": "MECH-GOV-002",
    "canonical_name": "Tiered Memory Storage",
    "aliases": ["Core Dynamic Archived Memory"],
    "entity_kind": "mechanic",
    "certainty": "STAGING",
    "doc_sources": [
      "intake/textAu.txt",
      "intake/recovered_textAu__2026-03-13/L2/03_galactic_union_mechanics_and_models.md",
      "intake/recovered_textAu__2026-03-13/L3/01_memory_architecture_and_registry.md"
    ],
    "notes": "Sits between L2 simulation design and L3 implementation concerns.",
    "mechanic_id": "MECH-GOV-002",
    "category": "governance",
    "description": "Organizes simulation memory into core, dynamic, and archived layers with relevance decay and compression.",
    "parameters": {
      "formula": "M_faction = B + alpha * R + beta * I + gamma * P"
    },
    "function_ref": null
  },
  {
    "canonical_id": "MECH-GOV-003",
    "canonical_name": "Event-Triggered Memory Recall",
    "aliases": ["ETMR"],
    "entity_kind": "mechanic",
    "certainty": "STAGING",
    "doc_sources": [
      "intake/textAu.txt",
      "intake/recovered_textAu__2026-03-13/L2/03_galactic_union_mechanics_and_models.md",
      "intake/recovered_textAu__2026-03-13/L3/01_memory_architecture_and_registry.md"
    ],
    "notes": "Recovered as a way to recall prior betrayals or treaties only when relevant to the active decision context.",
    "mechanic_id": "MECH-GOV-003",
    "category": "governance",
    "description": "Recalls historical events probabilistically when the current situation strongly matches prior high-impact contexts.",
    "parameters": {
      "formula": "P_recall = (E_impact * T_relevance) / (D_decay + C)"
    },
    "function_ref": null
  }
]
```

---

## Implementation Status (2026-06-13)

The faction-decision and trust mechanics are no longer design-only. Realized
in the governed control plane (tracked + tested), not the ungoverned engine dir:

| Mechanic | Status | Implementation |
|---|---|---|
| **MECH-GOV-001** Faction Decision Retrieval Model | **IMPLEMENTED** | `tools/mech_gov_001.py` — `FactionDecisionModel` (memory retrieval → disposition → action). Realizes the canon rules "betrayal history raises odds of future betrayal" and "weakness increases odds of negotiation". |
| **MECH-DIP-001** Diplomatic Trust Decay | **IMPLEMENTED** | same module — `T_new = T_old - lambda*B + delta*A` as the trust-update rule the decision model reads. |
| **MECH-SOC-001** Population Grievance Memory | **IMPLEMENTED** | `tools/mech_gov_001.py` — `PopulationGrievanceModel`. Populations remember hardship/repression/broken-promises (grievance) and relief/autonomy/prosperity (easing) with slow decay; net grievance feeds rebellion onset. Grounded in `canon/L2/social_dynamics/` (DSI, social cohesion, `P_stability = E + T - C`). |
| **MECH-SOC-002** Insurgency Resolution / War-Weariness | **IMPLEMENTED** | `tools/mech_gov_001.py` — `WarWearinessModel`. A grinding war wearies its population; eroding popular support lets the engine's own SUPPRESSED gate become reachable — the resolution the seed-42 attractor never had. |
| **MECH-SOC-003** Diplomatic Stability Index (non-war progression gate) | **IMPLEMENTED** | `tools/mech_gov_001.py` — `DiplomaticStabilityModel`. `DSI = (P+E+S)/(C+M)`: cohesion/economy over militarization → governance legitimacy → fewer insurgency onsets. Realizes `canon/L2/social_dynamics/non_war_progression_mechanics.md`. |

The episodic-memory substrate is a clean port of the recovered 2025
`memory_system.py` (importance-weighted strength, half-life decay,
reinforcement, recency+importance+relevance retrieval). One deliberate
correction: the original used wall-clock `time.time()`, breaking determinism;
the implementation uses a **logical turn clock**, so seed + event log → a
reproducible decision trace. Tests: `tests/test_mech_gov_001.py` (6).

Remaining: MECH-MIL-001 (weighted combat) and the recall-probability model
are still design-only; wiring MECH-GOV-001 into the live `engine_advanced`
faction loop is the next integration step.
