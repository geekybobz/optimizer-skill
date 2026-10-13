# Reviewed Bloch plotting

One plotting workflow within [Optimizer](SKILL.md), selected by `#> bloch` or a
Bloch-plot request inside an active `#> optimizer` task.

## Plan, review, plot

1. Inspect existing saved data and static system metadata only. Identify the source
   candidate, OLGS/OLSS family, basis/reference frame, selected layers and parameter
   units. Do not call `plot_data` or `simulate` yet: either may propagate the model.
2. Present the concrete plotting plan: data source and any required propagation;
   trajectories/uncertainty scenarios; camera azimuth/elevation; appearance, colors
   and shared normalization; start/end/desired target; arrows/labels; panels; output
   paths/formats and cost. Ask for review and wait for approval before generating plots.
   The initial trigger/request selects this workflow, not approval of an unseen plan.
3. After approval, call the installed library's `opt.plot_data(system, candidate,
   kind="bloch", ...)` if data must be produced, then `opt.visualization.plot_bloch`
   or `render_bloch`. Use the same renderer for standalone saved (N,3) Bloch arrays.
   OLGS uses compatible Controls; OLSS uses ShootingVariables. The system owns all
   physics and conversion. Do not write a replacement sphere renderer in the project.
4. Inspect the output for hidden loops, overlap, clipped labels, orientation, time
   colors and distinct actual endpoint/target. Check finite data and frame identity.
   Return artifact paths and the export receipt; retain its report with the existing
   experiment checkpoints when applicable. Do not create a second numerical log.

Approval may cover an explicit batch of camera angles or variants. Work within that
batch without repeated approval; changes outside the reviewed settings need an updated
plan and review. A missing renderer capability needs a proposed extension, not a silent
fallback. Local-rule exceptions must name their scope and receive user permission.

## Reusable calls

Azimuth rotates the camera about fixed Z in degrees; elevation adjusts its height.
Changing the camera reuses data and does no propagation. A single view cannot guarantee
all crossings are visible. Offer a reviewed second view when useful. Use paper appearance
for a light orthographic scaffold; legacy appearance preserves older plotting conventions.

```python
data = opt.plot_data(system, candidate, kind="bloch")
receipt = opt.visualization.render_bloch(
    data, "figures/trajectory",
    options={"appearance": "paper", "azimuth": 36, "elevation": 14,
             "cmap": "viridis_r", "axes": True, "arrows": 2},
)
```

Use explicit target annotations from the system; never label the actual endpoint as
its target by assumption. Shared colorbars require compatible quantities, units and
normalization. Mixed states remain inside the sphere. Export uses new filenames;
a lost reply/history failure does not remove completed files. Inspect before retrying.
Current installed API discovery belongs to [interfaces.md](interfaces.md); this guide
owns the plotting-review gate. Fresh-host adherence requires observed acceptance,
not only helper tests. No automatic plot or browser launch is required.

---

[⌂ Home](INDEX.md)
