# SNPM (Scalable Narrative Probability Model) — Canon Reconciliation Note

- **Routed:** 2026-07-10 (Cowork salvage sweep). Recovered from archive-only
  material during a review of early-generation Aurora v2.2.6b bundles.
- **Certainty:** **STAGING** — held pending owner review. Route through
  `aurora-canon-reconciler` before `CANON_PROMOTE`. Not silently promoted.
- **Layer:** L2 mechanics (galaxy-scale narrative-plausibility simulation).
- **Artifact:** `SNPM_Scalable_Narrative_Probability_Model__v1.0.json`
  (byte-identical to the archive source, sha256
  `4c43699b5b1be4fa6bc80c5e599db34754418f2c3d59fa7f0c1bc273b0cc5776`).

## Provenance

- **Source (archive-only):**
  `archives/unzipped/Unzipped Archives/Archy_Continuity_Thread_v1.0/Aurora_v2.2.6b_LIVE_EXPORT.zip`
  → `GUMAS+AUR Dev File Archive /SNPM_Scalable_Narrative_Model 2.json`
  (also present in the parallel `GUMAS+AUR Dev File Archive` v2.2.6b bundles).
- **Prior landing:** none. A 2026-07-10 sweep confirmed the model existed only
  inside archive zips — it was in no live repo (root, CloudBank, CanonRec) and
  is not referenced by the current narrative-engine work.

## Why it is genuine (not a duplicate)

The surrounding galactic-union worldbuilding from the same v2.2.6b bundle is
already canonized in CanonRec L2 (character roster, mechanics-and-models, the
simulation math framework, timeline, organizations). **SNPM is not.** A concept
sweep across all of `canon/L2/` for SNPM's five mechanics —
Character Encounter Likelihood, Narrative Cluster Partitioning, Memory Echo
Range Limiter, Rare Character Trigger, Timeline Staggering — returned **zero
matches**. So SNPM is a distinct, unrecovered simulation mechanic, not a
restatement of the landed math framework.

## What SNPM specifies

A model for galaxy-scale narrative fidelity that limits implausible character
interactions, via five components:

| Component | Role | Source status tag |
|---|---|---|
| Character Encounter Likelihood Engine | Probability of interaction by distance / faction transit / memory pathways | In Development |
| Narrative Cluster Partitioning | Location-anchored character clusters (Core Worlds, Outer Colonies) | Testing |
| Memory Echo Range Limiter | Restricts indirect memory propagation without a justifying network/event/lag | Integrated |
| Rare Character Trigger System | Central-character involvement gated on high tension / multi-thread convergence | Policy Design Finalized |
| Timeline Staggering for Interactions | Spatial-temporal delays (travel time, signal lag) to avoid real-time implausibility | Queued for Deployment |

## Relationship to the narrative engine (design corpus)

SNPM is **complementary** to the recovered narrative-engine spec
(`docs/ORION__SPEC__NARRATIVE_ENGINE__PARAMETERS_TO_NARRATIVE_CORE__v0.1…`):
the narrative engine adjudicates *whether a proposed event is continuity-valid*;
SNPM governs *whether a character interaction is spatially/temporally plausible
at galaxy scale*. If promoted, SNPM's likelihood/cluster/lag constraints are a
natural input to the engine's next-event continuity gating (the suspended task
`narrative-promotion-continuation-2026-06`, items 4–7).

## Caveat

The artifact's `governance` block (lead "Alex Thorne"; engineers; "Original
Expert Panel + Project Lead Approval") is **in-fiction metadata**, not a real
approval record. It does not constitute owner sign-off; canon promotion still
requires the actual owner via the canon-reconciler flow.

## Next gate

- Owner review; if accepted, `aurora-canon-reconciler` packet → `CANON_PROMOTE`.
- On promotion, cross-link into `03_galactic_union_mechanics_and_models.md` and
  note the narrative-engine input relationship above.
