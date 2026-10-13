# Runtime, persistence and visibility

Shared owner of the CLI/MCP connection, experiment persistence and report structure.
Source context defaults to `/Users/billabobz/OPTIMIZER`; `OPTIMIZER_SOURCE` may override
it. Source is documentation context; installed bytes govern numerical execution.

## Discover and connect

Run `python3 <skill>/scripts/optimizer_api.py status`; it uses the installed receipt
or an explicitly supplied runtime Python, with isolated imports. `discover <query>`,
`contract [olgs|olss]` and `methods` are bounded read-only queries. No project factory
is imported. Receipt metadata is provenance, not a fresh wheel-integrity certificate.
Read only the named live API/contract and relevant source topic, not the entire manual.

Select the interface by the next decision, not by an assumed solver-speed advantage:

- Use native MCP for adaptive discovery, typed references, bounded inspection,
  candidate selection and managed-job control when tools are exposed.
- Use the installed CLI for a predetermined repeatable sequence: one bounded
  script can run several operations in one host call. Stop and inspect failures;
  do not batch decisions that require looking at an earlier result first.
- Combine them through the same named experiment/coordinator and retained refs;
  a CLI batch need not export large arrays for MCP to continue the work.

Both routes use the same numerical service, persistence and history. Host tool
round trips, response envelopes and batching can dominate short calls. Wire bytes
are not measured model tokens; compare equal starts/options/work and separate
numerical runtime from client/host overhead. Do not claim MCP accelerates the solver
or that CLI is universally faster. Prefer summaries/refs, inspect only needed values,
and use bounded chunks or managed jobs for long work. Never weaken analytical
physics, multistart, independent verification or resource limits to save tokens.

Inspect live schemas before calling. If native tools are absent, use the installed
CLI and report the boundary. SDK transport tests do not establish native host-tool
availability. Do not silently install, reconfigure or reload a host. Project-only
hooks/callbacks require supported registration; MCP does not run arbitrary imports.

For a new run, initialize a named experiment with `project.init(name=..., root=...)`
through the installed CLI; open existing experiments explicitly, never overwrite one.
MCP attachment requires an existing persistent experiment; start the coordinator explicitly
when needed. When live provenance confirms fixed-root owner transport, TMPDIR need not match;
for an older runtime, follow its documented launch configuration. Inspect current
session state around failures; a lost reply does not mean cancellation or rollback.
Use bounded foreground chunks, or supported managed jobs with bounded waits. Numeric
candidate activation is explicit after inspection. Live-worker resume differs from
physical restart after a dead worker; exact disk continuation is method/certification-specific.
When supported by the installed API, mode="physical" resolves OLGS/OLSS per context
and resets method memory. Keep exact as an explicit distinct claim. Older runtimes
may require plain physical heads in every context or separate family experiments.

## Persistence receipt

Before numerical work, confirm the absolute `.optimizer/<name>` path, writer connection,
history recording, storage capacity/retention, input/source dependencies and environment.
Plain uninitialized CLI sessions have RAM history only; plain Python is not automatically
journaled. History owns frontend submissions/outcomes; checkpoints own typed state/results.
Capture required external theory/data as declared inputs/dependencies and verify identities.
Pin important results: a binding name alone does not protect payloads from retention pruning.
Use current `checkpoints.save(..., kind=..., pin=True)` or supported physical save/pin APIs.
Do not claim every protocol reject, disk-full attempt or uncommitted iteration is durable.

Save one structured report schema `optimizer-skill/report-v1` using existing input/report
checkpoints. For construction: theory references/hashes, equation-to-hook mapping, problem
identity, parameters/layouts, reviewed assumptions/exceptions and validation evidence.
For campaigns add seed descriptors/coverage, methods/options/budgets, result/checkpoint refs,
feasibility/stationarity/verification, rejected outcomes/reasons, transfers/scenarios,
decisions and claim limits. Missing evidence is marked absent. This is scientific context,
not a second numerical history. Never store credentials, transcripts or runtime socket tokens.

## Requested figures

Bloch plotting follows [bloch.md](bloch.md). CLI/MCP can call
`visualization.render_bloch` with retained PlotData or its mapping and explicit
output/options; it returns a serializable artifact receipt, not figure objects.
Rendering writes files without numerical activation. Those filesystem effects survive
a later history failure or lost reply; inspect before retrying. Store the receipt
using the existing report checkpoints, alongside its input/candidate provenance.

## Terminal visibility

Give the user a copyable absolute command when optimization starts:

```bash
python3 <skill>/scripts/optimizer_session.py <absolute-experiment-directory> --follow
```

This read-only viewer tails existing `history.jsonl`; `--once` shows recent entries.
It writes no ledger, attaches to no writer and performs no numerical calls. It displays
submitted/completed operations and stored compact summaries, not invented iteration
telemetry. Long MCP calls may stay submitted until their bounded chunk returns; choose
meaningful chunks for progress. No automatic browser, plot or viewer launch is required.
The viewer is observational; use native history inspection for validated decision evidence.

---

[⌂ Home](INDEX.md)
