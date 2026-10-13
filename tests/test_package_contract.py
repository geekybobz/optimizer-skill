from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

PACKAGE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("optimizer_viewer",PACKAGE/"scripts/optimizer_session.py")
viewer=importlib.util.module_from_spec(spec); spec.loader.exec_module(viewer)


def row(kind="outcome", **data):
    return dict(schema="optimizer-history/1", sequence=1, kind=kind, timestamp="now",
                command_id="c1", data=data)


class ViewerTests(unittest.TestCase):
    def test_controls_are_escaped_and_output_is_bounded(self):
        text=viewer.render(row(status="ok",operations=[{"operation":"solve"}],
                              summary={"value":"\x1b[31m"+"x"*5000}))
        self.assertNotIn("\x1b",text)
        self.assertLess(len(text),1000)

    def test_partial_append_is_read_exactly_once_when_completed(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"history.jsonl"
            raw=json.dumps(row(status="ok",operations=[],summary={}))
            path.write_text(raw[:20])
            reader=viewer.HistoryReader(path)
            self.assertEqual([],list(reader.read()))
            self.assertTrue(reader.partial)
            with path.open("a") as f: f.write(raw[20:]+"\n")
            self.assertEqual(1,len(list(reader.read())))
            self.assertEqual([],list(reader.read()))

    def test_read_leaves_history_bytes_and_metadata_unchanged(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"history.jsonl"
            path.write_text(json.dumps(row(status="ok",operations=[]))+"\n")
            before=(path.read_bytes(),path.stat().st_mtime_ns)
            list(viewer.HistoryReader(path).read())
            self.assertEqual(before,(path.read_bytes(),path.stat().st_mtime_ns))
            self.assertEqual(["history.jsonl"],[p.name for p in Path(d).iterdir()])

    def test_truncation_stops_instead_of_replaying(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"history.jsonl"
            path.write_text(json.dumps(row(status="ok",operations=[]))+"\n")
            reader=viewer.HistoryReader(path); list(reader.read()); path.write_text("")
            with self.assertRaisesRegex(ValueError,"truncated"):
                list(reader.read())

    def test_unknown_schema_and_bad_complete_line_fail(self):
        with self.assertRaises(ValueError): viewer.render({"schema":"unknown"})
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"history.jsonl";path.write_text("bad\n")
            with self.assertRaisesRegex(ValueError,"byte 0"):
                list(viewer.HistoryReader(path).read())

    def test_nested_mcp_request_names_the_submitted_operation(self):
        text=viewer.render(row("submitted",origin="mcp",
            expression={"action":"execute", "request":{"operation":"shooting.solve_shooting", "arguments":{"hidden":"private"}}}))
        self.assertIn("shooting.solve_shooting",text)
        self.assertNotIn("private",text)

    def test_submissions_omit_arguments_and_environment(self):
        text=viewer.render(row("submitted",origin="mcp",raw="private",environment={"token":"secret"},
                              expression={"operation":"gradient", "arguments":{"value":"secret"}}))
        self.assertIn("gradient",text)
        self.assertNotIn("secret",text); self.assertNotIn("private",text)


class PackageTests(unittest.TestCase):
    def test_local_links_and_home_footers_resolve(self):
        for path in PACKAGE.rglob("*.md"):
            with self.subTest(path=str(path.relative_to(PACKAGE))):
                text=path.read_text()
                lines=[line for line in text.splitlines() if line.strip()]
                self.assertEqual("---",lines[-2])
                self.assertIn("[⌂ Home]",lines[-1])
                for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)",text):
                    if "://" in target or target.startswith("#"): continue
                    self.assertTrue((path.parent/target.split("#")[0]).exists(),target)

    def test_execution_entry_is_compact_and_family_guides_are_nested(self):
        entry=(PACKAGE/"SKILL.md").read_text()
        self.assertLess(len(entry.encode()),3500)
        self.assertNotIn("](build-olgs.md)",entry)
        self.assertNotIn("](build-olss.md)",entry)
        parent=(PACKAGE/"build-system.md").read_text()
        self.assertIn("](build-olgs.md)",parent)
        self.assertIn("](build-olss.md)",parent)
        for child in ["build-olgs.md","build-olss.md"]:
            self.assertIn("](build-system.md)",(PACKAGE/child).read_text())

    def test_manual_host_invocation_policy_is_preserved(self):
        self.assertIn("allow_implicit_invocation: false",(PACKAGE/"agents/openai.yaml").read_text())

if __name__=="__main__": unittest.main()
