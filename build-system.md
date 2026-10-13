# Build a system

Plan, review, implement, and validate project-owned physics from the supplied theory.
This workflow does not optimize. Parent: [Optimizer](SKILL.md).

## Choose the formulation

Read [interfaces.md](interfaces.md) and inspect the current family contract. The user
may choose OLGS, OLSS, or both for one physical problem. Load only the selected
specializations: [OLGS](build-olgs.md) and/or [OLSS](build-olss.md).
Both formulations share a problem identity and theory references, with separate
native layouts and acceptance checks. Prefer one readable module containing two
self-contained classes when small; separate modules when it improves clarity.
Do not introduce a shared physics superclass or a compatibility-wrapper hierarchy.

## Review before construction

Present a concrete plan: theory sources and equation-to-hook mapping; assumptions,
units, dynamics, boundary conditions, objective/action and derivative derivation;
primary/secondary parameters; control/variable ordering, quadrature and grid;
soft/hard constraints; family choice; optional capabilities; file layout; simulation
and robustness scenarios; verification tolerances; measured cost and resource budget.
Identify unsupported or ambiguous terms. Stop for review before writing system code.
Approval covers that plan; a material change or unresolved conflict needs fresh review.

Implement native hooks directly. A helper must perform a distinct mathematical or
computational task, such as propagation or sensitivity integration; avoid aliases
that only rename a hook. Prefer NumPy contractions, broadcasting, batched independent
scenarios, allocation reuse, and combined evaluations where valid. Preserve sequential
time dependence, memory bounds, dtype and reproducibility; benchmark useful changes.

A project-defined `simulate` may return trajectories, observables, and scenario results.
Specify how to vary physical uncertainties with controls frozen. Keep numerical accuracy
options distinct from physical changes; do not disguise changed physics as verification.
Inspect the live interface before promising MCP access to a project-only simulation hook.

Validate static contracts, finite shapes, identity, input immutability, repeated-call
consistency, simple analytical limits and independent propagation. Check derived
formulas against explicit small diagnostic comparisons; finite differences are checks,
not the optimization derivative. Add bounded physical tests rather than mirroring code.
Return the system paths, derivation mapping, passed checks, unresolved issues and cost.

## Contract conflicts

Different names or inheritance alone need no adapter: implement the structural native
contract. An unusual update can use a supported custom-step path only when the existing
family contract still holds; inspect transport support before offering a live callback.
For genuinely incompatible mathematics, explain the smallest extension or project-owned
external solver needed, with effort and evidence limits. Do not fabricate gradients,
residuals, Jacobians, or a dummy family declaration. User-approved exceptions must name
the conflicting local rule, reason, scope and verification; they cannot waive API validity
or mathematical correctness. Save outside-solver reports truthfully as imported evidence.

Use the report ownership and persistence rules in [interfaces.md](interfaces.md).

---

[⌂ Home](INDEX.md)
