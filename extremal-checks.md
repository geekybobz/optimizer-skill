# Extremal and lowest-energy evidence

Read when qualifying a final candidate or investigating apparent convergence.
Parent: [Optimize](optimize.md). This page owns local qualification and claim strength;
[Optimize](optimize.md) owns search coverage and problem identity.

## Gradient acceptance

1. Independently replay the candidate; satisfy the stated target, constraints and bounds.
   Validate the analytical derivative before interpreting stationarity.
2. For a soft unconstrained objective, measure its full gradient. For hard constraints,
   audit the Lagrangian/KKT residual: objective gradient plus constraint-Jacobian transpose
   times multipliers, bound multipliers with correct signs, feasibility and complementarity.
   A raw objective gradient need not vanish at a constrained extremal. A tangent projection
   alone does not establish correct bound multipliers or nonlinear feasibility.
3. Derive scale-aware tolerances from the model and quadrature. Record both discrete and
   physical gradient conventions; a small grid-weighted derivative can hide a large
   continuum stationarity residual. Require stability under tighter propagation and,
   where relevant, grid refinement followed by replay and bounded reoptimization.
4. Screen for downhill feasible directions: use justified analytical HVP/curvature where
   available, and bounded local perturbation/reoptimization tests at separated amplitudes
   across admissible smooth directions. For hard constraints, construct feasible tests
   through a justified retraction/restoration; simple clipping or a tangent step need not
   preserve constraints. Include weak/negative-curvature directions when discovered.
5. For constrained second-order analysis, use the Hessian of the Lagrangian on the
   appropriate tangent/critical cone, including active inequalities and constraint
   curvature. Objective curvature alone is insufficient. Check regularity, rank, gauge
   freedom and degeneracy before applying a sufficient-condition theorem.

Use existing diagnostic tools only after checking their live derivative policy and
cost. Analytical derivatives remain the solver source. Explicit small numerical
comparisons/perturbations are diagnostic evidence, not silent derivative replacements.
Sampled curvature with no negative direction is a screening result, not positivity
throughout the full admissible space. Missing or inconclusive evidence stays explicit.

## Shooting acceptance

An independently verified shooting root supports an extremal candidate only when its
residuals enforce the derived stationarity, boundary/transversality and admissibility
conditions, including switches or singular arcs when present. Verify those conditions
and recovered-control full-state replay. Root convergence alone cannot distinguish a
minimum, maximum, saddle, or higher-energy branch. Apply the appropriate local evidence
above in the admissible representation when a minimum claim is needed.

## Numerical confidence in lowest energy

Compare independently qualified candidates from the multistart coverage in
[Optimize](optimize.md). Challenge the incumbent with an additional independent seed
batch and local restarts; check whether its energy changes beyond the declared numerical
uncertainty. Allocate/review this challenge budget before acceptance, not after reporting.
Cross-formulation comparison is useful when both systems and a valid transfer are available.
Record best-energy stability, refinement effects, rejected starts, coverage gaps and
unresolved branches. If a lower verified value appears, replace the incumbent and repeat
within the agreed budget. If the budget ends first, report incomplete confidence.

Use precise labels: feasible candidate; numerically stationary candidate; extremal
candidate supported by the model equations; numerically supported local minimum; or
lowest verified energy found across the stated search and checks. Feasibility and
first-order stationarity alone permit saddles. Claim a proved local extremum only when
applicable sufficient conditions are actually established. Finite searches cannot ensure
the lowest possible energy over all controls; global optimality requires separate proof
or certificate. State the tested domain and uncertainty even when confidence is strong.

---

[⌂ Home](INDEX.md)
