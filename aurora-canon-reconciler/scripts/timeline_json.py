#!/usr/bin/env python3
"""Print a reviewable patch to add or replace one enhanced timeline event."""

from __future__ import annotations

import argparse
import difflib
import json
import sys
from pathlib import Path
from typing import Any


TIMELINE_DIR = "canon/L2/timeline"
ENHANCED = f"{TIMELINE_DIR}/GUMAS_Galactic_Timeline_Detailed_Enhanced.json"
LEGACY = f"{TIMELINE_DIR}/GUMAS_Galactic_Timeline_Detailed.json"
FORMATS = {ENHANCED: (1, "\n"), LEGACY: (2, "")}


def format_timeline(path: str, payload: Any) -> str:
    """Serialize a timeline in its established committed format."""
    indent, ending = FORMATS[path]
    return json.dumps(payload, indent=indent, ensure_ascii=True, allow_nan=False) + ending


def event_patch(repo_root: Path, era_id: str, event: dict[str, Any], *, replace: bool = False) -> str:
    original = (repo_root / ENHANCED).read_bytes().decode("utf-8")
    timeline = json.loads(original)
    if original != format_timeline(ENHANCED, timeline):
        raise ValueError("enhanced timeline formatting must be reconciled before editing")

    event_id = event.get("event_id") if isinstance(event, dict) else None
    if not isinstance(event_id, str) or not event_id.strip():
        raise ValueError("event must be a JSON object with an event_id")

    eras = timeline["Galactic_Timeline"]
    matches = [era for era in eras if era["era_id"] == era_id]
    if len(matches) != 1:
        raise ValueError(f"expected one era with ID {era_id!r}, found {len(matches)}")
    target = matches[0]
    existing = [
        (era, index)
        for era in eras
        for index, entry in enumerate(era["events"])
        if entry.get("event_id") == event_id
    ]
    if replace:
        if len(existing) != 1 or existing[0][0] is not target:
            raise ValueError(f"expected one event {event_id!r} in era {era_id!r}")
        position = existing[0][1]
        # Keep the existing order of keys and append genuinely new fields.
        previous = target["events"][position]
        ordered = {key: event[key] for key in previous if key in event}
        target["events"][position] = ordered | event
    elif existing:
        raise ValueError(f"event ID {event_id!r} already exists")
    else:
        target["events"].append(event)

    updated = format_timeline(ENHANCED, timeline)
    return "".join(difflib.unified_diff(
        original.splitlines(keepends=True),
        updated.splitlines(keepends=True),
        fromfile=f"a/{ENHANCED}",
        tofile=f"b/{ENHANCED}",
    ))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--era", required=True, help="Target era_id")
    parser.add_argument("--event", type=Path, required=True, help="JSON file with the complete event")
    parser.add_argument("--replace", action="store_true", help="Replace a matching event in the target era")
    args = parser.parse_args()
    try:
        event = json.loads(args.event.read_text(encoding="utf-8"))
        patch = event_patch(args.repo_root, args.era, event, replace=args.replace)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")
    sys.stdout.write(patch)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
