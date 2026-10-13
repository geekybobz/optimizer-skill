# Optimizer Skill

Portable instructions and bounded helpers for a separately installed optimizer runtime.
[SKILL.md](SKILL.md) is the execution entry; [INDEX.md](INDEX.md) maps maintenance topics.

## Runtime connection and migration

`python3 scripts/optimizer_api.py status` reads `~/.local/share/optimizer/install.json`.
Use `--receipt <file>` or `--python <runtime-python>` for another installation;
`--source-root <path>` changes documentation context only. Execution uses isolated imports.
The standard installation here is `/Users/billabobz/OPTIMIZER` for source context and
an installed wheel in the `Optimizer` environment. No helper installs or promotes code.

This revision replaces removed registry/route/tracker discovery. Old `--resolver`,
`--route`, `OPTIMIZER_REGISTRY`, `OPTIMIZER_HOME`, `campaigns` and `tracker` helper modes
are unsupported. Consult [interfaces.md](interfaces.md) for current CLI/MCP persistence.
The old session `init/record/next/show` ledger commands are replaced by a read-only
history viewer. Existing ledgers and result archives are preserved; no migration deletes
or rewrites them. Use `scripts/optimizer_session.py <experiment> --once` or `--follow`.

## Maintenance

The canonical local skill is `/Users/billabobz/skills_ai/skills/optimizer`;
`/Users/billabobz/OPTIMIZER` owns library source and documentation context. An
explicit user request authorizes only its named skill-edit scope, which follows
the Skills AI maintenance workflow; saved context grants no future edit/release
authority. These local pointers are optional for a standalone installation.

Keep one public package and its manual invocation policy: `#> optimizer` and
`#> bloch`, plus `#> build system` for reviewed OLGS/OLSS construction. The registered spelling is `#> build-system`. Older standalone `#> optimize` and `#> use optimizer`
entry points are retired; building/optimization are operations under `#> optimizer`. Change/test the child Git
repository first; publication and parent-pointer integration are separate authorized
steps. Do not duplicate optimizer API docs, source physics or numerical results here.
See [CHANGELOG.md](CHANGELOG.md) for migration notes and `VERSION` for the release.
Run `python3 -m unittest discover -s tests` and the native skill metadata validator.
For live smoke checks, use the explicit installed Python/receipt and inspect source paths.
Forward host acceptance and numerical project validation need their own evidence;
helper tests alone do not establish either. See Skills AI's owning build/governance
protocols when integrating package metadata; this standalone package needs no registry.

## Standalone installation and recovery

Clone `https://github.com/geekybobz/optimizer-skill.git` and select `v0.2.1` for
fixed release bytes, or `main` for current source. Expose this folder through
your host's native skill installation when using it standalone. Within Skills AI,
use its registered package instead; do not expose both copies in the same host.
Install the optimizer library separately using its documented release procedure.
Update a standalone `main` checkout with `git pull --ff-only` after reading
[CHANGELOG.md](CHANGELOG.md). Version: `VERSION`. Roll back with `git revert`
or a checkout of an earlier tag. Skills AI integration is optional; this
repository needs nothing from it.

---

[⌂ Home](INDEX.md)
