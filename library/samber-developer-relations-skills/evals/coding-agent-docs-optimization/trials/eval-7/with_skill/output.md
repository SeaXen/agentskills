## What actually broke

Three strangers hit the same invented call. That's not noise — that's your cold-run baseline, already collected for free. `Engine::new_with_config` is a confident prior from pre-0.9 training data, and nothing in your current surfaces overrides it. Per the skill's calibration data: models reproduce removed APIs confidently unless an in-place, machine-readable label says otherwise. You don't have that label anywhere yet.

Your constraints already delete most of the skill's menu:

- ❌ No CDN, no response headers → drop header-based advertising (`Link:` relations, CDN bot policy) entirely.
- ❌ No docs team, no build pipeline beyond the mdbook CI job → drop anything needing new infrastructure.
- ❌ docs.rs is Rust Foundation infra, not yours → you can't change its crawler policy or its build. If it turns out to block AI crawlers, that's a report-upstream finding, not something you fix.

What's left fits in evenings. Do it in this order.

## 1. Fix the root cause first — make the compiler carry the migration note

This is the highest-leverage documentation surface you have, and it's specific to compiled languages: coding agents run `cargo build`/`cargo check` as part of their own loop, so a compiler diagnostic reaches them with zero crawling, zero index file, zero advertising.

**If the old constructor's behavior can still be reconstructed from the current API** (likely, since something replaced it), un-delete it as a thin deprecated shim for one more release:

```rust
#[deprecated(
    since = "0.9.0",
    note = "removed in 0.9; use `Engine::builder()...build()` instead — see CHANGELOG.md#0.9.0"
)]
pub fn new_with_config(config: EngineConfig) -> Engine {
    Engine::builder().apply_config(config).build()
}
```

Three independent bug reports justify the small upkeep cost. An agent that calls this now gets a compiler *warning* containing the exact fix, in its own build output, before it ever touches your docs.

**If forwarding isn't semantically possible** (config shape changed too much), you can't resurrect the symbol — a stub whose body unconditionally errors would break every downstream build at *ferroquant's own compile time*, not the caller's, so don't do that. Fall back to the doc-comment and CHANGELOG fixes below as your only lever.

## 2. Name the exact symbol in the CHANGELOG

Agents and humans alike often arrive by pasting the broken call or the error text. Match it exactly:

```markdown
## 0.9.0
### Removed
- `Engine::new_with_config(EngineConfig)` — replaced by `Engine::builder().build()`.
  Calling the old name now emits a deprecation warning naming the replacement
  (or fails to compile, if you didn't keep the shim). See migration notes below.
```

## 3. Doc comments — your typed-SDK surface, promote it above everything else

docs.rs is generated entirely from your `///` comments, and an in-editor agent reads the signature and its adjacent doc comment before it reads anything on the web. Put the removal notice there too, and make the replacement's example a real doctest so `cargo test` fails the build if it drifts — it can't rot silently the way book prose can:

```rust
/// Construct an `Engine` from a builder.
///
/// `Engine::new_with_config` existed before 0.9 and was removed; you will not
/// find it on this type in current releases. Build one with
/// [`Engine::builder`] instead:
///
/// ```
/// use ferroquant::Engine;
/// let engine = Engine::builder().build();
/// ```
impl Engine {
    pub fn builder() -> EngineBuilder { EngineBuilder::default() }
}
```

Sweep every book page that still shows the old constructor and apply the same label at the top, not a footnote.

## 4. Markdown endpoints — you already have them, just link to them

Your mdbook `src/*.md` files are plain markdown sitting in git right now. `raw.githubusercontent.com/<you>/ferroquant/main/book/src/quickstart.md` is a working markdown endpoint today, zero build change.

Fast follow once you touch the CI workflow again: **add one `cp` step** that copies `book/src/*.md` alongside the rendered HTML in the Pages output, so the markdown twins live on your own domain instead of GitHub's.

## 5. Ship one `llms.txt` at the repo root

```markdown
# ferroquant

> [one-line description]. Current version: X.Y (crates.io/crates/ferroquant).

## Getting started

- [Book: introduction](https://raw.githubusercontent.com/<you>/ferroquant/main/book/src/intro.md): what ferroquant does, install, first example
- [Book: quickstart](https://raw.githubusercontent.com/<you>/ferroquant/main/book/src/quickstart.md): build and run an Engine

## Reference

- [docs.rs](https://docs.rs/ferroquant/latest/ferroquant/): full generated API reference, current release
- [CHANGELOG](https://raw.githubusercontent.com/<you>/ferroquant/main/CHANGELOG.md): every breaking change and removed symbol, by exact name

## Optional

- [Full book, single page](https://<you>.github.io/ferroquant/print.html): entire book concatenated
```

One file, committed. Copy it into the mdbook static-asset directory so GitHub Pages also serves it.

## 6. Full-corpus bundle — you already have it too

mdbook ships `print.html` (whole book, one page) by default. Skip building anything new; just point `llms.txt`'s Optional section at it.

## 7. Advertise without needing headers

You can't set response headers, but you *can* inject `<head>` markup at build time via mdbook's theme override — that's a repo file, not a CDN setting. **Add `theme/head.hbs`**:

```html
<link rel="describedby" href="{{ path_to_root }}llms.txt">
```

Add one line to the README naming the `llms.txt` URL, and one entry in the book's `SUMMARY.md` pointing at it. That's your three advertising spots — repo, navigation, and page markup — with zero CDN involvement.

## What stays off the list

- ❌ OpenAPI-style spec annotation — no such spec exists for a Rust crate; rustdoc *is* your spec, handled by step 3.
- ❌ Building new full-corpus tooling — `print.html` already exists.
- ❌ Response-header or CDN-policy work — no CDN account.
- ❌ Touching docs.rs's build or crawler policy — not yours to change.

## Closing the loop going forward

Freeze a 5-task set, task 1 being the exact scenario that burned you: *"construct an `Engine` with a custom config."* Open a fresh chat session, restrict it to docs.rs + the book URL, run unattended, log whether it invents a call. Re-run after every release, never in a session that already solved the task.

Bar to hold, scaled to a solo evenings project — skip the published 80% stretch target as a formal KPI, it's not worth tracking for one maintainer:

- ✅ Zero invented calls on `Engine` construction specifically — this is the one that already reached three users.
- ✅ Corrective turns trend down release over release, not an absolute number.

That's the whole plan: one compiler-level fix, one CHANGELOG line, one doc-comment sweep, one `llms.txt`, one `head.hbs` addition. Nothing here needs a CDN, a header, or a new pipeline — it all rides the mdbook CI job you already run.