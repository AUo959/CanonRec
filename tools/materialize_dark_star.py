from __future__ import annotations

# Triggered after workflow registration; this materializer is intentionally one-use.

import base64
import json
import zlib
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TARGET = REPO / "canon/L2/narratives/GUMAS_L2__NARRATIVE__DARK_STAR_ARC_UNIFIED__v1.1__2026-07-22.md"
OLD = REPO / "canon/L2/narratives/GUMAS_L2__NARRATIVE__DARK_STAR_ARC_CHAPTER_03_THIRD_SILENCE__v1.0__2026-07-22.md"
EVENT = REPO / "canon/L2/events/event_dark_star_incident_4718_224.json"
DRIFT = REPO / "DRIFT_LOG.md"
PARTS = [
    REPO / "tools/dark_star_payload_00.b64",
    REPO / "tools/dark_star_payload_01.b64",
    REPO / "tools/dark_star_payload_02.b64",
    REPO / "tools/dark_star_payload_03.b64",
    REPO / "tools/dark_star_payload_04.b64",
    REPO / "tools/dark_star_payload_05.b64",
    REPO / "tools/dark_star_payload_06.b64",
]
TARGET_REF = "canon/L2/narratives/GUMAS_L2__NARRATIVE__DARK_STAR_ARC_UNIFIED__v1.1__2026-07-22.md"
OLD_REF = "canon/L2/narratives/GUMAS_L2__NARRATIVE__DARK_STAR_ARC_CHAPTER_03_THIRD_SILENCE__v1.0__2026-07-22.md"


def materialize_manuscript() -> None:
    payload = "".join(part.read_text(encoding="utf-8") for part in PARTS)
    content = zlib.decompress(base64.b64decode("".join(payload.split()))).decode("utf-8")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(content, encoding="utf-8")


def supersede_old_chapter() -> None:
    text = OLD.read_text(encoding="utf-8")
    text = text.replace("status: canon", "status: superseded", 1)
    marker = "parent_event: event_dark_star_incident_4718_224\n"
    addition = (
        "parent_event: event_dark_star_incident_4718_224\n"
        f"superseded_by: {TARGET_REF}\n"
        "supersession_note: Preserved for provenance; the unified v1.1 manuscript governs narrative wording, translation behavior, and continuity.\n"
    )
    if "superseded_by:" not in text:
        text = text.replace(marker, addition, 1)
    OLD.write_text(text, encoding="utf-8")


def update_event_graph() -> None:
    data = json.loads(EVENT.read_text(encoding="utf-8"))
    refs = [r for r in data.get("source_refs", []) if r != OLD_REF]
    if TARGET_REF not in refs:
        refs.insert(1 if refs else 0, TARGET_REF)
    data["source_refs"] = refs
    data["governing_narrative_ref"] = TARGET_REF
    superseded = data.setdefault("superseded_narrative_refs", [])
    if OLD_REF not in superseded:
        superseded.append(OLD_REF)
    data["translation_recording_policy"] = {
        "status": "CANON",
        "rule": "Shadow personnel speak fluently in their own language. Fragmentation, substitutions, confidence warnings, and subtle errors belong to the live Union translation system rather than to speaker competence.",
        "evidentiary_boundary": "Translated output is a provisional instrument record and may be revised by later context; it does not function as an omniscient gloss."
    }
    passes = data.get("promotion_pass", "")
    label = "Dark Star Unified Manuscript and Translation Improvement Pass — 2026-07-22"
    if label not in passes:
        data["promotion_pass"] = f"{passes}; {label}" if passes else label
    data["updated_at"] = "2026-07-22"
    note = data.get("notes", "")
    extra = "Unified narrative v1.1 governs prose and live-translation presentation; prior chapter-only narrative remains provenance only."
    if extra not in note:
        data["notes"] = (note.rstrip() + " " + extra).strip()
    EVENT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_drift_log() -> None:
    heading = "## Drift Entry — 2026-07-22 (Dark Star Unified Manuscript and Translation Improvement Pass)"
    if DRIFT.exists() and heading in DRIFT.read_text(encoding="utf-8"):
        return
    entry = (
        "\n\n" + heading + "\n"
        "- **Source:** Owner-directed full narrative improvement pass following review of Shadow-captain translation behavior.\n"
        "- **Type:** narrative supersession / translation-recording correction / continuity consolidation\n"
        "- **Entities affected:** event_dark_star_incident_4718_224; unified Dark Star narrative; prior Third Silence chapter source\n"
        "- **Description:** Committed a unified three-chapter v1.1 manuscript covering The Dark Star, Valkyrie, and Third Silence. Revised Shadow communications so speaker intelligence and professional cadence remain intact while uncertainty appears through delayed live translation, substitutions, confidence warnings, competing terms, and later corrections. Applied a general prose, rhythm, viewpoint, repetition, and evidentiary-clarity improvement pass without changing the locked event outcome.\n"
        "- **Resolution:** Unified v1.1 manuscript is the governing narrative source. The prior chapter-three file remains in place as superseded provenance. Translation output is an evidentiary instrument record, not an omniscient narrator.\n"
    )
    with DRIFT.open("a", encoding="utf-8") as f:
        f.write(entry)


def main() -> None:
    materialize_manuscript()
    supersede_old_chapter()
    update_event_graph()
    update_drift_log()


if __name__ == "__main__":
    main()
