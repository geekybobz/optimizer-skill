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

Prefer native optimizer MCP tools when exposed. Inspect schemas; attach to an existing
experiment/coordinator, execute canonical operations, inspect compact records/references.
If native tools are absent, use the installed CLI and report that boundary. SDK transport
testing proves that transport, not native host-tool availability. Do not silently install,
reconfigure or reload a host. Custom callbacks and project-only hooks require supported
registration/transport; MCP cannot run arbitrary Python imports or callbacks.

For a new run, initialize a named experiment with `project.init(name=..., root=...)`
through the installed CLI; open existing experiments explicitly, never overwrite one.
MCP attachment requires an existing persistent experiment; start the coordinator explicitly
when needed. Keep server/client temporary-directory settings consistent. Inspect current
session state around failures; a lost reply does not mean cancellation or rollback.
Use bounded foreground chunks, or supported managed jobs with bounded waits. Numeric
candidate activation is explicit after inspection. Live-worker resume differs from
physical restart after a dead worker; exact disk continuation is method/certification-specific.

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
