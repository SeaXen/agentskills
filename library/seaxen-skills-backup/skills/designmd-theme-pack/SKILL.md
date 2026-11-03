---
name: designmd-theme-pack
description: "Make Designmd theme packs from a real site."
---

# Designmd Theme Pack

Build a **theme pack** for the user's `/mnt/tb/#Sea/Designmd/` design store: extract a real live website's design system and ship four files (CSS, HTML demo, design notes, regeneration prompt) registered in the shared theme switcher. This is the user's recurring ask — they have said "do you best" on batches of 5-10 sites at a time, and the same recipe works every time.

## When to use

- The user names a website URL and asks to learn it, copy it, or add it to the design store.
- The user asks for a "1:1 copy" of a site (treat as full extraction; deliverable is the same).
- The user asks for a "theme pack", "design extraction", or "make it look like X".

## When NOT to use

- The user wants a Hermes **skin** (YAML for the CLI/TUI/desktop palette) — that's `hermes-themes`, a different skill entirely.
- The user wants a CSS framework to **use** in a project — that's a dependency, not a theme pack.
- The user wants a 1:1 HTML clone of a specific page of a large SPA, project by project — that is a *project*, not a theme pack; ask for scope before starting.

## User preferences (always-on)

- **All CSS scoped to `html[data-theme="<name>"]`** — never use bare tag selectors. The store has 40+ themes loaded together; non-scoped CSS collides.
- **Skill description frontmatter ≤ 60 characters** (validator enforces). Trim and re-check before saving.
- **Folder layout is fixed**: `<name>/<name>.css`, `<name>/<name>.html`, `<name>/<name>.md`, `<name>/<name>-prompt.md`. Optional `preview.png` from a prior render is fine to leave in place.
- **`theme.js` is the registry** — append the new entry, do not reorder existing ones.
- **README.md gets a new `### <N>. <name>` section** in numeric order, with the same 5-line shape (Mood / Palette / Type / Style / Source) and a Files bullet. Add the theme id to the bullet list at the bottom.
- **Sanity-check a 200 status on the home page before starting** — old GitHub-Pages URLs can return 200 with the literal string "Site not found" inside the body. Check for that string; if present, skip the site.
- **CSS is `oklch` when the source is** — don't silently down-convert OKLCH to hex. If the source uses hex, stay hex.
- **Dark-mode strategy follows the source**: `prefers-color-scheme` (most), `.dark` class (marcbouchenoire), or no dark mode (vercel). Don't add a toggle that isn't in the source.

## Procedure

1. **Read the user's intent precisely.**
   - "extract this", "add this to my design store" → design-system extraction (HTML demo with synthetic content, real tokens, real layout).
   - "1:1 copy", "make 1:1 duplicate" → full token extraction + HTML that mirrors the live markup pattern, not just the look.
   - "find more beautiful website like this" → propose 4-8 candidates from Godly / Awwwards / Muzli, do collision-check, present the list, then process.
2. **Pre-screen candidate sites** before cloning. Quick `curl` the home page; if the file is under 50KB it's likely a static-ish site (good), over 500KB is a heavy SPA (CSS may be in the JS bundle — see pitfall 2).
3. **Per site, fetch the source HTML + the linked CSS bundle** (the linked file is usually the one labelled `*.css` near the top of the HTML; ignore Tailwind preflight noise — search for the design tokens inside it).
4. **Extract the real design tokens** in this order, writing the answers to a scratch dict:
   - Background color (often the `<meta name="theme-color">` value is the design intent)
   - Foreground / text colors and metadata colors
   - One accent color (or "no accent — foreground is the only color")
   - Font stack (display serif, body sans, monospace)
   - Light / dark strategy
   - Border-radius family (0 / 0.375rem / 0.5rem / 0.875rem)
   - Content width
5. **Collision-check against existing skills** before writing — walk `/root/.hermes/skills/*/SKILL.md` recursively and read each parent-dir name. If the candidate skill name already exists, pick a different name (e.g. suffix with `-extract` or `-alt`).
6. **Write four files per site**, in this order, each scoped under 8K tokens so a single tool call completes:
   1. `<name>.css` — full design system, `html[data-theme="<name>"]` selector on every rule. Lead with `:root` token block; body + h1 + a + p + code at the top; component patterns (`.btn`, `.card`, `.hero`, `.grid`) after.
   2. `<name>.html` — working demo with realistic content. Reuse the same section names the source uses ("Featured", "Writing", "Experience"); pull real project names + tool lists from the source HTML if present.
   3. `<name>.md` — design notes. The first sentence answers "what's distinctive" (not "what is this"). The "Reuse pattern" section is the most important — it tells future sessions when to reach for this theme.
   4. `<name>-prompt.md` — a short regeneration prompt (~10-30 lines) the user can paste into Claude to re-derive the theme from a fresh source.
7. **Register in `theme.js`** — append to the `THEMES` map. Match the existing key naming convention (camelCase, no hyphens for the key).
8. **Append to `README.md`** — new `### <N>. <name>` section in numeric order + add the theme id to the bottom bullet list.
9. **Clean `/tmp/learn-*` and `/tmp/<site>scan/`** directories. /tmp persists between sessions; do not leave 50MB+ of CSS dumps lying around.
10. **Final report** — table with: skill name | source URL | description (one line) | notable pitfalls hit. Be honest about which sites you got at full-fidelity (real extracted tokens) vs. synthesis.

## Pitfalls

- **Long file writes fail.** `write_file` and large `patch` calls can stream-timeout if the content is much over 8K tokens. Split the content into 2-3 smaller files (CSS rule blocks split at logical sections) and write each separately. Use `patch` with a small `old_string` rather than rewriting whole files.
- **CSS-in-JS sites have no `:root` block.** Linear, Mercury, many Notion-style sites put all design tokens in the JS bundle or in inline `<style>` blocks. Detect this: if the CSS file is under 5KB and the home page is over 200KB, the design is in JS. Switch to extracting from inline `style="..."` attributes and the bundled `.js`.
- **GitHub-Pages 404s return 200.** The page exists, but it's the GitHub "site not found" page. Check for the literal string `Site not found` in the HTML; if present, skip the site and report, don't try to extract from the 404 page.
- **Color schemes vary by source.** `prefers-color-scheme: dark` is most common. Marcbouchenoire uses a class-based `.dark` on `<html>`. Mercury has no light mode. Don't add a light mode the source doesn't have.
- **Class-based dark mode needs a JS toggle to actually work.** A static demo with `html.dark` won't switch by itself — either ship a small inline toggle in the HTML, or document that the theme is "dark by default, opt-in to light by removing `dark` class."
- **Don't write summaries.** The `.md` notes file should answer "what makes this theme distinctive and when should I use it", not "this theme is a developer portfolio with X colors." Future sessions need the distinctive-different-from-the-other-40-themes answer.
- **Skills with the same name in different bundles collide.** A skill called `cortex` in the Forgecat bundle and one in the ECC bundle are both `cortex` from the registration system's view. Pick a name that's unique across all of `/root/.hermes/skills/`. If unsure, prefix with the source name.
- **The registry update is two coupled writes.** `theme.js` and `README.md` must be updated in the same turn — never just one. A theme that's in the folder but not in the registry is invisible. A theme that's in the registry but not the folder is a 404.
- **When extracting from a Tailwind-driven site, the design is in `tailwind.config.js`, not the CSS file.** If the CSS is mostly preflight + utility classes, the actual design tokens are in the build config — fetch the JS bundle and grep for the token names.
- **The system message about 8K-token tool calls is a hard limit, not a hint.** Plan content splits before writing. The split points should be logical (rule blocks, not arbitrary mid-line).

## References

- `references/inspect-live-css.md` — exact steps for `curl`ing, the 4 tools to use in sequence, how to handle Tailwind preflight noise, what to extract from inline styles when CSS-in-JS hides the design, and a worked example.
- `references/registrar-update.md` — exact `theme.js` insertion pattern (key naming, where to insert) and `README.md` section shape, so the registry never gets out of sync.
