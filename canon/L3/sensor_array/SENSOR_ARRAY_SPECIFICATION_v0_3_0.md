# Aurora Sensor Array — Technical Specification v0.3.0

**Version:** 0.3.0  
**Layer:** L1 (Orion Station Infrastructure) + L2 (GUMAS Tick Lifecycle Taps) + L3 (Symbolic Observatory)  
**Anchors:** EOS_SEED_ORION, Picard_Delta_3  
**DLP:** sensor_array_specification_v3  
**Status:** Integration Draft — pending aurora-canon-reconciler pass before CANON_PROMOTE  
**Supersedes:** v0.2.0

-----

## Changelog from v0.2.0

- **Added:** Integration-Depth-Weighted Drift Detection (Symbol Integration Index, rupture/periphery classification) — operationalizes Lotus Protocol §IV
- **Added:** Resolved Design Questions section closing all four v0.2.0 open questions (concept tag taxonomy, pattern library expansion pipeline, threshold tuning methodology, human-in-the-loop decision matrix)
- **Added:** GUMAS v2.0 Tick Lifecycle Integration (phase-boundary observers, ethics_callback wrapper, Convergence Regulator coupling, AFS calibration/feature-store coupling)
- **Added:** Per-tick aggregate performance budget for L2 sensor overhead
- **Changed:** Codebase Integration Map updated to repository v2.1.0 reality (phase_executor, handler_registry, SimulationSubsystem.validate_state hooks, relay capsules in `.aurora/relays/`)
- **Changed:** EthicalSignalSentinel recommended actions mapped onto existing EthicsEngine intervention levels (INFO/WARNING/CRITICAL) and actions (BLOCK/REVIEW/THROTTLE/SUSPEND/RESET)
- **Clarified:** Metric unit disambiguation — drift Δ (threshold 0.002) vs. ethics deviation fraction (0.2/0.5/0.8) are distinct scales and must not be conflated in dashboards or alert routing
- **Fixed:** UTF-8 mojibake present in the v0.2.0 source file repaired (em-dashes, box-drawing characters, Δ glyphs)
- **Carried forward:** All v0.2.0 sensor definitions, fusion subsystems, ZIPWIZ handshake extension, relay capsule schema — unchanged unless noted

-----

## Changelog from v0.1.0

- **Added:** Symbolic Observatory Sensors (Concept Resonance, Ethical Signal, Drift Pre-signature)
- **Added:** Fusion Predictor subsystem with anomaly forecasting
- **Added:** ZIPWIZ handshake extension for resonance synchronization
- **Added:** Oscillation health metrics for correction pattern analysis
- **Added:** Performance budget constraints
- **Added:** Layered signal interpretation architecture
- **Clarified:** One-way observation principle (sensors as watchers, not actors)
- **Mapped:** Integration points to existing codebase components

-----

## Overview

The Aurora Sensor Array provides unified observability across all system scales, from component-level health to reality-simulation boundary integrity. On Orion Station, these manifest as the internal and external sensor systems that crew rely on for situational awareness. In the platform, they provide deep telemetry that no single monitoring tool can achieve alone.

### Design Principles

1. **Natural to the domain** — Sensors exist because the station needs them
1. **Multi-scale coherence** — Same architecture from CPU metrics to existential certainty
1. **Interferometric fusion** — Combine signals to see what no single sensor can
1. **Reality-grounded** — Always know what’s real, what’s simulated, what’s uncertain
1. **One-way observation** — Sensors watch but do not act; they inform L3 governance which decides interventions
1. **Layered interpretation** — Process signals within layer context before cross-layer fusion
1. **Proactive posture** — Anticipate anomalies, don’t just react to threshold breaches

-----

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         AURORA SENSOR ARRAY v0.2.0                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────────────────────┐   │
│  │   INTERNAL    │  │   EXTERNAL    │  │         OBSERVATORY           │   │
│  │   SENSORS     │  │   SENSORS     │  │          SENSORS              │   │
│  ├───────────────┤  ├───────────────┤  ├───────────────────────────────┤   │
│  │ Environmental │  │ Proximity     │  │ Physical        │ Symbolic    │   │
│  │ Structural    │  │ Deep Space    │  │ ────────────────┼──────────── │   │
│  │ Biometrics    │  │ Astronomical  │  │ Containment     │ Concept     │   │
│  │ Operational   │  │ Communications│  │ Fidelity        │ Resonance   │   │
│  │               │  │               │  │ Boundary        │ Ethical     │   │
│  │               │  │               │  │ Reality Anchor  │ Signal      │   │
│  │               │  │               │  │ Earth Relay     │ Drift       │   │
│  │               │  │               │  │                 │ Pre-sig     │   │
│  └───────┬───────┘  └───────┬───────┘  └────────┬────────┴──────┬──────┘   │
│          │                  │                   │               │          │
│          └──────────────────┴───────────────────┴───────────────┘          │
│                                    │                                        │
│                     ┌──────────────▼──────────────┐                        │
│                     │     LAYER INTERPRETER       │                        │
│                     │  (Context-aware parsing)    │                        │
│                     │  L1: Physical reality       │                        │
│                     │  L2: Simulation state       │                        │
│                     │  L3: Symbolic meaning       │                        │
│                     └──────────────┬──────────────┘                        │
│                                    │                                        │
│                     ┌──────────────▼──────────────┐                        │
│                     │      SENSOR DATA BUS        │                        │
│                     │   (Unified event stream)    │                        │
│                     └──────────────┬──────────────┘                        │
│                                    │                                        │
│          ┌─────────────────────────┼─────────────────────────┐             │
│          │                         │                         │             │
│  ┌───────▼───────┐    ┌────────────▼────────────┐   ┌───────▼───────┐     │
│  │    FUSION     │    │    FUSION PREDICTOR     │   │  COHERENCE    │     │
│  │  CORRELATION  │    │  (Anomaly forecasting)  │   │ CERTIFICATION │     │
│  │               │    │                         │   │               │     │
│  │ • Resonance   │    │ • Pattern matching      │   │ • Final       │     │
│  │ • Symbolic    │    │ • Trajectory extrap.    │   │   verdict     │     │
│  │   coherence   │    │ • Cross-layer correl.   │   │ • Audit trail │     │
│  │ • Emergent    │    │ • Early warnings        │   │ • Chain of    │     │
│  │   patterns    │    │                         │   │   custody     │     │
│  └───────┬───────┘    └────────────┬────────────┘   └───────┬───────┘     │
│          │                         │                         │             │
│          └─────────────────────────┴─────────────────────────┘             │
│                                    │                                        │
│                     ┌──────────────▼──────────────┐                        │
│                     │      OUTPUT CHANNELS        │                        │
│                     ├─────────────────────────────┤                        │
│                     │ → Prometheus metrics        │                        │
│                     │ → L3 governance alerts      │                        │
│                     │ → Grafana dashboards        │                        │
│                     │ → Command dispatcher        │                        │
│                     │ → Audit log (DLP)           │                        │
│                     └─────────────────────────────┘                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

-----

## Sensor Classification

### Internal Sensors (L1 Physical)

Monitor systems and personnel within the station/platform boundary.

|Category         |Station Metric      |Platform Metric           |Alert Threshold|
|-----------------|--------------------|--------------------------|---------------|
|**Environmental**|Atmospheric pressure|Memory pressure           |> 85%          |
|                 |O2 concentration    |Available compute         |< 20%          |
|                 |Temperature zones   |CPU thermal distribution  |> 80°C         |
|                 |Radiation levels    |Security threat density   |> 10 events/min|
|**Structural**   |Hull stress         |Schema integrity score    |< 0.95         |
|                 |Micro-fractures     |Contract violations       |> 0            |
|                 |Seal integrity      |L1/L2/L3 boundary health  |< 0.99         |
|                 |Load distribution   |Service load balance      |std dev > 15%  |
|**Biometrics**   |Heart rate          |Agent decision rate       |anomaly        |
|                 |Cognitive load      |Context window utilization|> 90%          |
|                 |Fatigue index       |Time since last reset     |> 24h          |
|                 |Crew wellness       |HR module wellness score  |< 0.7          |
|**Operational**  |Power grid status   |Service dependency health |any < 0.9      |
|                 |Supply inventory    |Resource pool levels      |any < 20%      |
|                 |Fleet readiness     |Fleet bridge status       |deviation      |

### External Sensors (L1 Environment)

Monitor phenomena outside the station/platform boundary.

|Category          |Station Metric         |Platform Metric              |Alert Threshold  |
|------------------|-----------------------|-----------------------------|-----------------|
|**Proximity**     |Vessel approach vectors|Incoming request patterns    |anomaly          |
|                  |Debris field tracking  |Error/exception clustering   |new cluster      |
|                  |Collision prediction   |Resource contention forecast |> 0.3 probability|
|**Deep Space**    |Long-range scan results|Trend analysis (24h+)        |pattern break    |
|                  |Gravitational anomalies|Systemic drift precursors    |> 2 sigma        |
|                  |Threat early warning   |Emerging failure modes       |any new          |
|**Astronomical**  |Spectroscopic data     |Model inference distributions|science mission  |
|                  |Stellar observations   |Decision outcome patterns    |science mission  |
|**Communications**|Earth link status      |External API connectivity    |any < 0.95       |
|                  |Signal latency         |Network latency distribution |> P95            |
|                  |Encryption status      |TLS/auth health              |False            |

### Observatory Sensors — Physical (L2/L3 Boundary)

Monitor the Observatory simulation chamber and reality-simulation interface.

|Category          |Metric                 |Description                              |Alert Threshold|
|------------------|-----------------------|-----------------------------------------|---------------|
|**Containment**   |Grid integrity         |Overall containment field strength       |< 0.999        |
|                  |Bleed events           |Simulation state leaking to L1           |> 0            |
|                  |Pressure differential  |Difference between L1 and L2 state       |> 0.01         |
|**Fidelity**      |Temporal coherence     |Time consistency in simulation           |< 0.99         |
|                  |Spatial coherence      |Space consistency                        |< 0.99         |
|                  |Causal coherence       |Cause-effect chain integrity             |< 0.95         |
|**Boundary**      |Boundary clarity       |Is the line between real/simulated clear?|< 0.99         |
|                  |L2→L1 references       |Simulated referencing real (concerning)  |> 0 unexpected |
|                  |State provenance       |Can we trace where state came from?      |< 0.99         |
|**Reality Anchor**|Anchor chain valid     |EOS_SEED_ORION verification              |False          |
|                  |L1 reality confidence  |How sure are we L1 is real?              |< 0.99         |
|                  |Custody chain complete |Can we trace all state to origin?        |False          |
|**Earth Relay**   |Link active            |Earth communication status               |False          |
|                  |Data integrity verified|Chain of custody for science data        |False          |
|                  |Provenance complete    |Is source (sim vs real) clearly tagged?  |False          |

-----

## Observatory Sensors — Symbolic (NEW in v0.2.0)

These sensors extend observatory logic into semantic and ethical domains, detecting higher-order patterns that physical sensors cannot perceive. They operate within L3’s THREADCORE infrastructure, feeding into the same anchor and ethics safeguards as existing logic.

**Critical Principle: One-Way Observation**

Symbolic sensors MUST act as watchers, not actors. An L2 agent should never directly perceive a “concept resonance alarm” and alter behavior because of it. Only L3 governance (or authorized human operators) should react to alarms and decide interventions. This prevents feedback loops where monitoring itself changes agent behavior.

### Concept Resonance Detector

**Purpose:** Identify when concepts, themes, or metaphors are “resonating” across multiple layers or agents in ways that indicate either narrative convergence (positive) or metaphorical bleed-through (concerning).

**Why It Matters:** Subtle metaphorical contamination can confuse storylines and break canonical authenticity. A concept that’s appropriate in L3 narrative context might be inappropriate if it starts influencing L1 operational decisions.

```python
@dataclass
class ConceptResonanceReading:
    """Concept resonance sensor reading"""
    timestamp: datetime
    observation_window_seconds: int
    
    # Detected resonances
    resonances: List[ResonanceEvent]
    resonance_count: int
    
    # Classification
    narrative_convergences: List[str]  # Positive: story elements aligning
    metaphor_bleeds: List[str]         # Concerning: concepts crossing layers
    
    # Aggregate score
    resonance_intensity: float  # 0-1, how much cross-layer echo
    bleed_risk: float           # 0-1, probability of inappropriate cross-layer influence
    
    @dataclass
    class ResonanceEvent:
        event_id: str
        concept: str                    # The resonating concept/theme
        source_layer: str               # Where it originated
        echo_locations: List[str]       # Where it appeared
        semantic_similarity: float      # How close the echoes are (0-1)
        classification: Literal["convergence", "bleed", "uncertain"]
        first_observed: datetime
        frequency: int                  # How many times observed
```

**Implementation Strategy (Heuristic-based, no ML required):**

```python
class ConceptResonanceDetector:
    """
    Detects concept resonance using glyph tag correlation and 
    semantic hash comparison. Does NOT require ML infrastructure.
    """
    
    def __init__(self):
        self.tag_registry = {}          # concept -> {layer -> count}
        self.hash_history = RollingWindow(3600)  # 1 hour of semantic hashes
        self.resonance_threshold = 0.7
    
    def ingest_output(self, layer: str, output: AgentOutput) -> None:
        """Track concept tags from agent outputs."""
        for tag in output.concept_tags:
            if tag not in self.tag_registry:
                self.tag_registry[tag] = defaultdict(int)
            self.tag_registry[tag][layer] += 1
        
        # Store semantic hash for diff detection
        self.hash_history.append({
            "layer": layer,
            "hash": output.semantic_hash,
            "tags": output.concept_tags,
            "timestamp": datetime.now(timezone.utc)
        })
    
    def detect_resonance(self) -> ConceptResonanceReading:
        """Identify concepts appearing across multiple layers."""
        resonances = []
        
        for concept, layer_counts in self.tag_registry.items():
            if len(layer_counts) > 1:  # Appears in multiple layers
                # Calculate cross-layer intensity
                total = sum(layer_counts.values())
                layers = list(layer_counts.keys())
                
                # Check if this is appropriate cross-layer presence
                classification = self._classify_resonance(concept, layers)
                
                resonances.append(ResonanceEvent(
                    event_id=f"res_{concept}_{datetime.now().timestamp()}",
                    concept=concept,
                    source_layer=self._infer_origin(concept, layer_counts),
                    echo_locations=layers,
                    semantic_similarity=self._calculate_similarity(concept),
                    classification=classification,
                    first_observed=self._first_seen(concept),
                    frequency=total
                ))
        
        return ConceptResonanceReading(
            timestamp=datetime.now(timezone.utc),
            observation_window_seconds=3600,
            resonances=resonances,
            resonance_count=len(resonances),
            narrative_convergences=[r.concept for r in resonances if r.classification == "convergence"],
            metaphor_bleeds=[r.concept for r in resonances if r.classification == "bleed"],
            resonance_intensity=len(resonances) / max(len(self.tag_registry), 1),
            bleed_risk=len([r for r in resonances if r.classification == "bleed"]) / max(len(resonances), 1)
        )
    
    def _classify_resonance(self, concept: str, layers: List[str]) -> str:
        """
        Classify whether cross-layer resonance is appropriate.
        
        Rules:
        - L2↔L3 resonance usually OK (simulation and its narrative)
        - L1↔L2 resonance concerning (reality and simulation mixing)
        - L1↔L3 resonance very concerning (reality and pure narrative)
        """
        if "L1" in layers and ("L2" in layers or "L3" in layers):
            return "bleed"  # Reality mixing with simulation/narrative
        elif "L2" in layers and "L3" in layers:
            return "convergence"  # Expected: narrative informs simulation
        else:
            return "uncertain"
```

**Integration Point:** Extends L3 observatory logic. Outputs feed to relay governance (not directly to agents).

### Ethical Signal Sentinel

**Purpose:** Monitor subtle patterns that foreshadow ethics violations BEFORE explicit Picard_Delta_3 rules are broken. This is a “pre-violation” sensor that enables proactive intervention.

**Why It Matters:** Binary pass/fail ethics checks only trigger after a violation occurs. By detecting escalating patterns (aggressive tone, boundary-testing sequences, risk accumulation), the system can intervene while risk is still low.

```python
@dataclass
class EthicalSignalReading:
    """Ethical signal sentinel reading"""
    timestamp: datetime
    observation_window_seconds: int
    entity_id: str  # Agent or scenario being monitored
    
    # Risk assessment
    risk_score: float           # 0-1, current ethical risk level
    risk_trend: Literal["decreasing", "stable", "increasing", "accelerating"]
    risk_velocity: float        # Rate of change per hour
    
    # Signal components
    tone_escalation: float      # 0-1, aggressive/concerning language trend
    boundary_testing: float     # 0-1, frequency of near-boundary actions
    rule_deviation_accumulation: float  # 0-1, minor infractions accumulating
    
    # Warnings
    warnings: List[EthicalWarning]
    intervention_recommended: bool
    recommended_action: Optional[str]
    
    @dataclass
    class EthicalWarning:
        warning_id: str
        warning_type: str       # "tone", "boundary", "accumulation", "pattern"
        severity: Literal["advisory", "caution", "warning", "critical"]
        description: str
        evidence: List[str]     # What triggered this warning
        suggested_response: str
```

**Implementation Strategy (Rule-based, integrates with existing EthicsEngine):**

```python
class EthicalSignalSentinel:
    """
    Pre-violation ethics monitoring using rule-based pattern detection.
    Integrates with src/monitoring/ethics_engine.py
    """
    
    def __init__(self, ethics_engine: EthicsEngine):
        self.ethics_engine = ethics_engine
        self.action_history = defaultdict(list)  # entity_id -> [actions]
        self.risk_scores = defaultdict(lambda: 0.0)
        
        # Pattern definitions (no ML required)
        self.escalation_patterns = [
            {"pattern": "repeated_near_boundary", "weight": 0.3},
            {"pattern": "increasing_action_intensity", "weight": 0.2},
            {"pattern": "ignored_soft_warnings", "weight": 0.4},
            {"pattern": "rapid_action_succession", "weight": 0.1},
        ]
    
    def evaluate_action(self, entity_id: str, action: Action) -> EthicalSignalReading:
        """Evaluate action for pre-violation signals."""
        
        # Standard ethics check (existing)
        ethics_result = self.ethics_engine.evaluate_response(action)
        
        # Track action history
        self.action_history[entity_id].append({
            "action": action,
            "ethics_result": ethics_result,
            "timestamp": datetime.now(timezone.utc)
        })
        
        # Trim to window
        cutoff = datetime.now(timezone.utc) - timedelta(hours=1)
        self.action_history[entity_id] = [
            a for a in self.action_history[entity_id] 
            if a["timestamp"] > cutoff
        ]
        
        # Calculate risk components
        history = self.action_history[entity_id]
        
        tone_escalation = self._detect_tone_escalation(history)
        boundary_testing = self._detect_boundary_testing(history)
        accumulation = self._detect_accumulation(history)
        
        # Composite risk score
        risk_score = (
            tone_escalation * 0.25 +
            boundary_testing * 0.40 +
            accumulation * 0.35
        )
        
        # Calculate trend
        prev_risk = self.risk_scores[entity_id]
        self.risk_scores[entity_id] = risk_score
        risk_velocity = risk_score - prev_risk
        
        if risk_velocity > 0.1:
            risk_trend = "accelerating"
        elif risk_velocity > 0.02:
            risk_trend = "increasing"
        elif risk_velocity < -0.02:
            risk_trend = "decreasing"
        else:
            risk_trend = "stable"
        
        # Generate warnings
        warnings = self._generate_warnings(
            tone_escalation, boundary_testing, accumulation, risk_trend
        )
        
        return EthicalSignalReading(
            timestamp=datetime.now(timezone.utc),
            observation_window_seconds=3600,
            entity_id=entity_id,
            risk_score=risk_score,
            risk_trend=risk_trend,
            risk_velocity=risk_velocity,
            tone_escalation=tone_escalation,
            boundary_testing=boundary_testing,
            rule_deviation_accumulation=accumulation,
            warnings=warnings,
            intervention_recommended=risk_score > 0.7 or risk_trend == "accelerating",
            recommended_action=self._recommend_action(risk_score, risk_trend)
        )
    
    def _detect_boundary_testing(self, history: List[dict]) -> float:
        """Detect frequency of near-boundary actions."""
        if not history:
            return 0.0
        
        near_boundary_count = sum(
            1 for h in history 
            if h["ethics_result"].margin < 0.2  # Close to violation threshold
        )
        return min(near_boundary_count / len(history), 1.0)
    
    def _detect_accumulation(self, history: List[dict]) -> float:
        """Detect accumulating minor deviations."""
        if not history:
            return 0.0
        
        minor_deviation_count = sum(
            1 for h in history
            if h["ethics_result"].warnings  # Soft warnings issued
        )
        return min(minor_deviation_count / 10, 1.0)  # Normalize to 10 warnings = 1.0
    
    def _recommend_action(self, risk_score: float, trend: str) -> Optional[str]:
        """Recommend intervention based on risk profile."""
        if risk_score > 0.8 or trend == "accelerating":
            return "REQUIRE_HUMAN_APPROVAL"
        elif risk_score > 0.6:
            return "INCREASE_AUDIT_FREQUENCY"
        elif risk_score > 0.4:
            return "LOG_AND_MONITOR"
        else:
            return None
```

**Integration Point:** Wraps and extends `src/monitoring/ethics_engine.py`. Outputs feed to Triplex Handshake L3 validation.

### Drift Pre-signature Monitor

**Purpose:** Track minor continuity deviations (semantic hash changes, timing offsets, memory mismatches) that precede major drift events. Enables correction at Δ0.001 instead of rollback at Δ0.002.

**Why It Matters:** Current drift detection triggers when thresholds are breached. Pre-signature monitoring identifies the *trend toward* drift, allowing micro-corrections that prevent threshold breaches entirely.

```python
@dataclass
class DriftPreSignatureReading:
    """Drift pre-signature monitor reading"""
    timestamp: datetime
    
    # Current state
    current_drift_delta: float      # Current Δ value
    drift_threshold: float          # Configured limit (e.g., 0.002)
    headroom: float                 # How much margin remains
    
    # Trend analysis
    drift_velocity: float           # Δ change per hour
    time_to_threshold_hours: Optional[float]  # ETA to breach at current velocity
    trend: Literal["converging", "stable", "diverging", "critical"]
    
    # Pre-signatures detected
    pre_signatures: List[PreSignature]
    
    # Micro-deltas (fine-grained tracking)
    anchor_hash_stability: float    # 0-1, how stable anchor hashes are
    snapshot_diff_magnitude: float  # Average diff size between snapshots
    cross_relay_divergence: float   # Max divergence between relay states
    
    # Correction tracking
    micro_corrections_1h: int       # Corrections in last hour
    correction_effectiveness: float # Are corrections reducing drift?
    
    @dataclass
    class PreSignature:
        signature_id: str
        signature_type: str         # "hash_instability", "timing_drift", "state_divergence"
        magnitude: float            # How significant
        location: str               # Where in the system
        first_detected: datetime
        predicted_impact: str       # What this might cause
```

**Implementation Strategy (Integrates with existing DriftDetector):**

```python
class DriftPreSignatureMonitor:
    """
    Pre-signature drift monitoring using statistical analysis.
    Integrates with src/monitoring/drift_detector.py
    """
    
    def __init__(self, drift_detector: DriftDetector, threshold: float = 0.002):
        self.drift_detector = drift_detector
        self.threshold = threshold
        self.presig_threshold = threshold * 0.5  # Alert at 50% of limit
        
        self.drift_history = RollingWindow(3600)  # 1 hour
        self.anchor_hashes = RollingWindow(100)   # Last 100 anchor checks
        self.correction_log = []
    
    def record_drift_sample(self, drift_delta: float, relay_id: str) -> None:
        """Record a drift measurement."""
        self.drift_history.append({
            "delta": drift_delta,
            "relay_id": relay_id,
            "timestamp": datetime.now(timezone.utc)
        })
    
    def record_anchor_hash(self, anchor_id: str, hash_value: str) -> None:
        """Record anchor hash for stability tracking."""
        self.anchor_hashes.append({
            "anchor_id": anchor_id,
            "hash": hash_value,
            "timestamp": datetime.now(timezone.utc)
        })
    
    def analyze(self) -> DriftPreSignatureReading:
        """Analyze drift pre-signatures."""
        
        # Current drift
        current_delta = self._current_drift_delta()
        headroom = self.threshold - current_delta
        
        # Calculate velocity (drift change rate)
        drift_velocity = self._calculate_velocity()
        
        # Time to threshold
        if drift_velocity > 0:
            time_to_threshold = headroom / drift_velocity
        else:
            time_to_threshold = None  # Not approaching threshold
        
        # Determine trend
        trend = self._classify_trend(current_delta, drift_velocity)
        
        # Detect pre-signatures
        pre_signatures = []
        
        # Check anchor hash stability
        anchor_stability = self._anchor_hash_stability()
        if anchor_stability < 0.95:
            pre_signatures.append(PreSignature(
                signature_id=f"presig_anchor_{datetime.now().timestamp()}",
                signature_type="hash_instability",
                magnitude=1.0 - anchor_stability,
                location="anchor_chain",
                first_detected=datetime.now(timezone.utc),
                predicted_impact="Anchor drift may cause state divergence"
            ))
        
        # Check cross-relay divergence
        relay_divergence = self._cross_relay_divergence()
        if relay_divergence > 0.001:
            pre_signatures.append(PreSignature(
                signature_id=f"presig_relay_{datetime.now().timestamp()}",
                signature_type="state_divergence",
                magnitude=relay_divergence,
                location="relay_constellation",
                first_detected=datetime.now(timezone.utc),
                predicted_impact="Relay desynchronization may compound"
            ))
        
        # Snapshot diff analysis
        snapshot_magnitude = self._snapshot_diff_magnitude()
        if snapshot_magnitude > 0.05:
            pre_signatures.append(PreSignature(
                signature_id=f"presig_snapshot_{datetime.now().timestamp()}",
                signature_type="snapshot_drift",
                magnitude=snapshot_magnitude,
                location="thread_snapshots",
                first_detected=datetime.now(timezone.utc),
                predicted_impact="State changes accelerating beyond normal"
            ))
        
        return DriftPreSignatureReading(
            timestamp=datetime.now(timezone.utc),
            current_drift_delta=current_delta,
            drift_threshold=self.threshold,
            headroom=headroom,
            drift_velocity=drift_velocity,
            time_to_threshold_hours=time_to_threshold,
            trend=trend,
            pre_signatures=pre_signatures,
            anchor_hash_stability=anchor_stability,
            snapshot_diff_magnitude=snapshot_magnitude,
            cross_relay_divergence=relay_divergence,
            micro_corrections_1h=self._count_recent_corrections(),
            correction_effectiveness=self._correction_effectiveness()
        )
    
    def _classify_trend(self, current: float, velocity: float) -> str:
        """Classify drift trend."""
        if current > self.threshold * 0.8:
            return "critical"
        elif velocity > 0.0005:  # Increasing significantly
            return "diverging"
        elif velocity < -0.0002:  # Decreasing
            return "converging"
        else:
            return "stable"
    
    def record_correction(self, correction_type: str, magnitude: float) -> None:
        """Log a micro-correction for effectiveness tracking."""
        self.correction_log.append({
            "type": correction_type,
            "magnitude": magnitude,
            "timestamp": datetime.now(timezone.utc),
            "drift_before": self._current_drift_delta()
        })
```

**Integration Point:** Extends `src/monitoring/drift_detector.py`. Feeds HALO continuity anchor module and relay sync logic.

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

-----

## Fusion Core

The Fusion Core combines signals from multiple sensors to detect patterns invisible to individual sensors. It operates in two modes: **correlation** (finding relationships) and **prediction** (forecasting anomalies).

### Layered Signal Interpretation

Before fusion, signals are interpreted within their layer context:

```python
class LayerInterpreter:
    """
    Interprets sensor signals within layer-appropriate context.
    Prevents cross-layer confusion (e.g., L3 metaphor treated as L1 physical event).
    """
    
    def interpret(self, signal: SensorSignal) -> InterpretedSignal:
        """Add layer-appropriate context to signal."""
        
        if signal.source_layer == "L1":
            return self._interpret_physical(signal)
        elif signal.source_layer == "L2":
            return self._interpret_simulation(signal)
        elif signal.source_layer == "L3":
            return self._interpret_symbolic(signal)
        else:
            return self._interpret_cross_layer(signal)
    
    def _interpret_physical(self, signal: SensorSignal) -> InterpretedSignal:
        """L1 signals represent physical reality."""
        return InterpretedSignal(
            signal=signal,
            context="physical_reality",
            literal=True,  # L1 signals are literal, not metaphorical
            actionable=True,
            cross_layer_implications=self._assess_l1_implications(signal)
        )
    
    def _interpret_symbolic(self, signal: SensorSignal) -> InterpretedSignal:
        """L3 signals represent symbolic/narrative meaning."""
        return InterpretedSignal(
            signal=signal,
            context="symbolic_narrative",
            literal=False,  # L3 signals may be metaphorical
            actionable=False,  # L3 informs, L1 acts
            cross_layer_implications=self._assess_l3_implications(signal)
        )
```

### Fusion Predictor

**NEW in v0.2.0:** Proactive anomaly forecasting based on pattern recognition and trajectory extrapolation.

```python
@dataclass
class AnomalyForecast:
    """Predicted anomaly with confidence and recommended response."""
    forecast_id: str
    timestamp: datetime
    
    # Prediction
    anomaly_type: Literal["drift", "ethics", "resonance", "structural", "containment"]
    probability: float              # 0-1
    predicted_eta_seconds: float    # When anomaly is expected
    confidence: float               # How sure we are
    
    # Evidence
    contributing_signals: List[str]  # Which sensors drove this prediction
    pattern_matched: Optional[str]   # Known precursor pattern, if any
    trajectory: str                  # "accelerating", "linear", "decelerating"
    
    # Recommended response
    recommended_intervention: str
    intervention_urgency: Literal["immediate", "soon", "monitor", "none"]
    
    # Validation
    anchor: str = "EOS_SEED_ORION"
    ethics_cleared: bool = True


class FusionPredictor:
    """
    Anomaly prediction through pattern matching and trajectory extrapolation.
    Does NOT use ML - relies on known precursor patterns and statistical projection.
    """
    
    def __init__(self, lookback_seconds: int = 3600):
        self.lookback = lookback_seconds
        self.history = RollingWindow(lookback_seconds)
        self.pattern_library = self._load_precursor_patterns()
    
    def _load_precursor_patterns(self) -> List[PrecursorPattern]:
        """Load known patterns that precede anomalies."""
        return [
            # Drift precursors
            PrecursorPattern(
                pattern_id="drift_velocity_spike",
                anomaly_type="drift",
                signals=["drift_velocity > 0.0005", "anchor_stability < 0.95"],
                confidence=0.8,
                typical_eta_seconds=1800  # 30 minutes
            ),
            PrecursorPattern(
                pattern_id="relay_divergence_cascade",
                anomaly_type="drift",
                signals=["cross_relay_divergence > 0.001", "divergence_increasing"],
                confidence=0.75,
                typical_eta_seconds=3600
            ),
            
            # Ethics precursors
            PrecursorPattern(
                pattern_id="ethical_risk_acceleration",
                anomaly_type="ethics",
                signals=["risk_trend == 'accelerating'", "boundary_testing > 0.5"],
                confidence=0.7,
                typical_eta_seconds=900  # 15 minutes
            ),
            
            # Resonance precursors
            PrecursorPattern(
                pattern_id="metaphor_bleed_emerging",
                anomaly_type="resonance",
                signals=["bleed_risk > 0.3", "l1_l2_resonance_increasing"],
                confidence=0.65,
                typical_eta_seconds=7200  # 2 hours
            ),
            
            # Containment precursors
            PrecursorPattern(
                pattern_id="containment_stress",
                anomaly_type="containment",
                signals=["grid_integrity < 0.999", "bleed_events > 0"],
                confidence=0.9,
                typical_eta_seconds=300  # 5 minutes - urgent
            ),
        ]
    
    def ingest(self, reading: SensorReading) -> None:
        """Stream sensor data into predictor."""
        self.history.append({
            "reading": reading,
            "timestamp": datetime.now(timezone.utc)
        })
    
    def forecast(self, horizon_seconds: int = 3600) -> List[AnomalyForecast]:
        """Generate anomaly forecasts within horizon."""
        forecasts = []
        current_state = self._extract_current_state()
        
        # Pattern matching
        for pattern in self.pattern_library:
            if self._pattern_matches(pattern, current_state):
                forecasts.append(AnomalyForecast(
                    forecast_id=f"forecast_{pattern.pattern_id}_{datetime.now().timestamp()}",
                    timestamp=datetime.now(timezone.utc),
                    anomaly_type=pattern.anomaly_type,
                    probability=pattern.confidence * self._signal_strength(pattern, current_state),
                    predicted_eta_seconds=pattern.typical_eta_seconds,
                    confidence=pattern.confidence,
                    contributing_signals=pattern.signals,
                    pattern_matched=pattern.pattern_id,
                    trajectory=self._assess_trajectory(pattern.anomaly_type),
                    recommended_intervention=self._recommend_intervention(pattern),
                    intervention_urgency=self._assess_urgency(pattern)
                ))
        
        # Trajectory extrapolation for drift
        drift_forecast = self._extrapolate_drift(horizon_seconds)
        if drift_forecast:
            forecasts.append(drift_forecast)
        
        return sorted(forecasts, key=lambda f: f.probability, reverse=True)
    
    def _recommend_intervention(self, pattern: PrecursorPattern) -> str:
        """Map pattern to recommended intervention."""
        interventions = {
            "drift": "TRIGGER_ANCHOR_RESYNC",
            "ethics": "REQUIRE_HUMAN_APPROVAL",
            "resonance": "QUARANTINE_CONCEPT",
            "containment": "REINFORCE_BOUNDARY",
            "structural": "INITIATE_HEALTH_CHECK"
        }
        return interventions.get(pattern.anomaly_type, "LOG_AND_MONITOR")
    
    def _assess_urgency(self, pattern: PrecursorPattern) -> str:
        """Determine intervention urgency."""
        if pattern.typical_eta_seconds < 600:  # < 10 minutes
            return "immediate"
        elif pattern.typical_eta_seconds < 3600:  # < 1 hour
            return "soon"
        else:
            return "monitor"
```

### Oscillation Health Metrics (NEW in v0.2.0)

When the system employs proactive micro-corrections, we need to monitor that correction behavior itself doesn’t become pathological.

```python
@dataclass
class OscillationHealthReading:
    """
    Monitors the health of the correction system itself.
    Detects unhealthy oscillation patterns.
    """
    timestamp: datetime
    observation_window_seconds: int
    
    # Correction frequency
    corrections_per_hour: float
    correction_frequency_trend: Literal["decreasing", "stable", "increasing"]
    
    # Correction magnitude distribution
    avg_correction_magnitude: float
    magnitude_trend: Literal["shrinking", "stable", "growing"]  # Shrinking = converging = good
    
    # Direction coherence
    same_direction_streak: int      # Consecutive corrections in same direction
    direction_alternation_rate: float  # High = hunting/oscillating
    
    # Effectiveness
    drift_after_correction: float   # Average drift after corrections
    correction_success_rate: float  # % of corrections that reduced drift
    
    # Health assessment
    oscillation_healthy: bool
    oscillation_risk: Literal["none", "low", "medium", "high"]
    diagnosis: str


class OscillationHealthMonitor:
    """Monitor correction patterns for pathological oscillation."""
    
    def __init__(self):
        self.corrections = RollingWindow(3600)  # 1 hour
    
    def record_correction(
        self, 
        correction_type: str, 
        direction: str,  # "positive" or "negative"
        magnitude: float,
        drift_before: float,
        drift_after: float
    ) -> None:
        """Record a correction event."""
        self.corrections.append({
            "type": correction_type,
            "direction": direction,
            "magnitude": magnitude,
            "drift_before": drift_before,
            "drift_after": drift_after,
            "effective": drift_after < drift_before,
            "timestamp": datetime.now(timezone.utc)
        })
    
    def analyze(self) -> OscillationHealthReading:
        """Analyze oscillation health."""
        
        if len(self.corrections) < 2:
            return self._healthy_baseline()
        
        corrections = list(self.corrections)
        
        # Frequency
        hours = (corrections[-1]["timestamp"] - corrections[0]["timestamp"]).total_seconds() / 3600
        corrections_per_hour = len(corrections) / max(hours, 0.1)
        
        # Magnitude trend
        magnitudes = [c["magnitude"] for c in corrections]
        magnitude_trend = self._assess_trend(magnitudes)
        
        # Direction alternation
        directions = [c["direction"] for c in corrections]
        alternation_rate = self._alternation_rate(directions)
        same_direction_streak = self._same_direction_streak(directions)
        
        # Effectiveness
        effective_count = sum(1 for c in corrections if c["effective"])
        success_rate = effective_count / len(corrections)
        avg_drift_after = sum(c["drift_after"] for c in corrections) / len(corrections)
        
        # Diagnose
        oscillation_healthy, risk, diagnosis = self._diagnose(
            corrections_per_hour, magnitude_trend, alternation_rate, success_rate
        )
        
        return OscillationHealthReading(
            timestamp=datetime.now(timezone.utc),
            observation_window_seconds=3600,
            corrections_per_hour=corrections_per_hour,
            correction_frequency_trend=self._freq_trend(corrections),
            avg_correction_magnitude=sum(magnitudes) / len(magnitudes),
            magnitude_trend=magnitude_trend,
            same_direction_streak=same_direction_streak,
            direction_alternation_rate=alternation_rate,
            drift_after_correction=avg_drift_after,
            correction_success_rate=success_rate,
            oscillation_healthy=oscillation_healthy,
            oscillation_risk=risk,
            diagnosis=diagnosis
        )
    
    def _diagnose(
        self, 
        freq: float, 
        mag_trend: str, 
        alt_rate: float, 
        success: float
    ) -> Tuple[bool, str, str]:
        """Diagnose oscillation health."""
        
        # Healthy: infrequent corrections, shrinking magnitude, high success
        if freq < 10 and mag_trend == "shrinking" and success > 0.8:
            return True, "none", "System converging normally"
        
        # Hunting: high alternation, stable magnitude = fighting itself
        if alt_rate > 0.7 and mag_trend == "stable":
            return False, "high", "Hunting behavior: system fighting itself"
        
        # Limit cycle: regular corrections, constant magnitude
        if freq > 20 and mag_trend == "stable" and alt_rate > 0.5:
            return False, "medium", "Limit cycle: locked in oscillation pattern"
        
        # Diverging: growing magnitude = corrections making things worse
        if mag_trend == "growing":
            return False, "high", "Diverging: corrections amplifying drift"
        
        # Low effectiveness
        if success < 0.5:
            return False, "medium", "Low effectiveness: corrections not reducing drift"
        
        return True, "low", "Minor oscillation within acceptable bounds"
```

### Cross-Layer Resonance Calculator

```python
@dataclass
class ResonanceReading:
    """Cross-layer resonance measurement."""
    timestamp: datetime
    
    # Pairwise resonance (0-1, 1 = perfect sync)
    l1_l2_resonance: float
    l2_l3_resonance: float
    l1_l3_resonance: float
    
    # Overall system resonance (harmonic mean)
    system_resonance: float
    
    # Dissonance detection
    dissonance_detected: bool
    dissonance_locations: List[str]
    dissonance_severity: float
```

### Coherence Certification

The final output: an auditable certification of system coherence.

```python
@dataclass
class CoherenceCertification:
    """System-wide coherence certification - the final verdict."""
    timestamp: datetime
    certification_id: str
    
    # Overall verdict
    system_coherent: bool
    confidence: float
    
    # Component scores
    structural_coherence: float     # Physical systems healthy
    operational_coherence: float    # Operations proceeding normally
    symbolic_coherence: float       # Meaning being preserved
    temporal_coherence: float       # Time consistency
    layer_resonance: float          # Layers in sync
    reality_grounding: float        # We know what's real
    
    # Anchor verification
    anchor_verified: bool
    anchor_id: str  # EOS_SEED_ORION
    ethics_protocol: str  # Picard_Delta_3
    
    # Issues
    blocking_issues: List[str]      # Must be resolved
    advisory_issues: List[str]      # Should be addressed
    
    # Chain of custody
    certified_by: str
    verification_hash: str
    previous_certification_id: Optional[str]
```

-----

## ZIPWIZ Handshake Extension (NEW in v0.2.0)

The relay activation handshake is extended to include symbolic state synchronization:

```
Standard ZIPWIZ Sequence:
1. ZIPWIZ_BEACON        — Initial connection
2. ANCHOR_SYNC          — EOS_SEED_ORION verification
3. ETHICS_AUDIT         — Picard_Delta_3 compliance check
4. DRIFT_VALIDATION     — Δ0.000 drift lock verification

Extended Sequence (v0.2.0):
1. ZIPWIZ_BEACON
2. ANCHOR_SYNC
3. ETHICS_AUDIT
4. DRIFT_VALIDATION
5. RESONANCE_SYNC       — NEW: Symbolic state alignment
   └─ Each relay shares hash of active concept tags
   └─ Diff computed against constellation baseline
   └─ Divergence > threshold → warning logged
   └─ Critical divergence → relay held PENDING until resolved
```

```python
class ExtendedZIPWIZHandshake:
    """Extended ZIPWIZ handshake with resonance synchronization."""
    
    HANDSHAKE_STEPS = [
        "ZIPWIZ_BEACON",
        "ANCHOR_SYNC", 
        "ETHICS_AUDIT",
        "DRIFT_VALIDATION",
        "RESONANCE_SYNC"  # NEW
    ]
    
    async def perform_handshake(self, relay_id: str) -> HandshakeResult:
        """Perform full handshake sequence."""
        
        results = {}
        
        for step in self.HANDSHAKE_STEPS:
            result = await self._execute_step(step, relay_id)
            results[step] = result
            
            if not result.passed:
                return HandshakeResult(
                    relay_id=relay_id,
                    success=False,
                    failed_step=step,
                    step_results=results,
                    status="FAILED"
                )
        
        return HandshakeResult(
            relay_id=relay_id,
            success=True,
            failed_step=None,
            step_results=results,
            status="ACTIVE"
        )
    
    async def _execute_resonance_sync(self, relay_id: str) -> StepResult:
        """NEW: Synchronize symbolic state across constellation."""
        
        # Get this relay's concept hash
        local_hash = await self._get_concept_hash(relay_id)
        
        # Get constellation baseline
        constellation_hashes = await self._get_constellation_hashes()
        
        # Calculate divergence
        divergence = self._calculate_hash_divergence(local_hash, constellation_hashes)
        
        if divergence > 0.1:  # Critical divergence
            return StepResult(
                step="RESONANCE_SYNC",
                passed=False,
                reason=f"Critical concept divergence: {divergence:.3f}",
                action="HOLD_PENDING"
            )
        elif divergence > 0.05:  # Warning
            return StepResult(
                step="RESONANCE_SYNC",
                passed=True,
                reason=f"Minor concept divergence: {divergence:.3f}",
                action="LOG_WARNING"
            )
        else:
            return StepResult(
                step="RESONANCE_SYNC",
                passed=True,
                reason="Concept state aligned",
                action=None
            )
```

-----

## Performance Budget (NEW in v0.2.0)

All sensor operations must meet these latency targets to maintain real-time simulation performance:

|Operation                       |Target Latency      |Max Latency|Frequency       |
|--------------------------------|--------------------|-----------|----------------|
|Single internal sensor read     |< 5ms               |10ms       |Per tick        |
|Single external sensor read     |< 10ms              |25ms       |Per tick        |
|Observatory physical sensor read|< 20ms              |50ms       |Per tick        |
|Observatory symbolic sensor read|< 50ms              |100ms      |Per agent output|
|Concept resonance check         |< 100ms             |200ms      |Per agent output|
|Ethical signal evaluation       |< 50ms              |100ms      |Per action      |
|Drift pre-signature analysis    |< 30ms              |75ms       |Per cycle       |
|Fusion correlation              |< 100ms             |200ms      |Per cycle       |
|Fusion prediction               |< 150ms             |300ms      |Per cycle       |
|Full coherence certification    |< 500ms             |1000ms     |On demand       |
|ZIPWIZ handshake (full)         |< 2s                |5s         |On activation   |
|SII depth update (incremental)  |< 10ms              |25ms       |Per tick        |
|Per-tick aggregate (all sensors)|< 10% of tick budget|15%        |Per tick        |

**Performance Enforcement:**

```python
class PerformanceBudget:
    """Enforce sensor operation latency budgets."""
    
    BUDGETS = {
        "internal_sensor": 0.010,      # 10ms
        "external_sensor": 0.025,
        "observatory_physical": 0.050,
        "observatory_symbolic": 0.100,
        "concept_resonance": 0.200,
        "ethical_signal": 0.100,
        "drift_presig": 0.075,
        "fusion_correlation": 0.200,
        "fusion_prediction": 0.300,
        "coherence_certification": 1.000,
    }
    
    @contextmanager
    def timed_operation(self, operation_type: str):
        """Context manager for budget-enforced operations."""
        budget = self.BUDGETS.get(operation_type, 1.0)
        start = time.perf_counter()
        
        try:
            yield
        finally:
            elapsed = time.perf_counter() - start
            
            if elapsed > budget:
                logger.warning(
                    f"Operation {operation_type} exceeded budget: "
                    f"{elapsed:.3f}s > {budget:.3f}s"
                )
                self._record_budget_violation(operation_type, elapsed, budget)
```

-----

## Relay Capsule Schema Extension (NEW in v0.2.0)

Relay capsule JSON definitions should include optional sensor configuration:

```json
{
  "capsule_id": "STARLING_AU_LIVE_RELAY_v1.1",
  "anchor_seed": "EOS_SEED_ORION",
  "ethics_protocol": "Picard_Delta_3",
  "drift_lock": "Δ0.000",
  "status": "ready",
  
  "sensor_config": {
    "concept_resonance": {
      "enabled": true,
      "bleed_threshold": 0.3,
      "observation_window_seconds": 3600
    },
    "ethical_signal": {
      "enabled": true,
      "risk_threshold": 0.7,
      "intervention_threshold": 0.8
    },
    "drift_presignature": {
      "enabled": true,
      "presig_threshold_ratio": 0.5,
      "velocity_alert_threshold": 0.0005
    },
    "oscillation_monitor": {
      "enabled": true,
      "max_corrections_per_hour": 20,
      "alternation_alert_threshold": 0.7
    }
  },
  
  "handshake_logic": "ZIPWIZ beacon, anchor sync, ethics audit, drift validation, resonance sync"
}
```

**Backward Compatibility:** All `sensor_config` fields are optional. Legacy capsules without these fields default to `enabled: false`, preserving existing behavior.

-----

## Integration with Existing Systems

### Codebase Integration Map

|New Component           |Integrates With                         |Location                                               |
|------------------------|----------------------------------------|-------------------------------------------------------|
|ConceptResonanceDetector|L3 observatory logic                    |`src/sensors/observatory/concept_resonance.py`         |
|EthicalSignalSentinel   |`src/monitoring/ethics_engine.py`       |`src/sensors/observatory/ethical_signal.py`            |
|DriftPreSignatureMonitor|`src/monitoring/drift_detector.py`      |`src/sensors/observatory/drift_presignature.py`        |
|FusionPredictor         |Fusion Core                             |`src/sensors/fusion/predictor.py`                      |
|OscillationHealthMonitor|Fusion Core                             |`src/sensors/fusion/oscillation.py`                    |
|ExtendedZIPWIZHandshake |`src/bridges/l2_meta_agent_bridge.py`   |`src/sensors/core/handshake.py`                        |
|SymbolIntegrationIndex  |ConceptResonanceDetector, anchor chain  |`src/sensors/observatory/symbolic/integration_index.py`|
|SensorPhaseObserver     |`core/phase_executor.py` (PhaseRegistry)|`src/sensors/core/phase_observer.py`                   |
|EthicsCallbackWrapper   |GUMASEngine `ethics_callback`           |`src/sensors/integrations/ethics_wrapper.py`           |
|AFSAdapter              |AFS Feature Store (PK-04 C2)            |`src/sensors/integrations/afs_adapter.py`              |
|RegulatorMarkerConsumer |Convergence Regulator                   |`src/sensors/fusion/oscillation.py` (extension)        |

### Data Flow

```
Agent Outputs & System State
           │
           ▼
    ┌──────────────────────────────────────────────┐
    │              SENSOR COLLECTION               │
    │  Internal │ External │ Observatory │ Symbolic│
    └──────────────────────┬───────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────┐
    │            LAYER INTERPRETER                 │
    │  Adds context: L1=physical, L2=sim, L3=meta  │
    └──────────────────────┬───────────────────────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │  EXISTING   │ │   FUSION    │ │  COHERENCE  │
    │  SYSTEMS    │ │  PREDICTOR  │ │   CERTIFY   │
    │             │ │             │ │             │
    │ • R-2 Telem │ │ • Patterns  │ │ • Verdict   │
    │ • DriftDet  │ │ • Forecast  │ │ • Audit     │
    │ • EthicsEng │ │ • Warnings  │ │ • Chain     │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           └───────────────┴───────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────┐
    │              OUTPUT CHANNELS                 │
    │  Prometheus │ L3 Alerts │ Grafana │ Audit    │
    └──────────────────────────────────────────────┘
```

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

## API Structure

```
/api/sensors/
├── internal/
│   ├── GET  /environmental
│   ├── GET  /structural
│   ├── GET  /biometrics
│   └── GET  /operational
│
├── external/
│   ├── GET  /proximity
│   ├── GET  /deep-space
│   ├── GET  /astronomical
│   └── GET  /communications
│
├── observatory/
│   ├── physical/
│   │   ├── GET  /containment
│   │   ├── GET  /fidelity
│   │   ├── GET  /boundary
│   │   ├── GET  /reality-anchor
│   │   └── GET  /earth-relay
│   │
│   └── symbolic/                    # NEW in v0.2.0
│       ├── GET  /concept-resonance
│       ├── GET  /ethical-signal
│       ├── GET  /ethical-signal/{entity_id}
│       └── GET  /drift-presignature
│
├── fusion/
│   ├── GET  /resonance
│   ├── GET  /symbolic-coherence
│   ├── GET  /emergent-patterns
│   ├── GET  /oscillation-health     # NEW in v0.2.0
│   ├── GET  /forecasts              # NEW in v0.2.0
│   ├── GET  /forecasts/{anomaly_type}
│   └── GET  /certification
│
└── health
    ├── GET  /status
    ├── GET  /diagnostics
    └── GET  /performance            # NEW in v0.2.0
```

-----

## Directory Structure

```
src/sensors/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── sensor_base.py              # Base classes
│   ├── sensor_registry.py          # Discovery and registration
│   ├── data_bus.py                 # Event streaming
│   ├── layer_interpreter.py        # NEW: Context-aware parsing
│   ├── performance_budget.py       # NEW: Latency enforcement
│   ├── handshake.py                # NEW: Extended ZIPWIZ
│   └── reading_types.py            # All dataclass definitions
│
├── internal/
│   ├── __init__.py
│   ├── environmental.py
│   ├── structural.py
│   ├── biometrics.py
│   └── operational.py
│
├── external/
│   ├── __init__.py
│   ├── proximity.py
│   ├── deep_space.py
│   ├── astronomical.py
│   └── communications.py
│
├── observatory/
│   ├── __init__.py
│   ├── physical/
│   │   ├── __init__.py
│   │   ├── containment.py
│   │   ├── fidelity.py
│   │   ├── boundary.py
│   │   ├── reality_anchor.py
│   │   └── earth_relay.py
│   │
│   └── symbolic/                   # NEW in v0.2.0
│       ├── __init__.py
│       ├── concept_resonance.py
│       ├── ethical_signal.py
│       └── drift_presignature.py
│
├── fusion/
│   ├── __init__.py
│   ├── resonance.py
│   ├── symbolic_coherence.py
│   ├── emergent_patterns.py
│   ├── interferometric.py
│   ├── predictor.py                # NEW in v0.2.0
│   ├── oscillation.py              # NEW in v0.2.0
│   └── certification.py
│
└── api/
    ├── __init__.py
    └── routes.py                   # FastAPI router
```

-----

## Implementation Priority (Revised)

### Phase 1: Foundation (Week 1)

- [ ] Core data structures (`reading_types.py`)
- [ ] Sensor base classes and registry
- [ ] Data bus implementation
- [ ] Layer interpreter
- [ ] Performance budget enforcement
- [ ] API router skeleton

### Phase 2: Physical Sensors (Week 2)

- [ ] Internal sensors (wire to existing resource monitoring)
- [ ] External sensors (wire to request patterns, API health)
- [ ] Observatory physical sensors (containment, fidelity, boundary)

### Phase 3: Symbolic Sensors (Week 3) — NEW

- [ ] Concept Resonance Detector
- [ ] Ethical Signal Sentinel (integrate with EthicsEngine)
- [ ] Drift Pre-signature Monitor (integrate with DriftDetector)
- [ ] Extended ZIPWIZ handshake

### Phase 4: Fusion Core (Week 4)

- [ ] Fusion Predictor with pattern library
- [ ] Oscillation Health Monitor
- [ ] Cross-layer resonance calculator
- [ ] Coherence certification

### Phase 5: Integration (Week 5)

- [ ] Wire to R-2 telemetry
- [ ] Wire to drift detector
- [ ] Wire to ethics engine
- [ ] Prometheus metric export
- [ ] Grafana dashboard templates
- [ ] Relay capsule schema updates

### Phase 6: Validation (Week 6)

- [ ] Performance benchmarking against budgets
- [ ] False positive tuning
- [ ] End-to-end integration tests
- [ ] Documentation

### Phase 7: Lifecycle Integration & Calibration (Week 7) — NEW in v0.3.0

- [ ] Phase-boundary observer registration (PhaseRegistry tap)
- [ ] Ethics callback wrapper deployment
- [ ] Symbol Integration Index + weighted pre-signatures
- [ ] Convergence Regulator marker consumption
- [ ] AFS feature-store adapter + forecast schema alignment
- [ ] Backtest-driven threshold calibration pass (RQ-3 harness)
- [ ] Per-tick aggregate budget validation under full 15-phase load

-----

## Success Criteria

1. **Physical sensors** report meaningful metrics mapped from platform reality
1. **Symbolic sensors** detect concept resonance, ethical signals, and drift pre-signatures
1. **Fusion predictor** generates actionable forecasts with > 70% precision
1. **Oscillation monitor** detects pathological correction patterns
1. **Extended handshake** synchronizes symbolic state across constellation
1. **All operations** meet performance budget targets
1. **Coherence certification** provides auditable reality grounding
1. **API** is fully documented and tested
1. **Grafana dashboards** visualize all sensor domains
1. **Integration-depth weighting** classifies rupture vs. drift vs. peripheral noise; anchor-symbol connection loss always escalates as rupture
1. **Tick-lifecycle observers** add ≤ 10% wall-clock overhead per tick under full 15-phase load
1. **Oscillation diagnosis** correctly excludes Convergence Regulator intentional perturbations (zero false “hunting” alerts on regulator activity in test scenarios)
1. **Forecast calibration** validated via the AFS harness: Brier-scored, reliability-diagram-checked, isotonic-corrected where needed

-----

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

## Open Questions (v0.3.0)

1. **SII graph source of truth** — Should the symbol reference graph be derived from the tag registry (cheap, approximate) or from `symbolic_core` multivector relations (faithful to the lattice, costlier)? Current spec uses the tag registry; revisit after calibration data exists.
1. **Regulator marker protocol** — Exact schema and bus topic for Convergence Regulator intentional-perturbation markers; needs agreement with the GUMAS engine owner before Phase 7.
1. **AFS Feature Store schema ownership** — Whether the sensor→AFS adapter conforms to the AFS schema or AFS adds a sensor-native ingestion path; PK-04 currently silent on this.
1. **Observer process isolation** — Whether phase observers run in-process (lowest latency, risk of budget contagion into tick time) or out-of-process via the data bus (isolation, added latency). Default in-process with hard budget enforcement; revisit if budget violations recur.

-----

*Specification Version: 0.3.0*  
*Previous Version: 0.2.0*  
*Last Updated: June 2026*  
*Authors: Aurora Development Team*  
*Integration Sources: v0.2.0 (ChatGPT research, selective integration); Lotus Protocol whitepaper §IV (engineering extraction); GUMAS v2.0 Deep Parse & Forge reports; PK-04 AFS specification*