# What to publish now (3.x, before 4.0)

Publish three things: a deprecation notice page, a changelog entry, and a pinned issue about `Result.errCode`. The text is below. Items in `[brackets]` are facts you didn't give me, so fill them in and don't guess.

## Why these three, and why now

- **Users upgrade whenever they want.** Many will jump from 3.x straight to 5.0, so the notice has to reach them in 3.x and stay in the 4.x docs. A migration guide that appears only with 5.0 comes too late.
- **Only `Config.timeoutMs` has a stated replacement.** The three others don't, so the page needs a migration path for each. Fill in `renew()` and `--legacy-cache` if they have one. If they don't, say so plainly.
- **`Result.errCode` is the real risk.** Removing something with no replacement leaves its users stuck. The four months before 4.0 are your window to find those users. A pinned issue costs nothing and could change the decision.

## 1. `DEPRECATIONS.md` (also linked from the docs site and README)

```markdown
# Deprecations

Four APIs are deprecated since 3.4 and will be **removed in 5.0**.
They keep working, with a warning, throughout 3.x and 4.x.
No removal happens in a minor or patch release.

| Deprecated | Since | Removed in | Replacement |
| --- | --- | --- | --- |
| `Session.renew()` | 3.4 | 5.0 | [replacement, or "none"] |
| `--legacy-cache` flag | 3.4 | 5.0 | [replacement, or "none"] |
| `Config.timeoutMs` | 3.4 | 5.0 | `Config.timeout` |
| `Result.errCode` | 3.4 | 5.0 | None |

## Migrating

### `Config.timeoutMs` -> `Config.timeout`
[Before/after snippet. State the unit of `timeout`: if it is not
milliseconds, say so. State which wins if both are set.]

### `Session.renew()`
[Migration steps, or: "No replacement. Use X instead / stop calling it."]

### `--legacy-cache`
[Migration steps, including what changes in cache behavior for users
who relied on the legacy layout.]

### `Result.errCode`
Removed with no replacement: it is no longer exposed.
If you depend on it, tell us now: [link to pinned issue].
We want to know what you use it for before 5.0 is final.

## Timeline

- 3.4: deprecated, warnings added.
- 4.0 (planned [month/year]): still present, still warns.
- 5.0 (not scheduled): removed. [Optionally: "no sooner than N months after 4.0".]

If you skip 4.x, read this page before upgrading to 5.0.
```

## 2. Changelog entry (next 3.x release)

```markdown
### Deprecation notice
`Session.renew()`, `--legacy-cache`, `Config.timeoutMs` and `Result.errCode`
are deprecated and will be removed in 5.0. They still work in 3.x and 4.x.
See DEPRECATIONS.md for migration steps. If you use `Result.errCode`, please
comment on [issue link].
```

## 3. Pinned issue: "Do you rely on `Result.errCode`?"

```markdown
`Result.errCode` is deprecated and slated for removal in 5.0, with no replacement.
If you read it, tell us:
- what you use it for,
- what you would need instead.

We will decide before 4.0 ships whether to add a replacement or keep it.
```

## Code changes to ship with the notice

- Emit a **runtime warning once per process** for each of the four. Use stderr for the CLI flag and the language's deprecation mechanism for the API. Each warning should say "removed in 5.0" and link to `DEPRECATIONS.md`.
- Mark the symbols deprecated in types and docs, with the same link.
- Keep `timeoutMs` working. If both `timeoutMs` and `timeout` are set, `timeout` wins, and that is documented.

## Decisions for you

1. **Is `Result.errCode` already non-functional?** You said you "stopped exposing it". If it already returns nothing, that was a breaking change in a minor release. Document it as such, and the warning and removal timeline for it become moot. My notice assumes it still works with a warning.
2. **Do you want a minimum gap between 4.0 and 5.0?** A stated gap, for example 6 months, gives skip-upgraders predictability. Leaving it unscheduled costs you nothing now.
3. **Is the `errCode` decision reversible?** If the issue shows real users, be ready to add a replacement or drop it from the removal list. The notice says that outcome is possible.