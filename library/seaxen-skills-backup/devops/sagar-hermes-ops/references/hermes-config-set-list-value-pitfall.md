# `hermes config set` list-value pitfall + config edit channels

## Symptom

User asks to populate a list-typed config key (e.g. `fallback_providers`) and
the obvious CLI command writes a quoted string instead of a YAML sequence.

```
$ hermes config set fallback_providers '["openrouter"]'
✓ Set fallback_providers = ["openrouter"] in /root/.hermes/config.yaml
```

But the file ends up with:

```yaml
fallback_providers: '["openrouter"]'   # WRONG — YAML string
```

Hermes treats that as a string, not a fallback list. It will either error at
provider-resolution time or silently ignore the key.

The correct shape is a real YAML sequence:

```yaml
fallback_providers:
  - openrouter
```

## Root cause

`hermes config set` takes a single scalar value argument and stores it as-is.
There is no JSON/YAML coercion for list-typed keys — `["openrouter"]` is
interpreted as a literal string, then YAML-serialized with quoting because the
brackets would otherwise be parsed as a flow sequence.

## What does NOT work

- `hermes config set fallback_providers '["openrouter"]'` — string
- `hermes config set fallback_providers '- openrouter'` — string
- `hermes config set fallback_providers openrouter` — sets a scalar string,
  still wrong type
- Hermes' guard refuses agent-side `patch` / `write_file` against
  `~/.hermes/config.yaml`:

  ```
  Refusing to write to Hermes config file: /root/.hermes/config.yaml
  Agent cannot modify security-sensitive configuration.
  Edit ~/.hermes/config.yaml directly or use 'hermes config' instead.
  ```

## What works

For list-typed (or any structured) config keys, prefer one of:

1. **`hermes config edit`** — opens the editor against `~/.hermes/config.yaml`.
   User edits the YAML directly; Hermes validates on save. Best for list,
   dict, or nested keys.
2. **Ask the user to paste / hand-edit** the YAML block, then run
   `hermes config check` to validate. Useful when the agent cannot drop them
   into an editor.
3. **Repair after a bad `set`**: `hermes config edit` and remove the surrounding
   quotes, turning `'["openrouter"]'` back into a real YAML list.

## CLI quirks to remember

- `hermes config` subcommands are: `show, edit, set, path, env-path, check,
  migrate`. There is **no `get`** — use `hermes config show <key>` or
  `read_file ~/.hermes/config.yaml` (read is allowed even when write is not).
- Direct `patch` / `write_file` against `~/.hermes/config.yaml` is blocked by
  the security guard. Reading is fine.

## Verification after a list-key edit

1. `read_file ~/.hermes/config.yaml` — confirm the key is a YAML sequence,
   not a quoted string.
2. `hermes config check` — schema validation.
3. Restart the gateway/session so the new value is loaded.

## Related context

- For `fallback_providers` specifically, the **model name** must exist on the
  fallback provider, otherwise Hermes walks the list looking for a working
  match. `zyloo/claude-opus-4-7` is an OmniRoute-internal alias — when falling
  back to OpenRouter, a real OpenRouter slug (`anthropic/claude-opus-4` or
  similar) is needed, otherwise the fallback fires but returns "model not
  found".
- Also confirm the **primary** provider is what you think. If `model.provider`
  is already `openrouter`, setting `openrouter` as its own fallback is a no-op.
  The setup that actually mitigates OmniRoute outages requires primary =
  `custom:omniroute` and fallback chain pointing elsewhere.
