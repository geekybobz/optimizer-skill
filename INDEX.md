# Optimizer package map

One manual skill; selectively loaded references own distinct decisions.

| intention | owner |
|---|---|
| select a workflow | [SKILL.md](SKILL.md) |
| plan/review system construction | [build-system.md](build-system.md) |
| implement gradient formulation | [build-olgs.md](build-olgs.md) |
| implement shooting formulation | [build-olss.md](build-olss.md) |
| multistart and problem identity | [optimize.md](optimize.md) |
| extremal qualification and lowest-energy confidence | [extremal-checks.md](extremal-checks.md) |
| reviewed Bloch plotting and shared renderer usage | [bloch.md](bloch.md) |
| runtime, persistence, report and terminal visibility | [interfaces.md](interfaces.md) |
| diagnose and choose an intervention | [situation-analysis.md](situation-analysis.md) |
| host-specific lifecycle | [Codex](codex/CODEX.md), [Claude](claude/CLAUDE.md) |
| installation/migration and package maintenance | [README.md](README.md) |

Ordinary path: SKILL → selected workflow → selected specialization as needed.
Runtime connection adds interfaces; only the active host wrapper loads.
Scripts: [discovery](scripts/optimizer_api.py) queries installed contracts;
[viewer](scripts/optimizer_session.py) reads the existing history without a ledger.
Tests check helpers, bounded rendering and package links; live host behavior has its
own acceptance boundary. Registry/governance remain owned by Skills AI; physics and
run artifacts remain in the optimization project, not in this package.

---

[⌂ Home](README.md)
