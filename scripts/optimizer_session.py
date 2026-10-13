#!/usr/bin/env python3
"""Read-only terminal view of existing optimizer history; no session ledger or writer."""
from __future__ import annotations
import argparse
from collections import deque
import json
from pathlib import Path
import sys
import time

MAX_LINE = 32 * 1024 * 1024
SCHEMA = "optimizer-history/1"


def compact(value, limit=600):
    # JSON escapes terminal controls, including ESC; never execute file text.
    rendered = json.dumps(value, ensure_ascii=True, sort_keys=True, default=str)
    return rendered if len(rendered) <= limit else rendered[:limit] + "..."


def render(row):
    if not isinstance(row, dict) or row.get("schema") != SCHEMA:
        raise ValueError("unsupported history record")
    kind = row.get("kind")
    data = row.get("data")
    if not isinstance(data, dict):
        raise ValueError("history data must be an object")
    prefix = compact({"sequence": row.get("sequence"), "time": row.get("timestamp"),
                      "command": row.get("command_id")}, 260)
    if kind == "baseline":
        return prefix + " baseline"
    if kind == "submitted":
        # Print only origin/operation names: no arguments, raw commands or environment.
        expr = data.get("expression")
        return prefix + " submitted " + compact({"origin": data.get("origin"),
                "operation": (expr.get("operation") or (expr.get("request", {}).get("operation") if isinstance(expr.get("request"), dict) else None) or expr.get("action")) if isinstance(expr, dict) else None}, 200)
    if kind == "outcome":
        operations = data.get("operations", [])
        if not isinstance(operations, list):
            raise ValueError("invalid history operations")
        names = [item.get("operation") for item in operations if isinstance(item, dict)]
        error = data.get("error")
        return prefix + " " + compact({"status": data.get("status"), "operations": names,
            "summary": data.get("summary"),
            "error_code": error.get("code") if isinstance(error, dict) else None}, 600)
    raise ValueError("unknown history record kind")


class HistoryReader:
    def __init__(self, path):
        self.path = Path(path)
        stat = self.path.stat()
        self.identity = (stat.st_dev, stat.st_ino)
        self.offset = 0
        self.partial = False

    def read(self):
        stat = self.path.stat()
        if (stat.st_dev, stat.st_ino) != self.identity or stat.st_size < self.offset:
            raise ValueError("history replaced/truncated; stop and inspect the experiment")
        with self.path.open("rb") as stream:
            stream.seek(self.offset)
            while True:
                start = stream.tell()
                raw = stream.readline(MAX_LINE + 1)
                if not raw:
                    self.partial = False
                    return
                if len(raw) > MAX_LINE:
                    raise ValueError("history record exceeds 32 MiB")
                if not raw.endswith(b"\n"):
                    self.partial = True
                    return  # Writer may finish this record on the next poll.
                try:
                    row = json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
                    text = render(row)
                except (ValueError, UnicodeError, RecursionError) as exc:
                    raise ValueError("invalid history record at byte " + str(start)) from exc
                self.offset = stream.tell()
                self.partial = False
                yield text


def history_path(value):
    path = Path(value).expanduser().resolve()
    if path.is_dir():
        path = path / "history.jsonl"
    if not path.is_file():
        raise ValueError("existing history.jsonl required; initialize/open a persistent experiment first")
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment", help="exact experiment directory or history.jsonl")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--once", action="store_true")
    mode.add_argument("--follow", action="store_true")
    parser.add_argument("--tail", type=int, default=12)
    parser.add_argument("--interval", type=float, default=1.0)
    args = parser.parse_args(argv)
    if not 1 <= args.tail <= 200 or not 0.2 <= args.interval <= 60:
        parser.error("tail must be 1–200; interval must be 0.2–60 seconds")
    try:
        path = history_path(args.experiment)
        reader = HistoryReader(path)
        print("Read-only history view: " + compact(str(path)), flush=True)
        print("Displays stored operations; use native history inspection to validate evidence.", flush=True)
        for line in deque(reader.read(), maxlen=args.tail):
            print(line, flush=True)
        if not args.follow:
            if reader.partial:
                print("Incomplete trailing record omitted; no durable outcome inferred.", flush=True)
            return 0
        while True:
            time.sleep(args.interval)
            for line in reader.read():
                print(line, flush=True)
    except KeyboardInterrupt:
        return 0
    except (OSError, ValueError) as exc:
        print("History view stopped: " + compact(str(exc)), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
