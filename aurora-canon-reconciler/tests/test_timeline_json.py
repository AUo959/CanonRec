import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from timeline_json import ENHANCED, LEGACY, event_patch, format_timeline
from validate_repository import parse_data_files


REPO_ROOT = Path(__file__).resolve().parents[2]
ERA_ID = "PE-001"
NEW_EVENT = {"event_id": "PE-TEST", "name": "Test event", "details": "Unicode example — preserved."}


class TimelineFormattingTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.timeline = self.root / ENHANCED
        self.timeline.parent.mkdir(parents=True)
        self.original = (REPO_ROOT / ENHANCED).read_bytes()
        self.timeline.write_bytes(self.original)

    def apply_patch(self, patch):
        subprocess.run(
            ["git", "apply", "-"],
            input=patch,
            encoding="utf-8",
            cwd=self.root,
            check=True,
            capture_output=True,
        )

    def test_append_changes_only_the_inserted_event_and_its_comma(self):
        patch = event_patch(self.root, ERA_ID, NEW_EVENT)
        changes = [line for line in patch.splitlines()[2:] if line.startswith(("+", "-"))]
        self.assertTrue(all(line == "-    }" for line in changes if line.startswith("-")))
        self.assertLessEqual(len(changes), 7)

        self.apply_patch(patch)
        expected = json.loads(self.original)
        expected["Galactic_Timeline"][0]["events"].append(NEW_EVENT)
        self.assertEqual(json.loads(self.timeline.read_bytes()), expected)
        self.assertEqual(parse_data_files(self.root, [self.timeline]), [])

    def test_replace_preserves_key_order_and_is_repeatable(self):
        original_timeline = json.loads(self.original)
        original_event = original_timeline["Galactic_Timeline"][0]["events"][0]
        updated = dict(reversed(list(original_event.items()))) | {"name": "Updated test name"}
        patch = event_patch(self.root, ERA_ID, updated, replace=True)
        changes = [line for line in patch.splitlines()[2:] if line.startswith(("+", "-"))]
        self.assertEqual(len(changes), 2)
        self.apply_patch(patch)
        self.assertEqual(event_patch(self.root, ERA_ID, updated, replace=True), "")

    def test_duplicate_event_is_rejected_without_writing(self):
        with self.assertRaisesRegex(ValueError, "already exists"):
            event_patch(self.root, ERA_ID, {"event_id": "PE-E1"})
        self.assertEqual(self.timeline.read_bytes(), self.original)

    def test_whole_file_reindent_fails_validation_and_blocks_writer(self):
        reindented = json.dumps(json.loads(self.original), indent=2) + "\n"
        self.timeline.write_text(reindented, encoding="utf-8")
        findings = parse_data_files(self.root, [self.timeline])
        self.assertEqual([finding.check for finding in findings], ["timeline_json_format"])
        with self.assertRaisesRegex(ValueError, "formatting must be reconciled"):
            event_patch(self.root, ERA_ID, NEW_EVENT)

    def test_existing_layouts_round_trip_exactly(self):
        for timeline in (ENHANCED, LEGACY):
            with self.subTest(timeline=timeline):
                original = (REPO_ROOT / timeline).read_bytes()
                self.assertEqual(format_timeline(timeline, json.loads(original)).encode("utf-8"), original)
