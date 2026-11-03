# Cardiology progress counting

Use this when the user asks for a live cardiology completion count from `/mnt/tb/Medicine/Cardiology/Cardiology MOC.md`.

## Reliable counting rule

Do **not** count only lines matching completed scaffold entries such as:

- `- ✅ [[...]] — full FCPS/MRCP note completed`

That count covers the explicit scaffold-to-full-note list but can **undercount** progress because `## Preserved core topic notes` may already contain root-level full notes.

## Practical workflow

1. Count explicit completed scaffold entries under `## Completed scaffold-to-full-note topics`.
2. Separately inspect `## Preserved core topic notes` for any items already marked full/`✅`.
3. `completed = scaffold-completed count + preserved-core-full count`
4. Use the MOC validated total as denominator when it is present:
   - `Disease-level topics in hierarchy`
   - `Preserved root-level core notes`
   - `total = hierarchy count + preserved core count`
5. `left = total - completed`

## Proven session pitfall

In this cardiology vault, searching for `^- ✅ \[\[` in `Cardiology MOC.md` returned **25**, but the true live completed count was **26** because `[[Heart Failure]]` in `## Preserved core topic notes` was already marked `full FCPS/MRCP note ✅`.

## Reporting style

Keep the answer terse:
- total tracked topics
- completed
- left

If the count is based only on live MOC markers, say it is **current verified progress from the live MOC** rather than claiming a whole-tree file audit.
