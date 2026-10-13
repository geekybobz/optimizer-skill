# OLGS specialization

Load only for the OLGS branch of [build-system.md](build-system.md).
The live source contract is `optimizer/system_olgs/CONTRACT.md` under the source root
reported by [interfaces.md](interfaces.md); query the installed contract before coding.

## Equation-to-hook mapping

Implement `system_spec`, `control_spec`, `evaluate`, `gradient`, and `with_secondary`
directly, using the current runtime's signatures and containers. Subclassing `OLGS`
is optional. Declare finite metrics, objective direction and analytical derivative
provenance. Keep configuration dict-first and unknown keys explicit errors.
Primary parameters own physical identity and numerical layout; secondary parameters
own declared tunable objective/curriculum values. Reconfiguration returns a new system.

Derive the objective/action, forward equation, adjoint equation, boundary conditions
and discrete gradient from the supplied model. State whether returned entries are
Euclidean derivatives of discrete `J` or a continuum density converted using quadrature
weights. Verify signs, real/complex pairing, endpoint contributions and time weights.
Do not assume `N` counts intervals: declare endpoint/cell sampling, quadrature, `T`,
`dt` and ordered channels explicitly, preserving the full `ControlSpec` compatibility.

For soft formulations, derive every penalty and its derivative. For hard formulations,
provide the physical residuals and analytical Jacobian, declaring their ordering,
units and size. Add bounds, HVP, prox or other optional hooks only when the selected
method needs them and the derivation supports them. Combined `value_and_gradient`
may reuse propagation; cached data must match the exact controls and configuration.

Validate analytic limits and full-state replay; compare gradient directional products
at separated diagnostic steps; check residual Jacobian directional products for hard
constraints. Treat failed checks as construction failures before optimization. Explain
which acceptance tests concern feasibility, stationarity, local curvature or physics.
A converged objective alone establishes none of those properties.

Simulation follows the shared [build workflow](build-system.md), including frozen-control
uncertainty tests and independent accuracy settings. When both families are requested,
compare physical predictions on an explicitly mapped control before declaring consistency.

---

[⌂ Home](INDEX.md)
