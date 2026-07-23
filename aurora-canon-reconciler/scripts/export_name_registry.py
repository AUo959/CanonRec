#!/usr/bin/env python3
"""Export CanonRec L2 names as an Aurora NameRegistry-compatible snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

PROTOCOL_VERSION = "GUMAS_NAMING_PROTOCOL_v0.1"


def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch)).casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


def registry_digest(entries: Iterable[dict[str, Any]]) -> str:
    rows = []
    for entry in entries:
        rows.append(
            {
                "canonical_name": entry["canonical_name"],
                "entity_id": entry["entity_id"],
                "entity_type": entry.get("entity_type", "CUSTOM"),
                "aliases": sorted(entry.get("aliases", [])),
            }
        )
    encoded = json.dumps(
        sorted(rows, key=lambda row: (row["canonical_name"].casefold(), row["entity_id"])),
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _first_string(data: dict[str, Any], fields: tuple[str, ...]) -> str | None:
    for field in fields:
        value = data.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _iter_objects(payload: Any) -> Iterable[dict[str, Any]]:
    if isinstance(payload, dict):
        yield payload
    elif isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict):
                yield item


def extract_entry(data: dict[str, Any], source_path: str) -> dict[str, Any] | None:
    name = _first_string(data, ("canonical_name", "name", "designation", "title"))
    if not name:
        return None
    entity_id = _first_string(
        data,
        ("canonical_id", "entity_id", "character_id", "vessel_id", "id"),
    )
    if not entity_id:
        entity_id = Path(source_path).parent.name or Path(source_path).stem
    entity_type = str(
        data.get("entity_kind") or data.get("entity_type") or "CUSTOM"
    ).upper()
    aliases = data.get("aliases", [])
    if not isinstance(aliases, list):
        aliases = []
    aliases = [str(alias).strip() for alias in aliases if str(alias).strip()]
    return {
        "canonical_name": name,
        "entity_id": entity_id,
        "entity_type": entity_type,
        "aliases": aliases,
        "source_path": source_path,
    }


def build_registry(repo_root: Path) -> dict[str, Any]:
    canon_root = repo_root / "canon" / "L2"
    entries: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    if canon_root.exists():
        for path in sorted(canon_root.rglob("*.json")):
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            rel = path.relative_to(repo_root).as_posix()
            for data in _iter_objects(payload):
                entry = extract_entry(data, rel)
                if not entry:
                    continue
                key = (normalize_name(entry["canonical_name"]), entry["entity_id"])
                if key in seen:
                    continue
                seen.add(key)
                entries.append(entry)
    entries.sort(
        key=lambda entry: (entry["canonical_name"].casefold(), entry["entity_id"])
    )
    return {
        "protocol": PROTOCOL_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "entry_count": len(entries),
        "registry_digest": registry_digest(entries),
        "entries": entries,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = build_registry(args.repo_root.resolve())
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
