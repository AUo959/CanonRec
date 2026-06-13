# L2 Social Dynamics — the galaxy's societies, not just its governments

**Established:** 2026-06-13 (owner direction: "include social dynamics across
the galaxy"). The L2 simulation is more than faction diplomacy and fleets —
populations have cohesion, sentiment, grievances, and cultural movements that
drive change without war. This is the canonical home for those mechanics,
promoted from the recovered design drafts (`draft_logic/recovered/`).

## What's here

- **`non_war_progression_mechanics.md`** — the core social-dynamics frame:
  - **Diplomatic Stability Index (DSI)** — each polity has a stability rating;
    enough internal/external pressure fractures it or escalates to conflict.
  - **Social cohesion (S)** as a stability component; over-high control (C) or
    militarism (M) raises instability (authoritarianism/adventurism).
  - **`P_stability = E + T − C`** (economy + technology − control/conflict).
  - Cultural movements & social shifts with galaxy-wide effects; governments
    shift from cultural/economic/social pressure, not only war; cultural power
    as a soft weapon.
- **`galactic_union_state_variables.md`** — social state variables:
  **Public Sentiment** (shifts toward war/peace factions), **Union Popular
  Sentiment** (approval fluctuations), mixed-loyalty mercenary forces.
- **`galactic_union_simulation_math_framework.md`** — the broader state/math.
- **`simulation_expansion_systems_outline.md`** — expansion systems incl.
  economic/cultural/scientific progression paths.

## How this binds to the engine and the mechanics registry

These social signals feed the **rebellion/insurgency** dynamics (FORGE
`rebellion.py`: `economic_grievance`, `political_grievance`, `ethnic_grievance`,
`popular_support`, onset = demographic stress + low legitimacy) and the
**political-support / loyalty** formulas in
`../mechanics/03_galactic_union_mechanics_and_models.md`:

```
P(support)        = ideological_alignment + political_ambition − risk_assessment
political_loyalty = ideological_alignment − past_betrayals + personal_relationships
P_stability       = E + T − C
```

**MECH-SOC-001 (Population Grievance Memory)** applies the MECH-GOV-001 memory
substrate to populations: grievances (repression, hardship, broken promises)
are remembered with slow decay and raise insurgency odds; relief and autonomy
lower them — making instability *path-dependent* (history matters), the axis
the seed-42 runaway actually turns on. Implemented in `tools/mech_gov_001.py`
+ wired via `tools/gumas_memory_run.py`.

## Emergence note

These mechanics constrain but do not script: a polity's social trajectory
emerges from its actual event history (what its people lived through), and any
coherent, non-conflicting emergent social detail is admissible.
