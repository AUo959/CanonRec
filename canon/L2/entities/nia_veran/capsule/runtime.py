#!/usr/bin/env python3
"""
Minimal capsule runtime (stdlib only).

Commands:
  validate  - verify capsule/manifest.json hashes (excluding manifest itself)
  compile   - print a compact "system/user" prompt pack (JSON) from capsule files
  state     - print state.bin length + basic stats
"""
import argparse, hashlib, json, struct
from pathlib import Path

CAP_FILES = [
    "identity.json", "traits.json", "knowledge.jsonl",
    "cns.yaml", "state.bin", "runtime.py", "manifest.json",
]

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def cmd_validate(cap_dir: Path) -> None:
    manifest = json.loads((cap_dir / "manifest.json").read_text())
    records = manifest.get("records", [])
    ok = True
    for rec in records:
        fname = rec["path"]
        expected = rec["sha256"]
        actual = sha256_file(cap_dir / fname)
        status = "OK" if actual == expected else "FAIL"
        if status == "FAIL":
            ok = False
        print(f"  {status}  {fname}")
    print("PASS" if ok else "FAIL")

def cmd_compile(cap_dir: Path) -> None:
    identity = json.loads((cap_dir / "identity.json").read_text())
    traits = json.loads((cap_dir / "traits.json").read_text())
    knowledge = [(json.loads(line)) for line in (cap_dir / "knowledge.jsonl").read_text().splitlines() if line.strip()]
    cns = (cap_dir / "cns.yaml").read_text()
    pack = {
        "capsule_id": identity["capsule_id"],
        "system": f"You are {identity['character_name']}, {identity['character_role']} ({identity['faction_id']}). Layer: {identity['declared_layer']}. Ethics: {identity['ethics_protocol']}.",
        "knowledge_entries": len(knowledge),
        "traits_summary": traits,
        "cns_excerpt": cns[:300],
    }
    print(json.dumps(pack, indent=2))

def cmd_state(cap_dir: Path) -> None:
    data = (cap_dir / "state.bin").read_bytes()
    floats = struct.unpack(f"{len(data)//4}f", data[:len(data)-(len(data)%4)])
    print(f"state.bin: {len(data)} bytes, {len(floats)} floats")
    if floats:
        print(f"  min={min(floats):.4f} max={max(floats):.4f} mean={sum(floats)/len(floats):.4f}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("command", choices=["validate","compile","state"])
    p.add_argument("--capsule-dir", default=str(Path(__file__).parent))
    args = p.parse_args()
    cap_dir = Path(args.capsule_dir)
    if args.command == "validate":
        cmd_validate(cap_dir)
    elif args.command == "compile":
        cmd_compile(cap_dir)
    elif args.command == "state":
        cmd_state(cap_dir)

if __name__ == "__main__":
    main()
