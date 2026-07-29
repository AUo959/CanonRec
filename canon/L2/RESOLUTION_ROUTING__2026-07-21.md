# L2 Open-Item Resolution Routing — 2026-07-21

**Purpose:** correct a process error. Earlier passes stacked resolvable details as "owner
decisions" (e.g. picking map coordinates). That is wrong — GUMAS has **deterministic
processes** for these. This note routes each open item to its process. The owner is the
*gate* for promotion, not the mechanism for generating values.

| Open item | WRONG framing | Correct process (route here) |
|---|---|---|
| Placement of unplaced canonical locations (Teraxis Prime, the Expanses, Dyson Twin Systems, Velar Ruin/Outer anchors, macro-zones) | "owner chooses coordinates on the map" | **Reconciliation Workflow** (reference packet §4.5, "how evidence becomes placement") + **Claim Ledger** (§4.6, evidence store). Placement is *derived from evidence*, map-primacy adjudicated, recorded as a claim — not eyeballed. Locations stay `unplaced` until evidence resolves them. |
| Names for pending referents (e.g. vessel_gu_015 ship name, VEL-CORE/BORDER system names) | "owner invents a name" | **NameService / L2 Naming Admission Protocol** — deterministic candidate generation against the registry, collision-checked, receipted. Human *selection* among generated candidates is optional, not authoring. |
| Conflict dynamics, treaty formation, war outcomes | "record what happened / owner decides" | **The engine.** These are per-run tertiary/instance-local state (Canon Protocol §5). Only the *scenario-defined* canonical fixtures are canon (see the 3 conflict records this pass); run outputs are never promoted wholesale. |
| UNCONFIRMED affirmations (Haden Korr, Iskar Veyr, Vaxtan Rhel, Shroudborn) | "owner ratifies from nothing" | **Await a source-of-truth artifact** OR the reconciler's certainty advisor. These are generative/myth-only by construction; they rise to STAGING only when evidence appears, not by fiat. |
| Certainty promotion STAGING→CANON | (correct as owner gate) | **aurora-canon-reconciler** conflict scan + owner gate at commit. This one *is* an owner decision, but a scanned/receipted one (see the 50-record major promotion). |
| Capsule state-vector defect (anaya state.bin 0 bytes) | "owner fixes" | **Capsule rebuild tooling** (deterministic charforge rebuild) — a mechanical repair, queued as `anaya-capsule-state-defect`, not a judgement call. |

## What genuinely remains an owner gate

Only the **promotion gate** itself: approving that a reconciled, conflict-free record moves
to CANON. Everything above *feeds* that gate through a process; the owner does not hand-author
coordinates, names, or simulation outcomes.

## This pass's authoritative-source audit (why coverage is now trustworthy)

Rather than diff against documents, this pass diffed canon against the two **ground-truth**
sources:

1. **Engine runtime roster** (`SIM_ENGINE_OUTPUTS`): all **21 instantiated leaders** are
   recorded; all **13 factions** are recorded. The **3 scenario conflicts** ("canonical
   tension points") are now recorded (`conflict_*`); the 5 run **treaties** are correctly
   *excluded* as instance-local tertiary state.
2. **Formal 2026-03-13 promotion-candidate set** (`_staging/recovered_textAu/.../promotion_*`):
   all 10 characters + 6 polities landed (under normalized canonical_ids; the old
   `CHAR-GU-*`/`POL-*` scheme maps 1:1 to current records — verified via `canonical_name`).

Both authoritative sources come back **fully covered**. That is a stronger completeness
signal than any prose sweep.
