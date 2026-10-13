from __future__ import annotations
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1]/"scripts/optimizer_api.py"
spec = importlib.util.spec_from_file_location("optimizer_api", SCRIPT)
api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)


class DiscoveryTests(unittest.TestCase):
    def receipt(self, root, **changes):
        data = dict(schema="optimizer.install/1", python=sys.executable,
                    version="4.0.6", package="/installed/optimizer", commit="a"*40)
        data.update(changes)
        path = root/"receipt.json"
        path.write_text(json.dumps(data))
        return path

    def test_receipt_resolves_runtime_and_keeps_source_distinct(self):
        with tempfile.TemporaryDirectory() as d:
            path = self.receipt(Path(d))
            result = api.resolve(path, source_root=Path(d))
            self.assertEqual(str(Path(sys.executable).resolve()), result["python"])
            self.assertEqual(str(Path(d).resolve()), result["source_root"])
            self.assertEqual("a"*40, result["receipt_metadata"]["commit"])

    def test_explicit_python_needs_no_receipt(self):
        result = api.resolve(Path("/missing/receipt"), Path(sys.executable))
        self.assertIsNone(result["receipt"])

    def test_bad_receipt_schema_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError, "unsupported"):
                api.resolve(self.receipt(Path(d), schema="legacy"))

    def test_relative_receipt_executable_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError, "absolute"):
                api.resolve(self.receipt(Path(d), python="python"))

    def test_missing_executable_rejected(self):
        with self.assertRaisesRegex(ValueError, "missing"):
            api.resolve(python=Path("/missing/runtime-python"))

    def test_oversized_receipt_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"large"; path.write_bytes(b" "*(api.MAX_RECEIPT+1))
            with self.assertRaisesRegex(ValueError, "64 KiB"):
                api.resolve(path)

    def run_mock(self, payload, runtime=None):
        def run(args, **kwargs):
            self.assertIn("-I", args)
            self.assertEqual(30, kwargs["timeout"])
            for key in api.THREAD_KEYS: self.assertEqual("1", kwargs["env"][key])
            kwargs["stdout"].write(json.dumps(payload).encode())
            return subprocess.CompletedProcess(args, 0)
        runtime = runtime or {"python": sys.executable, "receipt_metadata": None}
        with mock.patch.object(api.subprocess, "run", side_effect=run):
            return api.live_payload(runtime, "status")

    def test_isolated_queries_with_one_native_thread(self):
        self.assertEqual({"version":"4.0.6"}, self.run_mock({"version":"4.0.6"})["payload"])

    def test_live_receipt_mismatch_stops(self):
        runtime={"python":sys.executable, "receipt_metadata":{"version":"4.0.6", "package":"/installed/optimizer"}}
        with self.assertRaisesRegex(ValueError, "differs"):
            self.run_mock({"version":"other", "package":"/installed/optimizer/__init__.py"}, runtime)

    def test_unknown_and_unbounded_queries_rejected_before_process(self):
        with mock.patch.object(api.subprocess,"run") as run:
            for command,topic in [("tracker",None),("discover","x"*257),("contract","unknown")]:
                with self.subTest(command=command), self.assertRaises(ValueError):
                    api.live_payload({"python":sys.executable},command,topic)
            run.assert_not_called()

    def test_timeout_propagates_without_retry(self):
        with mock.patch.object(api.subprocess,"run",side_effect=subprocess.TimeoutExpired("runtime",30)) as run:
            with self.assertRaises(subprocess.TimeoutExpired):
                api.live_payload({"python":sys.executable},"status")
            self.assertEqual(1,run.call_count)

if __name__ == "__main__": unittest.main()
