import json
import tempfile
import unittest
from pathlib import Path

from export_name_registry import build_registry
from validate_naming_receipts import (
    cadence_signature,
    name_root,
    normalize_name,
    phonetic_key,
    validate_file,
)


class NamingGateTests(unittest.TestCase):
    def test_registry_export_and_valid_receipt(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            canon = root / "canon" / "L2" / "entities" / "characters"
            canon.mkdir(parents=True)
            (canon / "existing.json").write_text(
                json.dumps(
                    {
                        "canonical_id": "existing",
                        "canonical_name": "Tessa Korr",
                        "entity_kind": "character",
                        "aliases": [],
                    }
                ),
                encoding="utf-8",
            )
            registry = build_registry(root)
            candidate = canon / "new.json"
            name = "Arian Kelm"
            candidate.write_text(
                json.dumps(
                    {
                        "canonical_id": "new",
                        "canonical_name": name,
                        "entity_kind": "character",
                        "naming_receipt": {
                            "protocol": "GUMAS_NAMING_PROTOCOL_v0.1",
                            "receipt_version": "1.0",
                            "canonical_name": name,
                            "aliases": [],
                            "signature": {
                                "normalized": normalize_name(name),
                                "root": name_root(name),
                                "phonetic_key": phonetic_key(name),
                                "cadence": cadence_signature(name),
                            },
                            "rejected_candidates": [],
                            "collisions_checked": 1,
                            "request": {
                                "entity_id": "new",
                                "entity_type": "PERSON",
                            },
                            "registry_digest": registry["registry_digest"],
                            "candidate_set": [name],
                            "selection_mode": "owner_selected_from_candidates",
                        },
                    }
                ),
                encoding="utf-8",
            )
            findings = validate_file(candidate, registry, True)
            self.assertFalse(
                [item for item in findings if item["level"] == "BLOCK"]
            )

    def test_missing_receipt_blocks(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "new.json"
            path.write_text(
                json.dumps(
                    {"canonical_id": "new", "canonical_name": "Hand Mint"}
                ),
                encoding="utf-8",
            )
            findings = validate_file(
                path,
                {"entries": [], "registry_digest": "0" * 64},
                True,
            )
            self.assertEqual(findings[0]["code"], "NAMING_RECEIPT_REQUIRED")

    def test_recovered_source_exemption_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "recovered.json"
            path.write_text(
                json.dumps(
                    {
                        "canonical_id": "recovered",
                        "canonical_name": "Cross",
                        "naming_exemption": {
                            "type": "recovered_source",
                            "reason": "Name preserved from observed-use capture",
                            "authority": "owner_resolution",
                            "source_refs": ["capture.md"],
                        },
                    }
                ),
                encoding="utf-8",
            )
            findings = validate_file(
                path,
                {"entries": [], "registry_digest": "0" * 64},
                True,
            )
            self.assertFalse(
                [item for item in findings if item["level"] == "BLOCK"]
            )


if __name__ == "__main__":
    unittest.main()
