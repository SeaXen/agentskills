# Hermes `providers:` vs `custom_providers:` — picker vs remove list (Jun 2026)

## Symptom

User sees Groq, TokenRouter, SambaNova, Together, 0g.ai, api.b.ai in the model provider picker (often alongside Manifest `auto`), but **not** in `hermes model` → remove custom provider. User believes these are separate Hermes custom adds (env-backed keys), not Manifest dashboard-only.

## Verified config shape (`~/.hermes/config.yaml`, `_config_version: 30`)

**Before consolidate (Jun 2026):** hybrid — dict had Groq/TokenRouter/etc.; list had Bynara/OpenModel/Menifest-Docker.

**After consolidate (2026-06-26):** `providers: {}`; **10** rows in `custom_providers:` (original 3 + moved 7: Groq, SambaNova, Together, api.b.ai, Manifest cloud, 0g.ai, TokenRouter).

**Historical `providers:` dict (pre-move):**

- `api.groq.com` — `key_env: GROQ_API_KEY`
- `api.sambanova.ai` — `key_env: SAMBANOVA_API_KEY`
- `api.together.xyz` — `key_env: TOGETHER_API_KEY`
- `https://api.b.ai/1` — inline `api_key`
- `manifest` — Manifest cloud router (`default_model: auto`)
- `router-api.0g.ai` — inline `api_key`
- `tokenrouter` — inline `api_key`, `default_model: MiniMax-M3`

**`custom_providers:` list (~795+):**

- Bynara.id, Api.openmodel.ai, Menifest - Docker (LAN self-hosted Manifest)

## Code behavior (hermes-agent)

- **Merged picker:** `hermes_cli/config.py` → `get_compatible_custom_providers()` reads list + `providers_dict_to_custom_providers(providers)`.
- **Remove menu:** `hermes_cli/main.py` → `_remove_custom_provider()` only `pop()`s from `custom_providers` list; never deletes `providers[<slug>]`.
- **Migration:** v11+ upgrade can move list entries into `providers:` and drop `custom_providers` from disk; runtime still resolves via compat layer (`tests/hermes_cli/test_config.py`).

## Operator actions

| Goal | Action |
|---|---|
| Remove Groq / TokenRouter from picker | Delete `api.groq.com:` / `tokenrouter:` (etc.) under `providers:` |
| Remove Bynara | Use remove menu **or** delete list entry |
| Add another endpoint | Append to `custom_providers` **or** add new slug under `providers:` (same runtime; different remove UX) |
| Want remove menu for dict entries | **Consolidate:** convert slugs to list rows, then `providers: {}` (see below) |

## Consolidate dict → list for remove-menu parity (2026-06-26)

User asked to move all `providers:` rows into `custom_providers:` so Groq/TokenRouter appear in remove list.

**Steps:**

1. Backup `config.yaml`.
2. Map each dict entry → `{name, base_url, model?, key_env?, api_key?, api_mode?}` (`api` → `base_url`, `default_model` → `model`).
3. Append to existing `custom_providers` (skip duplicates by name+URL).
4. Replace top `providers:` block with `providers: {}` (or delete only moved slugs).
5. Verify YAML loads; list count = prior list + moved count.

**Result on default profile:** 3 existing + 7 moved = **10** `custom_providers`; empty `providers:` dict. Backups: `config.yaml.bak-move-custom-*`, `config.yaml.bak-pre-move-custom`.

**Pitfall:** Full-file `yaml.safe_dump` destroys comments — use line-splice script or manual `patch` only.

## Misdiagnosis to avoid

- “Manifest manages Groq” — false; only `providers.manifest` is Manifest. Other slugs are independent user endpoints.
- “Not removable” — removable by YAML edit; only the **CLI remove list** is incomplete for `providers:` dict entries.