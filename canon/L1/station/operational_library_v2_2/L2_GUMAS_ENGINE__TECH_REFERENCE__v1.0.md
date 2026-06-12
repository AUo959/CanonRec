---
title: L2 GUMAS Engine — Technical Reference
doc_id: ORION.TOOL.GUMASENGINE.0001
doc_type: reference
version: 1.0.0
last_updated: 2026-02-07
authority: primary
layer: L2
domain: tooling
tags:
  - l2
  - gumas
  - engine
  - python
  - simulation
summary: "Operational + architectural reference for the Python GUMAS engine package."
related_docs:
  - ORION.LOG.CONFLICTS.0001
  - ORION.LOG.DRIFT.0001
  - ORION.LOG.PROMOTION.0001
audience: dev
topic_type: Reference
---

# L2 GUMAS Engine — Technical Reference (v1.0.0)

**Anchor seed:** `EOS_SEED_ORION`  
**Ethics protocol:** `Picard_Delta_3`  
**Timestamp (UTC-05):** 2026-02-07 16:29 UTC-05

## What this is
A deterministic, turn-based simulation engine that advances a `GUMASState` through:
- conflict escalation/de-escalation
- diplomacy + treaties
- espionage and intelligence shocks
- economic shifts
- leader bias evolution + reputation decay
- emergent event generation

## Package layout (clean)
- `modules/gumas/engine.py` — `GUMASEngine` (runtime)
- `modules/gumas/models.py` — enums + dataclasses (state model)
- `modules/gumas/scenarios.py` — canonical scenario builder
- `modules/gumas/formulas.py` — documented formulas (tested)
- `tests/test_gumas_engine.py` — pytest suite (**44 passed**)

## Quickstart (dev)
```python
from modules.gumas.engine import GUMASEngine

engine = GUMASEngine(seed=42)
engine.init_scenario()            # loads canonical scenario
ticks = engine.run(n_turns=10)    # list[TickResult]
print(ticks[-1].to_dict())
```

## Public API surface
- `GUMASEngine(seed=42, anchor="EOS_SEED_ORION")`
- `build_default_scenario(scenario_id="gumas_canonical_v1", seed=42)`

### Event types
The engine supports the following `EventType` values:
- `military_escalation`
- `diplomatic_overture`
- `espionage_exposure`
- `economic_shock`
- `leader_change`
- `treaty_proposal`
- `treaty_violation`
- `intelligence_leak`
- `humanitarian_crisis`
- `technology_breakthrough`
- `cultural_movement`
- `internal_coup`
- `mediation_offer`
- `trade_agreement`
- `economic_boom`
- `infrastructure_investment`
- `custom`

### Documented formulas (tested)
- `calc_deescalation_probability()` — Calculate de-escalation probability for a conflict.
- `calc_bias_evolution()` — Calculate new bias intensity after an event.
- `calc_treaty_breach_score()` — Calculate breach score for a potential treaty violation.
- `is_treaty_breach()` — Determine if breach_score exceeds the violation threshold.
- `calc_reputation_after_decay()` — Calculate reputation after time-based decay of breach penalties.
- `calc_double_agent_risk()` — Calculate probability of double-agent presence in intelligence sharing.
- `calc_trust_update()` — Update bilateral trust score.
- `apply_bias_hooks()` — Calculate effective bias hook values for a leader.

## Determinism + reproducibility
- The engine is seed-driven. Given the same seed and same injected events, you should get the same sequence of results.
- Use `export_state(path=..., include_history=True)` to persist a run for audit / replay.

## Integration notes (from intake)
- A staging archive contained duplicate code variants; the resolved package **prefers the outputs/gumas_engine variant** because it aligns with the test suite and includes the constructive event expansion. See **ORION.LOG.CONFLICTS.0001** and **ORION.LOG.DRIFT.0001**.

---
Built for consistency, clarity, and care.
