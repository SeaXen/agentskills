# Obsidian graph dashboard — force-layout, minimap, and saved positions

Use this when the user wants the Obsidian vault dashboard graph to feel smoother and more navigable instead of being a static cluster map.

## Scope

Target file:
- `/mnt/tb/hermes/obsidian_dashboard.py`

In this install, that path resolves to the same real file as:
- `/root/.hermes/obsidian_dashboard.py`

Do not patch one and assume the other is separate. Verify the real path first when confused.

## Proven upgrade bundle

For the existing single-file dashboard (`obsidian_dashboard.py` serving inline HTML/CSS/JS), the useful bundle was:

1. Replace static seeded graph behavior with an **animated force-layout**.
2. Add a **mini-map** canvas in the graph panel.
3. Add **browser-persistent saved positions** via `localStorage`.
4. Support **drag-to-pin** node behavior.
5. Add explicit controls:
   - `Repack`
   - `Save layout`
   - `Reset view`
6. Improve **label placement** with simple overlap avoidance instead of drawing every label in a fixed offset.
7. Improve **node collision** with pairwise repulsion + minimum-distance push.

## Practical implementation pattern

The dashboard is a Python file with a large inline `INDEX = r"""..."""` HTML/JS string.

Reliable edit path:
- patch CSS/HTML blocks directly if anchors are unique
- replace the whole `<script>...</script>` block in one operation when the graph logic changes substantially
- after editing, extract the inline JS to a temp file and run `node --check` on it
- also run `python3 -m py_compile` on the Python file

This is safer than many small string edits inside a long inline script.

## State model that worked

Useful browser-persisted keys:
- `hermes-obsidian-layout-v2:<vault-path>`
- `hermes-obsidian-view-v1:<vault-path>`

Persist:
- node positions
- pinned state
- last-saved timestamp
- zoom / pan view

Important product truth:
- this is **per-browser/per-device persistence** only
- if the user wants shared layouts across devices, the next step is a backend `/api/layout` read/write path, not more frontend storage tweaks

## Verification sequence

1. `python3 -m py_compile /root/.hermes/obsidian_dashboard.py`
2. extract inline JS and run `node --check`
3. restart `obsidian-vault-dashboard.service`
4. verify listener on `:6065`
5. load `http://127.0.0.1:6065/`
6. verify in browser that:
   - `Repack` button exists
   - `Save layout` button exists
   - minimap canvas exists
   - graph stats/meta blocks render
   - layout save survives refresh via `localStorage`

## UI details that improved usability

- help text should explicitly say `Animated force layout`
- minimap should live inside the graph panel, not outside it
- meta/status pills like `Pinned`, `Saved`, and `Labels` help make the feature legible
- selected / pinned / missing states need distinct colors in both main graph and minimap

## Pitfalls

- If you only patch `/mnt/tb/hermes/obsidian_dashboard.py` or `/root/.hermes/obsidian_dashboard.py` without checking realpath, you may think there are two files when there is only one.
- If you verify only page load, you can miss broken inline JS. The page shell can still render while the graph logic is dead.
- `localStorage` persistence is not shared persistence. Do not oversell it.
- For large inline-script changes, whole-script replacement is often more reliable than many tiny patch-tool edits.
