---
doc_type: L2_SIM_DERIVATION
doc_id: L2.SIM.MARSHAL.CHARTER.0001
version: 0.1.0
status: CANON (Articles I-III, V) / APPROX (Article IV) — owner-approved promotion 2026-07-20
layer: L2
controller: ORION
engine: GUMASAdvancedEngine (GUMAS_SIM_2.5/SIM_ENGINE_OUTPUTS)
runs: seeds 42 (canonical), 7, 99 — 40 turns each, deterministic
run_artifact: SIM_ENGINE_OUTPUTS/MARSHAL_CHARTER_RUN__seed42__2026-07-20.json
created: 2026-07-20
closes: LEDGER-CHARTER-0001..0004 (draft answers), Grand Marshal incumbent (LEDGER-MARSHALS-0006 open item)
---

# MARSHAL CHARTER v0.1 — Simulation-Derived Draft
## Union Marshals: Legal Scopes, Judicial Council Design, Chronology, SHC Incumbent

**Method statement (honesty discipline):** every parameter below is either (a) read
directly from deterministic engine output, (b) derived by a stated mapping rule from
engine output, or (c) selected from already-canon named material by a stated
deterministic rule. Nothing is free-invented. Where the engine cannot speak (calendar
dates), the value is expressed relatively and tagged APPROX.

---

## 0) Engine Findings Used (receipts)

| # | Finding | Value | Seeds |
|---|---|---|---|
| F1 | Saros oversight_resistance drifts upward in-run (MORAL_LICENSING) | 0.30 → 0.65 over 40 turns | 42, 7, 99 (invariant) |
| F2 | Chancellor (Zylox) public legitimacy collapses | 0.000 / 0.074 / 0.032 at T40; elite support 0.10–0.22 | all seeds |
| F3 | Senate speaker (Valcor) legitimacy stable | 0.700 at T40 | all seeds |
| F4 | Saros escalation_threshold below median | 0.45 | structural |
| F5 | GU covert ops get exposed | espionage_exposure events T7, T11 (seed 42) | 42 |
| F6 | GU canonical leadership roster size | 9 | structural |
| F7 | Systemic risk chronically elevated | risk 0.548–0.593, stability 0.450–0.485 at T40 | all seeds |
| F8 | GU early-escalation cadence | military_escalation T1 (Velar), T3/T13 (AI Warlords); tech breakthrough T6 | 42 |

---

## Article I — Local-Police Override Trigger (closes LEDGER-CHARTER-0001)

Mapping rule: F1 (the Marshals' own chief grows oversight-resistant over time) forbids a
Marshals-internal trigger; F2 (executive legitimacy collapse in every seed) forbids a
Chancellor-controlled trigger; F3 anchors checks in the Senate/independent-council side.

Three-tier regime:

1. **Standard tier — Union Warrant.** Override of planetary authorities requires a Union
   warrant issued by a **Judicial Council duty magistrate** on a showing of cross-boundary
   nexus (jurisdiction already CANON). Local-corruption findings are *grounds for a warrant
   application*, never self-executing authority.
2. **Exigent tier — Chief Marshal certification.** Where delay defeats the pursuit, the
   Chief Marshal may certify a **cross-sector nexus** override effective immediately,
   valid a maximum of **one operational cycle**, with mandatory retroactive Judicial
   Council review. (Short window is forced by F4: an escalation-prone service must not
   hold long unilateral authority.)
3. **Emergency tier — Senate declaration.** Theater-wide overrides require a Senate
   emergency declaration (F3: the legitimacy-stable organ), lapsing automatically unless
   renewed.

## Article II — Diplomatic Immunity Scope (closes LEDGER-CHARTER-0002)

Mapping rule: archive text is purpose-bound ("to chase criminals across borders"); F5
(covert operations do get exposed in-engine) demands a liability channel; corrupt-local-
government canon weakness demands that channel not run through local courts.

- Immunity is **official-acts immunity attached to a registered pursuit order** — not
  blanket personal immunity. No registered order, no immunity.
- **Waiver:** a host government may petition the Judicial Council for waiver; the Council
  decides, not the Chancellery (F2) and not local courts (canon weakness).
- **Liability:** alleged unlawful operations are tried before the **High Judiciary &
  Galactic Tribunal** on referral by the Judicial Council's investigative review. Marshals
  remain individually liable for acts outside the registered order's scope (F5 makes
  exposure, and therefore adjudication, a live institutional need).

## Article III — Judicial Council Design (closes LEDGER-CHARTER-0003)

Mapping rules: council size mirrors the canonical GU leadership bench (F6 = 9);
appointment anchored per F2/F3; suspension supermajority set at the Senate-side
escalation threshold band (Valcor 0.6 → ⅔).

- **Composition:** **nine jurists**, fixed staggered terms.
- **Appointment:** nominated by the Chancellor, **confirmed by the Union Senate** — the
  same pattern as the Chief Marshal (already CANON), keeping the volatile executive (F2)
  from owning the bench.
- **Status:** hybrid — an **administrative-judicial oversight organ**, not a trial court.
  Trial and appellate functions belong to the **High Judiciary & Galactic Tribunal**;
  the Council's magistrates issue warrants (Art. I), receive the Chief Marshal's reports
  (CANON), run investigative review of completed operations, and refer cases to the
  Tribunal (Art. II).
- **Suspension power:** the Council may suspend a specific Marshal operation by
  **supermajority (6 of 9)**; suspension of Sentinel deployments additionally notifies
  the Senate (F1 drift-check: the strongest check aims at the strongest capability).
- **Appeals:** Council warrant/waiver decisions are appealable to the Tribunal.

## Article IV — Durn Chronology (closes LEDGER-CHARTER-0004, tag APPROX)

The engine cannot produce calendar dates; chronology is **relative, in Union cycles**,
anchored at the Zylox–Durn Pact (= cycle 0). Interval structure follows engine cadence
(F8: program start → first breakthrough ≈ 6 turns; first external escalation waves at
T1–T3, recurring AI-Warlord pressure by T13).

| Cycle (rel.) | Event | Basis |
|---|---|---|
| 0 | Zylox–Durn Pact; Marshal Academy chartered | CANON (retcon) |
| +4 | First Sentinel cohort graduates; suits enter field service | Academy pipeline ≈ engine tech-breakthrough cadence (F8) |
| +6 | AI-Warlord escalation wave pulls Durn to Supreme Military Command | F8 recurring GU↔AI-Warlord aggression; coheres with canon "Oversaw AI Countermeasures" |
| +6 | **Saros confirmed Chief Marshal — immediate succession, no interim** | Parsimony rule: no interim leader exists in any canonical roster (F6 closed set) |
| ≥ +8 | World Bible v0.2 snapshot era (Saros "Expanded Sentinel Deployments") | CANON ordering constraint |

Calendar anchoring deferred until a canonical GU calendar exists; do not invent dates.

## Article V — Grand Marshal Incumbent (closes LEDGER-MARSHALS-0006 open item)

Deterministic selection rule — no invention: the incumbent must be (a) already named in
promoted canon, (b) a Sentinel-Praetor (the "Field Marshal" command variant, ~30 in
service), (c) the highest-seniority named Praetor commander, and (d) free of engine-roster
collision.

Unique qualifier: **Commander Aric Thal** — Sentinel-Praetor, mission author/lead of
Operation Silent Dagger (LEDGER-MISSIONS-0001, CANON-promoted ledger). Engine check:
`aric_thal` absent from all leader rosters, all seeds — no collision (verified in run).

→ **Grand Marshal Aric Thal**, Sentinel High Command (STAGING). His SHC seat coheres
with Praetor doctrine ("Battlefield command / Field Marshal unit") and the SHC's
direct advisory uplink to the Chancellor & Military High Command.

---

## Certainty & routing

- Articles I–III, V: **CANON** — owner-approved "Marshals Charter Promotion Pass —
  2026-07-20"; locked at commit.
- Article IV: **APPROX** by design (relative chronology only; calendar anchoring deferred
  until a canonical GU calendar exists).
- Out of this pass's scope, still STAGING: Sentinel-Diplomat variant (LEDGER-SENTINEL-0005),
  Judicator Prime "supercarrier" gloss (CL-04c UNCONFIRMED).
- This document extends, and does not modify, the CANON addendum Parts I–III.
- Claim ledger: CL-14 (charter articles), CL-15 (Grand Marshal Aric Thal),
  CL-16 (relative chronology).

## Promotion Receipt

Owner approval: 2026-07-20 session ("perform the promotion pass"). Entities locked in the
same commit: org_judicial_council (STAGING→CANON, charter design fields), 
org_sentinel_high_command (STAGING→CANON, incumbent Grand Marshal Aric Thal CANON),
org_union_marshals (charter fields CANON; oversight block CANON). Engine receipts:
SIM_ENGINE_OUTPUTS/MARSHAL_CHARTER_RUN__seed42__2026-07-20.json (root repo, commit 751218a).
