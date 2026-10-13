# Situation analysis

Inspect an unexpected result or proposed tactic before deciding the next bounded action.
Do not trigger numerical work while reading reports.

Use the identity table and execution-integrity gate in [optimize.md](optimize.md).
First state observations, interpretation, uncertainty, proposed action and what evidence
would change the decision. Code/setup failure is classified before strategy changes.

| evidence | response |
|---|---|
| feasible point improving | continue within budget and preserve a checkpoint |
| trusted derivatives, plateau | inspect stationarity/scaling; compare new structured starts or a justified method |
| rejected/unstable steps | inspect recorded scales, constraints and acceptance; propose a bounded discriminating check |
| constraint or verification failure | reject qualification; diagnose formulation/accuracy before more search |
| changed model/layout/formulation | new problem with explicit transfer and validation |
| symmetry or mechanism hypothesis | propose a targeted check; do not infer it from missing observables |
| source/environment/replay conflict | preserve evidence and resolve identity before reuse |

`explore` proposes routes; `intervene` applies an authorized tactic within the same
problem; `continue` requires compatible identity; `branch` names a tactic stage or
new problem explicitly. Record decisions through the report owner in
[interfaces.md](interfaces.md). A user-approved exception names its scope and evidence;
it never converts an invalid API or unsupported mathematical claim into a valid one.

---

[⌂ Home](INDEX.md)
