# Optimize

Run an evidence-led campaign on an existing verified system. Building or changing
physics routes to [build-system.md](build-system.md) for review.

## Preflight and bounded execution

Read [interfaces.md](interfaces.md); confirm the installed runtime and persistent
experiment before numerical execution. Match source/derivation, family, objective,
metric direction, physical parameters, layouts and previous replay. Verify required
derivatives and capabilities before choosing a method. Record acceptance tolerances,
multistart coverage, total budget, per-chunk limits and stopping conditions.
Use the decision boundaries in Efficient execution below.
Use available CPUs minus three, floored at one, as the total worker ceiling; independent
heavy runs are sequential by default and native numerical-library threads initially one.
Nested workers/threads count toward the ceiling. This does not reserve OS-wide cores.

## Efficient execution

- Establish the problem, runtime, acceptance checks, search coverage, budget and
  stopping conditions once. Recheck only what changed or became uncertain.
- Batch operations whose inputs and next steps are already determined. Preserve
  numerical checks and stop on failures; do not batch across a decision that needs
  scientific interpretation or user review.
- Numerical chunks and checkpoints do not each require a model turn. Continue
  approved work through supported CLI scripts or jobs within the recorded budget;
  use supported waits instead of repeated model-driven status polling.
- Inspect evidence when it can change the next action: completion, a declared
  acceptance or stopping check, unexpected failure or behaviour, or a proposed
  change of problem, method or selection criteria. Investigate exceptions promptly.
- Request compact decision-relevant summaries and references. Fetch detailed logs,
  arrays or diagnostics only when needed; reuse retained context and results.
- Keep human progress viewing separate from execution. Provide the existing
  read-only viewer command; do not navigate its display to obtain machine evidence.
- Preserve required verification and resource limits. Compare equivalent work
  before claiming efficiency gains; output size alone is not measured token usage.

## Multistart protocol

Unless the user explicitly reviews a reduced search, always include low-energy starts
across physically valid low-, mid- and high-frequency bands, with varied phases,
coefficients and channels. Add justified analytical baselines and the verified incumbent.
Normalize each realized waveform using the physical energy quadrature, not coefficient
norms. Record actual energy, spectrum/band, envelope, amplitudes, random seed, bounds
and feasibility; constrain high frequencies by physical bandwidth and numerical resolution.
Exact zero may be a singular/stationary seed; include nonzero low-energy starts.
For OLSS, design distinct variable/root seeds through the actual parametrization or
control recovery. Do not equate costate norm with energy or impose unsupported spectral
families. If a requested band is unavailable, explain and review the substitute coverage.
Use a Fourier family for basin entry or a declared restricted search; unrestricted
claims require releasing that restriction. Deduplicate only under justified equivalence.

## Problem identity and reuse

| change | treatment |
|---|---|
| identical model, objective, layout and successful replay | compatible continuation/refinement |
| declared secondary update preserving layout | explicit parameter stage through `with_secondary`; record changed objective/selection comparability |
| new grid, horizon, basis, bounds, cutoff, dynamics, target, bath or formulation | new problem; old controls are explicitly transferred seeds |
| changed implementation or derivative | revalidation boundary before any reuse |

Record the transfer rule, interpolation/extrapolation, units and time scaling. Replay
transferred controls before optimization. Changing duration does not imply generic
amplitude/energy scaling; derive it for the model. Robustness tests freeze the accepted
control and vary declared physical scenarios; reoptimization answers a different question.

## Execution integrity

For exceptions, non-finite/wrong-shape outputs, failed derivative checks, unexplained
invariants or replay disagreement: freeze identity and preserve inputs, checkpoint,
runtime and error; reproduce the smallest deterministic case; inspect API, units,
shapes, scaling and derivatives; run the cheapest discriminating check; classify setup,
implementation, derivative, modelling or unresolved cause. Do not mask the failure by
silently changing physics, objective or method. Review affected code changes and rerun
failed checks. Read [situation-analysis.md](situation-analysis.md) before a strategy change.

## Requested plotting

If Bloch plotting is requested, load [bloch.md](bloch.md). Present its plotting
plan and wait for user review before propagation or rendering; use the shared
installed renderer. Optimization completion does not trigger plotting.

## Evidence and claims

Inspect recorded objective, feasibility, stationarity/KKT, accepted/rejected steps,
stop reason, counters and run records at meaningful checkpoints. Missing quantities
require an explicit bounded diagnostic; inspection never performs hidden propagation.
Pin accepted controls/variables, then independent verification and the campaign report.
Keep failed/rejected starts and reasons in the report, with coverage and comparisons.

Before accepting or reporting a final result, load [extremal-checks.md](extremal-checks.md).
It owns gradient/KKT and shooting-extremal qualification, feasible descent/curvature
screens, refinement, incumbent challenges and precise claim strength. Search coverage
alone is insufficient; report independent replay, uncertainties and remaining gaps.

---

[⌂ Home](INDEX.md)
