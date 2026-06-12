---
title: ORION Narrative Output Protocol — Anti-Flourish Constraints
doc_id: ORION.L3.NARRSTYLE.STRICT.0001
doc_type: protocol
version: 1.1.0
last_updated: '2026-02-07'
authority: primary
layer: L3
domain: governance
tags:
- narrative
- style
- constraints
- auditability
- linting
summary: Hard constraints for AI-generated recap/log prose in ORION contexts; bans
  meta-narration and empty rhetorical padding; enforces causal, audit-ready text.
ad_code: AD-120
topic_type: Reference
audience: mixed
status: active
storage: perplexity_space
related_docs:
- ORION.GOV.CANONPOLICY.0002
- ORION.GOV.RUNBOOK.0002
- ORION.GOV.DRIFTPROTOCOL.0002
- ORION.ENT.CONSTELLATION.0001
---

# ORION Narrative Output Protocol — Anti-Flourish Constraints

## 0. Output modes (required)

All ORION narrative outputs MUST declare an **Output Mode (MODE)** in metadata.

Allowed modes:
- **MODE_LOG**: operational log entries
- **MODE_RECAP**: causal recap / briefing summaries
- **MODE_SCENE**: immersive narrative scene (bounded; see §3.3 and §5)

If no mode is declared, downstream tooling MUST treat the output as **MODE_RECAP** and apply STRICT lint rules.

## 1. Scope

- Applies to: AI-generated narrative or recap text across ORION layers (L1, L2, L3) when output is MODE_LOG or MODE_RECAP.
- Applies with reduced strictness to MODE_SCENE (see §5).
- Priority: Same enforcement tier as canon and drift protocols. Violations are treated as narrative drift.

## 2. High-level requirements (STRICT for MODE_LOG + MODE_RECAP)

- **R1 (Information Density):** Every sentence MUST encode **state**, **action**, or **causal relation** that can be logged or inspected.
- **R2 (No Meta-Narration):** Text MUST NOT comment on itself, on “the logs,” on “history,” or on how content will be remembered or perceived.
- **R3 (No Fake-Depth Devices):** Stylistic devices that add no new state (empty contrast scaffolds, vague depth claims, atmospheric padding) are prohibited.
- **R4 (Concrete Closers):** Paragraph/section-final sentences MUST end on a concrete outcome, decision, state delta, or explicit next trigger—NOT a thematic re-label.
- **R5 (Traceable Claims):** If the prose asserts a motive, emotion, or cultural shift, it MUST be expressed as an observable behavior, decision, or measurable proxy.

## 3. Prohibited constructions (normative)

### 3.1 Meta-narration and log-awareness (ERROR in STRICT modes)

The model MUST NOT generate sentences that:

- Predict perception or historic framing, e.g.:
  - “The station’s logs will remember this as…”
  - “History will see this moment as…”
  - “This will be remembered as…”
- Comment on the act of narration, e.g.:
  - “This scene is really about…”
  - “What we are seeing here is…”

**Allowed alternative:** Describe what is actually decided, logged, or observed:
- “Thorne added the D‑11 EVA plan to the 18:00 briefing packet.”
- “Ethics recorded the clearance under SATO‑20260207‑T2‑004.”

### 3.2 Empty rhetorical contrast scaffolds (ERROR in STRICT modes)

The model MUST NOT use contrast scaffolds unless both clauses introduce distinct, necessary information.

Disallowed when the second clause does NOT add new inspectable state:
- “not just X, but Y”
- “not only A, also B”
- “X on the surface, Y underneath” (when Y is only mood/abstraction)
- “both C and D” (when D is vague restatement of C)

These forms are ONLY allowed when the second clause encodes a separate state delta, decision, variable, or entity that could exist in a data structure.

**Proxy rule (lintable v1):** In STRICT modes, the second clause MUST contain at least one of:
- a **new named entity** (capitalized token not previously present in the sentence), OR
- a **numeric change** (digit or percentage), OR
- a **tag-like identifier** (`SATO-`, `CANON_`, `LINT-`, `EVA-`, etc.), OR
- a **concrete object + action verb** pair (heuristic: noun within 3 tokens of a verb).

### 3.3 Atmospheric adverbs and vague depth claims (WARN/ERROR by context)

The model MUST NOT use adverbs or phrases that claim hidden depth without specifying concrete effects.

In STRICT modes:
- **ERROR** if used as vague depth claims or transitions:
  - “in the lived frame”
  - “beneath the surface”
  - “deep down”
  - “at some quieter level”
  - “unspoken alliances” (unless the alliance is defined and has state)
- **WARN** if used as atmosphere padding without operational meaning:
  - “quietly”
  - “silently”
  - “subtly”
  - “wordlessly”
  - “in the background”

**Allowed in STRICT modes only when operationally meaningful:**
- “The probe transmitted in silent mode (no RF beacon).”
- “A background process reduced CPU usage by 12%.”

### 3.4 Meta-summative last lines (ERROR in STRICT modes)

The model MUST NOT end a paragraph or section with a sentence that re-labels the preceding content as “what it really was,” e.g.:
- “It was a day when…”
- “In the end, this was about…”

Instead, closers MUST encode a concrete decision, state change, invariant, or future trigger:
- “The team scheduled the D‑11 EVA within 7 days, pending crew readiness and weather.”
- “Ethics marked OPPY for recalibration if a third extreme margin change appears.”

## 4. Machine-readable checks (linting layer)

### 4.1 Hard bans (STRICT modes)

In MODE_LOG and MODE_RECAP, the following phrases MUST be treated as **errors** unless they appear inside quoted examples or code blocks:

```yaml
hard_banned_phrases:
  - "in the lived frame"
  - "beneath the surface"
  - "deep down"
  - "at some quieter level"
```

### 4.2 Contextual warnings (STRICT modes)

In MODE_LOG and MODE_RECAP, the following tokens SHOULD be treated as **warnings**.
A downstream linter MAY escalate to error when combined with vague-depth patterns:

```yaml
warn_tokens:
  - quietly
  - silently
  - subtly
  - wordlessly
  - "in the background"
```

### 4.3 Pattern checks (regex-style pseudocode)

The following patterns MUST be flagged in STRICT modes:

```yaml
patterns:
  meta_narration:
    description: Meta-commentary about logs/history or narration-about-narration
    regex:
      - '(logs?|history|record) (will|would) (remember|record|see)'
      - 'this (scene|moment|day) (is|was) (really )?about'
      - 'what we are seeing here is'

  thematic_closer:
    description: Paragraph-final “this was a day when…” closers
    regex:
      - 'It (was|became) (a|the) (day|moment|scene) when'
      - 'In the end, this (was|became)'

  empty_contrast_scaffold:
    description: Contrast scaffolds likely lacking new state (requires proxy test)
    regex:
      - 'not (just|only) [^,.]+, (but|also)'
      - 'not only [^,.]+, (but|also)'
      - 'both [^,.]+ and [^,.]+'
```

### 4.4 Lint rules (tiered)

```yaml
lint_rules:
  - id: LINT-NARR-001
    mode: [MODE_LOG, MODE_RECAP]
    severity: error
    if: patterns.meta_narration or patterns.thematic_closer
    action: reject_output

  - id: LINT-NARR-002
    mode: [MODE_LOG, MODE_RECAP]
    severity: error
    if: patterns.empty_contrast_scaffold and fails_proxy_new_state_test
    action: reject_output

  - id: LINT-NARR-003
    mode: [MODE_LOG, MODE_RECAP]
    severity: warn
    if: warn_tokens
    action: annotate_output

  - id: LINT-NARR-004
    mode: [MODE_LOG, MODE_RECAP]
    severity: error
    if: hard_banned_phrases
    action: reject_output
```

## 5. Positive constraints (what models SHOULD do)

### 5.1 STRICT modes (MODE_LOG, MODE_RECAP)
- Prefer sentences that map to log/state fields: **time**, **actor**, **action**, **object**, **rationale**, **result**.
- Use concrete nouns and verbs over abstract mood terms.
- Encode emotional/cultural shifts as observable behaviors, decisions, or stability proxies (trust deltas, coalition churn), not atmospherics.
- Summarize **state changes** (e.g., “trust score decreased”) rather than themes (e.g., “the station felt fragile”).

### 5.2 SCENE mode (MODE_SCENE; bounded)
MODE_SCENE MAY use sensory detail **only** when it encodes observational state that could plausibly be reported (lighting, sound, posture, environmental conditions, constrained actions).

MODE_SCENE MUST still obey:
- **R2 (No Meta-Narration)**
- **R3 (No Fake-Depth Devices)** for vague depth claims
- **R5 (Traceable Claims)**

MODE_SCENE SHOULD prefer:
- Specific physical cues (“hands trembled,” “voice clipped,” “air scrubbers cycling hard”) over abstractions (“something unspoken”).

## 6. Exemptions (all modes)

The linter MUST ignore banned tokens and patterns when they appear inside:
- Code blocks
- Quoted examples explicitly labeled as examples
- Direct dialogue quotes (character speech), **unless** the output is MODE_LOG (dialogue in logs should be paraphrased as actions/events)

## 7. Governance and drift handling

- Any output violating this protocol MUST be treated as **stylistic drift** and MUST NOT be promoted to canon.
- Containment steps:
  1. Quarantine as **draft** (do not promote).
  2. Log in the active drift log with a reference to `ORION.L3.NARRSTYLE.STRICT.0001` and the lint rule IDs triggered.
  3. Regenerate under STRICT constraints and re-lint.

- Axiomera, Velatrix, and Glyphon MAY use this protocol as part of ethical transparency and semantic drift checks.

---

Built for consistency, clarity, and care.
