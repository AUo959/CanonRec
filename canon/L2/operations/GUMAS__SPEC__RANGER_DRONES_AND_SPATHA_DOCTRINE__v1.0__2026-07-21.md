# Ranger Drone Systems & Spatha Moderna Field Doctrine

**Domain:** GUMAS L2 / Union Marshals  
**Artifact:** Formal equipment and employment specification  
**Version:** v1.0  
**Date:** 2026-07-21  
**Certainty:** STAGING  
**Source basis:** Owner-authored Marshals narrative experiment; extends the CANON Ranger field-drone ruling in `canon/L2/operations/Marshal_Standard_Kit.md`.

## 1. Design intent

Ranger crews operate as small, autonomous law-enforcement teams with disproportionate reach. Their deployable drones are treated as ordinary field equipment: launched during arrival, ingress, pursuit, perimeter establishment, evidence handling, and contact with minimal ceremony. Drones extend Ranger perception, communications, logistics, deception, and precision force, but do not replace judgment, legal authority, or human responsibility.

The **Spatha Moderna** remains the opposite kind of instrument: visible, personal, and publicly attributable. It is both a practical close-quarters weapon/tool and a recognizable symbol of Marshal office. The combination is intentional—Rangers may shape a field remotely through distributed machines, but they still carry an unmistakable sign that a named officer stands behind the action.

## 2. Common control architecture

All Ranger drones use a shared control and evidence architecture:

- **Ranger Tactical Mesh (RTM):** encrypted, frequency-agile local network linking personnel, gunboat, drones, and authorized support platforms.
- **Human–AI cooperative tasking:** onboard autonomy handles stabilization, navigation, collision avoidance, return/recovery, sensor cueing, and nonlethal defensive reactions. It may not independently authorize lethal engagement.
- **Affirmative lethal authorization:** FPV precision munitions require a positive human command after target identification and use-of-force validation.
- **Evidence continuity:** sensor records, control inputs, authorization events, and munition employment are cryptographically time-stamped and retained for after-action and judicial review.
- **Degraded-mode operation:** drones retain limited local navigation and return behavior when links fail; mission-critical lethal action defaults to inhibit unless an already-authorized terminal command remains valid.
- **Control hierarchy:** the logistics officer normally manages fleet allocation, mesh integrity, recovery, maintenance, and data custody. Field agents may assume direct control of individual drones when tactical immediacy requires it.

## 3. Ranger drone family

Model designations describe standard capability envelopes. Ranger crews may carry local variants or mission-specific modules without creating a new class.

### RFD-1 **Kite** — Multispectrum overwatch drone

| Field | Specification |
|---|---|
| Primary role | Aerial reconnaissance, route inspection, perimeter awareness, pursuit tracking, persistent overwatch |
| Configuration | Compact folding rotor/ducted-fan platform; atmosphere-capable |
| Typical mass | ~1.8 kg |
| Endurance | ~3 hours normal loiter; ~45 minutes sustained high-speed pursuit |
| Practical control radius | ~35 km direct/mesh-assisted; extendable by relay drones |
| Sensors | Optical, low-light, thermal, lidar, acoustic direction finding, basic chemical/particulate sampling |
| Payload | Sensor package, marker beacon, micro-illuminator, small evidence tagger |
| Signature | Low acoustic and thermal profile; not true stealth |
| Limits | Weather, dense urban interference, anti-drone fire, prolonged high-speed operation |

### RFD-2 **Mote** — Interior and confined-space scout

| Field | Specification |
|---|---|
| Primary role | Interior mapping, room/duct inspection, covert observation, close-range relay |
| Configuration | Palm-sized microdrone; rotor, crawler, and perch-capable variants |
| Typical mass | 0.25–0.45 kg |
| Endurance | 45–70 minutes active; up to 8 hours passive perch monitoring |
| Practical control radius | ~3 km in open conditions; mesh-dependent inside structures |
| Sensors | Optical, thermal, short-range lidar, microphone, air-quality sampling |
| Payload | Micro-marker, fiber probe, evidence seal, limited distraction emitter |
| Signature | Very low when perched; vulnerable while moving |
| Limits | Fragile, low payload, easily lost in heavy interference or physical obstruction |

### RFD-3 **Span** — Relay and mapping node

| Field | Specification |
|---|---|
| Primary role | Communications extension, sensor-network bridging, terrain/structure mapping, navigation reference |
| Configuration | Medium endurance aerial or surface-deployed node |
| Typical mass | ~2.5 kg |
| Endurance | 8–12 hours stationary relay; 4–6 hours mobile |
| Practical network span | Up to ~80 km through chained nodes under favorable conditions |
| Sensors | Navigation lidar, spectrum survey, atmospheric/weather package, limited optical observation |
| Payload | High-gain relay, deployable micro-beacons, hardened storage cache |
| Signature | Detectable when transmitting at high power |
| Limits | Electronic warfare, terrain masking, compromised node risk |

### RFD-4 **Trace** — Evidence and hazardous-scene drone

| Field | Specification |
|---|---|
| Primary role | Evidence documentation, sample recovery, hazardous inspection, casualty-location support |
| Configuration | Stabilized aerial/surface hybrid with fine manipulators |
| Typical mass | ~4.5 kg |
| Endurance | 2–3 hours |
| Practical control radius | ~15 km; normally kept within strong mesh coverage |
| Sensors | High-resolution imaging, multispectrum scanner, radiation/chemical/biological hazard suite |
| Payload | Sealed sample cells, evidence markers, compact manipulator, emergency medical drop |
| Evidence features | Continuous chain-of-custody log and tamper-evident storage |
| Limits | Slower than combat scouts; manipulators cannot replace full forensic personnel |

### RFD-5 **Porter** — Resupply and recovery drone

| Field | Specification |
|---|---|
| Primary role | Ammunition, medical, power-cell, tool, component, and mission-payload delivery |
| Configuration | Heavy multirotor/grav-assist cargo platform; atmospheric and limited zero-g variants |
| Empty mass | ~22 kg |
| Normal payload | Up to ~45 kg; reduced by range, altitude, and environmental conditions |
| Endurance/range | ~90 minutes or ~60 km under standard load |
| Payload interfaces | Secured cargo frame, medical pod, power-transfer coupling, casualty drag harness |
| Defensive behavior | Evasive routing, decoy release, return/ditch logic; no independent weapons authority |
| Limits | Visible, noisy, vulnerable under direct fire, maintenance intensive |

### RFD-6 **Mirage** — Decoy and countermeasure drone

| Field | Specification |
|---|---|
| Primary role | False signatures, sensor exposure, withdrawal support, counter-drone and electronic deception |
| Configuration | Modular aerial or ground emitter platform |
| Typical mass | ~3.2 kg |
| Endurance | 60–90 minutes active deception; longer passive decoy life |
| Effects | Simulated personnel/vehicle emissions, false transponder traffic, directional noise/light, limited jamming and spoofing |
| Counter-drone role | Detection cueing, link disruption, expendable interception screens |
| Limits | Effects are temporary and legally constrained; strong use may reveal Ranger presence |

### RFM-7 **Javelin** — FPV precision munition

| Field | Specification |
|---|---|
| Primary role | Operator-directed precision strike against a validated hostile person, vehicle, weapon, drone, or infrastructure point |
| Configuration | Expendable high-speed FPV platform with mission-selectable effect package |
| Typical launch mass | 4–9 kg depending on payload |
| Endurance | 20–35 minutes loiter or ~25 km direct pursuit under normal conditions |
| Control | Direct operator view with AI stabilization, obstacle avoidance, and target-cue assistance |
| Authorization | Positive human lethal command required; no autonomous target selection or engagement |
| Effect packages | Anti-personnel, anti-materiel, breaching, electronic-disruption, or nonlethal disabling packages; exact yields are mission controlled |
| Safeties | Biometric control link, geofencing, target-confirmation gate, abort/self-neutralization, full event logging |
| Limits | Vulnerable to jamming, interception, concealment, civilian proximity, and restrictive rules of engagement |

## 4. Standard carriage and deployment

A Ranger-class gunboat is the launch, recovery, recharge, repair, data-ingestion, and control platform for the crew’s organic drone complement. Counts are deliberately variable. A routine independent patrol may carry approximately 12–24 active drones plus reserve airframes and expendable munitions; a supported special-service deployment may carry materially more.

Typical ready posture:

- 2–4 drones already airborne or deployed before personnel dismount in an uncertain environment.
- At least one persistent overwatch node and one communications path held in reserve.
- Interior scouts staged for immediate release from armor, packs, or vehicle dispensers.
- Porter and evidence drones normally launched from the gunboat rather than carried by field agents.
- FPV munitions remain physically and digitally safed until mission authority permits readiness.

## 5. Preferred crew loadouts — *Third Measure*

These are preferred starting allocations, not rigid personal ownership. Maelin may rebalance the drone pool as conditions change.

### Tessa Korr — Command and forced-tempo package

**Preference:** fast visibility, controlled pressure, immediate options.

- 2 × Kite overwatch drones
- 2 × Mote interior scouts
- 1 × Mirage decoy/countermeasure drone
- 1 × Porter held at gunboat readiness
- 2 × Javelin FPV munitions held in reserve

Tessa prefers a simple, legible field picture and drones that can rapidly expose threats, close escape routes, or create a decisive opening. She is most likely to request a Javelin into ready status early, which can create friction when Iven believes the evidence picture is incomplete.

### Iven Raal — Pursuit and reconstruction package

**Preference:** persistent observation, distributed tracking, quiet corroboration.

- 1 × Kite overwatch drone
- 4 × Mote scouts/perch sensors
- 2 × Span relay/mapping nodes
- 1 × Trace evidence drone
- 1 × Javelin FPV munition as contingency

Iven favors depth over spectacle. His preferred network watches exits, reconstructs movement, and preserves evidence across time. He often leaves drones in place after the apparent conclusion of an operation because he expects the most revealing behavior to occur when a target believes surveillance has ended.

### Maelin Saye — Field-shaping and network-control package

**Preference:** layered awareness, communications dominance, deception, and logistical control.

- 2 × Kite overwatch drones
- 2 × Mote scouts
- 3 × Span relay/mapping nodes
- 1 × Trace evidence drone
- 2 × Mirage decoy/countermeasure drones
- 2 × Porter drones at variable readiness
- 2 × Javelin FPV munitions held under dual-confirmation workflow

Maelin’s loadout is a system rather than a collection of airframes. They use relay placement, decoys, supply timing, and sensor coverage to change the geometry of the operation before the field agents perceive the full effect. They may autonomously launch, position, retask, and recover nonlethal drones within mission orders. Lethal employment remains human-authorized.

## 6. Spatha Moderna — formal field specification

### Identity

- **Formal name:** Spatha Moderna
- **Common name:** *spade*
- **Category:** Powered field sword / Marshal badge-of-office weapon
- **Issue:** Standard to sworn Ranger personnel and other qualified Marshal field personnel; carried openly when local law and mission posture permit

### Physical specification

| Field | Specification |
|---|---|
| Overall length | ~92 cm |
| Blade length | ~70 cm |
| Mass | ~1.7 kg including integral power cell |
| Blade | Durable high-density composite/metallic laminate capable of functioning unpowered |
| Powered edge | Contained energizing field that improves cutting against armor, locks, barriers, and hardened materials |
| Power modes | Safe/inert, utility cut, combat edge, short-duration breach overdrive |
| Authentication | Marshal ident-key and biometric grip recognition |
| Carry system | Powered locking scabbard with recharge, condition monitoring, and draw-event logging |
| Failure mode | Remains a functional physical sword if power or network systems fail |

### Practical doctrine

The Spatha Moderna is retained because it remains useful in:

- confined boarding and urban interiors where long guns are awkward;
- close defense when ammunition, power, or communications are degraded;
- shield-heavy engagements where sustained contact can matter more than a single ranged impact;
- cutting doors, restraints, wreckage, cables, and emergency access points;
- weapon-retention situations where a holstered sidearm may be easier to seize;
- environments where electronic warfare may suppress more complex weapons.

It is not an all-purpose answer. Drawing it against a firearm in open space is generally poor tactics unless shielding, cover, surprise, or exceptional proximity changes the balance.

### Symbolic doctrine

The visible sword is a public declaration of Marshal identity and accountability. It communicates that:

- the bearer exercises Union authority in person rather than through an anonymous remote system;
- the bearer is expected to enter danger rather than merely direct it from safety;
- force, when used, is attributable to a sworn officer operating under law;
- the Marshal tradition survives technological disruption and remains legible when networks, uniforms, or credentials fail.

In many civilian settings, Rangers and other Marshal field personnel are among the only people openly carrying swords. The sight is therefore distinctive and consequential. It may reassure, intimidate, provoke resentment, or immediately alter a room’s social hierarchy.

### Escalation meaning

The Spatha is **worn, not brandished**. Marshal doctrine is diplomacy-first and lethal-when-drawn: in a confrontation, drawing the blade is a commitment to immediate force rather than an intermediate display or theatrical warning.

- **Carried openly:** normal Marshal presence; authority is visible without escalation.
- **Hand on hilt or scabbard release:** final warning and readiness signal. The blade remains sheathed while a peaceful resolution is still being offered.
- **Drawn in confrontation:** committed-force threshold. The Marshal has concluded that immediate force is legally justified and tactically required; the blade may remain unpowered or be energized according to the threat, target, and proportionality requirements.
- **Powered edge engaged:** effect selection within an already committed use of force, not a separate first threshold for seriousness.
- **Utility draw:** permitted for rescue, cutting, or breaching when the noncombat purpose is unmistakable from context and conduct.
- **Breach overdrive:** extraordinary utility or combat mode; logged automatically and subject to after-action review.

## 7. Sword–drone interaction in Ranger identity

Rangers carry two contrasting forms of power:

- **Distributed power:** drones observe, relay, deceive, supply, and strike from beyond the immediate body.
- **Embodied power:** the Spatha Moderna remains visible on the officer who is legally and morally responsible for the operation.

This contrast is operationally useful and culturally intentional. A Ranger may command a remote network capable of shaping an entire engagement, yet still enter the scene wearing a weapon that makes their office, presence, and accountability impossible to mistake.

## 8. Open parameters for later CanonRec CI

- Whether exact drone counts should be standardized by Ranger mission category.
- Formal manufacture/vendor names and maintenance intervals.
- Exact effect-package taxonomy for Javelin munitions.
- Historical origin of the open-sword tradition.
- Local-jurisdiction rules governing visible carry during covert or diplomatic operations.

Until these are resolved, no narrower claim should be inferred.