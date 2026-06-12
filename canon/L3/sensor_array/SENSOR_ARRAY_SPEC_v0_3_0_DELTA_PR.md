# PR: Sensor Array Specification v0.2.0 → v0.3.0

**Type:** Specification revision (delta)  
**Target file:** `SENSOR_ARRAY_SPECIFICATION_v0_3_0.md` (supersedes v0.2.0)  
**Anchors:** EOS_SEED_ORION, Picard_Delta_3  
**DLP:** sensor_array_specification_v3  
**Artifact identity:** v0.2.0 (encoding-repaired) sha256:13fe465edcefa6e3 → v0.3.0 sha256:bd9017ebb5ed10ac  
**Status:** STAGING — route through aurora-canon-reconciler before CANON_PROMOTE  
**Layer classification:** L3 protocol_update (spec governs L1/L2/L3 observation; no L2→L1 entity mapping introduced)

-----

## Summary

v0.3.0 is a full revision across four areas: (A) integration-depth-weighted drift detection extracted from Lotus Protocol §IV; (B) closure of all four v0.2.0 open questions; (C) binding of the sensor array to the GUMAS v2.0 15-phase tick lifecycle, Convergence Regulator, and AFS; (D) alignment of integration points with CloudBank repository v2.1.0 (post-Forge module layout). All v0.2.0 sensor definitions and fusion subsystems carry forward unchanged unless listed in Modified Sections.

The one-way observation principle is preserved and strengthened in every addition: sensors gain new taps and weighting logic but acquire no actuation path.

-----

## Motivation

**A — Drift weighting.** v0.2.0 treated all pre-signatures equally, deferring false-positive control entirely to threshold tuning (its own open question #3). Lotus §IV supplies a structural answer: weight by integration depth. High-depth connection loss is rupture and must never wait on trend confirmation; periphery noise should be damped structurally, not by global threshold inflation.

**B — Open questions.** Four unresolved questions blocked Phases 3–6 of the v0.2.0 implementation plan from being executed with confidence. Each now has a concrete, governed resolution (RQ-1 through RQ-4).

**C — GUMAS/AFS binding.** v0.2.0 said “per tick” without defining where in the 15-phase lifecycle sampling occurs, how the ethics_callback is observed, or how sensor forecasting relates to AFS. Unbound, the spec risked duplicate forecasting infrastructure and observer-feedback loops with the Convergence Regulator.

**D — Repo alignment.** The Forge refactor (phase_executor, handler_registry, SimulationSubsystem.validate_state) and live relay capsules in `.aurora/relays/` changed the correct integration surfaces. Also resolves a latent unit-conflation hazard between drift Δ and ethics deviation fractions.

-----

## Source Basis (certainty tags)

|Claim                                                 |Tag       |Source                                                              |
|------------------------------------------------------|----------|--------------------------------------------------------------------|
|Integration depth definition                          |FACT      |lotus_whitepaper.docx §IV                                           |
|SII formula, thresholds (0.8/0.2, 10%/hr)             |INFERENCE |This spec’s proposal; requires RQ-3 calibration                     |
|15-phase lifecycle, ethics_callback hook, 33 handlers |FACT      |GUMAS_DEEP_PARSE_REPORT_v1                                          |
|PhaseRegistry / SimulationSubsystem.validate_state    |FACT      |GUMAS_FORGE_MODE_REPORT_v1 (refactor design; merge status to verify)|
|Convergence Regulator implemented                     |FACT      |Project canon (GUMAS v2.0)                                          |
|AFS components 2/5/6, 87 tests                        |FACT      |PK_04__FORECAST_SYSTEM_SPEC                                         |
|EthicsEngine levels 0.2/0.5/0.8 + 5 actions           |FACT      |AURORA_COMPREHENSIVE_REFERENCE                                      |
|AFS↔sensor harness reuse                              |INFERENCE |Reuse proposal                                                      |
|Decimation N=5, 10% tick budget, 24h quarantine review|ASSUMPTION|Initial values; tune via RQ-3                                       |

-----

## New Sections (full text as merged)

### Integration-Depth-Weighted Drift Detection (NEW in v0.3.0)

**Purpose:** Weight drift pre-signature alerts by how load-bearing the affected Symbol is. A high-integration Symbol losing connections is structurally different from peripheral noise — it is rupture, not drift — and must escalate immediately rather than waiting on trend analysis.

**Source basis:** Engineering extraction of Lotus Protocol §IV (“Integration Depth”). The whitepaper claim — *integration depth is the measure of how many other Symbols would have to change if this one disappeared* — is treated here as a computable graph metric, not a metaphor. [FACT: lotus_whitepaper.docx §IV; INFERENCE: the specific formula and thresholds below are this spec’s proposal and require calibration]

**Symbol Integration Index (SII):**

```python
@dataclass
class IntegrationDepthReading:
    """Snapshot of integration depth across the symbol graph."""
    timestamp: datetime
    symbol_count: int

    # Per-symbol depth, normalized 0-1 within current graph
    depths: Dict[str, float]            # symbol_id -> depth

    # Distribution summary
    core_symbols: List[str]             # depth >= 0.8 (load-bearing)
    peripheral_symbols: List[str]       # depth < 0.2 (unintegrated)
    median_depth: float

    # Stability
    depth_deltas_1h: Dict[str, float]   # symbol_id -> depth change in window
    rupture_candidates: List[str]       # core symbols with rapid connection loss


class SymbolIntegrationIndex:
    """
    Maintains the symbol reference graph and computes integration depth.
    Sources edges from: concept tag co-occurrence (ConceptResonanceDetector
    tag_registry), anchor reference chains, and relay capsule dependencies.
    Stdlib-only; no ML required.
    """

    CORE_THRESHOLD = 0.8
    PERIPHERY_THRESHOLD = 0.2

    def __init__(self):
        self.edges = defaultdict(set)       # symbol_id -> set(dependent_ids)
        self.depth_history = RollingWindow(3600)

    def record_reference(self, symbol_id: str, referenced_by: str) -> None:
        self.edges[symbol_id].add(referenced_by)

    def depth(self, symbol_id: str) -> float:
        """Normalized integration depth: weighted dependent count.
        Direct dependents weight 1.0; transitive dependents (1 hop) weight 0.3.
        Normalized against the max raw depth in the current graph."""
        raw = self._raw_depth(symbol_id)
        max_raw = max((self._raw_depth(s) for s in self.edges), default=1.0)
        return raw / max(max_raw, 1.0)

    def _raw_depth(self, symbol_id: str) -> float:
        direct = self.edges.get(symbol_id, set())
        transitive = set()
        for d in direct:
            transitive |= self.edges.get(d, set())
        transitive -= direct
        return len(direct) + 0.3 * len(transitive)
```

**Weighted pre-signatures:** `DriftPreSignatureMonitor` is extended so every `PreSignature` carries a depth weight and a derived priority:

```python
@dataclass
class WeightedPreSignature(PreSignature):
    depth_weight: float                 # SII depth of the affected symbol(s)
    priority: float                     # magnitude * (0.3 + 0.7 * depth_weight)
    classification: Literal["rupture", "drift", "peripheral_noise"]
```

**Classification rules:**

|Condition                                           |Classification       |Response                                                             |
|----------------------------------------------------|---------------------|---------------------------------------------------------------------|
|depth ≥ 0.8 AND connection loss rate > 10%/hr       |**rupture**          |CRITICAL immediately; bypass trend analysis; alert L3 governance     |
|0.2 ≤ depth < 0.8, any pre-signature                |**drift**            |Standard pre-signature pipeline (velocity, ETA, micro-correction)    |
|depth < 0.2, isolated pre-signature                 |**peripheral_noise** |Advisory log only                                                    |
|depth < 0.2, ≥ 5 correlated pre-signatures in window|**drift** (clustered)|Promote to standard pipeline — coordinated periphery change is signal|

**Effect on alert economics:** This is the false-positive control the v0.2.0 spec deferred to threshold tuning. Periphery damping suppresses the noisiest alert class structurally; rupture escalation guarantees core damage is never queued behind trend confirmation. Picard_Delta_3 and EOS_SEED_ORION are by construction maximum-depth symbols: any connection loss involving them classifies as rupture.

**API addition:** `GET /api/sensors/observatory/symbolic/integration-depth`

**Integration Point:** New module `src/sensors/observatory/symbolic/integration_index.py`. Consumes ConceptResonanceDetector tag registry and anchor chain records; feeds DriftPreSignatureMonitor and Coherence Certification (symbolic_coherence component).

## Resolved Design Questions (NEW in v0.3.0)

The four open questions from v0.2.0 are closed as follows. Each resolution is a design decision subject to canon promotion; certainty tags per Canon Protocol.

### RQ-1: Concept Tag Taxonomy

Tags are namespaced, canonical artifacts: **`{layer}:{domain}:{concept}`** (e.g., `L2:faction:galactic_marshals`, `L1:system:life_support`, `L3:agent:liora`).

- **Seed registries** [FACT — existing canon]: GUMAS enums (13 faction types, 33 event types, 8 bias types, 9 conflict phases), the L3 relay/glyph agent registry, and L1 station system inventories.
- **Governance** [INFERENCE — proposed]: tags follow the STAGING → CANON_PROMOTE pipeline with hash-based identity, exactly like other canon artifacts. New tags enter STAGING automatically on first observation.
- **Unknown-tag handling:** any tag not in the canonical registry is prefixed `uncanonized:` and quarantined from resonance *classification* — it is still counted (so frequency data accumulates for later promotion) but is always classified `uncertain`, never `convergence` or `bleed`. This prevents the resonance detector from making layer-contamination judgments about vocabulary canon has not defined.

### RQ-2: Pattern Library Expansion

Precursor patterns are added through a post-incident pipeline, never ad hoc:

1. **Trigger:** any anomaly that reached threshold (drift breach, ethics violation, containment event).
1. **Extract:** pull the T-minus window (default 2h) from the sensor data bus archive.
1. **Stage:** author a candidate `PrecursorPattern` with `status: staged`, `pattern_hash`, and provenance (incident ID, author, date).
1. **Backtest:** replay the candidate against the historical archive. Promotion requires precision ≥ 0.7 across ≥ 10 historical occurrences (or all available occurrences if fewer, flagged `low_n`).
1. **Promote / retire:** promoted patterns enter the live library as versioned artifacts. Live patterns with rolling false-positive rate > 30% over 30 days are auto-demoted to `staged` for re-tuning.

This mirrors the canon promotion pipeline: patterns are canon-like artifacts with hash identity and an evidence requirement.

### RQ-3: Threshold Tuning Methodology

Reuse the AFS calibration harness (PK-04, Component 6) rather than building a parallel one [INFERENCE — reuse proposal; AFS harness existence is FACT, 87 tests]:

- **Rolling-origin backtesting** over recorded sensor streams from the data bus archive.
- **Scoring:** Brier score and reliability diagrams for FusionPredictor forecasts; precision/recall for binary alert thresholds.
- **Calibration:** isotonic regression on forecast probabilities where reliability diagrams show miscalibration.
- **Storage:** all thresholds live in `shared/constants.py` (single source of truth, consistent with the GUMAS Forge refactor). Threshold changes are commits carrying backtest evidence; quarterly tuning cycle, with out-of-cycle changes permitted only for rupture-class incidents.

### RQ-4: Human-in-the-Loop Boundaries

Explicit decision matrix. The governing principle extends one-way observation: sensors never act, and *automation may act only where actions are reversible and confined below L1*.

|Intervention                                                    |Mode                                   |Rationale                                                                     |
|----------------------------------------------------------------|---------------------------------------|------------------------------------------------------------------------------|
|LOG_AND_MONITOR, INCREASE_AUDIT_FREQUENCY                       |Automatic                              |Observation-side only; no state mutation                                      |
|Micro-correction, magnitude < 0.5 × presig threshold, L2/L3 only|Automatic                              |Reversible, bounded, below pre-signature alert level                          |
|TRIGGER_ANCHOR_RESYNC                                           |Automatic, human notified              |Restorative, idempotent; PATCHWEAVER-class operation                          |
|QUARANTINE_CONCEPT                                              |Automatic, mandatory human review ≤ 24h|Containment is reversible; prolonged quarantine is a canon decision           |
|REQUIRE_HUMAN_APPROVAL (ethics ≥ 0.8 or accelerating)           |Human                                  |Picard_Delta_3 boundary cases are never automated                             |
|Any action affecting L1 actuation or physical operations        |Human                                  |Hard rule; no exceptions                                                      |
|THROTTLE                                                        |Automatic at CRITICAL ethics level only|Matches existing EthicsEngine behavior                                        |
|SUSPEND, RESET                                                  |Human only                             |Irreversible-in-practice; existing EthicsEngine actions reserved for operators|

**Mapping to existing EthicsEngine levels** [FACT — levels exist in repo]: sentinel risk < 0.4 → INFO (log); 0.4–0.7 → WARNING (alert operators / REVIEW queue); > 0.7 or accelerating → CRITICAL path, but the *sentinel* only ever recommends — the EthicsEngine and L3 governance own the action, preserving one-way observation.

-----

## GUMAS v2.0 Tick Lifecycle Integration (NEW in v0.3.0)

The v0.2.0 spec defined sensors abstractly “per tick” without binding them to the engine. This section binds the sensor array to the GUMAS v2.0 15-phase tick lifecycle and the Forge-refactor abstractions (PhaseRegistry, handler registry, SimulationSubsystem).

### Phase-Boundary Observers

Sensors attach as **post-phase observers** registered against the PhaseRegistry. Observers receive `(state, result, phase_id)` read-only after each phase completes. This preserves the one-way observation principle mechanically: observers have no mutation path into `GUMASState`, and the engine does not read observer output — only L3 governance does.

```python
class SensorPhaseObserver:
    """Read-only post-phase tap. Registered via PhaseRegistry.
    MUST NOT mutate state; receives a frozen view."""
    def observe(self, phase_id: str, state_view: GUMASStateView,
                result: TickResult) -> None:
        for sensor in self.sensors_for_phase(phase_id):
            with self.budget.timed_operation(sensor.budget_key):
                sensor.ingest(phase_id, state_view, result)
```

### Phase → Sensor Tap Map

|Tick Phase                |Sensor Tap                                                           |Notes                                                   |
|--------------------------|---------------------------------------------------------------------|--------------------------------------------------------|
|1 — Event Queue           |External proximity (event clustering), Concept Resonance (event tags)|Injected events are the main external signal source     |
|2 — Leader Bias           |Biometrics analog (agent decision rate)                              |Bias velocity feeds Ethical Signal tone component       |
|4 — Treaty Evaluation     |Ethical Signal Sentinel                                              |Breach scores are near-boundary evidence                |
|6.5 — Naming Resolution   |Concept Resonance                                                    |New referents = new concept tags (auto-STAGING per RQ-1)|
|9 — Combat Resolution     |Ethical Signal Sentinel, Structural                                  |Escalation patterns; casualty/intensity trends          |
|10 — Economic Tick        |Operational sensors                                                  |Resource pool analogs                                   |
|12 — Precursor Tick       |Fusion Predictor input                                               |Activation risk is a native precursor signal            |
|14 — Doctrine (Q-learning)|Oscillation Health + Convergence Regulator coupling                  |See below                                               |
|15b — Emergent Events     |Fusion Predictor input                                               |Emergent event generation closes the forecast loop      |
|End of tick               |Drift Pre-signature, SII update, per-tick budget check               |One consolidated end-of-tick pass                       |

Phases not listed are sampled by decimation (every Nth tick, default N=5) to stay within budget.

### Ethics Callback Wrapper

GUMAS already routes all 33 event handlers through an optional `ethics_callback` [FACT — engine hook exists]. The Ethical Signal Sentinel wraps this callback to accumulate pre-violation evidence **without altering pass/fail outcomes**:

```python
def wrap_ethics_callback(inner_cb, sentinel: EthicalSignalSentinel):
    def wrapped(action_type: str, params: dict) -> bool:
        allowed = inner_cb(action_type, params)
        sentinel.evaluate_action(
            entity_id=params.get("faction_id", "unknown"),
            action=Action(action_type, params, allowed=allowed),
        )
        return allowed          # verdict unchanged — observation only
    return wrapped
```

### SimulationSubsystem Validation Hook

The Forge refactor gives every subsystem `validate_state(state) -> List[str]` [FACT — interface defined in Forge report]. These violation lists are the canonical source for the **Structural / contract violations** metric in the internal sensor table (alert threshold > 0). No new validation logic is written in the sensor layer; sensors aggregate subsystem self-reports.

### Convergence Regulator Coupling

The Convergence Regulator injects intentional anti-convergence perturbations [FACT — implemented in GUMAS v2.0]. Without coordination, the Oscillation Health Monitor would misdiagnose regulator-induced variation as “hunting.” Resolution:

- The regulator emits an **intentional-perturbation marker** (tick, target, magnitude) on the sensor data bus.
- `OscillationHealthMonitor._diagnose()` excludes marker-matched corrections from alternation-rate and hunting calculations.
- A new derived metric, `regulator_share`, reports what fraction of observed variation is regulator-intentional. `regulator_share > 0.8` with rising drift is itself an advisory: the regulator may be masking genuine instability.

### AFS Coupling

The Aurora Forecast System (PK-04) and the Fusion Predictor solve the same problem class at different scales. v0.3.0 aligns them instead of duplicating:

- **Ingestion:** the Sensor Data Bus gains an adapter exporting timestamped readings into the AFS Feature Store (Component 2) format, making sensor history a first-class AFS data source.
- **Forecast schema:** `AnomalyForecast` adds optional `resolution_criteria: str` and `confidence_interval: Tuple[float, float]`, aligning with the AFS Forecast Question Module (Component 5) so sensor forecasts are scoreable by the same harness.
- **Calibration:** shared use of the AFS Calibration & Backtesting Harness (Component 6) per RQ-3 — one Brier-scored pipeline for both systems.
- **Boundary:** AFS consumes sensor data; sensors do not consume AFS forecasts as inputs (prevents forecast feedback loops, consistent with one-way observation).

### Per-Tick Performance Budget

Aggregate sensor overhead per tick (all phase observers + end-of-tick pass) must not exceed **10% of the tick wall-clock budget**, enforced by `PerformanceBudget` with a new `per_tick_aggregate` key. On breach: decimation factor N doubles for non-critical sensors (rupture-class monitoring is never decimated), and a budget violation is logged.

**Integration Points:** `src/sensors/core/phase_observer.py` (new), `src/sensors/integrations/afs_adapter.py` (new), wraps `core/phase_executor.py` PhaseRegistry and engine `ethics_callback`.

-----

## Repository Alignment Notes (v0.3.0 ↔ CloudBank v2.1.0)

- **Refactor targets** [FACT — Forge report]: integration points reference the post-Forge module layout (`core/phase_executor.py`, `core/handler_registry.py`, `subsystems/base.py`, `shared/constants.py`). Where the refactor is not yet merged, the v0.2.0 monolithic `engine.py` hook points remain valid; the phase-observer pattern degrades to a single end-of-tick tap.
- **Relay capsules** [FACT]: live capsule definitions reside in `.aurora/relays/` (e.g., `ARCHY_LIVE_RELAY_v1.json`). The `sensor_config` schema extension from v0.2.0 applies to these files; backward compatibility rule unchanged (absent = disabled).
- **Metric unit disambiguation** [FACT — both scales exist in repo docs]: drift Δ (lock Δ0.000, threshold 0.002, pre-signature at 0.001) and EthicsEngine deviation fractions (INFO 0.2 / WARNING 0.5 / CRITICAL 0.8) are **different scales measuring different things**. Dashboards, alert routing, and capsule configs MUST label units explicitly. The deploy-reference `alert_threshold=0.2` is an ethics-deviation value, not a drift Δ.
- **Observability stack** [FACT]: Prometheus + Grafana are already operational in the repo; sensor output channels wire into the existing stack and R-2 telemetry rather than introducing new exporters.
- **Encoding repair**: the v0.2.0 source file contained UTF-8 mojibake (double-encoded em-dashes, box-drawing characters, Δ glyphs). v0.3.0 is emitted as clean UTF-8; diffs against v0.2.0 should be read with this in mind.

-----

## Open Questions (v0.3.0)

1. **SII graph source of truth** — Should the symbol reference graph be derived from the tag registry (cheap, approximate) or from `symbolic_core` multivector relations (faithful to the lattice, costlier)? Current spec uses the tag registry; revisit after calibration data exists.
1. **Regulator marker protocol** — Exact schema and bus topic for Convergence Regulator intentional-perturbation markers; needs agreement with the GUMAS engine owner before Phase 7.
1. **AFS Feature Store schema ownership** — Whether the sensor→AFS adapter conforms to the AFS schema or AFS adds a sensor-native ingestion path; PK-04 currently silent on this.
1. **Observer process isolation** — Whether phase observers run in-process (lowest latency, risk of budget contagion into tick time) or out-of-process via the data bus (isolation, added latency). Default in-process with hard budget enforcement; revisit if budget violations recur.

-----

## Modified Sections

|Section                 |Change                                                                                                           |
|------------------------|-----------------------------------------------------------------------------------------------------------------|
|Header                  |Version 0.3.0; Layer line adds L2 (tick lifecycle taps); DLP bumped to v3; status notes reconciler gate          |
|Changelog               |New “Changelog from v0.2.0” block prepended (v0.1.0 changelog retained)                                          |
|Performance Budget table|+ SII incremental update row; + per-tick aggregate row (≤10% tick budget, 15% max)                               |
|Codebase Integration Map|+ 5 rows: SymbolIntegrationIndex, SensorPhaseObserver, EthicsCallbackWrapper, AFSAdapter, RegulatorMarkerConsumer|
|Implementation Priority |+ Phase 7: Lifecycle Integration & Calibration (Week 7)                                                          |
|Success Criteria        |+ criteria 10–13 (rupture classification, ≤10% overhead, regulator exclusion, AFS-harness calibration)           |
|Open Questions          |v0.2.0’s four questions moved to “Resolved Design Questions”; four new v0.3.0 questions opened                   |
|Footer                  |Version/date/sources updated                                                                                     |
|Whole file              |UTF-8 mojibake repaired (em-dashes, box-drawing, Δ) — diff noise against the raw v0.2.0 file is expected         |

## Unchanged (carried forward verbatim)

Internal/External/Observatory-Physical sensor tables; Concept Resonance Detector; Ethical Signal Sentinel core; Drift Pre-signature Monitor core; Layer Interpreter; Fusion Predictor core; Oscillation Health Monitor core (extended, not modified, by regulator markers); Cross-Layer Resonance Calculator; Coherence Certification; ZIPWIZ Handshake Extension (5-step sequence unchanged); Relay Capsule Schema Extension; API structure (v0.3.0 adds one endpoint, documented inline); Directory structure (new files listed in Integration Map).

-----

## Compatibility & Migration

- **Relay capsules:** no schema change beyond v0.2.0; `sensor_config` remains optional, absent = disabled.
- **Engine:** if the Forge refactor is unmerged, phase observers degrade to a single end-of-tick tap against monolithic `engine.py`; ethics wrapper works against either layout (it wraps the callback, not the engine).
- **Dashboards:** unit labels (Δ vs. deviation fraction) must be added before v0.3.0 alerting goes live — this is the only breaking operational change.

## Instructions for Simulation Programmers

1. Implement in Phase-7 order (observer registration → ethics wrapper → SII → regulator markers → AFS adapter → calibration → budget validation).
1. Do not begin Phase 3 symbolic-sensor work from the v0.2.0 text; RQ-1 tag taxonomy supersedes the undefined taxonomy assumed there.
1. SII thresholds (0.8/0.2) and decimation N=5 are ASSUMPTION-tagged starting values — ship them behind `shared/constants.py` entries so RQ-3 calibration can tune without code changes.
1. Zero regressions: the 116 GUMAS engine tests and 87 AFS tests must pass untouched; sensor taps are additive and read-only by construction.

## Reconciliation Gate

Before CANON_PROMOTE: run aurora-canon-reconciler on this delta (L3 protocol_update). Expected checks: no L2→L1 entity mapping (none introduced), anchor references valid (EOS_SEED_ORION, Picard_Delta_3), hash identity recorded above, certainty tags present.