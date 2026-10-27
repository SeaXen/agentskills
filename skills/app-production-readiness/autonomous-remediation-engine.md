# Autonomous Remediation Engine

> **STATUS: implemented, tested, verified.**
> `scripts/remediate.py` + `scripts/remediation_handlers.py` apply deterministic
> codemods to the blockers found by a review, keep a pristine backup of every
> file it touches, and hand everything it cannot fix safely to an AI agent as a
> recipe.

---

## 1. Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                       qa/report.md                          │
│               (Exact file:line BLOCKERS)                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 scripts/remediate.py                        │
│            (Finding Parser & Handler Router)                │
└──────┬───────────────────────┬───────────────────────┬──────┘
       │                       │                       │
       ▼                       ▼                       ▼
┌──────────────┐       ┌──────────────┐       ┌────────────────┐
│ Deterministic│       │   Atomic     │       │  Agent Recipe  │
│   Codemods   │       │ Backup &     │       │   Generator    │
│ (regex+parse)│       │  Validation  │       │ (Complex Logic)│
└──────────────┘       └──────────────┘       └────────────────┘
```

### Core tenets

1. **Never break the source.**
   Every transformation is computed in memory, validated (a real parser for
   JSON/Python/HTML, `node --check` for JavaScript when Node is installed,
   brace balancing otherwise) and **only written when it still parses**.  A
   transformation that would break the file is reported as `failed` and the
   file is left untouched.
2. **Hybrid execution.**
   - *Deterministic codemods* handle mechanical, unambiguous fixes.
   - *Structured recipes* (`qa/recipes/<gate>_<target>_<rule>.md`) are generated
     for anything that needs a human or an agent decision - long functions,
     migration chains, CORS allowlists that cannot be guessed.
3. **Reversible.** Every file is copied to `qa/fix-backup/<session>/` before it
   is written, and the **pristine** copy wins: running the engine twice never
   overwrites the original backup, so a rollback always restores the pre-fix
   state.
4. **Dry run really is dry.** `--dry-run` computes and validates every change
   and writes nothing at all - not the source, not the backup, not the log.

---

## 2. The handler library

| Handler | What it does | File types | Failure mode |
|---|---|---|---|
| `sec_xss_innerhtml` | rewrites `el.innerHTML = "plain text"` to `el.textContent` | `.js/.jsx/.ts/.tsx/.mjs/.cjs` | leaves HTML fragments and string literals alone |
| `sec_cors_wildcard` | replaces `Access-Control-Allow-Origin: *` with an allowlist check | `.js/.jsx/.ts/.tsx/.mjs/.cjs` | `manual` + recipe when the allowlist cannot be derived |
| `ui_touch_targets` | injects a `pointer: coarse` block with a 44px minimum | `.css` | `skipped` when there is no stylesheet |
| `ui_focus_visible` | injects a `:focus-visible` outline | `.css` | `skipped` when there is no stylesheet |
| `ui_reduced_motion` | injects a `prefers-reduced-motion` override | `.css` | `skipped` when there is no stylesheet |
| `code_empty_catch` | injects `console.error` into an empty `catch` | `.js/.jsx/.ts/.tsx/.mjs/.cjs` | TypeScript type annotations are dropped, never emitted raw |
| `a11y_aria_labels` | adds `aria-label` to an unlabelled `<button>` | `.html/.htm` | attributes containing `>` survive |
| `seo_meta_tags` | scaffolds description / Open Graph / Twitter tags | `.html/.htm` | values are derived from the `<title>` and the first paragraph |

Every handler returns the same shape:

```json
{"id": "sec_xss_innerhtml", "status": "applied|planned|skipped|already-ok|failed|manual",
 "detail": "...", "recipe": "qa/recipes/....md"}
```

`status` semantics:

| status | meaning |
|---|---|
| `applied` | the file was changed |
| `planned` | dry run - the change would be applied, nothing was written |
| `already-ok` | the pattern is already handled, nothing to do |
| `skipped` | nothing matched, or the file type is not supported |
| `manual` | a human/agent decision is required - a recipe was written |
| `failed` | the transformation did not validate - the file was **not** changed |

---

## 3. Safety rules (all of them are enforced in code)

- **Path containment.** Every path that comes out of `qa/report.md` is
  resolved and rejected when it escapes the project root
  (`../../etc/passwd` is refused).
- **Type containment.** A codemod only ever writes the file types it
  understands.  A JSON config never receives JavaScript.
- **Atomic writes.** A change is written to a temporary file in the same
  directory and moved into place with `os.replace`, so a crash can never leave
  a half-written file.
- **Byte fidelity.** Files are read and written as bytes, so `\r\n` line
  endings and the file encoding survive untouched.
- **Count invariants.** A codemod verifies that it changed the expected number
  of occurrences (one `innerHTML` per rewrite, one `catch` per rewrite, one
  `<button>` per rewrite).  A mismatch aborts the transformation.
- **Code awareness.** Rewrites are skipped inside strings, template literals
  and comments, so `catch (e) {}` inside a template literal is never touched.
- **Pristine backups.** `qa/fix-backup/<session>/` holds the file as it was
  *before* the first change.
- **Evidence is not source.** `qa/` is skipped by the secret scanner, the
  bundle report, the environment detector and preflight, so the engine's own
  backups can never be reported as live findings.

---

## 4. CLI

```bash
python scripts/remediate.py --root <app>              # apply the fixes
python scripts/remediate.py --root <app> --dry-run    # simulate, write nothing
python scripts/remediate.py --root <app> --recipe-only # only write recipes
python scripts/remediate.py --root <app> --rollback    # restore the backups
python scripts/remediate.py --root <app> --clean-backup
python scripts/remediate.py --root <app> --json
```

Exit codes: `0` everything succeeded (or there was nothing to do), `1` at
least one remediation failed, or a rollback restored nothing.

The mechanical fixes in `scripts/fixes.py` share the same dry-run switch
(`python scripts/fixes.py --root <app> --dry-run`) and the same backup layout
(`qa/fix-backup/latest/`), so a rollback restores both.  Among them: the
`.env.example` is generated from the variables the code actually reads, and a
project that has **no** `.gitignore` gets one that keeps `.env`,
`node_modules/` and the local review backups out of git - without it a real
secret is one `git add .` away from being committed.

---

## 5. What the engine does *not* do

- It does **not** re-measure the gate it just fixed.  Re-run the review to
  confirm the finding is closed:
  `python scripts/review.py --root <app> --serve`.
- It does **not** run the test suite or a type checker after a change.  The
  guard is a syntax validation, not a build.
- It does **not** invent a CORS allowlist, a migration, or a refactor.  Those
  become recipes.
- It does **not** touch files outside the project root.

---

## 6. Self-tests

`python -m pytest scripts/test_remediation.py -q` covers the parser, every
handler, the dry-run guarantee, the path containment, the backup/rollback
cycle, the line-ending fidelity and the CORS allowlist rules.
