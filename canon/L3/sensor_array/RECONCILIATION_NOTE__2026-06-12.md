# Sensor Array v0.3.0 — Canon Reconciliation Note

- **Routed:** 2026-06-12, per the delta's own instruction ("STAGING — route
  through aurora-canon-reconciler before CANON_PROMOTE").
- **Certainty:** **STAGING** (held at the artifact's self-declared tag; owner
  may promote after the RQ-3 calibration items mature).
- **Layer:** L3 protocol_update — governs L1/L2/L3 observation; introduces no
  L2→L1 entity mapping; one-way observation principle preserved (sensors
  acquire no actuation path).
- **Identity:** v0.2.0 sha256:13fe465edcefa6e3 → v0.3.0 sha256:bd9017ebb5ed10ac
  (per artifact header). Source files registered at workspace root by the
  2026-06-11 manifest scan; canonical copies live here.

## Integration-surface grounding (verified against CloudBank main, 2026-06-12)

| Spec claim | Verified |
|---|---|
| `src/monitoring/drift_detector.py` exists | ✓ |
| `src/monitoring/ethics_engine.py` exists | ✓ |
| `src/bridges/l2_meta_agent_bridge.py` exists | ✓ |
| `.aurora/relays/` live relay capsules exist | ✓ (ARCHY/LIORA/OPPY/…) |
| `src/sensors/` greenfield | ✓ (does not exist yet — clean build surface) |
| `core/phase_executor.py` (Forge refactor) | **✗ unmerged anywhere in the workspace** — the spec's own "merge status to verify" hedge resolves to NOT MERGED. **Phases 1–6 are unblocked; Phase 7 (tick-lifecycle integration) depends on the Forge refactor landing first.** |

## Relationship to existing observability

The control plane already operates desk-level sensors (workspace verifier,
landing ledger, flight log, scorecard, canon/skill propagation checks); the
drift metrics API and autonomous drift responder (#985) cover runtime drift
reaction. The Sensor Array is the missing third tier: continuous in-runtime
observation with layered interpretation and fusion — and its one-way
observation principle mirrors the control plane's detect-don't-act posture.

## Addendum — Salvage Operations Doctrine (same day)

`canon/L1/station/SPEC__SALVAGE_OPERATIONS__v0_1_0.md` routed at STAGING per
its own status header. L1 doctrine expressing the control plane's recovery
mission ("survey the debris field… answer every beacon; nothing is scuttled
by survey; the registry decision belongs to the gatekeeper"), extending the
Sensor Array's external family. Companion surfaces verified live:
`tools/aurora_salvage_scan.py` (root), `src/sensors/external/salvage.py`
(CloudBank PR #1005), salvage report JSON as the interface between them.
