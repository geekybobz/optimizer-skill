# Changelog

Versions follow SemVer. Below 1.0.0 a MINOR release may break, and its entry says so.

## 0.2.0 — 2026-10-13

Breaking pre-1.0 migration: the standalone aliases and helper commands listed
below change. Existing numerical archives are preserved.

Manual entry points are `#> optimizer`, `#> bloch` and the reviewed-construction
shortcut `#> build system` (registered as `#> build-system`). Standalone
`#> optimize` and `#> use optimizer` entry points are retired. Bloch requests must present a plan, wait for review,
and use the installed shared renderer after approval.

Reviewed OLGS/OLSS construction now routes through specialized guides; optimization
requires structured low-energy multistart and independent evidence. A final-candidate
guide adds gradient/KKT checks, feasible downhill tests, constrained curvature, shooting
extremal checks and independent incumbent challenges without global-optimality claims. Runtime discovery
uses installed receipts/isolated imports. The session helper is a read-only history
viewer; old registry/tracker discovery and ledger commands are unsupported. Existing
archives are preserved. No optimizer library release is included.

## 0.1.0

First tracked version, tagged `v0.1.0` on 2026-10-09. The portable skill adapter for
a separately installed Optimizer system: manual `#> optimizer`, `#> build-system`
and `#> optimize` routes, the adaptive build and campaign workflows, situation
analysis, Claude and Codex wrappers, and a read-only discovery helper. The package
now carries its own tests (`tests/test_package_contract.py`), `VERSION`, this
changelog and a CI workflow, so a standalone clone verifies on its own.

---

[⌂ Home](INDEX.md)
