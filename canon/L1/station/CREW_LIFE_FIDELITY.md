---
entity_id: "ORION.STATION.OPS.CREW_LIFE"
entity_type: "doctrine"
layer: "L1"
name: "Crew-Life Fidelity — the Human Layer of Orion Station"
certainty: "CANON"
registry_authority: "owner_ruling"
ruled_at: "2026-06-13"
doc_sources:
  - "Owner ruling (the Pilot), 2026-06-13: 'if we're not simulating eating and going to the bathroom, then we're not running a high fidelity simulation'"
  - "reference_sources/orion_station_life_infrastructure.md (THE RHYTHM OF STATION LIFE; WATER/FOOD/HYGIENE SYSTEMS)"
  - "reference_sources/orion_station_technical_addendum_equipment_and_personnel.md (Carmen Rivas post-shift routine)"
  - "tools/crew_life.py; catalog/crew_life_model.json; first crewed live watch 2026-06-13"
---

# Crew-Life Fidelity — the Human Layer of Orion Station

The crew are people, not task-executors. High fidelity requires simulating
that they sleep, eat, shower, use the head, take recreation, and tire — and
that the station must physically sustain them. This was already iterated in
canon (the life-infrastructure doc: Alpha/Bravo/Charlie/Delta shifts, 3-minute
showers, galley meal service, vacuum toilets into the 98% water loop, quiet
hours, the Carmen Rivas post-shift routine). It is now **simulated**, not just
described.

## What is modeled (`tools/crew_life.py`, `catalog/crew_life_model.json`)

Per crew member, per station-hour, exactly one activity —
`on_shift | asleep | meal | hygiene | recreation | personal` — on the
canonical four-shift rotation:

| Shift | Watch | Manning | Sleeps |
|---|---|---|---|
| Alpha | 06:00–14:00 | primary | 22:00–05:00 |
| Bravo | 14:00–22:00 | full | 05:00–12:00 |
| Charlie | 22:00–02:00 | skeleton | 14:00–21:00 |
| Delta | 02:00–06:00 | minimum | 18:00–01:00 |

Tracked needs: sleep-debt (real circadian fatigue, recovered by sleeping),
hunger (reset at the three meal services; crew eat at post during the lunch
overlap, so on-shift crew don't starve), hygiene (daily shower rotation),
morale (recreation), and bathroom events. **Life-support load** is the
consequence the station must meet: water drawn vs recycled through the 98%
loop, galley portions, and the CO₂/O₂ the scrubbers handle — the
life-support tasks on the watch board (scrubber rotation, hydroponics, galley
resupply) exist because real people consume real consumables.

## The consequence (it is not decoration)

In a crewed watch, **only on-shift, awake crew work** — the rest are asleep,
at meals, or off — and a tired crew member's sleep-debt fatigue slows their
work. A four-hour morning watch runs the Alpha shift (~14 on duty) while the
other ~21 rest; a skeleton night watch has far fewer hands, which changes how
much the engine gets serviced and therefore how the simulated galaxy behaves.
The human layer feeds straight back into the L2 payload.

## Reality guardrail and an open reconciliation

The station operates as if literally on station, so the crew's biology is a
hard constraint, not flavor. One honesty item is logged rather than papered
over: the life-infrastructure rhythm uses a **24-hour** clock (Alpha at 06:00,
etc.), while the environment packet records a **22.1-hour station day**. The
model treats an hour as a station-hour on the canonical rhythm and flags the
discrepancy; promotion of the environment packet must reconcile the
day-length datum (see STATION_PURPOSE_DEFINITION and the crew_life_model
`_clock_note`).
