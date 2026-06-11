---
entity_id: ORION.ROLE.PILOT
entity_type: station_architecture
layer: L1
certainty: CANON
owner_ruled: "2026-06-11"
doc_sources:
  - "Owner definitional ruling, 2026-06-11 session"
  - "canon/L1/station/mesh_transcripts/ (legacy alias evidence)"
---

# Pilot — the User-Interface Role

**Owner ruling (2026-06-11):** the human user's role in all Aurora / Orion
Station interfaces is **Pilot**. The term was specifically chosen for the
user interface.

## Command distinction

- **Pilot** — the human at the interface. Speaks to the station and its
  crew; is not a crew seat and holds no station command.
- **Commander Alex Thorne** (`ORION.ENTITY.0001`) — commands Orion Station.
  Station command authority is Thorne's, under Aurora's arbitration
  (`aurora_core`: "all major actions require Aurora arbitration and ethics
  validation").

## Legacy alias: "Captain"

In early conversations Aurora addressed the user as **Captain**; that alias
is preserved verbatim in the primary-source transcripts
(`sender_name: "Captain"`, channel `private:captain:alex`) and in runtime
identifiers descending from that era. Treat "Captain" in historical
material as referring to the Pilot. Historical channel identifiers are NOT
renamed (primary sources stay verbatim; runtime channel ids are stable
contracts) — new surfaces use Pilot.

## Runtime alignment

CloudBank mesh defaults (`MeshMessageRequest.sender_id/sender_name`) adopt
`pilot`/`Pilot`; `captain`/`Captain` remain accepted legacy aliases in
routing for back-compatibility with historical channels and transcripts.
