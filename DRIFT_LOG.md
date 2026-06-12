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
