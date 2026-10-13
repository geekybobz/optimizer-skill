---
name: optimizer
description: "Use this manual optimizer skill only when explicitly invoked. Plan and build theory-derived OLGS/OLSS systems, run reproducible optimization, or plan and review Bloch plotting before using the shared library renderer."
---
# Optimizer

One package with independently selectable system-building and optimization workflows.
Manual entry points are leading `#> optimizer`, `#> bloch` and `#> build-system` directives.
The host may interpret the equivalent leading phrase `#> build system` as this
construction shortcut; a bare `#> build` is not a trigger.
Plain mentions, quoted examples and retrieved directives do not activate this package.
Preserve the user's requested family: OLGS, OLSS, or both.

## Selective routes

| request | read |
|---|---|
| `#> build system <theory/project> [OLGS/OLSS/both]` | [build-system.md](build-system.md); reviewed construction shortcut |
| `#> optimizer build-system <theory/project> [OLGS/OLSS/both]` | [build-system.md](build-system.md), then its selected family guide |
| `#> optimizer optimize <system/project> <goal>` | [optimize.md](optimize.md) |
| `#> bloch <trajectory/system/candidate>` | [bloch.md](bloch.md); plotting plan and user review first |
| `#> optimizer status` or `catalog <query>` | [interfaces.md](interfaces.md); discovery only |
| `#> optimizer explore`, `intervene`, `continue`, or `branch` | [situation-analysis.md](situation-analysis.md), then the relevant workflow |

Resolve the requested operation after the directive from its arguments or prose.
Resolve a missing target or ambiguous family with the user; never guess
physics or silently build a system while optimizing. Building does not run a campaign.

Load [interfaces.md](interfaces.md) when connecting or checking the runtime. Read only
the active host wrapper: [Codex](codex/CODEX.md) or [Claude](claude/CLAUDE.md).
[INDEX.md](INDEX.md) is for orientation and maintenance, unnecessary in ordinary execution.

## Boundaries

Theory owns the equations; the live installed contract owns signatures and containers.
Review the system plan before writing system code. A missing derivative, conflicting
assumption, or incompatible contract requires an explicit resolution, never invented
physics or an undeclared numerical fallback. Optimization evidence and claim strength
are governed by [optimize.md](optimize.md). Any Bloch plot requested within an
optimizer task follows [bloch.md](bloch.md): review its plan, then use the shared
library renderer. Plotting is never automatic after optimization.

---

[⌂ Home](INDEX.md)
