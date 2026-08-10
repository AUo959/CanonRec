# L2 Route Registry — v0.1

**Certainty: STAGING** (structure ratified in scope; named routes pending evidence)
**Created:** 2026-08-09, to make FABRIC P4 enforceable and satisfiable.

## Why this exists

P4 (RULING-ENGINE-P4) gates canon promotion: a record citing a movement or
cross-region event must cite a canonical route or drive. When the check was first
wired into `aurora-canon-reconciler` it was implemented as a hard BLOCK — and canon
contained **no route, corridor, lane or drive entity to cite**. Every movement event
became permanently unpromotable with no compliant action available.

That is a defect, not a gate. An exit condition nobody can meet is the same failure
shape as a task whose completion criterion is "owner review before X": it can never
close. This registry, plus the exemption mechanism below, is the fix.

## Current state of routes in canon

Canon establishes **movements between named places**, but has never named a corridor.

| Referent | Status | Notes |
|---|---|---|
| Hollow Expanse | CANON (placement STAGING) | Typed `region / lawless corridor`; shadow-logistics function, precursor-linked. The one corridor-typed entity in canon. |
| "Galactic Union trade routes" | Attested, unnamed | Referenced as the target of Omega-Veil's raids (Operation Obsidian Dawn briefing). A class of routes, not a named route. |
| "Outer Colony trade routes" | Attested, unnamed | Referenced in `virex_talvaren` recent_actions (covert destabilization). |
| Kharis Sector ↔ Lethan system transits | Endpoints CANON, corridor unnamed | Shadow Fleet operated through Kharis and withdrew from Lethan. Both places are canon; the corridor between them is not named anywhere. |

**No named route entity has been minted.** Naming one would create an L2 referent with
no source, which the L2 Naming Admission gate exists to prevent. Route names must come
from NameService or a recovered source, not from a validator's convenience.

## How P4 is satisfied

A record promoted to canon that cites a movement/cross-region event must **answer the
route question**. It may do so in either of two ways:

1. **Cite a route** — `route_ref`, `route_citation`, `route_id`, `drive_ref`,
   `transit_route`, or similar, pointing at a canonical route entity.
2. **Record an explicit exemption** — `route_exemption`, stating that no canonical
   route is established, listing the **canonical endpoints that do define the transit**,
   the basis, why a name was not invented, and what would resolve it.

The gate requires the question to be *answered*, not that an answer be *fabricated*.
This mirrors two conventions already in the project: `naming_exemption` for referents
that predate the naming gate, and `canonical_position_status: unplaced` as a placement
*fact* rather than a certainty hedge.

### Records currently carrying a route exemption

- `event_dark_star_incident_4718_224` — endpoints: Kharis Sector, Lethan system, Kallis Foundry.
- `fleet_shadow_fleet` — endpoints: Kharis Sector, Lethan system. Note recorded that the
  Hollow Expanse would be a *plausible* citation (a lawless corridor used for shadow
  logistics) but canon establishes **no link** between it and the Shadow Fleet, so citing
  it would be inference presented as fact.

## Enforcement

`aurora-canon-reconciler` (`validate_entity.py`) self-activates P4: it reports
`FABRIC_P4_NO_ROUTE_REGISTRY` as a WARN while no route registry exists, and escalates to
a BLOCK once one does. As of 2026-08-09 the Hollow Expanse satisfies the registry test,
so **P4 is live and blocking**.

## Next

Named routes should be established from evidence — the Kharis transit corridor, the Union
trade-route network, and the Velar Crescent approaches are all attested as *activity*
without names. Route them through NameService (candidate generation + collision check +
receipt) rather than minting names here.
