# README audit — stagline/toolbelt (audience: developers evaluating a Python package/CLI toolbelt — confirm if procurement/enterprise readers matter too)

**Access caveat, stated up front, not buried:** I don't have a checkout of this repo and can't run `scripts/readme-audit.sh`, install anything, or verify a single claim against source. Per the skill this audit is built on: Band A (identity, install-runs, claim-verification, status honesty, licence reachability) is **not scored** — I'd be guessing, and guessing is exactly what this process exists to replace. Everything below is scored only from the facts you gave me, which happen to be enough to find a real, high-impact problem.

## The finding that outranks the other three

You have two READMEs — `.github/README.md` and root `README.md` — and GitHub's own precedence order is `.github` → root → `docs`. That means **the version you're judging ("on GitHub it looks great") is the `.github/` copy.** It is not the file anyone sees anywhere else:

- Not on PyPI. Four of your six packages publish there, and a `pyproject.toml`/`setup.cfg` `readme =` pointer almost always resolves to the **root** file, not `.github/`.
- Not in a `git clone` opened locally, in an IDE preview, on `raw.githubusercontent.com`, or on any mirror.

So the file most of your evaluators actually read is the root one — the one carrying the three problems below. "It looks great on GitHub" is true and irrelevant; you audited the wrong surface.

This is a named anti-pattern in the skill I'm working from, not a taste call: *"Keep only one rendered README. Where a host renders a `.github/` copy in preference to the root file, the root copy is what registries and mirrors publish, so the two silently diverge."* Yours has already diverged — you said so yourself.

**Fix, before anything else on this list:** pick one canonical file. For a project with four PyPI packages, that has to be the root `README.md`, since that's the one your registry pages depend on. Delete `.github/README.md` outright, or make it a symlink to the root file so it's physically impossible for them to drift again. Don't maintain two hand-edited copies — that's the mechanism that got you here.

## The three problems in the surviving (root) file

**1. `![architecture](docs/img/arch.png)` — relative path, breaks on every PyPI project page.**
PyPI has no support for relative image paths at all — this isn't a maybe, it's confirmed behavior on the registry, not a GitHub-only nicety. On all four package pages this renders as a broken-image icon. Fix: point it at an absolute URL (`https://raw.githubusercontent.com/stagline/toolbelt/main/docs/img/arch.png`), or drop the diagram from the README entirely and link out to a docs page — an architecture diagram is rarely fast-eval content anyway; a reader deciding "does this fit my codebase" gets there from the one-liner and the usage example, not the box-and-arrow diagram.

**2. `<details><summary>` wrapping the config table — raw HTML, and registries are documented to strip raw HTML.** Best case on PyPI, the collapse/expand behavior just vanishes and the table dumps flat (survivable). Worst case, the tags get stripped in a way that mangles or hides the table (config reference silently gone for every registry reader). Either way, this is real reference material — a config table isn't identity-or-differentiation content — and it belongs in a linked doc, not inlined behind a click. Move it to `docs/configuration.md` (or the relevant package's own reference doc), leave one line in the README pointing at it, and delete the `<details>` wrapper. That also removes the raw-HTML risk outright instead of hoping the registry renderer is forgiving.

**3. A 6 MB demo GIF pinned above everything else.** Three separate problems stacked in one element:
- **Weight and position**: 6 MB loads before a reader reaches the one-liner, the differentiation paragraph, or the install command — the opposite of "let the reader disqualify fast." A GIF that heavy at the very top actively works against the funnel, it doesn't serve it.
- **Content trapped in an image**: if any command or flag shown in the recording doesn't also exist as copyable text somewhere in the README, that's decision-relevant content invisible to a PyPI reader, a terminal, or a screen reader — none of them render animated GIFs.
- **Wrong altitude for a monorepo root.** This is a six-package repo; the demo shows one CLI. Putting one package's demo at the top of the *router* page implicitly promotes that package over the other five. A monorepo root should route to per-package READMEs, not carry one package's full demo inline — that belongs on that package's own README, sized and placed there (short, high-contrast, right after its own tagline, regenerated from a script — e.g. VHS or asciinema — so it doesn't go stale, rather than hand-recorded once and left to rot at 6 MB).

## What this means for the root's overall shape

Given six packages and an architecture diagram, a demo GIF, and a config table all inlined at the top, this reads like a single-package README that a monorepo grew around, not a router. The fix for items 1–3 above naturally produces the router shape: name, one-liner, a short table of the six packages with links to their own READMEs (flagging which four are on PyPI), a why-this paragraph, and pointers out to the architecture doc and the config reference — each package's own README carries its own install, usage, and demo.

## Scorecard

```
README audit — stagline/toolbelt   (audience: developer evaluating a package/CLI to add; confirm procurement audience)
Band A: NOT SCORED — no repository access (need Q1: repo path/clone, or pasted README + pyproject.toml files)
Band B: B4 0/2 (6 MB media before identity/why content) · B6 0/2 (image trapped content, likely no alt text, unconfirmed) ·
        B7 0/2 (relative image path + raw HTML — both break on the PyPI pages that 4 of 6 packages depend on) ·
        B8 unscored (can't confirm section count/overflow without full text)
Verdict: does not pass — shadowed-README divergence is the root cause; fix that before rescoring anything else
```

## Fix order (return-per-hour, this case)

1. Collapse the two READMEs to one canonical file (root) — everything else is wasted effort while two copies can still drift.
2. Absolute-URL the architecture image.
3. Un-wrap the config table from `<details>`, relocate it, leave a pointer.
4. Move the demo GIF off the root and onto its package's own README; regenerate it smaller and script-driven; ensure its commands also exist as text.
5. Once you can give me repo access (or paste both files, the four packages' `pyproject.toml` readme fields, and the actual install commands): I'll run the mechanical script, verify every flag/command/config key against source (A3), execute the install path from clean (A2), and pull two weeks of traffic split by referrer to confirm the README — not distribution — is actually the bottleneck (Step 1 of this process; skipping it risks polishing a page almost nobody reaches).

I'm not citing GIF-conversion-rate or contribution-rate figures anywhere above — those numbers circulate widely and have no real source behind them; the argument for moving the demo rests on page weight, funnel order, and content-trapped-in-image, all of which hold regardless of any conversion percentage.