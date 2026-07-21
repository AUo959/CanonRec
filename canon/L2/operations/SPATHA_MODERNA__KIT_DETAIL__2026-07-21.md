# Spatha Moderna — Kit Detail (CANON)

**Promotion:** Spatha Promotion Pass — 2026-07-21 (owner-authorized). Ratifies the owner's
"canon locked" declarations from the 2026-02-01/02 design thread (raw archive
`ZIP_Archives/9c9ce296…/conversations.json`) and observed use in the L2 sim capture
(`L2_SIM_CAPTURE__MARSHALS_RANGER_SENTINEL__v1.0.md` §4). Gap analysis:
root `reports/analysis/spatha_context_report__2026-07-21.md`.
**Parent record:** `Marshal_Standard_Kit.md` (this file carries the detail behind its one-line entry).

## Naming (three-layer structure, owner-locked)

| Register | Name |
|---|---|
| Formal / doctrinal | **Spatha Moderna** (plural *spathae* in formal registers) |
| Marshal internal | **spade** |
| Civilian / frontier | *spade*, "Marshal blade", "that thing they carry" |

- "Moderna" = *current, adapted, fit for present conditions* — a variant designation in the
  historical pattern (*gladius hispaniensis*, *usus modernus*), not futurism.
- Etymology (design rationale): spatha → *spada / espada / épée / spade* — "the frontier
  didn't invent a nickname; it inherited one."
- Historical anchor: the Roman spatha — longer one-handed institutional sword; "a reach
  extension for authority operating in less controlled spaces."
- Pronunciation: SPA-thuh (/ˈspæ.θə/); frontier dialect drift ("spather", "spath", "spade")
  expected and historically apt.

## Physical description (owner-locked constraints)

- **Katana-like profile** (more than longsword/rapier); slightly curved, single-edge dominant
- Strong thrusting point; geometry supports **slashing, lopping, and thrusting** (sim-observed)
- **Powered blade**; modern materials and power integration; decisive-strike emphasis
- One-handed; substantial enough for **sword-and-board** tactics — employed with the
  one-handed deployable shield in close-quarters engagements (sim-observed)
- Traditionally worn at the hip; personal variations develop in the field
- Worn opposite the MR-6 sidearm

## Doctrine & cultural register

- **Class:** Marshal close-engagement authority blade; recognized symbol of Marshal
  authority across the frontier — a combat implement **and** a visible marker of office
- **"Worn, not brandished. Drawn only when something has already gone wrong."**
- Diplomacy-first, lethal-when-drawn: Marshals seek diplomatic solutions as a matter of
  course, but once swords are drawn they commit (2026-02-03 forensic sweep, confirmed)
- Kit linguistic asymmetry (deliberate): only the anomalous tool gets a distinct name —
  **Spade** (Spatha Moderna) / **Iron** (MR-6) / **Viper** (MFR-9). "Spade and Viper" is
  frontier shorthand for a Ranger team's presence.
- Locked usage idioms: "Secure your spade." / "If the spades come out, it's over." /
  "He didn't draw the spade—went straight to iron."

## Provenance chain

1. DuelSim historical-fencing research track (HIST_FENCE_CORE scaffold, real-world spatha)
2. Design thread 2026-02-01/02: gladius→spatha analysis → *Spatha/Spade* lock →
   *Spatha Moderna* formal lock → kit canvas v1.0/v1.1
3. `Marshal_Standard_Kit.md` (one-line canon distillation)
4. L2 sim capture (observed use; §9 L1 promotion, honored by this pass)
5. Union Marshals dossier 2026-07-20 (promotion table receipt)

**Certainty: CANON** (locked at commit, Spatha Promotion Pass 2026-07-21).
Not established (do not invent): blade length/mass figures, power-cell mechanism,
manufacturer, issue date, training curriculum.

---

## G5 addendum — equipment records & crew capsules (2026-07-21)

Equipment-class entity records created (CANON, `canon/L2/entities/equipment/`):
`eq_spatha_moderna`, `eq_mr6_service_revolver`, `eq_mfr9_viper_rifle`,
`eq_marshal_energy_shield`. Ranger gunboat recorded as `vessel_gu_015`
(CLASS-RANGER-01; crew Cross/Vorn/Roake; ship name pending ratification; carries the
P2 `placement_rule`).

CharForge capsules built for all four capture actors (`charforge-capsule-v1.0`,
7 files + BUILD_RECEIPT + bundle manifest each). **First rollout of `location_binding`**
(C1, RULING-FABRIC-SCHEMA): Cross/Vorn/Roake bind to `vessel_gu_015`; Kade binds to
`org_sentinel_high_command`.

State-vector derivation rule (deterministic, auditable): baseline 0.500 on all 21 slots;
evidence-based deltas only, |Δ| ≤ 0.2, big-endian float32 per existing capsule precedent.
Each BUILD_RECEIPT records its own basis. No invented psychology — deltas trace to
capture-observed behavior only.
