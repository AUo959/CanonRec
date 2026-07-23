# L2 GUMAS Ship-Class Registry Addendum — Judicator Escort and Logistics Classes

**Layer:** L2  
**Date:** 2026-07-21  
**Status:** CANON  
**Authority:** Direct owner ruling  
**Related formation:** `org_judicator_prime_task_group`

This addendum extends the landed L2 ship-class registry without reformatting or rewriting the large legacy registry file.

## Added classes

| Entity ID | Class ID | Name | Division | Core role | Certainty |
|---|---|---|---|---|---|
| `cls_vigilant` | `CLASS-VIGILANT-01` | Vigilant-Class | escort_destroyer | General-purpose medium fleet escort, screening, interception, picket, convoy protection, patrol, and rescue | CANON |
| `cls_sustainer` | `CLASS-SUSTAINER-01` | Sustainer-Class | fleet_bulker | Dedicated fuel, stores, feedstock, ordnance, parts, and high-volume task-group replenishment | CANON |

## Registry-schema extension

The legacy registry schema enumerated `stealth_destroyer` and `logistics` but did not include the more precise divisions created by this owner ruling.

The following division values are therefore admitted:

- `escort_destroyer`
- `fleet_bulker`

These values refine rather than invalidate the older categories:

- Vigilant is distinct from the `stealth_destroyer` Obsidian-Class.
- Sustainer is a specialized bulk-replenishment class distinct from the broader `logistics` Reliant-Class.

## Judicator task-group bindings

- `JPTG-ESCORT-01` → `cls_vigilant`
- `JPTG-ESCORT-02` → `cls_vigilant`
- `JPTG-LOGISTICS-01` → `cls_sustainer`

Individual vessels and commanding officers remain open pending separate admission.

## Technical-certainty boundary

The class records contain owner-approved canonical roles and capability families. Exact dimensions, complements, weapon counts, drive architecture, cargo capacity, transfer performance, and embarked-craft counts remain `STAGING` until reviewed and promoted.

## Authoritative records

- `canon/L2/entities/ship_classes/cls_vigilant.json`
- `canon/L2/entities/ship_classes/cls_sustainer.json`
- `canon/L2/entities/organizations/org_judicator_prime_task_group.json`
- `canon/L2/operations/GUMAS_L2__DOCTRINE__JUDICATOR_PRIME_STANDING_ESCORT_GROUP__v1.1__2026-07-21.md`
