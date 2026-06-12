# Orion Station — L1 Physical Configuration

**Status:** STAGING (recovered 2026-06-12; owner promotion pending)
**Provenance:** `projects/GUMAS_SIM_2.0/03_SIMULATION/Location_Data/Sim_Locations/`

`DATA__OrionStationPhysicalSpace__v1.0__2026-02-15.md` is the physical-space
mapping session (372 lines, multi-pass): hybrid rotating/non-rotating
architecture — habitat ring at 2 RPM providing ~0.3g (implied walking-deck
radius ~67 m from r = a/ω²), non-rotating zero-g core cylinder, 4 primary
docking bays + 8 auxiliary ports, the Dome (observation lounge, ring Deck 4,
270° windows). Coordinate frame: origin at core center of mass, +Z along
rotation axis.

Supporting L2/L3 surfaces from the same staging bay (2026-02-08):
- `L2_MAP__LOCATION_AUTHORITY_TABLE__v0.1` — which document is authoritative per location
- `L2_SYSTEM__GUMAS_L2_World_Bible__v0.2` — world-state substrate
- `L3_LOG__CONFLICT_MATRIX_GUMAS_StagingBay__v0.2` — recorded contradictions
- `L3_QUEUE__PROMOTION_QUEUE_GUMAS_StagingBay__v0.2` — what was awaiting promotion when work paused

Cross-references: the library set in `../operational_library_v2_2/`
(STATION_OVERVIEW, SYSTEMS_BIBLE) and the CloudBank dossier surfaces
(`simulation/ORION_STATION_MASTER_DOSSIER_v2.6.md`,
`ORION_STATION_TECHNICAL_REGISTER_v2.6.json`) are the comparison baseline
for promoting these physical parameters to CANON.
