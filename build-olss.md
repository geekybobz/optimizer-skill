# OLSS specialization

Load only for the OLSS branch of [build-system.md](build-system.md).
The live source contract is `optimizer/system_olss/CONTRACT.md` under the source root
reported by [interfaces.md](interfaces.md); query the installed contract before coding.

## Equation-to-hook mapping

Implement `system_spec`, `shooting_spec`, `residuals`, `jacobian`, `evaluate`, `verify`,
and `with_secondary` with current signatures, including per-call `options` where
required. Subclassing `OLSS` is optional. Declare ordered real variable blocks, shapes,
units, scales and roles; document real/imaginary packing for complex physics.

Derive the Hamiltonian/PMP or other supplied shooting equations, forward/backward
boundary conditions, control recovery and stationarity law. State branch, switching,
gauge and singular-arc assumptions. Derive sensitivities/variational equations or
another justified exact derivative route. This workflow defaults to theory-derived
analytical/variational Jacobians; any different supported provenance needs explicit
review. Do not silently replace a missing derivation with numerical differences.

`residuals` returns the complete unscaled physical vector; solver scaling belongs to
numerical policy. The Jacobian differentiates exactly that vector in variable order.
Include declared feasibility metrics `residual_norm` and `residual_max_abs`, plus the
physical selection metric and direction. For direct cost shooting, implement the
supported `cost_gradient` only from a justified derivation. Soft/hard equations must
follow the objective and boundary conditions, rather than a method label.

`verify` recomputes at independent accuracy or a declared independent route, with named
physics checks. Current qualification also requires non-empty verification options
different from working options; a hook's claim alone cannot satisfy this runtime gate.
Declare tolerances that account for working discretization error. A qualified shooting
root is not automatically an extremum or minimum.

Check analytical limits, residual dimensions, deterministic re-evaluation, input
immutability and Jacobian directional agreement at separated diagnostic steps. Verify
recovered controls through independent full-state propagation. Provide `recover_controls`
when requested for comparison/export; frequency-based starts must be justified through
that recovery or the actual shooting parametrization. Costate size is not pulse energy.

Simulation follows [build-system.md](build-system.md). For both families, document the
variable-to-control map, grid transfer and reverse seed construction where possible;
a missing inverse map is an explicit limitation, not an implicit equivalence.

---

[⌂ Home](INDEX.md)
