---
title: L2 GUMAS Engine — API Reference
doc_id: ORION.TOOL.GUMASAPI.0001
doc_type: reference
version: 1.0.0
last_updated: 2026-02-07
authority: primary
layer: L2
domain: tooling
tags:
  - api
  - gumas
  - engine
summary: "Signatures + field maps for the GUMAS engine’s public objects."
related_docs:
  - ORION.TOOL.GUMASENGINE.0001
audience: dev
topic_type: Reference
---

# L2 GUMAS Engine — API Reference (v1.0.0)

## `GUMASEngine`
L2 GUMAS multi-agent galactic simulation engine.

Manages a GUMASState and advances it turn-by-turn through
conflict resolution, diplomacy, bias evolution, treaty
enforcement, and espionage mechanics.

Usage:
    engine = GUMASEngine(seed=42)
    engine.init_scenario()
    for _ in range(20):
        result = engine.step()
        print(f"Turn {result.turn}: {len(result.events_generated)} events")
    engine.export_state("output.json")

### `init_scenario(self, state: 'Optional[GUMASState]' = None, scenario_id: 'str' = 'gumas_canonical_v1') -> 'GUMASState'`
Initialize the simulation with a scenario.
### `step(self) -> 'TickResult'`
Advance the simulation by one turn.
### `run(self, n_turns: 'int' = 10) -> 'List[TickResult]'`
Run n_turns of simulation. Returns list of TickResults.
### `get_state(self) -> 'GUMASState'`
Return the current simulation state.
### `inject_event(self, event: 'SimulationEvent') -> 'None'`
Queue an external event for processing on the next tick.
### `export_state(self, path: 'str', include_history: 'bool' = True) -> 'None'`
Export current state to JSON file.


## State model (dataclasses)
### `LeaderState`
- `leader_id: str`
- `name: str`
- `role: str`
- `faction_id: str`
- `dominant_bias: BiasType`
- `secondary_biases: List[BiasType]`
- `bias_intensity: float`
- `plasticity: float`
- `evidence_gain_multiplier: float`
- `risk_tolerance: float`
- `diplomacy_openness: float`
- `escalation_threshold: float`
- `oversight_resistance: float`
- `public_legitimacy: float`
- `elite_support: float`
- `institutional_control: float`
- `war_pressure: float`
- `war_losses: int`
- `betrayals: int`
- `scandals: int`
- `economic_shock: float`
- `certainty: CertaintyTag`
### `FactionState`
- `faction_id: str`
- `name: str`
- `faction_type: FactionType`
- `notes: str`
- `leader_id: Optional[str]`
- `military_strength: float`
- `economic_strength: float`
- `technology_level: float`
- `population_stability: float`
- `trust_scores: Dict[str, float]`
- `reputation: float`
- `verification_demand: float`
- `deal_discount: float`
- `coalition_invite_weight: float`
- `economic_potential: float`
- `certainty: CertaintyTag`
### `ConflictState`
- `conflict_id: str`
- `parties: List[str]`
- `phase: ConflictPhase`
- `war_cost_estimate: Dict[str, float]`
- `stalemate_index: float`
- `internal_pressure: Dict[str, float]`
- `mediation_available: bool`
- `mediator_id: Optional[str]`
- `deescalation_probability: float`
- `eligible_compromises: List[str]`
- `turns_active: int`
- `casualty_index: float`
### `TreatyState`
- `treaty_id: str`
- `parties: List[str]`
- `phase: TreatyPhase`
- `enforcement_level: float`
- `violation_threshold: float`
- `ambiguity_tolerance: float`
- `breach_count: Dict[str, int]`
- `breach_history: List[Dict[str, Any]]`
- `reputation_impact: float`
- `terms: Dict[str, Any]`
- `turns_since_ratification: int`
- `is_active: bool`
### `SimulationEvent`
- `event_id: str`
- `event_type: EventType`
- `turn: int`
- `source_faction: Optional[str]`
- `target_faction: Optional[str]`
- `parameters: Dict[str, Any]`
- `severity: float`
- `description: str`
- `injected: bool`
### `TickResult`
- `turn: int`
- `events_processed: List[SimulationEvent]`
- `events_generated: List[SimulationEvent]`
- `state_changes: List[Dict[str, Any]]`
- `ethics_flags: List[Dict[str, Any]]`
- `timestamp: str`
### `GUMASState`
- `scenario_id: str`
- `turn: int`
- `seed: int`
- `factions: Dict[str, FactionState]`
- `leaders: Dict[str, LeaderState]`
- `conflicts: Dict[str, ConflictState]`
- `treaties: Dict[str, TreatyState]`
- `event_queue: List[SimulationEvent]`
- `history: List[TickResult]`
- `anchor: str`
- `ethics_protocol: str`
- `version: str`


## Enums
### `EventType`
- `MILITARY_ESCALATION` = `military_escalation`
- `DIPLOMATIC_OVERTURE` = `diplomatic_overture`
- `ESPIONAGE_EXPOSURE` = `espionage_exposure`
- `ECONOMIC_SHOCK` = `economic_shock`
- `LEADER_CHANGE` = `leader_change`
- `TREATY_PROPOSAL` = `treaty_proposal`
- `TREATY_VIOLATION` = `treaty_violation`
- `INTELLIGENCE_LEAK` = `intelligence_leak`
- `HUMANITARIAN_CRISIS` = `humanitarian_crisis`
- `TECHNOLOGY_BREAKTHROUGH` = `technology_breakthrough`
- `CULTURAL_MOVEMENT` = `cultural_movement`
- `INTERNAL_COUP` = `internal_coup`
- `MEDIATION_OFFER` = `mediation_offer`
- `TRADE_AGREEMENT` = `trade_agreement`
- `ECONOMIC_BOOM` = `economic_boom`
- `INFRASTRUCTURE_INVESTMENT` = `infrastructure_investment`
- `CUSTOM` = `custom`

---
Built for consistency, clarity, and care.
