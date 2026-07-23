# L2 Identity Dimensions — v0.1 (2026-07-21)

**Purpose:** keep the axes of identity **orthogonal** in canon records. A political
entity does not inherently describe a whole people. Species, culture, state, and place are
separable and must not be collapsed into one another.

## The four orthogonal dimensions

1. **Species / people** (`entity_kind: species`) — a biological people with a broad cultural
   origin. Members may hold *any* citizenship, faction, or ideology. A species is **not**
   bounded by a polity. Fields: `origin_polity_id` (where it arose, if any — nullable),
   `member_polities` (non-exhaustive), `distribution` (prose, membership spread).
2. **Polity / state** (`entity_kind: polity`, factions, organizations) — a government or
   political structure. It **describes a state, not a people.** Fields: `founding_species_id`
   or `dominant_species_id`, `multispecies` (bool), `peoplehood_note`. A polity may be
   multispecies, and its founding species almost always extends beyond it.
3. **Culture / heritage** — a tradition, which may outlive or cross states. Recorded as a
   `cultural_note` where it matters. Example: **Velari** heritage persists across the Velar
   Imperium, the Republican Reformists, and Union-aligned worlds alike.
4. **Region / place** (`entity_kind: location`, map zones) — physical geography, governed by
   the map source-of-truth. Independent of who currently holds it.

## Anti-flattening rules

- **Do not equate a polity with a people.** "The Velar Imperium" ≠ "the Velari." "The Harkon
  Sovereignty" ≠ "the Harkoni." The state is one expression of a people, often contested and
  never total.
- **Species membership is many-to-many with polities.** Humans span the Union, the
  Separatist Confederation, and PMCs. Velari span the Imperium, the reformists, and the
  Union. Xenon span the Union and the Zyphari trade sphere.
- **A polity's citizenry may exceed its dominant species.** The **Nythran Ascendancy** is a
  polity of *two peoples* — organic Nythrans and AI intelligences as co-equal citizens. The
  **Zyphari Compact** is explicitly multispecies.
- **Character records keep `faction_id`/`faction_bindings` (allegiance) separate from
  species** (recorded in capsule knowledge / notes). Zylox is Xenon *and* leads the Galactic
  Union; those are independent facts. Never write a species token into `faction_bindings`.
- **Culture crosses state lines.** The canonical precedent is Vel-Surak (2026-07-21):
  Velari *heritage*, Union *jurisdiction* — the name is cultural, the sovereignty is not.

## Applied corrections (this pass)

- Species records: dropped the single `primary_polity_id`; added `origin_polity_id` +
  `member_polities` (plural) + `distribution`. `species_human` and `species_velari` explicitly
  span multiple polities.
- Polity records: dropped the `species` field (which implied polity == people); added
  `founding_species_id`/`dominant_species_id` + `multispecies` + `peoplehood_note`. Nythran
  Ascendancy marked as a two-peoples (organic + AI) citizenry.

**Certainty: STAGING** (modeling principle; owner may ratify to CANON). Future salvage passes
and the reconciler should honor these dimensions rather than re-collapse them.
