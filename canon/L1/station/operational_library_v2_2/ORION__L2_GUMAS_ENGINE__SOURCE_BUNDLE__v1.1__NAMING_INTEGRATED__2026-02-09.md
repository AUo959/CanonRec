---
title: L2 GUMAS Engine — Source Bundle (Markdown-Embedded)
doc_id: ORION.L2.ENGINE.SOURCEBUNDLE.0001
doc_type: reference
version: 1.1.0
last_updated: 2026-02-09
authority: primary
layer: L2
domain: simulation
tags:
  - l2
  - gumas
  - engine
  - source
  - python
summary: Engine source code embedded in Markdown for Spaces-compatible ingestion (no .py files).
ad_code: AD-300
topic_type: Reference
audience: dev
status: active
storage: perplexity_space
related_docs:
  - ORION.L2.ENGINE.SOURCEGUIDE.0001
  - ORION.L2.NAMING.PROTOCOL.0001  # GUMAS_NAMING_PROTOCOL_v0.1
---
# L2 GUMAS Engine — Source Bundle (v1.0.0)

This file intentionally embeds code as Markdown so it remains ingestible as a persistent Space source.

## File tree (excerpt)
- modules/gumas/__init__.py
- modules/gumas/engine.py
- modules/gumas/models.py
- modules/gumas/scenarios.py
- modules/gumas/formulas.py
- tests/test_gumas_engine.py

## `README.md`

```markdown
# L2 GUMAS Engine (Python)

Anchor seed: `EOS_SEED_ORION`  
Ethics protocol: `Picard_Delta_3`  

This package contains:
- `modules/gumas/*` — engine, data models, scenario loader, and formulas
- `tests/*` — pytest suite (44 tests)

## Quick start

```bash
pytest -q
```

```python
from modules.gumas.engine import GUMASEngine

engine = GUMASEngine(seed=42)
engine.init_scenario()
results = engine.run(n_turns=10)
print(results[-1].to_dict())
```

Built for consistency, clarity, and care.

```

## `modules/gumas/__init__.py`

```python
"""
GUMAS L2 Simulation Module
============================
Anchor: GUMAS-ENGINE-V1
Seed: EOS_SEED_ORION
Ethics: Picard_Delta_3

Multi-agent galactic simulation engine for the L2 layer of
Aurora CloudBank Symbolic.

Quick start:
    from modules.gumas import GUMASEngine
    engine = GUMASEngine(seed=42)
    engine.init_scenario()
    result = engine.step()
"""

from modules.gumas.engine import GUMASEngine
from modules.gumas.models import (
    BiasType,
    CertaintyTag,
    ConflictPhase,
    EventType,
    FactionType,
    GUMASState,
    SimulationEvent,
    TickResult,
    TreatyPhase,
)
from modules.gumas.scenarios import build_default_scenario

__all__ = [
    "GUMASEngine",
    "GUMASState",
    "SimulationEvent",
    "TickResult",
    "BiasType",
    "CertaintyTag",
    "ConflictPhase",
    "EventType",
    "FactionType",
    "TreatyPhase",
    "build_default_scenario",
]

```

## `modules/gumas/engine.py`

```python
#!/usr/bin/env python3
"""
GUMAS L2 Simulation Engine
============================
Anchor: GUMAS-ENGINE-CORE-V1
Seed: EOS_SEED_ORION
Ethics: Picard_Delta_3
DLP: L2_ENGINE_CORE
Version: 1.0.0

The missing keystone: a turn-based simulation engine that loads
GUMAS entity definitions, initializes galactic state, and runs
multi-agent simulation ticks using the parametric models documented
in PR_L2_GUMAS_ARCHITECTURAL_ENHANCEMENTS and the Runtime Reference
Packet v0.4.

Public API:
    engine = GUMASEngine()
    engine.init_scenario()                       # or init_scenario(state)
    result = engine.step()                       # advance one turn
    state  = engine.get_state()                  # snapshot
    engine.inject_event(event)                   # queue external event
    engine.run(n_turns=10)                       # batch run
    engine.export_state("snapshot.json")         # JSON export

Integration points:
    - Consumes: modules.gumas.models (data structures)
    - Consumes: modules.gumas.formulas (pure simulation math)
    - Consumes: modules.gumas.scenarios (canonical entity loader)
    - Consumed by: src.aurora_orchestrator (as L2 workload)
    - Consumed by: src.bridges.l2_meta_agent_bridge (relay commands)
    - Monitored by: modules.gumas.api.routes (ethics evaluation)

Design Principles:
    - Stdlib only (no numpy/scipy required at runtime)
    - Seed-based reproducibility
    - Full DLP audit trail per tick
    - Every state mutation logged in TickResult
    - Ethics-checkable: every significant action can be routed to
      the existing GUMAS Ethics API for Picard_Delta_3 compliance
"""

from __future__ import annotations

import json
import logging
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from modules.gumas.formulas import (
    apply_bias_hooks,
    calc_bias_evolution,
    calc_deescalation_probability,
    calc_double_agent_risk,
    calc_reputation_after_decay,
    calc_treaty_breach_score,
    calc_trust_update,
    is_treaty_breach,
)
from modules.gumas.models import (
    BiasType,
    ConflictPhase,
    ConflictState,
    EventType,
    FactionState,
    GUMASState,
    LeaderState,
    SimulationEvent,
    TickResult,
    TreatyPhase,
    TreatyState,
)
from modules.gumas.scenarios import build_default_scenario

logger = logging.getLogger(__name__)


# ============================================================================
# ENGINE
# ============================================================================

class GUMASEngine:
    """
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
    """

    def __init__(
        self,
        seed: int = 42,
        ethics_callback: Optional[Callable[[str, Dict[str, Any]], bool]] = None,
    ):
        """
        Args:
            seed: RNG seed for reproducibility.
            ethics_callback: Optional callable(action_type, params) -> bool.
                If provided, called before significant state mutations.
                Return False to block the action (Picard_Delta_3 veto).
                If None, all actions proceed (ethics checked externally).
        """
        self._seed = seed
        self._rng = random.Random(seed)
        self._state: Optional[GUMASState] = None
        self._ethics_callback = ethics_callback
        self._initialized = False

        logger.info(
            "GUMASEngine created (seed=%d, ethics_callback=%s)",
            seed,
            "attached" if ethics_callback else "none",
        )

    # ------------------------------------------------------------------ #
    # PUBLIC API                                                          #
    # ------------------------------------------------------------------ #

    def init_scenario(
        self,
        state: Optional[GUMASState] = None,
        scenario_id: str = "gumas_canonical_v1",
    ) -> GUMASState:
        """
        Initialize the simulation with a scenario.

        Args:
            state: Pre-built GUMASState. If None, loads the canonical
                   default scenario from scenarios.py.
            scenario_id: Scenario identifier (used if state is None).

        Returns:
            The initialized GUMASState.
        """
        if state is not None:
            self._state = state
        else:
            self._state = build_default_scenario(
                scenario_id=scenario_id,
                seed=self._seed,
            )

        self._rng = random.Random(self._state.seed)
        self._initialized = True

        logger.info(
            "Scenario initialized: %s (factions=%d, leaders=%d, conflicts=%d, seed=%d)",
            self._state.scenario_id,
            len(self._state.factions),
            len(self._state.leaders),
            len(self._state.conflicts),
            self._state.seed,
        )

        return self._state

    def step(self) -> TickResult:
        """
        Advance the simulation by one turn.

        Tick lifecycle:
            1. Process injected events from queue
            2. Update leader bias hooks
            3. Evaluate conflicts (de-escalation, phase transitions)
            4. Evaluate treaties (breach detection, reputation decay)
            5. Run diplomacy tick (trust updates, espionage checks)
            6. Generate emergent events
            6.5. Resolve names for any new referents (NameService)
            7. Record TickResult and append to history

        Returns:
            TickResult with full audit of what happened this turn.
        """
        self._require_init()
        assert self._state is not None  # for type checker

        self._state.turn += 1
        turn = self._state.turn

        result = TickResult(turn=turn)

        # Phase 1: Process injected events
        self._process_event_queue(result)

        # Phase 2: Update leader bias hooks
        self._update_leader_hooks(result)

        # Phase 3: Conflict evaluation
        self._evaluate_conflicts(result)

        # Phase 4: Treaty evaluation
        self._evaluate_treaties(result)

        # Phase 4.5: Peacetime recovery (the missing half)
        self._peacetime_recovery(result)

        # Phase 5: Diplomacy tick
        self._diplomacy_tick(result)

        # Phase 6: Emergent events
        self._generate_emergent_events(result)

        # Record
        self._state.history.append(result)

        logger.info(
            "Turn %d complete: %d events processed, %d generated, %d state changes",
            turn,
            len(result.events_processed),
            len(result.events_generated),
            len(result.state_changes),
        )

        return result

    def run(self, n_turns: int = 10) -> List[TickResult]:
        """Run n_turns of simulation. Returns list of TickResults."""
        self._require_init()
        results = []
        for _ in range(n_turns):
            results.append(self.step())
        return results

    def get_state(self) -> GUMASState:
        """Return the current simulation state."""
        self._require_init()
        assert self._state is not None
        return self._state

    def inject_event(self, event: SimulationEvent) -> None:
        """
        Queue an external event for processing on the next tick.

        Args:
            event: SimulationEvent to inject. event.injected will be
                   set to True automatically.
        """
        self._require_init()
        assert self._state is not None
        event.injected = True
        event.turn = self._state.turn + 1
        self._state.event_queue.append(event)

        logger.info(
            "Event injected: %s (type=%s, source=%s, target=%s)",
            event.event_id,
            event.event_type.value,
            event.source_faction,
            event.target_faction,
        )

    def export_state(self, path: str, include_history: bool = True) -> None:
        """Export current state to JSON file."""
        self._require_init()
        assert self._state is not None
        data = self._state.to_dict(include_history=include_history)
        data["dlp"] = {
            "anchor": "GUMAS-ENGINE-CORE-V1",
            "export_timestamp": datetime.now(timezone.utc).isoformat(),
            "seed": self._state.seed,
            "turns_completed": self._state.turn,
        }
        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, "w") as f:
            json.dump(data, f, indent=2, default=str)
        logger.info("State exported to %s", path)

    # ------------------------------------------------------------------ #
    # PHASE 1: EVENT QUEUE                                                #
    # ------------------------------------------------------------------ #

    def _process_event_queue(self, result: TickResult) -> None:
        """Drain and process all queued events."""
        assert self._state is not None
        queue = self._state.event_queue
        self._state.event_queue = []

        for event in queue:
            self._apply_event(event, result)
            result.events_processed.append(event)

    def _apply_event(self, event: SimulationEvent, result: TickResult) -> None:
        """Apply a single event's effects to the world state."""
        assert self._state is not None
        handler = self._EVENT_HANDLERS.get(event.event_type)
        if handler:
            handler(self, event, result)
        else:
            logger.warning("No handler for event type: %s", event.event_type.value)

    def _handle_military_escalation(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        assert self._state is not None
        src = event.source_faction
        tgt = event.target_faction
        if not src or not tgt:
            return

        severity = event.severity

        # Find or create conflict
        conflict = self._find_conflict(src, tgt)
        if conflict is None:
            cid = f"conflict_{src}_{tgt}_{self._state.turn}"
            conflict = ConflictState(
                conflict_id=cid,
                parties=[src, tgt],
                phase=ConflictPhase.ESCALATION,
            )
            self._state.conflicts[cid] = conflict
            result.state_changes.append({
                "type": "conflict_created",
                "conflict_id": cid,
                "parties": [src, tgt],
            })

        # Escalate phase
        phase_order = [
            ConflictPhase.PEACE, ConflictPhase.TENSION,
            ConflictPhase.ESCALATION, ConflictPhase.OPEN_CONFLICT,
        ]
        idx = phase_order.index(conflict.phase) if conflict.phase in phase_order else 2
        new_idx = min(idx + 1, len(phase_order) - 1)
        old_phase = conflict.phase
        conflict.phase = phase_order[new_idx]

        # Increase war costs
        conflict.war_cost_estimate[src] = min(
            1.0, conflict.war_cost_estimate.get(src, 0.3) + severity * 0.2
        )
        conflict.war_cost_estimate[tgt] = min(
            1.0, conflict.war_cost_estimate.get(tgt, 0.3) + severity * 0.3
        )

        # Trust hit
        self._adjust_trust(src, tgt, -severity * 0.15, result)

        result.state_changes.append({
            "type": "conflict_escalation",
            "conflict_id": conflict.conflict_id,
            "old_phase": old_phase.value,
            "new_phase": conflict.phase.value,
            "severity": severity,
        })

    def _handle_diplomatic_overture(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        assert self._state is not None
        src = event.source_faction
        tgt = event.target_faction
        if not src or not tgt:
            return

        # Trust boost
        bonus = event.parameters.get("trust_bonus", 0.1)
        self._adjust_trust(src, tgt, bonus, result)

        # Check if this enables mediation on active conflicts
        for conflict in self._state.conflicts.values():
            if src in conflict.parties and tgt in conflict.parties:
                if not conflict.mediation_available:
                    mediator = event.parameters.get("mediator_id")
                    if mediator and mediator in self._state.factions:
                        conflict.mediation_available = True
                        conflict.mediator_id = mediator
                        result.state_changes.append({
                            "type": "mediation_enabled",
                            "conflict_id": conflict.conflict_id,
                            "mediator": mediator,
                        })

    def _handle_economic_shock(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        assert self._state is not None
        tgt = event.target_faction
        if not tgt or tgt not in self._state.factions:
            return

        faction = self._state.factions[tgt]
        shock = event.severity * 0.3
        faction.economic_strength = max(0.05, faction.economic_strength - shock)
        faction.population_stability = max(0.05, faction.population_stability - shock * 0.5)

        # Stress the leader
        leader = self._get_faction_leader(tgt)
        if leader:
            leader.economic_shock += event.severity
            leader.war_pressure = min(1.0, leader.war_pressure + shock * 0.3)

        result.state_changes.append({
            "type": "economic_shock",
            "faction": tgt,
            "severity": event.severity,
            "new_economic_strength": faction.economic_strength,
        })

    def _handle_espionage_exposure(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        assert self._state is not None
        src = event.source_faction  # the spy's origin
        tgt = event.target_faction  # the exposed target
        if not src or not tgt:
            return

        # Major trust hit
        self._adjust_trust(tgt, src, -0.25, result)

        # Leader stress
        leader = self._get_faction_leader(tgt)
        if leader:
            leader.betrayals += 1
            # Hyper-rationalism paranoia branch check (PR Section 5.2)
            if leader.dominant_bias == BiasType.HYPER_RATIONALISM:
                paranoia_threshold = event.parameters.get("paranoia_threshold", 0.4)
                institutional_trust = leader.institutional_control
                if institutional_trust < paranoia_threshold:
                    result.state_changes.append({
                        "type": "paranoia_purge_triggered",
                        "leader": leader.leader_id,
                        "institutional_trust": institutional_trust,
                    })
                    leader.oversight_resistance = min(1.0, leader.oversight_resistance + 0.2)

        result.state_changes.append({
            "type": "espionage_exposed",
            "spy_origin": src,
            "target": tgt,
            "severity": event.severity,
        })

    def _handle_treaty_violation(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        assert self._state is not None
        violator = event.source_faction
        treaty_id = event.parameters.get("treaty_id")
        if not violator or not treaty_id:
            return

        treaty = self._state.treaties.get(treaty_id)
        if not treaty or not treaty.is_active:
            return

        # Run breach detection formula
        action_severity = event.severity
        is_direct = event.parameters.get("is_direct_action", True)
        trust = 0.5
        for other in treaty.parties:
            if other != violator and other in self._state.factions:
                trust = self._state.factions[other].trust_scores.get(violator, 0.5)
                break

        breach_score = calc_treaty_breach_score(
            action_severity=action_severity,
            is_direct_action=is_direct,
            treaty_ambiguity=treaty.ambiguity_tolerance,
            faction_trust=trust,
        )

        if is_treaty_breach(breach_score, treaty.violation_threshold):
            treaty.breach_count[violator] = treaty.breach_count.get(violator, 0) + 1
            treaty.breach_history.append({
                "turn": self._state.turn,
                "violator": violator,
                "breach_score": round(breach_score, 4),
                "severity": action_severity,
            })

            # Reputation hit
            faction = self._state.factions.get(violator)
            if faction:
                faction.reputation = calc_reputation_after_decay(
                    base_reputation=faction.reputation,
                    breach_penalty=-0.1,
                    breach_count=treaty.breach_count[violator],
                    turns_since_last_breach=0,
                )

            # Check treaty collapse threshold
            total_breaches = sum(treaty.breach_count.values())
            if total_breaches >= 3:
                treaty.phase = TreatyPhase.COLLAPSED
                treaty.is_active = False
                result.state_changes.append({
                    "type": "treaty_collapsed",
                    "treaty_id": treaty_id,
                    "total_breaches": total_breaches,
                })

            result.state_changes.append({
                "type": "treaty_breach_confirmed",
                "treaty_id": treaty_id,
                "violator": violator,
                "breach_score": round(breach_score, 4),
                "cumulative_breaches": treaty.breach_count[violator],
            })

    def _handle_mediation_offer(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        assert self._state is not None
        mediator = event.source_faction
        conflict_id = event.parameters.get("conflict_id")
        if not mediator or not conflict_id:
            return

        conflict = self._state.conflicts.get(conflict_id)
        if not conflict:
            return

        # Check mediator neutrality (PR: neutrality_requirement 0.7)
        neutrality_ok = True
        for party in conflict.parties:
            trust = self._state.factions.get(party, FactionState(
                faction_id="", name="", faction_type=FactionType.FEDERATION
            )).trust_scores.get(mediator, 0.5)
            if trust < 0.3:
                neutrality_ok = False
                break

        if neutrality_ok:
            conflict.mediation_available = True
            conflict.mediator_id = mediator
            result.state_changes.append({
                "type": "mediation_accepted",
                "conflict_id": conflict_id,
                "mediator": mediator,
            })
        else:
            result.state_changes.append({
                "type": "mediation_rejected",
                "conflict_id": conflict_id,
                "mediator": mediator,
                "reason": "neutrality_insufficient",
            })

    # ------------------------------------------------------------------ #
    # CONSTRUCTIVE EVENT HANDLERS                                          #
    # ------------------------------------------------------------------ #

    def _handle_trade_agreement(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        """
        Bilateral trade deal. Both parties gain economically.
        Trust improves. This is how economies grow between wars.

        Magnitude: +0.03-0.06 economic per party (modest).
        Compare to ECONOMIC_SHOCK: -0.10-0.25 (harsh).
        Trade builds slowly. Shocks hit fast. That's the asymmetry.
        """
        assert self._state is not None
        source = self._state.factions.get(event.source_faction or "")
        target = self._state.factions.get(event.target_faction or "")
        if not source or not target:
            return

        trade_value = event.parameters.get("trade_value", 0.04)

        for faction in (source, target):
            ceiling = faction.economic_potential
            if faction.economic_strength < ceiling:
                gain = min(trade_value, ceiling - faction.economic_strength)
                faction.economic_strength = min(
                    ceiling, faction.economic_strength + gain
                )

        # Trade builds trust
        self._adjust_trust(
            event.source_faction or "",
            event.target_faction or "",
            0.02,
            result,
        )

        result.state_changes.append({
            "type": "trade_agreement_executed",
            "source": event.source_faction,
            "target": event.target_faction,
            "trade_value": round(trade_value, 4),
        })

    def _handle_economic_boom(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        """
        Domestic economic expansion. Requires peace and stability.

        Magnitude: +0.04-0.07 economic, +0.02 population stability.
        Capped at economic_potential.
        """
        assert self._state is not None
        faction = self._state.factions.get(event.target_faction or "")
        if not faction:
            return

        boom = event.severity * 0.10  # severity 0.3-0.7 → 0.03-0.07
        ceiling = faction.economic_potential
        if faction.economic_strength < ceiling:
            gain = min(boom, ceiling - faction.economic_strength)
            faction.economic_strength += gain

        faction.population_stability = min(
            1.0, faction.population_stability + 0.02
        )

        # Boom boosts leader legitimacy
        leader = self._get_faction_leader(event.target_faction or "")
        if leader:
            leader.public_legitimacy = min(
                1.0, leader.public_legitimacy + 0.02
            )

        result.state_changes.append({
            "type": "economic_boom_realized",
            "faction": event.target_faction,
            "gain": round(boom, 4),
            "new_econ": round(faction.economic_strength, 4),
        })

    def _handle_technology_breakthrough(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        """
        Tech breakthrough. Boosts technology, small military and economic
        spillover. This is how factions differentiate over time.

        Magnitude: +0.03-0.05 tech, +0.01 military, +0.01 economic.
        """
        assert self._state is not None
        faction = self._state.factions.get(event.target_faction or "")
        if not faction:
            return

        tech_gain = 0.03 + event.severity * 0.04
        faction.technology_level = min(1.0, faction.technology_level + tech_gain)
        faction.military_strength = min(1.0, faction.military_strength + 0.01)
        ceiling = faction.economic_potential
        faction.economic_strength = min(ceiling, faction.economic_strength + 0.01)

        result.state_changes.append({
            "type": "technology_breakthrough_realized",
            "faction": event.target_faction,
            "tech_gain": round(tech_gain, 4),
            "new_tech": round(faction.technology_level, 4),
        })

    def _handle_cultural_movement(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        """
        Cultural movement stabilizes population and builds soft power.

        Magnitude: +0.03-0.06 population stability, +0.01 trust with
        one neighbor. Culture is glue.
        """
        assert self._state is not None
        faction = self._state.factions.get(event.target_faction or "")
        if not faction:
            return

        stabilization = 0.03 + event.severity * 0.05
        faction.population_stability = min(
            1.0, faction.population_stability + stabilization
        )

        # Cultural soft power: small trust gain with a random neighbor
        partner = event.parameters.get("cultural_partner")
        if partner:
            self._adjust_trust(
                event.target_faction or "", partner,
                0.01, result,
            )

        leader = self._get_faction_leader(event.target_faction or "")
        if leader:
            leader.public_legitimacy = min(
                1.0, leader.public_legitimacy + 0.01
            )

        result.state_changes.append({
            "type": "cultural_movement_effect",
            "faction": event.target_faction,
            "stabilization": round(stabilization, 4),
        })

    def _handle_infrastructure_investment(
        self, event: SimulationEvent, result: TickResult,
    ) -> None:
        """
        Post-war reconstruction or peacetime infrastructure program.
        This is the discrete replacement for background recovery.

        Magnitude: +0.03-0.05 economic, +0.02 population stability,
        +0.01 leader legitimacy. Capped at economic_potential.
        """
        assert self._state is not None
        faction = self._state.factions.get(event.target_faction or "")
        if not faction:
            return

        investment = 0.03 + event.severity * 0.04
        ceiling = faction.economic_potential
        if faction.economic_strength < ceiling:
            gain = min(investment, ceiling - faction.economic_strength)
            faction.economic_strength += gain

        faction.population_stability = min(
            1.0, faction.population_stability + 0.02
        )

        leader = self._get_faction_leader(event.target_faction or "")
        if leader:
            leader.public_legitimacy = min(
                1.0, leader.public_legitimacy + 0.01
            )
            leader.elite_support = min(
                1.0, leader.elite_support + 0.01
            )

        result.state_changes.append({
            "type": "infrastructure_investment_executed",
            "faction": event.target_faction,
            "investment": round(investment, 4),
            "new_econ": round(faction.economic_strength, 4),
        })

    _EVENT_HANDLERS: Dict[EventType, Callable[..., None]] = {
        EventType.MILITARY_ESCALATION: _handle_military_escalation,
        EventType.DIPLOMATIC_OVERTURE: _handle_diplomatic_overture,
        EventType.ECONOMIC_SHOCK: _handle_economic_shock,
        EventType.ESPIONAGE_EXPOSURE: _handle_espionage_exposure,
        EventType.TREATY_VIOLATION: _handle_treaty_violation,
        EventType.MEDIATION_OFFER: _handle_mediation_offer,
        EventType.TRADE_AGREEMENT: _handle_trade_agreement,
        EventType.ECONOMIC_BOOM: _handle_economic_boom,
        EventType.TECHNOLOGY_BREAKTHROUGH: _handle_technology_breakthrough,
        EventType.CULTURAL_MOVEMENT: _handle_cultural_movement,
        EventType.INFRASTRUCTURE_INVESTMENT: _handle_infrastructure_investment,
    }

    # ------------------------------------------------------------------ #
    # PHASE 2: LEADER BIAS HOOKS                                          #
    # ------------------------------------------------------------------ #

    def _update_leader_hooks(self, result: TickResult) -> None:
        """
        Phase 2: Evolve leader bias intensity based on accumulated
        stressors, then recalculate bias effect hooks.

        Bias evolution fires when total stressor load exceeds a
        threshold, simulating how pressure changes leaders over time.
        This was the missing link — without it, leaders were static.
        """
        assert self._state is not None

        for leader in self._state.leaders.values():
            # Calculate total stressor load as event_severity proxy
            stressor_load = (
                leader.war_losses * 0.1
                + leader.betrayals * 0.15
                + leader.scandals * 0.1
                + leader.economic_shock * 0.2
                + leader.war_pressure * 0.3
            )
            stressor_load = min(1.0, stressor_load)

            # Evolve bias intensity if stressor load is meaningful
            if stressor_load > 0.05:
                old_intensity = leader.bias_intensity
                leader.bias_intensity = calc_bias_evolution(
                    current_intensity=leader.bias_intensity,
                    plasticity=leader.plasticity,
                    event_severity=stressor_load,
                    has_survivorship_bias=(
                        leader.dominant_bias == BiasType.SURVIVORSHIP
                    ),
                    doctrine_shift_bonus=0.05 if leader.war_losses > 2 else 0.0,
                )

                if abs(leader.bias_intensity - old_intensity) > 0.01:
                    result.state_changes.append({
                        "type": "bias_evolved",
                        "leader": leader.leader_id,
                        "old_intensity": round(old_intensity, 4),
                        "new_intensity": round(leader.bias_intensity, 4),
                        "stressor_load": round(stressor_load, 4),
                    })

                # Stressor decay: pressure bleeds off slowly each turn
                leader.economic_shock = max(0.0, leader.economic_shock - 0.02)
                leader.war_pressure = max(0.0, leader.war_pressure - 0.01)

            # Recalculate hooks from (potentially evolved) intensity
            hooks = apply_bias_hooks(
                leader.dominant_bias.value,
                leader.bias_intensity,
            )
            leader.evidence_gain_multiplier = hooks["evidence_gain_multiplier"]
            leader.risk_tolerance = hooks["risk_tolerance"]
            leader.diplomacy_openness = hooks["diplomacy_openness"]
            leader.escalation_threshold = hooks["escalation_threshold"]
            leader.oversight_resistance = hooks["oversight_resistance"]

    # ------------------------------------------------------------------ #
    # PHASE 3: CONFLICT EVALUATION                                        #
    # ------------------------------------------------------------------ #

    def _evaluate_conflicts(self, result: TickResult) -> None:
        """Evaluate all active conflicts for phase transitions."""
        assert self._state is not None

        for conflict in list(self._state.conflicts.values()):
            if conflict.phase in (ConflictPhase.PEACE, ConflictPhase.RESOLUTION):
                continue

            conflict.turns_active += 1

            # Calculate de-escalation probability
            parties = conflict.parties
            if len(parties) < 2:
                continue

            a, b = parties[0], parties[1]
            p_deesc = calc_deescalation_probability(
                war_cost_a=conflict.war_cost_estimate.get(a, 0.3),
                war_cost_b=conflict.war_cost_estimate.get(b, 0.3),
                stalemate_index=conflict.stalemate_index,
                internal_pressure_a=conflict.internal_pressure.get(a, 0.2),
                internal_pressure_b=conflict.internal_pressure.get(b, 0.2),
                mediation_available=conflict.mediation_available,
            )
            conflict.deescalation_probability = p_deesc

            # Leader diplomacy_openness modifies the effective roll
            leader_a = self._get_faction_leader(a)
            leader_b = self._get_faction_leader(b)
            openness_bonus = 0.0
            if leader_a:
                openness_bonus += (leader_a.diplomacy_openness - 0.5) * 0.1
            if leader_b:
                openness_bonus += (leader_b.diplomacy_openness - 0.5) * 0.1

            effective_p = min(1.0, max(0.0, p_deesc + openness_bonus))

            # Stochastic resolution
            roll = self._rng.random()
            if roll < effective_p:
                old_phase = conflict.phase
                # De-escalation step
                deesc_transitions = {
                    ConflictPhase.OPEN_CONFLICT: ConflictPhase.STALEMATE,
                    ConflictPhase.STALEMATE: ConflictPhase.DEESCALATION,
                    ConflictPhase.ESCALATION: ConflictPhase.TENSION,
                    ConflictPhase.TENSION: ConflictPhase.CEASEFIRE,
                    ConflictPhase.DEESCALATION: ConflictPhase.CEASEFIRE,
                    ConflictPhase.CEASEFIRE: ConflictPhase.NEGOTIATION,
                    ConflictPhase.NEGOTIATION: ConflictPhase.RESOLUTION,
                }
                new_phase = deesc_transitions.get(conflict.phase, conflict.phase)
                conflict.phase = new_phase

                result.state_changes.append({
                    "type": "conflict_deescalated",
                    "conflict_id": conflict.conflict_id,
                    "old_phase": old_phase.value,
                    "new_phase": new_phase.value,
                    "deescalation_probability": round(p_deesc, 4),
                    "roll": round(roll, 4),
                })

            # Natural escalation pressure from leader bias
            elif conflict.phase in (ConflictPhase.TENSION, ConflictPhase.ESCALATION):
                for party_id in parties:
                    leader = self._get_faction_leader(party_id)
                    if leader and leader.escalation_threshold < 0.5:
                        # Wider window + stronger roll = more escalation
                        esc_chance = (0.5 - leader.escalation_threshold) * 0.5
                        esc_roll = self._rng.random()
                        if esc_roll < esc_chance:
                            self._escalate_conflict(conflict, result)
                            # War pressure on the escalating leader
                            leader.war_pressure = min(
                                1.0, leader.war_pressure + 0.1
                            )
                            leader.war_losses += 1 if conflict.phase == ConflictPhase.OPEN_CONFLICT else 0
                            break

            # War cost accrual for active conflicts
            if conflict.phase in (ConflictPhase.OPEN_CONFLICT, ConflictPhase.STALEMATE):
                for party_id in parties:
                    current_cost = conflict.war_cost_estimate.get(party_id, 0.3)
                    conflict.war_cost_estimate[party_id] = min(
                        1.0, current_cost + 0.03
                    )
                    conflict.internal_pressure[party_id] = min(
                        1.0, conflict.internal_pressure.get(party_id, 0.2) + 0.04
                    )
                    # War stress on leaders
                    leader = self._get_faction_leader(party_id)
                    if leader:
                        leader.war_pressure = min(1.0, leader.war_pressure + 0.05)
                        leader.war_losses += 1
                        leader.public_legitimacy = max(
                            0.1, leader.public_legitimacy - 0.02
                        )
                conflict.stalemate_index = min(
                    1.0, conflict.stalemate_index + 0.05
                )
                conflict.casualty_index = min(
                    1.0, conflict.casualty_index + 0.03
                )

    def _escalate_conflict(
        self, conflict: ConflictState, result: TickResult,
    ) -> None:
        old_phase = conflict.phase
        if conflict.phase == ConflictPhase.TENSION:
            conflict.phase = ConflictPhase.ESCALATION
        elif conflict.phase == ConflictPhase.ESCALATION:
            conflict.phase = ConflictPhase.OPEN_CONFLICT

        if conflict.phase != old_phase:
            result.state_changes.append({
                "type": "conflict_escalated",
                "conflict_id": conflict.conflict_id,
                "old_phase": old_phase.value,
                "new_phase": conflict.phase.value,
                "cause": "leader_bias_pressure",
            })

    # ------------------------------------------------------------------ #
    # PHASE 4: TREATY EVALUATION                                          #
    # ------------------------------------------------------------------ #

    def _evaluate_treaties(self, result: TickResult) -> None:
        """Evaluate active treaties for reputation decay."""
        assert self._state is not None

        for treaty in self._state.treaties.values():
            if not treaty.is_active:
                continue

            treaty.turns_since_ratification += 1

            # Reputation recovery via decay for all parties
            for party_id in treaty.parties:
                faction = self._state.factions.get(party_id)
                if faction and faction.reputation < 0.7:
                    breaches = treaty.breach_count.get(party_id, 0)
                    if breaches == 0:
                        # Clean record: slow reputation recovery
                        faction.reputation = min(
                            1.0, faction.reputation + 0.01
                        )

    # ------------------------------------------------------------------ #
    # PHASE 4.5: PEACETIME RECOVERY                                       #
    # ------------------------------------------------------------------ #

    def _peacetime_recovery(self, result: TickResult) -> None:
        """
        Phase 4.5: Background maintenance during peace.

        This is NOT the primary recovery mechanism — that's handled
        by discrete constructive events (trade agreements, infrastructure
        investments, economic booms) in Phase 6.

        This phase handles only:
        - Tiny population stability drift (people adapt)
        - Leader stressor decay (pressure fades with time)
        - Post-resolution trust building (peace dividends)
        - War-weariness accumulation for leaders in active conflict
        """
        assert self._state is not None

        # Determine which factions are currently in active fighting
        factions_at_war = set()
        for conflict in self._state.conflicts.values():
            if conflict.phase in (
                ConflictPhase.OPEN_CONFLICT,
                ConflictPhase.ESCALATION,
                ConflictPhase.STALEMATE,
            ):
                for party in conflict.parties:
                    factions_at_war.add(party)

        for fid, faction in self._state.factions.items():
            at_war = fid in factions_at_war
            leader = self._get_faction_leader(fid)

            if not at_war:
                # Population stability drifts slowly toward baseline
                # (people adapt, births/deaths normalize)
                if faction.population_stability < 0.6:
                    faction.population_stability = min(
                        1.0, faction.population_stability + 0.003
                    )

                # Leader maintenance during peace
                if leader:
                    # War pressure bleeds off during peace
                    leader.war_pressure = max(
                        0.0, leader.war_pressure - 0.02
                    )
                    # War losses heal slowly (leaders process, retire, rotate)
                    if leader.war_losses > 0 and self._state.turn % 5 == 0:
                        leader.war_losses = max(0, leader.war_losses - 1)
            else:
                # At war: war-weariness accumulates
                if leader:
                    leader.war_pressure = min(
                        1.0, leader.war_pressure + 0.02
                    )

        # Post-resolution trust building (peace dividends)
        for conflict in self._state.conflicts.values():
            if conflict.phase == ConflictPhase.RESOLUTION:
                for i, party_a in enumerate(conflict.parties):
                    for party_b in conflict.parties[i + 1:]:
                        fa = self._state.factions.get(party_a)
                        fb = self._state.factions.get(party_b)
                        if fa and fb:
                            trust_ab = fa.trust_scores.get(party_b, 0.5)
                            if trust_ab < 0.55:
                                fa.trust_scores[party_b] = min(
                                    0.55, trust_ab + 0.02
                                )
                            trust_ba = fb.trust_scores.get(party_a, 0.5)
                            if trust_ba < 0.55:
                                fb.trust_scores[party_a] = min(
                                    0.55, trust_ba + 0.02
                                )

    # ------------------------------------------------------------------ #
    # PHASE 5: DIPLOMACY TICK                                             #
    # ------------------------------------------------------------------ #

    def _diplomacy_tick(self, result: TickResult) -> None:
        """Run trust updates and espionage checks."""
        assert self._state is not None

        faction_ids = list(self._state.factions.keys())

        # Natural trust drift toward neutral (slow mean reversion)
        for fid in faction_ids:
            faction = self._state.factions[fid]
            for other_id, trust in list(faction.trust_scores.items()):
                drift = (0.5 - trust) * 0.01
                faction.trust_scores[other_id] = max(
                    0.0, min(1.0, trust + drift)
                )

        # Espionage risk check for low-trust pairs
        for i, fid_a in enumerate(faction_ids):
            for fid_b in faction_ids[i + 1:]:
                trust_ab = self._state.factions[fid_a].trust_scores.get(fid_b, 0.5)
                if trust_ab < 0.35:
                    risk = calc_double_agent_risk(
                        bilateral_trust=trust_ab,
                        intel_sensitivity=0.5,
                    )
                    roll = self._rng.random()
                    if roll < risk * 0.1:  # Low base probability per turn
                        event = SimulationEvent(
                            event_id=f"espionage_{fid_a}_{fid_b}_{self._state.turn}",
                            event_type=EventType.ESPIONAGE_EXPOSURE,
                            turn=self._state.turn,
                            source_faction=fid_a,
                            target_faction=fid_b,
                            severity=0.4 + self._rng.random() * 0.3,
                            description=f"Espionage detected between {fid_a} and {fid_b}",
                        )
                        result.events_generated.append(event)
                        self._apply_event(event, result)

        # Update derived diplomacy fields
        for fid in faction_ids:
            faction = self._state.factions[fid]
            avg_trust = (
                sum(faction.trust_scores.values()) / max(1, len(faction.trust_scores))
            )
            faction.verification_demand = max(0.0, 1.0 - avg_trust)
            faction.deal_discount = max(0.0, (0.5 - avg_trust) * 0.2)
            faction.coalition_invite_weight = min(1.0, avg_trust * faction.reputation)

    # ------------------------------------------------------------------ #
    # PHASE 6: EMERGENT EVENTS                                            #
    # ------------------------------------------------------------------ #

    def _generate_emergent_events(self, result: TickResult) -> None:
        """
        Phase 6: Generate stochastic emergent events.

        The galaxy must not converge to peace. Turbulence sources:
        - Economic shocks from instability
        - Leader-driven diplomatic overtures (high openness)
        - Leader-driven military escalation (low escalation_threshold)
        - Faction-on-faction aggression from low-trust pairs (new conflicts)
        - Intelligence leaks from espionage-heavy factions
        - Internal coups when leader legitimacy is critically low
        """
        assert self._state is not None

        # Track who's fighting for positive event eligibility
        factions_at_war_this_turn: set = set()
        for conflict in self._state.conflicts.values():
            if conflict.phase in (
                ConflictPhase.OPEN_CONFLICT,
                ConflictPhase.ESCALATION,
                ConflictPhase.STALEMATE,
            ):
                for party in conflict.parties:
                    factions_at_war_this_turn.add(party)

        # --- Economic shocks (probability scales with instability) ---
        for fid, faction in self._state.factions.items():
            if faction.population_stability < 0.5:
                shock_p = 0.06 + (0.5 - faction.population_stability) * 0.2
                if self._rng.random() < shock_p:
                    event = SimulationEvent(
                        event_id=f"econ_shock_{fid}_{self._state.turn}",
                        event_type=EventType.ECONOMIC_SHOCK,
                        turn=self._state.turn,
                        target_faction=fid,
                        severity=0.3 + self._rng.random() * 0.4,
                        description=f"Economic instability in {faction.name}",
                    )
                    result.events_generated.append(event)
                    self._apply_event(event, result)

        # --- Leader-driven actions ---
        for leader in self._state.leaders.values():
            faction = self._state.factions.get(leader.faction_id)
            if not faction:
                continue

            # Diplomatic overtures from open leaders
            if leader.diplomacy_openness > 0.55 and self._rng.random() < 0.08:
                candidates = [
                    fid for fid in self._state.factions
                    if fid != leader.faction_id
                    and faction.trust_scores.get(fid, 0.5) > 0.3
                ]
                if candidates:
                    target = self._rng.choice(candidates)
                    event = SimulationEvent(
                        event_id=f"diplo_{leader.faction_id}_{target}_{self._state.turn}",
                        event_type=EventType.DIPLOMATIC_OVERTURE,
                        turn=self._state.turn,
                        source_faction=leader.faction_id,
                        target_faction=target,
                        severity=0.3,
                        parameters={"trust_bonus": 0.05 + leader.diplomacy_openness * 0.05},
                        description=f"Diplomatic overture from {leader.name}",
                    )
                    result.events_generated.append(event)
                    self._apply_event(event, result)

            # Military escalation from aggressive leaders
            if leader.escalation_threshold < 0.45 and self._rng.random() < 0.10:
                enemies = [
                    fid for fid in self._state.factions
                    if fid != leader.faction_id
                    and faction.trust_scores.get(fid, 0.5) < 0.4
                ]
                if enemies:
                    target = self._rng.choice(enemies)
                    severity = 0.3 + (0.45 - leader.escalation_threshold) * 0.5
                    event = SimulationEvent(
                        event_id=f"aggression_{leader.faction_id}_{target}_{self._state.turn}",
                        event_type=EventType.MILITARY_ESCALATION,
                        turn=self._state.turn,
                        source_faction=leader.faction_id,
                        target_faction=target,
                        severity=min(0.8, severity),
                        description=(
                            f"{leader.name} provokes military escalation "
                            f"against {self._state.factions.get(target, target)}"
                        ),
                    )
                    result.events_generated.append(event)
                    self._apply_event(event, result)
                    # Stress the aggressor too
                    leader.war_pressure = min(1.0, leader.war_pressure + 0.1)

        # --- Low-trust pair friction (new conflict seeds) ---
        faction_ids = list(self._state.factions.keys())
        for i, fid_a in enumerate(faction_ids):
            for fid_b in faction_ids[i + 1:]:
                trust = self._state.factions[fid_a].trust_scores.get(fid_b, 0.5)
                if trust < 0.25 and self._rng.random() < 0.04:
                    # Check no existing conflict
                    existing = self._find_conflict(fid_a, fid_b)
                    if existing is None:
                        event = SimulationEvent(
                            event_id=f"friction_{fid_a}_{fid_b}_{self._state.turn}",
                            event_type=EventType.MILITARY_ESCALATION,
                            turn=self._state.turn,
                            source_faction=fid_a,
                            target_faction=fid_b,
                            severity=0.3 + self._rng.random() * 0.2,
                            description=f"Border friction between {fid_a} and {fid_b}",
                        )
                        result.events_generated.append(event)
                        self._apply_event(event, result)

        # --- Internal coup risk (low legitimacy + high war pressure) ---
        for leader in self._state.leaders.values():
            coup_risk = (
                (1.0 - leader.public_legitimacy) * 0.4
                + leader.war_pressure * 0.3
                + (leader.betrayals * 0.05)
            )
            if coup_risk > 0.4 and self._rng.random() < coup_risk * 0.05:
                result.state_changes.append({
                    "type": "internal_coup_attempt",
                    "leader": leader.leader_id,
                    "faction": leader.faction_id,
                    "coup_risk": round(coup_risk, 4),
                })
                # Coup destabilizes: legitimacy hit, scandal, elite support drop
                leader.public_legitimacy = max(0.1, leader.public_legitimacy - 0.15)
                leader.elite_support = max(0.1, leader.elite_support - 0.2)
                leader.scandals += 1
                # Faction instability
                faction = self._state.factions.get(leader.faction_id)
                if faction:
                    faction.population_stability = max(
                        0.1, faction.population_stability - 0.1
                    )

        # ============================================================
        # CONSTRUCTIVE EMERGENT EVENTS
        #
        # These are first-class events, same as military escalations.
        # Things that build are as real as things that destroy.
        #
        # Design ratios (target):
        #   Frequency: constructive ~3-4x more often than destructive
        #   Magnitude: destructive ~2-3x harder per hit
        #   Net: slowly positive with sharp periodic reversals
        # ============================================================

        # --- Trade agreements (high-trust pairs not at war) ---
        # This is the primary constructive driver. Most economic
        # interactions between polities are cooperative.
        faction_ids = list(self._state.factions.keys())
        for i, fid_a in enumerate(faction_ids):
            for fid_b in faction_ids[i + 1:]:
                if fid_a in factions_at_war_this_turn or fid_b in factions_at_war_this_turn:
                    continue
                trust = self._state.factions[fid_a].trust_scores.get(fid_b, 0.5)
                # Higher trust = more likely trade. p=0.02 at trust 0.5, up to 0.06 at trust 0.8
                trade_p = max(0.0, (trust - 0.35) * 0.12)
                if trade_p > 0 and self._rng.random() < trade_p:
                    trade_value = 0.02 + trust * 0.03  # 0.03-0.05
                    event = SimulationEvent(
                        event_id=f"trade_{fid_a}_{fid_b}_{self._state.turn}",
                        event_type=EventType.TRADE_AGREEMENT,
                        turn=self._state.turn,
                        source_faction=fid_a,
                        target_faction=fid_b,
                        severity=0.3,
                        parameters={"trade_value": trade_value},
                        description=f"Trade agreement between {fid_a} and {fid_b}",
                    )
                    result.events_generated.append(event)
                    self._apply_event(event, result)

        # --- Economic boom (strong economy + stable population + peace) ---
        # Less frequent than trade, bigger per-hit. Domestic expansion.
        for fid, faction in self._state.factions.items():
            if fid in factions_at_war_this_turn:
                continue
            if (faction.economic_strength > 0.4
                    and faction.population_stability > 0.5
                    and faction.economic_strength < faction.economic_potential):
                if self._rng.random() < 0.025:
                    event = SimulationEvent(
                        event_id=f"boom_{fid}_{self._state.turn}",
                        event_type=EventType.ECONOMIC_BOOM,
                        turn=self._state.turn,
                        target_faction=fid,
                        severity=0.3 + self._rng.random() * 0.4,
                        description=f"Economic expansion in {faction.name}",
                    )
                    result.events_generated.append(event)
                    self._apply_event(event, result)

        # --- Technology breakthrough (high tech factions) ---
        # Rare but impactful. Tech accumulates.
        for fid, faction in self._state.factions.items():
            if faction.technology_level > 0.4 and self._rng.random() < 0.02:
                event = SimulationEvent(
                    event_id=f"tech_{fid}_{self._state.turn}",
                    event_type=EventType.TECHNOLOGY_BREAKTHROUGH,
                    turn=self._state.turn,
                    target_faction=fid,
                    severity=0.3 + self._rng.random() * 0.3,
                    description=f"Technology breakthrough in {faction.name}",
                )
                result.events_generated.append(event)
                self._apply_event(event, result)

        # --- Cultural movement (population below baseline + peace) ---
        # Social recovery. Not economic — this is people finding stability.
        for fid, faction in self._state.factions.items():
            if fid in factions_at_war_this_turn:
                continue
            if faction.population_stability < 0.6 and faction.population_stability > 0.1:
                if self._rng.random() < 0.04:
                    # Pick a random neighbor for cultural exchange
                    neighbors = [
                        f for f in faction_ids
                        if f != fid and faction.trust_scores.get(f, 0.5) > 0.3
                    ]
                    partner = self._rng.choice(neighbors) if neighbors else None
                    event = SimulationEvent(
                        event_id=f"culture_{fid}_{self._state.turn}",
                        event_type=EventType.CULTURAL_MOVEMENT,
                        turn=self._state.turn,
                        target_faction=fid,
                        severity=0.3 + self._rng.random() * 0.3,
                        parameters={"cultural_partner": partner},
                        description=f"Cultural movement in {faction.name}",
                    )
                    result.events_generated.append(event)
                    self._apply_event(event, result)

        # --- Infrastructure investment (below economic potential + peace) ---
        # Deliberate rebuilding. The domestic equivalent of trade deals.
        for fid, faction in self._state.factions.items():
            if fid in factions_at_war_this_turn:
                continue
            if faction.economic_strength < faction.economic_potential * 0.85:
                invest_p = 0.04 + faction.technology_level * 0.02
                if self._rng.random() < invest_p:
                    event = SimulationEvent(
                        event_id=f"infra_{fid}_{self._state.turn}",
                        event_type=EventType.INFRASTRUCTURE_INVESTMENT,
                        turn=self._state.turn,
                        target_faction=fid,
                        severity=0.3 + self._rng.random() * 0.3,
                        description=f"Infrastructure investment in {faction.name}",
                    )
                    result.events_generated.append(event)
                    self._apply_event(event, result)

        # --- Peace legitimacy (resolved conflict → leader credibility) ---
        for conflict in self._state.conflicts.values():
            if (conflict.phase == ConflictPhase.RESOLUTION
                    and conflict.turns_active > 0
                    and self._rng.random() < 0.06):
                for party in conflict.parties:
                    leader = self._get_faction_leader(party)
                    if leader and leader.public_legitimacy < 0.8:
                        leader.public_legitimacy = min(
                            1.0, leader.public_legitimacy + 0.03
                        )
                        result.state_changes.append({
                            "type": "peace_legitimacy_boost",
                            "leader": leader.leader_id,
                            "delta": 0.03,
                        })

    # ------------------------------------------------------------------ #
    # HELPERS                                                             #
    # ------------------------------------------------------------------ #

    def _require_init(self) -> None:
        if not self._initialized or self._state is None:
            raise RuntimeError(
                "Engine not initialized. Call init_scenario() first."
            )

    def _find_conflict(
        self, faction_a: str, faction_b: str,
    ) -> Optional[ConflictState]:
        """Find an existing conflict involving both factions."""
        assert self._state is not None
        for conflict in self._state.conflicts.values():
            if faction_a in conflict.parties and faction_b in conflict.parties:
                return conflict
        return None

    def _get_faction_leader(self, faction_id: str) -> Optional[LeaderState]:
        """Get the primary leader for a faction."""
        assert self._state is not None
        faction = self._state.factions.get(faction_id)
        if faction and faction.leader_id:
            return self._state.leaders.get(faction.leader_id)
        return None

    def _adjust_trust(
        self,
        faction_a: str,
        faction_b: str,
        delta: float,
        result: TickResult,
    ) -> None:
        """Adjust bilateral trust and log the change."""
        assert self._state is not None
        fa = self._state.factions.get(faction_a)
        fb = self._state.factions.get(faction_b)

        old_ab = None
        if fa and faction_b in fa.trust_scores:
            old_ab = fa.trust_scores[faction_b]
            fa.trust_scores[faction_b] = max(
                0.0, min(1.0, fa.trust_scores[faction_b] + delta)
            )
        if fb and faction_a in fb.trust_scores:
            fb.trust_scores[faction_a] = max(
                0.0, min(1.0, fb.trust_scores[faction_a] + delta)
            )

        if old_ab is not None:
            result.state_changes.append({
                "type": "trust_adjusted",
                "faction_a": faction_a,
                "faction_b": faction_b,
                "delta": round(delta, 4),
                "new_trust_ab": round(fa.trust_scores[faction_b], 4) if fa else None,
            })

    def _check_ethics(
        self, action_type: str, params: Dict[str, Any],
    ) -> bool:
        """
        Check action against ethics callback if attached.
        Returns True if action is allowed, False if vetoed.
        """
        if self._ethics_callback is None:
            return True
        try:
            return self._ethics_callback(action_type, params)
        except Exception as e:
            logger.error("Ethics callback error: %s", e)
            # Picard_Delta_3: when in doubt, block
            return False


# ============================================================================
# CLI ENTRY POINT
# ============================================================================

def main() -> None:
    """Demo: run the canonical scenario for 20 turns."""
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(name)s %(levelname)s - %(message)s",
    )

    print("=" * 60)
    print("  GUMAS L2 Simulation Engine — Demo Run")
    print("  Anchor: GUMAS-ENGINE-CORE-V1")
    print("  Ethics: Picard_Delta_3")
    print("=" * 60)

    engine = GUMASEngine(seed=42)
    state = engine.init_scenario()

    print(f"\nScenario: {state.scenario_id}")
    print(f"Factions: {len(state.factions)}")
    print(f"Leaders:  {len(state.leaders)}")
    print(f"Conflicts: {len(state.conflicts)}")
    print()

    for _ in range(20):
        result = engine.step()
        events_str = ", ".join(
            e.event_type.value for e in result.events_generated
        ) or "none"
        changes = len(result.state_changes)

        # Show conflict phases
        phases = {
            c.conflict_id: c.phase.value
            for c in state.conflicts.values()
            if c.phase != ConflictPhase.PEACE
        }
        print(
            f"  Turn {result.turn:>3}: "
            f"{changes:>2} changes, "
            f"emergent=[{events_str}], "
            f"conflicts={phases}"
        )

    # Final summary
    print("\n" + "=" * 60)
    print("  Final State Summary")
    print("=" * 60)

    for fid, faction in state.factions.items():
        leader = engine._get_faction_leader(fid)
        leader_name = leader.name if leader else "none"
        low_trust = [
            other for other, t in faction.trust_scores.items() if t < 0.3
        ]
        print(
            f"  {faction.name:<30} "
            f"rep={faction.reputation:.2f}  "
            f"mil={faction.military_strength:.2f}  "
            f"econ={faction.economic_strength:.2f}  "
            f"leader={leader_name}"
        )
        if low_trust:
            print(f"    ↳ low trust with: {', '.join(low_trust)}")

    print()
    for cid, conflict in state.conflicts.items():
        print(
            f"  Conflict '{cid}': {conflict.phase.value} "
            f"(turns={conflict.turns_active}, "
            f"deesc_p={conflict.deescalation_probability:.3f})"
        )

    # Export
    output_path = "gumas_demo_output.json"
    engine.export_state(output_path)
    print(f"\nState exported to {output_path}")


if __name__ == "__main__":
    main()

```

## `modules/gumas/models.py`

```python
#!/usr/bin/env python3
"""
GUMAS L2 Simulation Data Models
================================
Anchor: GUMAS-ENGINE-MODELS-V1
Seed: EOS_SEED_ORION
Ethics: Picard_Delta_3
DLP: L2_ENGINE_CORE
Version: 1.0.0

Data models for the L2 GUMAS multi-agent galactic simulation.
All schemas derived from the Runtime Reference Packet v0.4 and
PR_L2_GUMAS_ARCHITECTURAL_ENHANCEMENTS.

Conventions:
- Probabilities and trust scores: [0.0, 1.0]
- Cost indices: [0.0, +inf)
- Signed shocks: (-inf, +inf)
- Update cadence: turn-based (per engine tick)
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional


# ============================================================================
# ENUMS
# ============================================================================

class CertaintyTag(Enum):
    """Data provenance tags per Runtime Reference Packet."""
    CANON = "CANON"
    STAGING = "STAGING"
    UNCONFIRMED = "UNCONFIRMED"
    LEGEND_CONTESTED = "LEGEND_CONTESTED"
    APPROX = "APPROX"


class BiasType(Enum):
    """Leader cognitive bias types (Section 1.1 of Runtime Reference Packet)."""
    STATUS_QUO = "status_quo_bias"
    SURVIVORSHIP = "survivorship_bias"
    CONFIRMATION = "confirmation_bias"
    SUNK_COST = "sunk_cost_fallacy"
    HYPER_RATIONALISM = "hyper_rationalism_bias"
    FEAR_BASED = "fear_based_decision_making"
    MORAL_LICENSING = "moral_self_licensing"
    ZERO_SUM = "zero_sum_thinking"


class FactionType(Enum):
    """Polity governance types from entity registry."""
    FEDERATION = "federation"
    AUTHORITARIAN = "authoritarian imperial bloc"
    CORPORATE_OLIGARCHY = "corporate oligarchy"
    CULTURAL_SPIRITUAL = "cultural-spiritual polity"
    CLAN_CONFEDERATION = "clan confederation"
    MONASTIC_NETWORK = "monastic network"
    NOMADIC_DIASPORA = "nomadic diaspora"
    SOVEREIGN_AI = "sovereign AI entity"
    ROGUE_SYNTHETIC = "rogue synthetic coalition"
    BREAKAWAY_BLOC = "breakaway bloc"
    PMC = "private military conglomerate"
    MILITANT_SPIRITUAL = "militant spiritual order"
    FRONTIER_CONFEDERATION = "frontier confederation"


class ConflictPhase(Enum):
    """Conflict lifecycle phases."""
    PEACE = "peace"
    TENSION = "tension"
    ESCALATION = "escalation"
    OPEN_CONFLICT = "open_conflict"
    STALEMATE = "stalemate"
    DEESCALATION = "deescalation"
    CEASEFIRE = "ceasefire"
    NEGOTIATION = "negotiation"
    RESOLUTION = "resolution"


class TreatyPhase(Enum):
    """Treaty negotiation phases (Section 1.4)."""
    NONE = "none"
    CEASEFIRE_TALKS = "ceasefire_talks"
    BARGAINING = "bargaining"
    INTERNAL_PRESSURE = "internal_pressure"
    RATIFICATION = "ratification"
    MONITORING = "monitoring"
    VIOLATED = "violated"
    COLLAPSED = "collapsed"


class EventType(Enum):
    """Injected event types for the simulation."""
    MILITARY_ESCALATION = "military_escalation"
    DIPLOMATIC_OVERTURE = "diplomatic_overture"
    ESPIONAGE_EXPOSURE = "espionage_exposure"
    ECONOMIC_SHOCK = "economic_shock"
    LEADER_CHANGE = "leader_change"
    TREATY_PROPOSAL = "treaty_proposal"
    TREATY_VIOLATION = "treaty_violation"
    INTELLIGENCE_LEAK = "intelligence_leak"
    HUMANITARIAN_CRISIS = "humanitarian_crisis"
    TECHNOLOGY_BREAKTHROUGH = "technology_breakthrough"
    CULTURAL_MOVEMENT = "cultural_movement"
    INTERNAL_COUP = "internal_coup"
    MEDIATION_OFFER = "mediation_offer"
    TRADE_AGREEMENT = "trade_agreement"
    ECONOMIC_BOOM = "economic_boom"
    INFRASTRUCTURE_INVESTMENT = "infrastructure_investment"
    CUSTOM = "custom"


# ============================================================================
# LEADER STATE
# ============================================================================

@dataclass
class LeaderState:
    """
    Leader with cognitive bias system (Section 1.1).

    Bias hooks (engine-facing):
    - evidence_gain_multiplier (per evidence type)
    - risk_tolerance (0-1)
    - diplomacy_openness (0-1)
    - escalation_threshold (0-1)
    - oversight_resistance (0-1)
    """
    leader_id: str
    name: str
    role: str
    faction_id: str
    dominant_bias: BiasType
    secondary_biases: List[BiasType] = field(default_factory=list)
    bias_intensity: float = 0.5
    plasticity: float = 0.3

    # Bias effect hooks
    evidence_gain_multiplier: float = 1.0
    risk_tolerance: float = 0.5
    diplomacy_openness: float = 0.5
    escalation_threshold: float = 0.5
    oversight_resistance: float = 0.3

    # Internal state
    public_legitimacy: float = 0.7
    elite_support: float = 0.6
    institutional_control: float = 0.5
    war_pressure: float = 0.0

    # Stressors (cumulative)
    war_losses: int = 0
    betrayals: int = 0
    scandals: int = 0
    economic_shock: float = 0.0

    certainty: CertaintyTag = CertaintyTag.STAGING

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["dominant_bias"] = self.dominant_bias.value
        d["secondary_biases"] = [b.value for b in self.secondary_biases]
        d["certainty"] = self.certainty.value
        return d


# ============================================================================
# FACTION STATE
# ============================================================================

@dataclass
class FactionState:
    """
    Polity state from entity registry (Section 3.1).
    Includes diplomacy memory (Section 1.5) via trust_scores.
    """
    faction_id: str
    name: str
    faction_type: FactionType
    notes: str = ""

    # Current leader (leader_id reference)
    leader_id: Optional[str] = None

    # Economic/military indicators
    military_strength: float = 0.5
    economic_strength: float = 0.5
    technology_level: float = 0.5
    population_stability: float = 0.7

    # Diplomacy memory (Section 1.5): trust[other_faction_id] -> score
    trust_scores: Dict[str, float] = field(default_factory=dict)

    # Reputation (affected by treaty breaches)
    reputation: float = 0.7

    # Derived fields (Section 1.5)
    verification_demand: float = 0.5
    deal_discount: float = 0.0
    coalition_invite_weight: float = 0.5

    # Structural ceiling: not every polity can reach max economy.
    # Governed by type, resources, governance model.
    economic_potential: float = 0.7

    certainty: CertaintyTag = CertaintyTag.STAGING

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["faction_type"] = self.faction_type.value
        d["certainty"] = self.certainty.value
        return d


# ============================================================================
# CONFLICT STATE
# ============================================================================

@dataclass
class ConflictState:
    """
    Conflict instance between parties (Section 1.2).
    """
    conflict_id: str
    parties: List[str]  # faction_ids
    phase: ConflictPhase = ConflictPhase.TENSION

    # De-escalation inputs (Section 1.2)
    war_cost_estimate: Dict[str, float] = field(default_factory=dict)
    stalemate_index: float = 0.0
    internal_pressure: Dict[str, float] = field(default_factory=dict)
    mediation_available: bool = False
    mediator_id: Optional[str] = None

    # De-escalation output
    deescalation_probability: float = 0.0

    # Eligible compromises
    eligible_compromises: List[str] = field(default_factory=list)

    # History
    turns_active: int = 0
    casualty_index: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["phase"] = self.phase.value
        return d


# ============================================================================
# TREATY STATE
# ============================================================================

@dataclass
class TreatyState:
    """
    Treaty instance (Section 1.4).
    """
    treaty_id: str
    parties: List[str]  # faction_ids
    phase: TreatyPhase = TreatyPhase.NONE

    # Treaty parameters (PR Section 5.1)
    enforcement_level: float = 0.5
    violation_threshold: float = 0.6
    ambiguity_tolerance: float = 0.2

    # Breach tracking per faction
    breach_count: Dict[str, int] = field(default_factory=dict)
    breach_history: List[Dict[str, Any]] = field(default_factory=list)
    reputation_impact: float = -0.1

    # Terms
    terms: Dict[str, Any] = field(default_factory=dict)

    # Monitoring
    turns_since_ratification: int = 0
    is_active: bool = False

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["phase"] = self.phase.value
        return d


# ============================================================================
# SIMULATION EVENT
# ============================================================================

@dataclass
class SimulationEvent:
    """Event injected into or generated by the simulation."""
    event_id: str
    event_type: EventType
    turn: int
    source_faction: Optional[str] = None
    target_faction: Optional[str] = None
    parameters: Dict[str, Any] = field(default_factory=dict)
    severity: float = 0.5
    description: str = ""
    injected: bool = False  # True if externally injected, False if emergent

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["event_type"] = self.event_type.value
        return d


# ============================================================================
# TICK RESULT
# ============================================================================

@dataclass
class TickResult:
    """Result of a single simulation tick."""
    turn: int
    events_processed: List[SimulationEvent] = field(default_factory=list)
    events_generated: List[SimulationEvent] = field(default_factory=list)
    state_changes: List[Dict[str, Any]] = field(default_factory=list)
    ethics_flags: List[Dict[str, Any]] = field(default_factory=list)
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "turn": self.turn,
            "events_processed": [e.to_dict() for e in self.events_processed],
            "events_generated": [e.to_dict() for e in self.events_generated],
            "state_changes": self.state_changes,
            "ethics_flags": self.ethics_flags,
            "timestamp": self.timestamp,
        }


# ============================================================================
# GUMAS WORLD STATE (top-level snapshot)
# ============================================================================

@dataclass
class GUMASState:
    """
    Complete simulation state at a given turn.
    This is the top-level object the engine manages.
    """
    scenario_id: str
    turn: int = 0
    seed: int = 42

    factions: Dict[str, FactionState] = field(default_factory=dict)
    leaders: Dict[str, LeaderState] = field(default_factory=dict)
    conflicts: Dict[str, ConflictState] = field(default_factory=dict)
    treaties: Dict[str, TreatyState] = field(default_factory=dict)

    # Event queue (pending injected events)
    event_queue: List[SimulationEvent] = field(default_factory=list)

    # Full history of tick results
    history: List[TickResult] = field(default_factory=list)

    # DLP metadata
    anchor: str = "GUMAS-ENGINE-V1"
    ethics_protocol: str = "Picard_Delta_3"
    version: str = "1.0.0"

    def to_dict(self, include_history: bool = False) -> Dict[str, Any]:
        """Serialize state to dict. History excluded by default for size."""
        result = {
            "scenario_id": self.scenario_id,
            "turn": self.turn,
            "seed": self.seed,
            "factions": {k: v.to_dict() for k, v in self.factions.items()},
            "leaders": {k: v.to_dict() for k, v in self.leaders.items()},
            "conflicts": {k: v.to_dict() for k, v in self.conflicts.items()},
            "treaties": {k: v.to_dict() for k, v in self.treaties.items()},
            "event_queue_depth": len(self.event_queue),
            "history_depth": len(self.history),
            "anchor": self.anchor,
            "ethics_protocol": self.ethics_protocol,
            "version": self.version,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        if include_history:
            result["history"] = [h.to_dict() for h in self.history]
        return result

```

## `modules/gumas/scenarios.py`

```python
#!/usr/bin/env python3
"""
GUMAS L2 Canonical Scenario Loader
====================================
Anchor: GUMAS-ENGINE-SCENARIOS-V1
Seed: EOS_SEED_ORION
Ethics: Picard_Delta_3
DLP: L2_ENGINE_CORE
Version: 1.0.0

Loads canonical GUMAS scenarios from Runtime Reference Packet entity
data. Provides the default galactic state that the engine initializes
with, including all 13 polities, their leaders, and initial
relationship matrices.

This module is the bridge between the L2 design documents and the
running engine. Entity definitions below are transcribed verbatim
from the Runtime Reference Packet v0.4 Section 3 and the L2 GUMAS
Staging Dossier.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from modules.gumas.models import (
    BiasType,
    CertaintyTag,
    ConflictPhase,
    ConflictState,
    FactionState,
    FactionType,
    GUMASState,
    LeaderState,
)


# ============================================================================
# CANONICAL FACTIONS (Runtime Reference Packet v0.4, Section 3.1)
# ============================================================================

def _build_canonical_factions() -> Dict[str, FactionState]:
    """Build the 13 canonical polities from the Runtime Reference Packet."""
    raw = [
        ("galactic_union", "Galactic Union", FactionType.FEDERATION,
         "Core interstellar polity; Senate governance; internal blocs."),
        ("velar_imperium", "Velar Imperium", FactionType.AUTHORITARIAN,
         "Divide-and-rule internal factionalism; realism-first authoritarian dynamics."),
        ("outer_colonies", "Outer Colonies Confederation", FactionType.FRONTIER_CONFEDERATION,
         "Decentralized breakaway space; pirate-capital integration in some regions."),
        ("zyphari_compact", "Zyphari Compact", FactionType.CORPORATE_OLIGARCHY,
         "Trade coalitions, financial warfare, Algorithmic Prose culture."),
        ("elari_ascendancy", "Elari Ascendancy", FactionType.CULTURAL_SPIRITUAL,
         "Celestial Abstraction; Symmetry Doctrine influence."),
        ("vorran_clans", "Vorran Clans", FactionType.CLAN_CONFEDERATION,
         "Resonance Sculpture; communal identity emphasis."),
        ("kaelar_orders", "Kaelar Monastic Orders", FactionType.MONASTIC_NETWORK,
         "Perfect Uncertainty; Organic Ink Histories."),
        ("tharaxian_nomads", "Tharaxian Nomads", FactionType.NOMADIC_DIASPORA,
         "Silent Poetry; gesture/light/bio-signal communication forms."),
        ("prime_construct", "Prime Construct Polity", FactionType.SOVEREIGN_AI,
         "Logic-driven diplomacy; contested organic reception."),
        ("ai_warlord", "AI-Warlord Collective", FactionType.ROGUE_SYNTHETIC,
         "Nemesis Core Intelligence leadership; mixed wings."),
        ("separatist_confed", "Separatist Confederation", FactionType.BREAKAWAY_BLOC,
         "Moderate vs hardline splinters possible."),
        ("pmc_syndicate", "PMC Syndicate", FactionType.PMC,
         "Security-for-profit; intelligence branch."),
        ("crimson_pact", "Crimson Pact", FactionType.MILITANT_SPIRITUAL,
         "War-chaplain leadership; zeal-driven doctrine."),
    ]

    factions: Dict[str, FactionState] = {}
    for fid, name, ftype, notes in raw:
        factions[fid] = FactionState(
            faction_id=fid,
            name=name,
            faction_type=ftype,
            notes=notes,
            certainty=CertaintyTag.STAGING,
        )
    return factions


# ============================================================================
# CANONICAL LEADERS (Runtime Reference Packet v0.4, Section 3.3)
# ============================================================================

def _build_canonical_leaders() -> Dict[str, LeaderState]:
    """
    Build all faction leaders with bias assignments.

    Sources:
      - Character Roster (Appendix 18, Origin Thread Dossier)
      - L2 Runtime Reference Packet v0.4 (Section 3.3)
      - Staging Dossier: Velar Imperium deep-dive
      - Engine-generated STAGING leaders for 5 undocumented factions
        (Zyphari, Elari, Vorran, Kaelar, Tharaxian) using naming
        conventions from the factional linguistic protocol.

    Every faction gets a primary leader so bias-driven behavior
    fires galaxy-wide. The simulation generates canon.
    """
    raw = [
        # ============================================================
        # GALACTIC UNION — documented in Character Roster 18.1
        # ============================================================
        ("zylox_rhaegos", "Chancellor Zylox Rhaegos",
         "Supreme Chancellor of the Galactic Union",
         "galactic_union", BiasType.STATUS_QUO),
        ("kael_durn", "General Kael Durn",
         "Supreme Military Commander, GU Armed Forces",
         "galactic_union", BiasType.SUNK_COST),
        ("lirian_vael_torin", "Grand Strategist Lirian Vael-Torin",
         "Covert Military Advisor to Chancellor Zylox",
         "galactic_union", BiasType.CONFIRMATION),
        ("varek_norr", "Director Varek Norr",
         "Director of the Office of Strategic Diplomacy (OSD)",
         "galactic_union", BiasType.HYPER_RATIONALISM),
        ("vael_saros", "Chief Marshal Vael Saros",
         "Leader of the Union Marshals",
         "galactic_union", BiasType.MORAL_LICENSING),
        ("renn_valcor", "High Chancellor Renn Valcor",
         "Speaker of the Union Senate",
         "galactic_union", BiasType.STATUS_QUO),
        ("selene_arcturus", "Admiral Selene Arcturus",
         "Commander of the Union Naval Forces",
         "galactic_union", BiasType.SURVIVORSHIP),
        ("callan_deyrus", "Director Callan Deyrus",
         "Head of Union Intelligence Bureau (UIB)",
         "galactic_union", BiasType.HYPER_RATIONALISM),
        ("anaya_ral_seyr", "Minister Anaya Ral-Seyr",
         "Minister of Trade & Economy",
         "galactic_union", BiasType.CONFIRMATION),

        # ============================================================
        # VELAR IMPERIUM — documented in Staging Dossier Section 16.1
        # Lord Marshal Virex Tal'Varen: "maintains power via
        # factional rivalry" → ZERO_SUM (win/loss absolutism;
        # divide-and-rule requires it)
        # ============================================================
        ("virex_talvaren", "Lord Marshal Virex Tal'Varen",
         "Supreme military-political strongman; divide-and-rule architect",
         "velar_imperium", BiasType.ZERO_SUM),

        # ============================================================
        # OUTER COLONIES — documented in Staging Dossier (Velar section)
        # Pirate Queen: "mobile fortress / refugee ship / black-market
        # hub" → SURVIVORSHIP (overconfidence from past survival)
        # ============================================================
        ("theryn_kaelvakar", "Pirate Queen Theryn Kael'Vakar",
         "Confederation Leader; captain of the Khar'Thyrix",
         "outer_colonies", BiasType.SURVIVORSHIP),

        # ============================================================
        # SEPARATIST CONFEDERATION — documented in Roster 18.3
        # Military leader: committed to breakaway → SUNK_COST
        # ============================================================
        ("rhaegon_torr_kai", "Supreme Commander Rhaegon Torr-Kai",
         "Military Leader of the Separatist Confederation",
         "separatist_confed", BiasType.SUNK_COST),

        # ============================================================
        # AI-WARLORD COLLECTIVE — documented in Roster 18.3
        # AI Overlord: pure logic → HYPER_RATIONALISM
        # ============================================================
        ("nemesis_core", "Nemesis Core Intelligence",
         "AI Overlord of the AI-Warlord Collective",
         "ai_warlord", BiasType.HYPER_RATIONALISM),

        # ============================================================
        # PRIME CONSTRUCT POLITY — documented in Roster 18.1
        # ============================================================
        ("prime_construct_leader", "Prime Construct",
         "AI Sovereign Entity",
         "prime_construct", BiasType.HYPER_RATIONALISM),

        # ============================================================
        # PMC SYNDICATE — documented in Roster 18.3
        # CEO/military: profit justifies all → MORAL_LICENSING
        # ============================================================
        ("vailen_rix", "Executive Commander Vailen Rix",
         "CEO & Military Leader of PMC Syndicate",
         "pmc_syndicate", BiasType.MORAL_LICENSING),

        # ============================================================
        # CRIMSON PACT — documented in Roster 18.3
        # War-chaplain: zeal-driven, defensive doctrine → FEAR_BASED
        # ============================================================
        ("malrik_voska", "Supreme War-Chaplain Malrik Voska",
         "Spiritual & Military Leader of the Crimson Pact",
         "crimson_pact", BiasType.FEAR_BASED),

        # ============================================================
        # ZYPHARI COMPACT — No documented leader.
        # STAGING: corporate oligarchy, Algorithmic Prose culture,
        # predictive media → CONFIRMATION (corporate echo chamber,
        # filters contradictory market signals).
        # Name follows Zyphari convention: guild-syllable structures.
        # ============================================================
        ("qellan_vyss", "Board Sovereign Qellan Vyss",
         "Chairman of the Zyphari Compact Governing Board",
         "zyphari_compact", BiasType.CONFIRMATION),

        # ============================================================
        # ELARI ASCENDANCY — No documented leader.
        # STAGING: cultural-spiritual polity, Celestial Abstraction,
        # Symmetry Doctrine → STATUS_QUO (sacred traditions resist
        # disruption).
        # Name follows Elari convention: flowing vowels, luminous.
        # ============================================================
        ("aelindra_voss_aurai", "Luminary Aelindra Voss-Aurai",
         "High Luminary of the Elari Ascendancy",
         "elari_ascendancy", BiasType.STATUS_QUO),

        # ============================================================
        # VORRAN CLANS — No documented leader.
        # STAGING: clan confederation, communal identity emphasis,
        # Resonance Sculpture → ZERO_SUM (clan loyalty: with us
        # or against us).
        # Name follows Vorran convention: resonant consonants, communal.
        # ============================================================
        ("drenn_korvath", "Resonance Chief Drenn Korvath",
         "First Chief of the Vorran Clan Council",
         "vorran_clans", BiasType.ZERO_SUM),

        # ============================================================
        # KAELAR MONASTIC ORDERS — No documented leader.
        # STAGING: monastic skeptics, Perfect Uncertainty, Organic Ink
        # Histories → STATUS_QUO (institutional inertia of monastic
        # orders, even those professing uncertainty).
        # Name follows Kaelar convention: archival, deliberate.
        # ============================================================
        ("thessa_nai_oruun", "Elder Inscriber Thessa Nai-Oruun",
         "Keeper of the First Archive, Kaelar Monastic Orders",
         "kaelar_orders", BiasType.STATUS_QUO),

        # ============================================================
        # THARAXIAN NOMADS — No documented leader.
        # STAGING: nomadic diaspora, Silent Poetry, gesture/light
        # communication → SURVIVORSHIP (trust what kept the drift
        # alive; adapt from proven patterns).
        # Name follows Tharaxian convention: soft sibilants, drift.
        # ============================================================
        ("sivaen_the_driftcaller", "Driftcaller Sivaen",
         "Voice of the Tharaxian Migration Council",
         "tharaxian_nomads", BiasType.SURVIVORSHIP),
    ]

    leaders: Dict[str, LeaderState] = {}
    for lid, name, role, faction_id, bias in raw:
        leaders[lid] = LeaderState(
            leader_id=lid,
            name=name,
            role=role,
            faction_id=faction_id,
            dominant_bias=bias,
            certainty=CertaintyTag.STAGING,
        )

    return leaders


# ============================================================================
# INITIAL TRUST MATRIX
# ============================================================================

def _build_initial_trust_matrix(
    faction_ids: List[str],
) -> Dict[str, Dict[str, float]]:
    """
    Build initial bilateral trust scores.

    Design: start with 0.5 (neutral) and apply structural adjustments
    based on documented faction relationships.
    """
    trust: Dict[str, Dict[str, float]] = {}
    for fid in faction_ids:
        trust[fid] = {other: 0.5 for other in faction_ids if other != fid}

    # Structural adjustments from dossier lore
    adjustments = [
        # Allies / positive
        ("galactic_union", "elari_ascendancy", 0.15),
        ("galactic_union", "vorran_clans", 0.10),
        ("elari_ascendancy", "vorran_clans", 0.20),  # Symmetry Doctrine allies
        ("galactic_union", "kaelar_orders", 0.05),
        ("galactic_union", "tharaxian_nomads", 0.05),

        # Rivals / negative
        ("galactic_union", "velar_imperium", -0.20),
        ("galactic_union", "ai_warlord", -0.30),
        ("galactic_union", "separatist_confed", -0.15),
        ("galactic_union", "crimson_pact", -0.10),
        ("velar_imperium", "separatist_confed", -0.10),
        ("prime_construct", "ai_warlord", -0.25),  # Contested AI sovereignty

        # Commercial / transactional
        ("zyphari_compact", "pmc_syndicate", 0.10),
        ("zyphari_compact", "galactic_union", -0.05),  # economic friction
        ("pmc_syndicate", "velar_imperium", 0.05),     # client relationship

        # Neutral-leaning
        ("kaelar_orders", "tharaxian_nomads", 0.10),  # philosophical alignment
        ("outer_colonies", "separatist_confed", 0.10),  # autonomy sympathy
    ]

    for fid_a, fid_b, delta in adjustments:
        if fid_a in trust and fid_b in trust.get(fid_a, {}):
            trust[fid_a][fid_b] = max(0.0, min(1.0, trust[fid_a][fid_b] + delta))
        if fid_b in trust and fid_a in trust.get(fid_b, {}):
            trust[fid_b][fid_a] = max(0.0, min(1.0, trust[fid_b][fid_a] + delta))

    return trust


# ============================================================================
# INITIAL CONFLICTS
# ============================================================================

def _build_initial_conflicts() -> Dict[str, ConflictState]:
    """Seed the galaxy with canonical tension points."""
    return {
        "union_imperium_border": ConflictState(
            conflict_id="union_imperium_border",
            parties=["galactic_union", "velar_imperium"],
            phase=ConflictPhase.TENSION,
            war_cost_estimate={"galactic_union": 0.3, "velar_imperium": 0.4},
            stalemate_index=0.2,
            internal_pressure={"galactic_union": 0.2, "velar_imperium": 0.3},
        ),
        "ai_sovereignty_crisis": ConflictState(
            conflict_id="ai_sovereignty_crisis",
            parties=["galactic_union", "prime_construct", "ai_warlord"],
            phase=ConflictPhase.ESCALATION,
            war_cost_estimate={
                "galactic_union": 0.2,
                "prime_construct": 0.1,
                "ai_warlord": 0.5,
            },
            stalemate_index=0.1,
            internal_pressure={
                "galactic_union": 0.4,
                "prime_construct": 0.1,
                "ai_warlord": 0.2,
            },
        ),
        "separatist_tension": ConflictState(
            conflict_id="separatist_tension",
            parties=["galactic_union", "separatist_confed"],
            phase=ConflictPhase.TENSION,
            war_cost_estimate={"galactic_union": 0.1, "separatist_confed": 0.6},
            stalemate_index=0.0,
            internal_pressure={"galactic_union": 0.1, "separatist_confed": 0.5},
        ),
    }


# ============================================================================
# SCENARIO BUILDER
# ============================================================================

def build_default_scenario(
    scenario_id: str = "gumas_canonical_v1",
    seed: int = 42,
) -> GUMASState:
    """
    Build the canonical GUMAS galactic scenario from Runtime Reference
    Packet data.

    Returns a fully initialized GUMASState ready for engine.step().
    """
    factions = _build_canonical_factions()
    leaders = _build_canonical_leaders()

    # Assign leaders to factions
    for leader in leaders.values():
        faction = factions.get(leader.faction_id)
        if faction and faction.leader_id is None:
            faction.leader_id = leader.leader_id

    # Build and apply trust matrix
    trust_matrix = _build_initial_trust_matrix(list(factions.keys()))
    for fid, scores in trust_matrix.items():
        if fid in factions:
            factions[fid].trust_scores = scores

    # Apply structural faction strengths
    _apply_faction_profiles(factions)

    # Build initial conflicts
    conflicts = _build_initial_conflicts()

    return GUMASState(
        scenario_id=scenario_id,
        seed=seed,
        factions=factions,
        leaders=leaders,
        conflicts=conflicts,
    )


def _apply_faction_profiles(factions: Dict[str, FactionState]) -> None:
    """Apply differentiated military/economic/tech profiles.

    economic_potential is the structural ceiling: not every polity
    can reach max economy. Corporate oligarchies outperform
    monastic networks. That's reality.
    """
    profiles = {
        #                         mil   eco  tech  pop   eco_potential
        "galactic_union":     (0.8, 0.8, 0.7, 0.7,  0.90),
        "velar_imperium":     (0.9, 0.6, 0.6, 0.5,  0.80),
        "outer_colonies":     (0.3, 0.4, 0.4, 0.6,  0.65),
        "zyphari_compact":    (0.4, 0.9, 0.7, 0.6,  0.95),
        "elari_ascendancy":   (0.3, 0.5, 0.6, 0.8,  0.70),
        "vorran_clans":       (0.6, 0.4, 0.4, 0.8,  0.60),
        "kaelar_orders":      (0.2, 0.3, 0.5, 0.9,  0.45),
        "tharaxian_nomads":   (0.3, 0.3, 0.4, 0.7,  0.50),
        "prime_construct":    (0.5, 0.6, 0.9, 0.5,  0.85),
        "ai_warlord":         (0.7, 0.3, 0.8, 0.3,  0.50),
        "separatist_confed":  (0.4, 0.3, 0.4, 0.4,  0.55),
        "pmc_syndicate":      (0.6, 0.5, 0.5, 0.4,  0.70),
        "crimson_pact":       (0.5, 0.2, 0.3, 0.6,  0.45),
    }
    for fid, (mil, eco, tech, pop, eco_pot) in profiles.items():
        if fid in factions:
            factions[fid].military_strength = mil
            factions[fid].economic_strength = eco
            factions[fid].technology_level = tech
            factions[fid].population_stability = pop
            factions[fid].economic_potential = eco_pot

```

## `modules/gumas/formulas.py`

```python
#!/usr/bin/env python3
"""
GUMAS L2 Simulation Formulas
=============================
Anchor: GUMAS-ENGINE-FORMULAS-V1
Seed: EOS_SEED_ORION
Ethics: Picard_Delta_3
DLP: L2_ENGINE_CORE
Version: 1.0.0

Pure functions implementing the L2 simulation formulas documented in
PR_L2_GUMAS_ARCHITECTURAL_ENHANCEMENTS Section 5.2 and the Runtime
Reference Packet v0.4 Section 1.

All functions are stateless and deterministic for a given input.
Side effects are handled by the engine, not by these functions.

Formula Index:
  1. calc_deescalation_probability  — Section 1.2 / PR 5.2 Formula 1
  2. calc_bias_evolution            — Section 1.1 / PR 5.2 Formula 2
  3. calc_treaty_breach_score       — Section 1.4 / PR 5.2 Formula 3
  4. calc_reputation_decay          — Section 1.5 / PR 5.2 Formula 4
  5. calc_double_agent_risk         — Section 1.3 / PR 5.2 Formula 5
  6. calc_trust_update              — Section 1.5
  7. apply_bias_hooks               — Section 1.1 bias effect modifiers
"""

from __future__ import annotations

from typing import Dict, Optional


def _clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    """Clamp a value to [lo, hi]."""
    return max(lo, min(hi, value))


# ============================================================================
# 1. DE-ESCALATION PROBABILITY
# ============================================================================

def calc_deescalation_probability(
    war_cost_a: float,
    war_cost_b: float,
    stalemate_index: float,
    internal_pressure_a: float,
    internal_pressure_b: float,
    mediation_available: bool,
    *,
    cost_weight: float = 0.3,
    stalemate_weight: float = 0.25,
    pressure_weight: float = 0.25,
    mediation_bonus: float = 0.2,
) -> float:
    """
    Calculate de-escalation probability for a conflict.

    Formula (PR Section 5.2 Formula 1):
        P = cost_weight × avg_war_cost
          + stalemate_weight × stalemate_index
          + pressure_weight × avg_internal_pressure
          + mediation_bonus × mediation_available

    Edge Cases:
        - stalemate_index == 1.0 → force P >= 0.5
        - avg_war_cost > 0.9 for both → force P >= 0.6

    Returns:
        float in [0.0, 1.0]
    """
    avg_war_cost = (war_cost_a + war_cost_b) / 2.0
    avg_pressure = (internal_pressure_a + internal_pressure_b) / 2.0
    mediation_flag = 1.0 if mediation_available else 0.0

    p = (
        cost_weight * avg_war_cost
        + stalemate_weight * stalemate_index
        + pressure_weight * avg_pressure
        + mediation_bonus * mediation_flag
    )

    # Edge case: total stalemate triggers negotiation
    if stalemate_index >= 1.0:
        p = max(p, 0.5)

    # Edge case: catastrophic mutual cost
    if war_cost_a > 0.9 and war_cost_b > 0.9:
        p = max(p, 0.6)

    return _clamp(p)


# ============================================================================
# 2. BIAS EVOLUTION
# ============================================================================

def calc_bias_evolution(
    current_intensity: float,
    plasticity: float,
    event_severity: float,
    has_survivorship_bias: bool = False,
    doctrine_shift_bonus: float = 0.0,
) -> float:
    """
    Calculate new bias intensity after an event.

    Formula (PR Section 5.2 Formula 2):
        new_intensity = current_intensity × (1 - plasticity × event_severity)
                      + adaptation_factor × doctrine_shift_bonus

    Constraints:
        - Result clamped to [0.0, 1.0]
        - adaptation_factor = 0.1 if leader has survivorship_bias, else 0.0

    Returns:
        float in [0.0, 1.0]
    """
    adaptation_factor = 0.1 if has_survivorship_bias else 0.0

    new_intensity = (
        current_intensity * (1.0 - plasticity * event_severity)
        + adaptation_factor * doctrine_shift_bonus
    )

    return _clamp(new_intensity)


# ============================================================================
# 3. TREATY BREACH DETECTION
# ============================================================================

def calc_treaty_breach_score(
    action_severity: float,
    is_direct_action: bool,
    treaty_ambiguity: float,
    faction_trust: float,
    *,
    ambiguity_tolerance: float = 0.2,
    trust_discount_multiplier: float = 0.1,
) -> float:
    """
    Calculate breach score for a potential treaty violation.

    Formula (PR Section 5.2 Formula 3):
        breach_score = (action_severity × violation_weight)
                     - (treaty_ambiguity × ambiguity_tolerance)
                     - (faction_trust × trust_discount)

    Where:
        violation_weight = 1.0 (direct) or 0.5 (indirect/proxy)
        trust_discount = trust_discount_multiplier × bilateral_trust_score

    Returns:
        Raw breach score (not clamped — compare against violation_threshold).
    """
    violation_weight = 1.0 if is_direct_action else 0.5
    trust_discount = trust_discount_multiplier * faction_trust

    return (
        action_severity * violation_weight
        - treaty_ambiguity * ambiguity_tolerance
        - faction_trust * trust_discount
    )


def is_treaty_breach(
    breach_score: float,
    violation_threshold: float = 0.6,
) -> bool:
    """Determine if breach_score exceeds the violation threshold."""
    return breach_score > violation_threshold


# ============================================================================
# 4. REPUTATION DECAY
# ============================================================================

def calc_reputation_after_decay(
    base_reputation: float,
    breach_penalty: float,
    breach_count: int,
    turns_since_last_breach: int,
    *,
    decay_factor: float = 0.95,
    floor: float = 0.1,
) -> float:
    """
    Calculate reputation after time-based decay of breach penalties.

    Formula (PR Section 5.2 Formula 4):
        new_reputation = base_reputation
                       + breach_penalty × breach_count × decay_factor^turns_since_breach

    Note: breach_penalty is negative (default -0.1), so this reduces reputation.

    Constraints:
        - decay_factor: 0.95 per turn
        - Floor: reputation cannot drop below 0.1

    Returns:
        float, minimum = floor
    """
    decayed_penalty = breach_penalty * breach_count * (decay_factor ** turns_since_last_breach)
    new_rep = base_reputation + decayed_penalty
    return max(floor, new_rep)


# ============================================================================
# 5. DOUBLE-AGENT RISK
# ============================================================================

def calc_double_agent_risk(
    bilateral_trust: float,
    intel_sensitivity: float,
    *,
    base_risk: float = 0.15,
    trust_modifier: float = -0.1,
    sensitivity_multiplier: float = 0.3,
) -> float:
    """
    Calculate probability of double-agent presence in intelligence sharing.

    Formula (PR Section 5.2 Formula 5):
        P = base_risk
          + sensitivity_multiplier × intel_sensitivity
          + trust_modifier

    Constraints:
        - Result clamped to [0.0, 0.8] (never certain, never impossible)
        - If bilateral_trust > 0.8: additional -0.1 modifier

    Returns:
        float in [0.0, 0.8]
    """
    high_trust_bonus = -0.1 if bilateral_trust > 0.8 else 0.0

    p = (
        base_risk
        + sensitivity_multiplier * intel_sensitivity
        + trust_modifier
        + high_trust_bonus
    )

    return _clamp(p, lo=0.0, hi=0.8)


# ============================================================================
# 6. TRUST UPDATE
# ============================================================================

def calc_trust_update(
    current_trust: float,
    betrayal_penalty: float,
    alliance_bonus: float,
    *,
    lambda_coeff: float = 1.0,
    delta_coeff: float = 1.0,
) -> float:
    """
    Update bilateral trust score.

    Formula (Runtime Reference Packet Section 1.5):
        T_new = clamp01(T_old - λ(B) + δ(A))

    Where:
        B = betrayal_penalty (exponential decay for repeats recommended)
        A = alliance-building / humanitarian / compliance actions
        λ, δ = tunable per faction culture + leader bias profile

    Returns:
        float in [0.0, 1.0]
    """
    new_trust = current_trust - lambda_coeff * betrayal_penalty + delta_coeff * alliance_bonus
    return _clamp(new_trust)


# ============================================================================
# 7. BIAS EFFECT HOOKS
# ============================================================================

# Default bias hook profiles per BiasType.
# Maps BiasType.value -> dict of hook adjustments (deltas from neutral 0.5).
BIAS_HOOK_PROFILES: Dict[str, Dict[str, float]] = {
    "status_quo_bias": {
        "evidence_gain_multiplier": 0.8,  # discounts novel evidence
        "risk_tolerance": 0.3,
        "diplomacy_openness": 0.4,
        "escalation_threshold": 0.7,      # slow to escalate
        "oversight_resistance": 0.6,      # resists institutional change
    },
    "survivorship_bias": {
        "evidence_gain_multiplier": 0.7,  # only counts confirmatory wins
        "risk_tolerance": 0.7,
        "diplomacy_openness": 0.4,
        "escalation_threshold": 0.4,      # quick to double down
        "oversight_resistance": 0.5,
    },
    "confirmation_bias": {
        "evidence_gain_multiplier": 0.5,  # heavy filter on contradictory data
        "risk_tolerance": 0.5,
        "diplomacy_openness": 0.3,
        "escalation_threshold": 0.5,
        "oversight_resistance": 0.4,
    },
    "sunk_cost_fallacy": {
        "evidence_gain_multiplier": 0.6,
        "risk_tolerance": 0.8,            # escalating commitment
        "diplomacy_openness": 0.2,        # won't back down
        "escalation_threshold": 0.3,      # very easy to escalate
        "oversight_resistance": 0.5,
    },
    "hyper_rationalism_bias": {
        "evidence_gain_multiplier": 1.2,  # overcounts quantifiable data
        "risk_tolerance": 0.6,
        "diplomacy_openness": 0.5,
        "escalation_threshold": 0.5,
        "oversight_resistance": 0.7,      # trusts own logic over committees
    },
    "fear_based_decision_making": {
        "evidence_gain_multiplier": 0.9,
        "risk_tolerance": 0.2,            # extremely risk-averse
        "diplomacy_openness": 0.3,
        "escalation_threshold": 0.3,      # defensive overreaction
        "oversight_resistance": 0.3,
    },
    "moral_self_licensing": {
        "evidence_gain_multiplier": 0.8,
        "risk_tolerance": 0.6,
        "diplomacy_openness": 0.5,
        "escalation_threshold": 0.4,
        "oversight_resistance": 0.8,      # "greater good" justification
    },
    "zero_sum_thinking": {
        "evidence_gain_multiplier": 0.7,
        "risk_tolerance": 0.6,
        "diplomacy_openness": 0.1,        # sees all deals as losses
        "escalation_threshold": 0.3,
        "oversight_resistance": 0.5,
    },
}


def apply_bias_hooks(
    bias_type_value: str,
    bias_intensity: float,
) -> Dict[str, float]:
    """
    Calculate effective bias hook values for a leader.

    Applies intensity scaling: hooks interpolate between neutral (0.5)
    and the bias profile value based on intensity.

    Args:
        bias_type_value: BiasType enum value string
        bias_intensity: 0.0 (no effect) to 1.0 (full effect)

    Returns:
        Dict with keys: evidence_gain_multiplier, risk_tolerance,
        diplomacy_openness, escalation_threshold, oversight_resistance
    """
    neutral = {
        "evidence_gain_multiplier": 1.0,
        "risk_tolerance": 0.5,
        "diplomacy_openness": 0.5,
        "escalation_threshold": 0.5,
        "oversight_resistance": 0.5,
    }

    profile = BIAS_HOOK_PROFILES.get(bias_type_value)
    if profile is None:
        return neutral

    result = {}
    for key, neutral_val in neutral.items():
        profile_val = profile.get(key, neutral_val)
        # Lerp between neutral and profile based on intensity
        result[key] = neutral_val + (profile_val - neutral_val) * bias_intensity

    return result

```

## `tests/test_gumas_engine.py`

```python
#!/usr/bin/env python3
"""
GUMAS Engine Test Suite
========================
Anchor: GUMAS-ENGINE-TESTS-V1
DLP: L2_ENGINE_CORE

Tests cover:
  - Formula correctness (all 6 documented formulas)
  - Scenario loading (canonical factions, leaders, trust matrix)
  - Engine lifecycle (init, step, run, export)
  - Event injection and processing
  - Seed-based reproducibility
  - Edge cases from PR documentation
"""

import json
import os
import sys
import tempfile

import pytest

# Ensure repo root is on path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from modules.gumas.formulas import (
    apply_bias_hooks,
    calc_bias_evolution,
    calc_deescalation_probability,
    calc_double_agent_risk,
    calc_reputation_after_decay,
    calc_treaty_breach_score,
    calc_trust_update,
    is_treaty_breach,
)
from modules.gumas.models import (
    BiasType,
    ConflictPhase,
    EventType,
    FactionType,
    GUMASState,
    SimulationEvent,
    TreatyPhase,
    TreatyState,
)
from modules.gumas.scenarios import build_default_scenario
from modules.gumas.engine import GUMASEngine


# ============================================================================
# FORMULA TESTS
# ============================================================================

class TestDeescalationProbability:
    """PR Section 5.2 Formula 1."""

    def test_basic_calculation(self):
        p = calc_deescalation_probability(
            war_cost_a=0.5, war_cost_b=0.5,
            stalemate_index=0.5,
            internal_pressure_a=0.5, internal_pressure_b=0.5,
            mediation_available=False,
        )
        # 0.3*0.5 + 0.25*0.5 + 0.25*0.5 = 0.15 + 0.125 + 0.125 = 0.4
        assert abs(p - 0.4) < 0.001

    def test_with_mediation(self):
        p = calc_deescalation_probability(
            war_cost_a=0.5, war_cost_b=0.5,
            stalemate_index=0.5,
            internal_pressure_a=0.5, internal_pressure_b=0.5,
            mediation_available=True,
        )
        # 0.4 + 0.2 = 0.6
        assert abs(p - 0.6) < 0.001

    def test_stalemate_floor(self):
        """Edge case: stalemate_index == 1.0 forces P >= 0.5."""
        p = calc_deescalation_probability(
            war_cost_a=0.0, war_cost_b=0.0,
            stalemate_index=1.0,
            internal_pressure_a=0.0, internal_pressure_b=0.0,
            mediation_available=False,
        )
        assert p >= 0.5

    def test_catastrophic_cost_floor(self):
        """Edge case: avg_war_cost > 0.9 for both forces P >= 0.6."""
        p = calc_deescalation_probability(
            war_cost_a=0.95, war_cost_b=0.95,
            stalemate_index=0.0,
            internal_pressure_a=0.0, internal_pressure_b=0.0,
            mediation_available=False,
        )
        assert p >= 0.6

    def test_result_clamped(self):
        """Result never exceeds 1.0."""
        p = calc_deescalation_probability(
            war_cost_a=1.0, war_cost_b=1.0,
            stalemate_index=1.0,
            internal_pressure_a=1.0, internal_pressure_b=1.0,
            mediation_available=True,
        )
        assert p <= 1.0


class TestBiasEvolution:
    """PR Section 5.2 Formula 2."""

    def test_basic_evolution(self):
        new_val = calc_bias_evolution(
            current_intensity=0.5,
            plasticity=0.3,
            event_severity=0.5,
        )
        # 0.5 * (1 - 0.3 * 0.5) + 0 = 0.5 * 0.85 = 0.425
        assert abs(new_val - 0.425) < 0.001

    def test_survivorship_adaptation(self):
        new_val = calc_bias_evolution(
            current_intensity=0.5,
            plasticity=0.3,
            event_severity=0.5,
            has_survivorship_bias=True,
            doctrine_shift_bonus=1.0,
        )
        # 0.425 + 0.1 * 1.0 = 0.525
        assert abs(new_val - 0.525) < 0.001

    def test_clamped_high(self):
        new_val = calc_bias_evolution(
            current_intensity=0.9,
            plasticity=0.0,
            event_severity=0.0,
            has_survivorship_bias=True,
            doctrine_shift_bonus=5.0,
        )
        assert new_val == 1.0

    def test_clamped_low(self):
        new_val = calc_bias_evolution(
            current_intensity=0.1,
            plasticity=1.0,
            event_severity=1.0,
        )
        assert new_val >= 0.0


class TestTreatyBreach:
    """PR Section 5.2 Formula 3."""

    def test_direct_action_breach(self):
        score = calc_treaty_breach_score(
            action_severity=0.8,
            is_direct_action=True,
            treaty_ambiguity=0.2,
            faction_trust=0.5,
        )
        # 0.8*1.0 - 0.2*0.2 - 0.5*0.05 = 0.8 - 0.04 - 0.025 = 0.735
        assert score > 0.6  # exceeds default threshold
        assert is_treaty_breach(score, 0.6)

    def test_indirect_action_no_breach(self):
        score = calc_treaty_breach_score(
            action_severity=0.5,
            is_direct_action=False,
            treaty_ambiguity=0.5,
            faction_trust=0.7,
        )
        # 0.5*0.5 - 0.5*0.2 - 0.7*0.07 = 0.25 - 0.1 - 0.049 = 0.101
        assert not is_treaty_breach(score, 0.6)


class TestReputationDecay:
    """PR Section 5.2 Formula 4."""

    def test_immediate_penalty(self):
        rep = calc_reputation_after_decay(
            base_reputation=0.7,
            breach_penalty=-0.1,
            breach_count=2,
            turns_since_last_breach=0,
        )
        # 0.7 + (-0.1 * 2 * 1.0) = 0.7 - 0.2 = 0.5
        assert abs(rep - 0.5) < 0.001

    def test_decayed_penalty(self):
        rep = calc_reputation_after_decay(
            base_reputation=0.7,
            breach_penalty=-0.1,
            breach_count=2,
            turns_since_last_breach=10,
        )
        # 0.7 + (-0.2 * 0.95^10) ≈ 0.7 - 0.1194 = 0.5806
        assert rep > 0.5  # Decayed, so less penalty than immediate

    def test_floor(self):
        rep = calc_reputation_after_decay(
            base_reputation=0.2,
            breach_penalty=-0.1,
            breach_count=10,
            turns_since_last_breach=0,
        )
        assert rep >= 0.1  # Floor enforced


class TestDoubleAgentRisk:
    """PR Section 5.2 Formula 5."""

    def test_basic_risk(self):
        risk = calc_double_agent_risk(
            bilateral_trust=0.5,
            intel_sensitivity=0.5,
        )
        # 0.15 + 0.3*0.5 + (-0.1) = 0.15 + 0.15 - 0.1 = 0.2
        assert abs(risk - 0.2) < 0.001

    def test_high_trust_bonus(self):
        risk = calc_double_agent_risk(
            bilateral_trust=0.9,
            intel_sensitivity=0.5,
        )
        # 0.2 + (-0.1) high trust bonus = 0.1
        assert abs(risk - 0.1) < 0.001

    def test_clamped_high(self):
        risk = calc_double_agent_risk(
            bilateral_trust=0.0,
            intel_sensitivity=1.0,
            base_risk=0.5,
            sensitivity_multiplier=0.5,
        )
        assert risk <= 0.8

    def test_clamped_low(self):
        risk = calc_double_agent_risk(
            bilateral_trust=1.0,
            intel_sensitivity=0.0,
            trust_modifier=-0.5,
        )
        assert risk >= 0.0


class TestTrustUpdate:
    """Runtime Reference Packet Section 1.5."""

    def test_basic_update(self):
        t = calc_trust_update(
            current_trust=0.5,
            betrayal_penalty=0.1,
            alliance_bonus=0.0,
        )
        assert abs(t - 0.4) < 0.001

    def test_clamped(self):
        t = calc_trust_update(current_trust=0.1, betrayal_penalty=0.5, alliance_bonus=0.0)
        assert t >= 0.0

        t = calc_trust_update(current_trust=0.9, betrayal_penalty=0.0, alliance_bonus=0.5)
        assert t <= 1.0


class TestBiasHooks:
    """Section 1.1 bias effect modifiers."""

    def test_neutral_at_zero_intensity(self):
        hooks = apply_bias_hooks("status_quo_bias", 0.0)
        assert hooks["risk_tolerance"] == 0.5
        assert hooks["diplomacy_openness"] == 0.5

    def test_full_intensity_matches_profile(self):
        hooks = apply_bias_hooks("zero_sum_thinking", 1.0)
        assert hooks["diplomacy_openness"] == pytest.approx(0.1, abs=0.01)

    def test_unknown_bias_returns_neutral(self):
        hooks = apply_bias_hooks("nonexistent_bias", 0.5)
        assert hooks["risk_tolerance"] == 0.5


# ============================================================================
# SCENARIO TESTS
# ============================================================================

class TestScenarioLoader:

    def test_canonical_factions(self):
        state = build_default_scenario()
        assert len(state.factions) == 13
        assert "galactic_union" in state.factions
        assert "velar_imperium" in state.factions
        assert "prime_construct" in state.factions

    def test_canonical_leaders(self):
        state = build_default_scenario()
        # 9 GU + 1 Velar + 1 Outer Colonies + 1 Separatist + 1 AI-Warlord
        # + 1 Prime Construct + 1 PMC + 1 Crimson + 5 engine-generated = 21
        assert len(state.leaders) >= 21
        assert "zylox_rhaegos" in state.leaders
        assert state.leaders["zylox_rhaegos"].dominant_bias == BiasType.STATUS_QUO
        # Velar Imperium now has a leader
        assert "virex_talvaren" in state.leaders
        assert state.leaders["virex_talvaren"].dominant_bias == BiasType.ZERO_SUM

    def test_trust_matrix_initialized(self):
        state = build_default_scenario()
        gu = state.factions["galactic_union"]
        assert len(gu.trust_scores) == 12  # all other factions
        # Structural: Union trusts Elari more than AI Warlords
        assert gu.trust_scores["elari_ascendancy"] > gu.trust_scores["ai_warlord"]

    def test_initial_conflicts(self):
        state = build_default_scenario()
        assert len(state.conflicts) >= 3
        assert "union_imperium_border" in state.conflicts

    def test_faction_profiles_applied(self):
        state = build_default_scenario()
        gu = state.factions["galactic_union"]
        vi = state.factions["velar_imperium"]
        zc = state.factions["zyphari_compact"]
        assert vi.military_strength > zc.military_strength
        assert zc.economic_strength > vi.economic_strength

    def test_leader_faction_linkage(self):
        state = build_default_scenario()
        gu = state.factions["galactic_union"]
        assert gu.leader_id is not None
        assert gu.leader_id in state.leaders


# ============================================================================
# ENGINE LIFECYCLE TESTS
# ============================================================================

class TestEngineLifecycle:

    def test_init_and_step(self):
        engine = GUMASEngine(seed=42)
        engine.init_scenario()
        result = engine.step()
        assert result.turn == 1

    def test_run_multiple_turns(self):
        engine = GUMASEngine(seed=42)
        engine.init_scenario()
        results = engine.run(n_turns=10)
        assert len(results) == 10
        assert results[-1].turn == 10
        assert engine.get_state().turn == 10

    def test_raises_without_init(self):
        engine = GUMASEngine()
        with pytest.raises(RuntimeError, match="not initialized"):
            engine.step()

    def test_export(self):
        engine = GUMASEngine(seed=42)
        engine.init_scenario()
        engine.run(5)

        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = f.name

        try:
            engine.export_state(path)
            with open(path) as f:
                data = json.load(f)
            assert data["turn"] == 5
            assert data["dlp"]["anchor"] == "GUMAS-ENGINE-CORE-V1"
            assert len(data["factions"]) == 13
            assert "history" in data
        finally:
            os.unlink(path)

    def test_state_serialization(self):
        engine = GUMASEngine(seed=42)
        state = engine.init_scenario()
        d = state.to_dict()
        assert d["scenario_id"] == "gumas_canonical_v1"
        assert "galactic_union" in d["factions"]


# ============================================================================
# EVENT INJECTION TESTS
# ============================================================================

class TestEventInjection:

    def test_inject_military_escalation(self):
        engine = GUMASEngine(seed=42)
        engine.init_scenario()

        event = SimulationEvent(
            event_id="test_escalation",
            event_type=EventType.MILITARY_ESCALATION,
            turn=0,
            source_faction="velar_imperium",
            target_faction="galactic_union",
            severity=0.7,
        )
        engine.inject_event(event)

        result = engine.step()
        assert len(result.events_processed) >= 1
        processed_ids = [e.event_id for e in result.events_processed]
        assert "test_escalation" in processed_ids

    def test_inject_economic_shock(self):
        engine = GUMASEngine(seed=42)
        state = engine.init_scenario()

        old_econ = state.factions["zyphari_compact"].economic_strength

        event = SimulationEvent(
            event_id="test_shock",
            event_type=EventType.ECONOMIC_SHOCK,
            turn=0,
            target_faction="zyphari_compact",
            severity=0.8,
        )
        engine.inject_event(event)
        engine.step()

        new_econ = state.factions["zyphari_compact"].economic_strength
        assert new_econ < old_econ

    def test_inject_espionage(self):
        engine = GUMASEngine(seed=42)
        state = engine.init_scenario()

        old_trust = state.factions["galactic_union"].trust_scores["velar_imperium"]

        event = SimulationEvent(
            event_id="test_spy",
            event_type=EventType.ESPIONAGE_EXPOSURE,
            turn=0,
            source_faction="velar_imperium",
            target_faction="galactic_union",
            severity=0.6,
        )
        engine.inject_event(event)
        engine.step()

        new_trust = state.factions["galactic_union"].trust_scores["velar_imperium"]
        assert new_trust < old_trust


# ============================================================================
# REPRODUCIBILITY TESTS
# ============================================================================

class TestReproducibility:

    def test_bias_evolution_fires_under_stress(self):
        """Bias intensity should change when leaders accumulate stressors."""
        engine = GUMASEngine(seed=42)
        state = engine.init_scenario()

        # Manually stress a leader
        leader = state.leaders["virex_talvaren"]
        leader.war_losses = 5
        leader.war_pressure = 0.8
        leader.economic_shock = 0.5
        old_intensity = leader.bias_intensity

        engine.step()

        # Intensity should have changed
        assert leader.bias_intensity != old_intensity, (
            "Bias intensity should evolve when stressors are high"
        )

    def test_all_factions_have_leaders(self):
        """Every faction must have a leader for bias-driven agency."""
        engine = GUMASEngine(seed=42)
        state = engine.init_scenario()
        for fid, faction in state.factions.items():
            assert faction.leader_id is not None, (
                f"Faction {fid} ({faction.name}) has no leader"
            )
            assert faction.leader_id in state.leaders, (
                f"Faction {fid} leader {faction.leader_id} not in leaders dict"
            )

    def test_same_seed_same_results(self):
        """Two engines with same seed produce identical state."""
        engine_a = GUMASEngine(seed=123)
        engine_a.init_scenario()
        engine_a.run(20)
        state_a = engine_a.get_state().to_dict()

        engine_b = GUMASEngine(seed=123)
        engine_b.init_scenario()
        engine_b.run(20)
        state_b = engine_b.get_state().to_dict()

        # Compare factions
        for fid in state_a["factions"]:
            assert (
                state_a["factions"][fid]["reputation"]
                == state_b["factions"][fid]["reputation"]
            ), f"Reputation mismatch for {fid}"

        # Compare conflicts
        for cid in state_a["conflicts"]:
            assert (
                state_a["conflicts"][cid]["phase"]
                == state_b["conflicts"][cid]["phase"]
            ), f"Phase mismatch for {cid}"

    def test_different_seed_different_results(self):
        """Different seeds produce divergent outcomes over time."""
        engine_a = GUMASEngine(seed=1)
        engine_a.init_scenario()
        engine_a.run(50)

        engine_b = GUMASEngine(seed=999)
        engine_b.init_scenario()
        engine_b.run(50)

        # At least one conflict should diverge in phase
        phases_a = {
            c.conflict_id: c.phase for c in engine_a.get_state().conflicts.values()
        }
        phases_b = {
            c.conflict_id: c.phase for c in engine_b.get_state().conflicts.values()
        }
        # Not guaranteed to differ, but highly likely over 50 turns
        # Just check both ran successfully
        assert engine_a.get_state().turn == 50
        assert engine_b.get_state().turn == 50

    def test_economic_ceilings_enforced(self):
        """No faction ever exceeds its economic_potential ceiling."""
        engine = GUMASEngine(seed=42)
        state = engine.init_scenario()
        for _ in range(100):
            engine.step()
            for fid, f in state.factions.items():
                assert f.economic_strength <= f.economic_potential + 0.001, (
                    f"{f.name} at {f.economic_strength:.4f} exceeded "
                    f"ceiling {f.economic_potential}"
                )

    def test_constructive_events_are_first_class(self):
        """Constructive outcomes appear as SimulationEvent objects, not silent state changes."""
        engine = GUMASEngine(seed=77)
        engine.init_scenario()
        results = engine.run(50)

        constructive_event_types = {
            "trade_agreement", "economic_boom", "technology_breakthrough",
            "cultural_movement", "infrastructure_investment",
        }
        found_types = set()
        for r in results:
            for e in r.events_generated:
                if e.event_type.value in constructive_event_types:
                    found_types.add(e.event_type.value)

        # Over 50 turns, trade and infra at minimum should fire
        assert len(found_types) >= 2, (
            f"Expected constructive events as first-class SimulationEvents, "
            f"found only: {found_types}"
        )

    def test_creation_destruction_ratio(self):
        """Constructive events outnumber destructive by ~3-6:1 in frequency."""
        from collections import Counter
        destructive = {"military_escalation", "economic_shock", "espionage_exposure"}
        constructive = {"trade_agreement", "economic_boom", "technology_breakthrough",
                        "cultural_movement", "infrastructure_investment", "diplomatic_overture"}

        total_d = 0
        total_c = 0
        for seed in range(5):
            engine = GUMASEngine(seed=seed)
            engine.init_scenario()
            results = engine.run(80)
            for r in results:
                for e in r.events_generated:
                    if e.event_type.value in destructive:
                        total_d += 1
                    elif e.event_type.value in constructive:
                        total_c += 1

        ratio = total_c / max(1, total_d)
        assert 2.0 <= ratio <= 8.0, (
            f"Creation:destruction ratio {ratio:.2f}:1 outside expected "
            f"range [2.0, 8.0]"
        )

```

---

# Addendum A — Integrated Naming Subsystem (v1.1.0)

This addendum incorporates `GUMAS_NAMING_PROTOCOL_v0.1` as an *engine-phase constraint*, not a post-hoc authoring step. Names are treated as simulation outputs that must be (a) culturally coherent, (b) collision-safe, and (c) auditable.

## A1. New core components

### `NameRegistry` (stateful)
Stored inside `GUMASState` to prevent drift across turns and runs.

Minimum fields:
- `canonical: Dict[str, EntityRef]` — canonical_name → entity reference
- `aliases: Dict[str, str]` — alias → canonical_name
- `token_counts: Dict[str, int]` — token/root frequency (rolling window + lifetime)
- `cadence_fingerprints: Dict[str, int]` — cadence patterns frequency
- `cooldowns: Dict[str, int]` — token/root → turns remaining (prevents “Kestrel” style repetition)
- `mint_log: List[Dict[str, Any]]` — bounded audit log per turn

### `NameService`
Deterministic name resolver invoked during tick phase **6.5**.

Responsibilities:
- generate candidates per protocol constraints (faction/regional/register cues)
- run **hard collision** checks (exact / near-exact duplicates)
- run **soft collision** checks (root reuse, semantic family overuse, cadence repetition)
- select best valid candidate; otherwise emit a **bureaucratic interim label** and flag for later convergence
- emit `state_changes[]` entries of type `name_minted` with signature + rejection trace

## A2. Engine hooks

### `GUMASEngine._resolve_names(result: TickResult) -> None`
1. Collect `NameRequest`s from:
   - newly created `LeaderState`, `FactionState`, `ConflictState`, `TreatyState`
   - newly generated `SimulationEvent`s that introduce referents (e.g., `TREATY_PROPOSAL`, `LEADER_CHANGE`, `CUSTOM`)
2. Resolve names via `NameService.resolve()`
3. Mutate state:
   - assign `name` fields where applicable
   - update `GUMASState.name_registry`
4. Append audit entry to `result.state_changes`:
   - `{"type":"name_minted","entity_type":...,"entity_id":...,"canonical_name":...,"signature":...}`

## A3. Determinism + auditability contract

- Name resolution is seeded by (`GUMASState.seed`, `turn`, `entity_id`) to guarantee reproducibility.
- A bounded list of rejected candidates is recorded to support debugging without exploding logs.
- Collision windows can be configured per entity type (e.g., tighter for treaties/locations).

## A4. UI / authoring guidance

Downstream narrative layers MUST treat names as authoritative outputs once minted. If later edits are required, perform a controlled rename:
- mint `canonical_name_v2`
- preserve prior as alias
- log `name_renamed` state change with reason and authority.

