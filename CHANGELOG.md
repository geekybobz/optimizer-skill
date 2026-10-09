# Changelog

Versions follow SemVer. Below 1.0.0 a MINOR release may break, and its entry says so.

## 0.1.0

First tracked version, not yet tagged. The portable skill adapter for a separately
installed Optimizer system: manual `#> optimizer`, `#> build-system` and
`#> optimize` routes, the adaptive build and campaign workflows, situation analysis,
Claude and Codex wrappers, and a read-only discovery helper. The package now carries
its own tests (`tests/test_package_contract.py`), `VERSION`, this changelog and a CI
workflow, so a standalone clone verifies on its own.
