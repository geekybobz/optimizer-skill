#!/usr/bin/env python3
"""Bounded read-only discovery from an installed optimizer, never a project factory."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

THREAD_KEYS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
               "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS")
MAX_RECEIPT = 65536
MAX_OUTPUT = 1048576


def resolve(receipt: Path | None = None, python: Path | None = None,
            source_root: Path | None = None) -> dict:
    source = (source_root or Path(os.environ.get("OPTIMIZER_SOURCE", str(Path.home()/"OPTIMIZER")))).expanduser().resolve()
    out = {"source_root": str(source), "receipt": None, "receipt_metadata": None}
    if python is None:
        path = (receipt or Path.home()/".local/share/optimizer/install.json").expanduser().resolve()
        with path.open("rb") as stream:
            raw = stream.read(MAX_RECEIPT + 1)
        if len(raw) > MAX_RECEIPT:
            raise ValueError("install receipt exceeds 64 KiB")
        metadata = json.loads(raw)
        if not isinstance(metadata, dict) or metadata.get("schema") != "optimizer.install/1":
            raise ValueError("unsupported install receipt")
        value = metadata.get("python")
        if not isinstance(value, str) or not Path(value).is_absolute():
            raise ValueError("receipt requires an absolute Python executable")
        python = Path(value)
        out.update(receipt=str(path), receipt_metadata={k: metadata.get(k) for k in
                   ("version", "commit", "package", "wheel_sha256")})
    executable = python.expanduser().resolve()
    if not executable.is_file() or not os.access(executable, os.X_OK):
        raise ValueError("runtime Python missing/not executable: " + str(executable))
    out["python"] = str(executable)
    return out


QUERY = r"""
import json, sys
import optimizer as opt
mode, topic = sys.argv[1], sys.argv[2]
if mode == 'status':
    payload = {'version': opt.__version__, 'package': opt.__file__,
               'python': sys.executable}
elif mode == 'discover':
    payload = opt.search(topic)
elif mode == 'contract':
    payload = opt.shooting_contract_info() if topic == 'olss' else opt.contract_info()
elif mode == 'methods':
    payload = {'olgs': opt.optimizers.list(), 'olss': opt.shooting.list()}
else:
    raise ValueError('unsupported discovery command')
print(json.dumps(payload, sort_keys=True, default=str))
"""


def live_payload(runtime: dict, command: str, topic: str | None = None) -> dict:
    if command not in {"status", "discover", "contract", "methods"}:
        raise ValueError("unsupported discovery command")
    if command == "discover" and (not topic or len(topic) > 256):
        raise ValueError("discover requires a query of 1–256 characters")
    if command == "contract" and topic not in (None, "olgs", "olss"):
        raise ValueError("contract family must be olgs or olss")
    env = dict(os.environ)
    env.update({key: "1" for key in THREAD_KEYS})
    # An on-disk anonymous output avoids unbounded capture in agent memory.
    import tempfile
    with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        result = subprocess.run([runtime["python"], "-I", "-c", QUERY, command, topic or ""],
                                env=env, stdout=stdout, stderr=stderr, timeout=30)
        stdout.seek(0)
        raw = stdout.read(MAX_OUTPUT + 1)
        if result.returncode:
            stderr.seek(0)
            error = stderr.read(4096).decode("utf-8", errors="replace")
            raise ValueError("installed-runtime discovery failed: " + error)
        if len(raw) > MAX_OUTPUT:
            raise ValueError("discovery output exceeds 1 MiB; use a narrower query")
    payload = json.loads(raw)
    metadata = runtime.get("receipt_metadata")
    if command == "status" and metadata:
        if payload["version"] != metadata["version"] or str(Path(payload["package"]).parent) != metadata["package"]:
            raise ValueError("live runtime differs from install receipt; inspect installation before use")
    return {"runtime": runtime, "payload": payload}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("status", "discover", "contract", "methods"))
    parser.add_argument("topic", nargs="?")
    identity = parser.add_mutually_exclusive_group()
    identity.add_argument("--receipt", type=Path)
    identity.add_argument("--python", type=Path)
    parser.add_argument("--source-root", type=Path)
    args = parser.parse_args(argv)
    try:
        runtime = resolve(args.receipt, args.python, args.source_root)
        result = live_payload(runtime, args.command, args.topic)
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
