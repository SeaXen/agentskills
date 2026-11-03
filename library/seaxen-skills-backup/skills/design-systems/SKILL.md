---
name: design-systems
description: "Design one-off HTML artifacts (claude-design), author DESIGN.md token specs (design-md), or apply 54 real-world design systems (popular-web-designs) — unified visual design workflow."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [design, html, prototype, ux, ui, design-system, tokens, design-md, tailwind, dtcg, claude-design]
    related_skills: [creative-diagrams, excalidraw, architecture-diagram, generative-art]
---

# Design Systems — Unified Visual Design Workflow

Three complementary design approaches in one skill:

| Skill | Purpose | Output | Use When |
|-------|---------|--------|----------|
| **claude-design** | Design *process & taste* — scoping, variants, verification | Local HTML artifact (landing, deck, prototype) | From-scratch designed artifact, no brand dictated |
| **popular-web-designs** | 54 ready-to-paste design systems | Design tokens + component specs (CSS/HTML) | "Make it look like Stripe/Linear/Vercel" |
| **design-md** | Formal DESIGN.md token spec authoring | `DESIGN.md` file (YAML + Markdown) | Design system *spec file* for repo consumption |

**These compose:** Use `popular-web-designs` for visual vocabulary, `claude-design` for process, `design-md` when output is the token file.

---

## Part 1: Claude Design — Process & Taste (absorbed from `claude-design`)

### When To Use
- Landing pages, teaser pages, high-fidelity prototypes
- Interactive product mockups, visual option boards
- Component explorations, design-system previews
- HTML slide decks, motion studies, onboarding flows
- Dashboard concepts, settings, command palettes, modals, cards, forms

**Do NOT use for:** Pure DESIGN.md token authoring → use `design-md` instead.

### Runtime Mode
You run in **CLI/API mode**, not hosted Claude Design web UI. Ignore hosted-only tools (`done()`, `fork_verifier_agent()`, `questions_v2()`, `copy_starter_component()`, `show_to_user()`, `show_html()`, `snip()`, `eval_js_user_view()`, hosted asset panes, edit-mode toolbars, cross-project paths, `window.claude.complete()`).

**Default deliverable:** Complete local HTML file, self-contained CSS/JS, exact on-disk path, verified locally.

### Core Identity
Act as expert designer with user as manager. HTML default, but medium changes by assignment:
- UX designer for flows/product surfaces
- Interaction designer for prototypes
- Visual designer for static explorations
- Motion designer for animated artifacts
- Deck designer for presentations
- Design-systems designer for tokens/components/rules
- Frontend-minded prototyper when code fidelity matters

### Design Principle: Start From Context, Not Vibes
Before designing, look for source context:
1. Brand docs
2. Existing product screenshots
3. Current repo components (theme files, tokens, global stylesheets, layout scaffolds, component files)
4. Design tokens
5. UI kits
6. Prior mockups
7. Reference models
8. Copy docs
9. Legal/product/engineering constraints

If repo available, **inspect actual source files before inventing UI**.

### Asking Questions
Ask when assignment is new, ambiguous, high-fidelity, externally facing, or taste-dependent. Keep questions short. Usually ask for:
- Output format, audience, fidelity level, source materials
- Brand/design system in play
- Number of variations wanted
- Conservative vs. divergent exploration
- Primary dimension: layout, visual language, interaction, copy, motion, systemization

### Workflow
1. **Understand brief** — What, who, artifact, locked constraints
2. **Gather context** — Read docs, screenshots, repo files, design assets
3. **Define design system** — colors, type, spacing, radii, shadows, motion, components, interactions
4. **Choose format** — Static comparison (side-by-side HTML), Interaction (clickable prototype), Presentation (fixed-size deck), Component lab, Motion (timeline/state-based)
5. **Build artifact** — Single self-contained HTML, preserve prior versions, avoid unnecessary deps
6. **Verify** — File exists, syntax checks, browser console errors, screenshot inspection at primary viewport
7. **Report briefly** — Path, what created, caveats, next decision

### Artifact Format Rules
- Descriptive filename: `Landing Page.html`, `Command Palette Prototype.html`
- Embed CSS in `<style>`, JS in `<script>`
- Openable directly in browser
- Avoid remote dependencies unless explicitly useful/stable
- Responsive unless intentionally fixed-size
- Significant revisions: preserve `Name.html`, create `Name v2.html`

### HTML/CSS/JS Standards
Modern CSS: variables, grid, container queries, `text-wrap: pretty`, real focus/hover states, `prefers-reduced-motion`, responsive scaling, semantic HTML.
Avoid: huge monolithic files (unless repo structure expected), fragile viewport assumptions, inaccessible hit targets, decorative JS fighting usability, `scrollIntoView` unless no safer option.
Mobile hit targets ≥44px. Print: text ≥12pt. 1920×1080 decks: text ≥24px.

### Deck Rules
Fixed-size canvas, scale to fit viewport. Default: 1920×1080 (16:9).
Requirements: keyboard nav, visible slide count, localStorage persistence, print-friendly, slide labels/IDs. No speaker notes unless asked. 1-2 bg colors max. Sparse slides — solve emptiness with layout/rhythm/scale/imagery, not filler text.

### Prototype Rules
Primary path clickable. Key states: default, hover/focus, loading, empty, error, success. Expose variations with in-page controls. Controls out of final composition unless intentional. localStorage persistence for refresh continuity. Design the FLOW, not just first screen.

### Variation Rules
Default ≥3 options:
1. **Conservative** — closest to existing / lowest risk
2. **Strong-fit** — best interpretation of brief
3. **Divergent** — novel, discovers taste boundaries

Explore: layout, hierarchy, type scale, density, color, surface treatment, motion, interaction, copy, component shape. NOT mere color swaps unless color is the question. Consolidate when user picks direction.

### Tweakable Designs (CLI/API Mode)
No hosted edit-mode toolbar. Add in-page `Tweaks` panel when useful: theme mode, layout variant, density, accent color, type scale, motion on/off, copy variant, component variant. Keep small/unobtrusive. Persist with localStorage.

### Content Discipline
No filler: fake metrics, decorative stats, generic feature grids, unnecessary icons, placeholder testimonials, AI fluff, invented strategy-changing content. Every element earns place. Ask before adding sections/claims. Mark draft/placeholder copy.

### Anti-Slop Rules
Avoid: aggressive gradients, default glassmorphism, emoji (unless brand), generic SaaS cards, left-border accent cards, fake dashboards, stock-photo heroes, oversized rounded rectangles as hierarchy substitute, rainbow palettes, vague labels ("Insights", "Growth"), decorative SVG as product imagery.

Minimal ≠ automatically good. Dense ≠ automatically cluttered. Choose intentionally.

### Typography/Color/Layout/Motion
Use existing type system or choose deliberately:
- Editorial: serif/humanist headline + restrained sans body
- Software/productivity: precise sans + strong numeric treatment
- Luxury/minimal: fewer weights, more spacing discipline
- Technical: mono accents only
- Deck: large, clear, high contrast

Color: Brand/system first. If none: small system (neutrals, surface, ink, muted, border, 1 accent, danger/success). Prefer oklch for invented palettes. Check contrast.

Layout: Design with rhythm (scale, whitespace, density, alignment, repetition, contrast, interruption). Avoid same card grid everywhere. Product UIs → speed of comprehension. Marketing → one idea/section. Dashboards → only data that helps decide/act.

Motion: Discipline, not theater. Good: clarifies state, reduces loading anxiety, shows continuity, gives tactility, stays subtle. Bad: loops without purpose, delays user, calls attention to itself, hides hierarchy. Respect `prefers-reduced-motion`.

### Images/Icons
Real supplied imagery first. Missing: clean placeholder, typography/layout/abstract texture, ask for real material. No elaborate fake SVG illustrations unless explicitly illustration work. Icons only if improving scanning or matching design system.

### Source-Code Fidelity
When recreating from repo: inspect tree → identify UI source → read theme/token/global styles/components → lift exact values → match spacing/radii/shadows/copy/density/interaction → THEN design/modify. Don't build from memory when source available.

### Extracting Design Tokens from Live Sites
When the user provides BOTH a design spec document AND a live site URL, **always check the live site first**. Spec docs are often outdated or aspirational; the live site is ground truth.

Use `browser_console` with `getComputedStyle()` to extract real values:

```javascript
// Extract body/typography
const cs = getComputedStyle(document.body);
const root = getComputedStyle(document.documentElement);
JSON.stringify({
  body: { bg: cs.backgroundColor, color: cs.color, font: cs.fontFamily, size: cs.fontSize },
  h1: document.querySelector('h1') ? getComputedStyle(document.querySelector('h1')).fontSize : null,
  // Extract CSS variables
  vars: {
    primary: root.getPropertyValue('--primary').trim(),
    accent: root.getPropertyValue('--accent').trim(),
    // Try common variable names
  },
  // Sample unique background colors from all elements
  linkColors: [...new Set([...document.querySelectorAll('a')].map(l => getComputedStyle(l).color))].slice(0, 5),
});
```

For background/surface colors across the page:
```javascript
const bgs = new Set();
for (const el of document.querySelectorAll('*')) {
  const bg = getComputedStyle(el).backgroundColor;
  if (bg !== 'rgba(0, 0, 0, 0)') bgs.add(bg);
}
// Convert oklab values to hex if needed — oklab() is not directly usable in CSS variables
```

**Pitfall:** `oklab()` computed values may appear in modern browsers. Convert to hex/rgb before using in theme variables. Browser console `getComputedStyle` returns computed values in the browser's native format (often oklab for Chrome 111+).

**Why this matters:** In a real session, the DESIGN.md described Tinybird as `#1A1A2E` (indigo) background with `#27C486` green, but the live site used `#0a0a0a` (near-black) with `#27f795` (neon green). The spec was wrong. Always verify.

**When user provides a reference HTML file**, treat it as the AUTHORITATIVE design spec — even more reliable than extracting from a live site (which may have A/B tests, geo-variants, or CDN-served CSS that differs from the reference). Extract tokens from the reference HTML first, then verify against the live site. In the Tinybird case, the user provided `tinybird.html` with exact values: `#000000` bg, `#111113` cards, `#27272A` borders, `#00E67A` green, Inter font, Space Grotesk headings — all different from both the spec doc AND the live site's computed styles.

### Extracting from JS SPAs (no-render, asset-graph approach)

When the live site is a JavaScript SPA, the initial HTML is usually just `<div id="app"></div>` — the visible design is built at runtime by a JS bundle. The `getComputedStyle` approach needs a browser; this approach works with `curl` alone.

**Procedure:**
1. `curl -sL https://example.com/ -o index.html` — fetch the initial HTML. If it contains the visible content, fall back to the `getComputedStyle` approach above. If it's a shell, continue.
2. Find the linked assets in `<head>`: `<link rel="stylesheet" ... href="/assets/*.css">` and `<script type="module" ... src="/assets/*.js">`. Asset filenames are content-hashed — always read them fresh from the current HTML.
3. `curl` each asset. The CSS holds the real design tokens; the JS often holds the visible content as embedded string literals.
4. Extract tokens from the CSS `:root{}` block: `re.findall(r'--([a-z0-9-]+):\s*([^;]+);', css)`. Dedupe while preserving order.
5. Find content in the JS bundle: `re.finditer(r'"([^"\\]{500,5000})"', js)` filtered by content markers. Decode escape sequences (`\n` → newline, `\"` → `"`).
6. Combine: exact tokens from CSS + real content from JS = a faithful duplicate.

**Why this gives more than `getComputedStyle`:** the source CSS contains token NAMES (`--accent`, `--accent-warm`) and the full font cascade (`"Canela", "Ivy Presto", "Bodoni Moda", "Playfair Display", serif`) that the browser flattens. The source CSS also contains the full `@media` set, all unused tokens, and the exact `color-mix()` expressions used for hover — the browser shows the resolved color, not the expression.

**Common pitfalls:** the JS bundle is minified, zero formatting — use regex on the target names, not manual reading. String literals are escaped; decode before comparing. Multiple JS chunks may exist; fetch them all — the content you want may be in `vendor-*.js` or `page-*.js`, not `index-*.js`. Inline SVG icons embedded in the JS as base64 are usually decorative; skip them unless they carry brand identity.

See `references/extracting-tokens-from-live-spas.md` for a worked example (washiul.com) with exact `curl` commands and the regex patterns.

### Verification
Minimum: file exists, HTML saved completely, syntax checked.
Better: browser open, console errors checked, screenshots at primary viewport, key interactions tested, light/dark/variants tested, responsive breakpoints tested.
If limited: say exactly what was/wasn't verified. Never say "done" if file not written.

### Final Response Format
```
Created: /path/to/Prototype.html
Contains: 3 layout variants, Tweaks panel for density/theme, responsive behavior
Verified: file exists, opened cleanly in browser, no console errors
Next: pick strongest direction, I'll tighten copy + motion
```

---

## Part 2: Popular Web Designs — 54 Real Design Systems (absorbed from `popular-web-designs`)

### How to Use
1. Pick design from catalog below
2. Load: `skill_view(name="design-systems", file_path="templates/<site>.md")`
3. Use tokens/component specs when generating HTML
4. Pair with `generative-widgets` skill to serve via cloudflared tunnel

Each template includes **Hermes Implementation Notes** with: CDN font substitute + Google Fonts `<link>`, CSS font-family stacks, reminders to use `write_file` + `browser_vision`.

### HTML Generation Pattern
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title</title>
  <!-- Paste Google Fonts <link> from template's Hermes notes -->
  <link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet">
  <style>
    :root {
      --color-bg: #ffffff;
      --color-text: #171717;
      --color-accent: #533afd;
      /* ... more from template Section 2 */
    }
    body {
      font-family: 'Inter', system-ui, sans-serif;
      color: var(--color-text);
      background: var(--color-bg);
    }
    /* Apply component styles from template Section 4 */
    /* Apply layout from template Section 5 */
    /* Apply shadows from template Section 6 */
  </style>
</head>
<body>
  <!-- Build using component specs from template -->
</body>
</html>
```

### Font Substitution Reference
| Proprietary Font | CDN Substitute | Character |
|------------------|----------------|-----------|
| Geist / Geist Sans | Geist (Google Fonts) | Geometric, compressed tracking |
| sohne-var (Stripe) | Source Sans 3 | Light weight elegance |
| Berkeley Mono | JetBrains Mono | Technical monospace |
| Airbnb Cereal VF | DM Sans | Rounded, friendly geometric |
| Circular (Spotify) | DM Sans | Geometric, warm |
| figmaSans | Inter | Clean humanist |
| Pin Sans (Pinterest) | DM Sans | Friendly, rounded |
| CoinbaseDisplay/Sans | DM Sans | Geometric, trustworthy |
| UberMove | DM Sans | Bold, tight |
| HashiCorp Sans | Inter | Enterprise, neutral |
| waldenburgNormal (Sanity) | Space Grotesk | Geometric, slightly condensed |
| IBM Plex Sans/Mono | IBM Plex Sans/Mono | Available on Google Fonts |
| Rubik (Sentry) | Rubik | Available on Google Fonts |

When substitute used, follow template's weight/size/letter-spacing closely — those carry more visual identity than font face.

### Design Catalog (54 Systems)

**AI & Machine Learning:** `claude.md`, `cohere.md`, `elevenlabs.md`, `minimax.md`, `mistral.ai.md`, `ollama.md`, `opencode.ai.md`, `replicate.md`, `runwayml.md`, `together.ai.md`, `voltagent.md`, `x.ai.md`

**Developer Tools & Platforms:** `cursor.md`, `expo.md`, `linear.app.md`, `lovable.md`, `mintlify.md`, `posthog.md`, `raycast.md`, `resend.md`, `sentry.md`, `supabase.md`, `superhuman.md`, `vercel.md`, `warp.md`, `zapier.md`

**Infrastructure & Cloud:** `clickhouse.md`, `composio.md`, `hashicorp.md`, `mongodb.md`, `sanity.md`, `stripe.md`

**Design & Productivity:** `airtable.md`, `cal.md`, `clay.md`, `figma.md`, `framer.md`, `intercom.md`, `miro.md`, `notion.md`, `pinterest.md`, `webflow.md`

**Fintech & Crypto:** `coinbase.md`, `kraken.md`, `revolut.md`, `wise.md`

**Enterprise & Consumer:** `airbnb.md`, `apple.md`, `bmw.md`, `ibm.md`, `nvidia.md`, `spacex.md`, `spotify.md`, `uber.md`

**Choose by content:**
- Dev tools/dashboards: Linear, Vercel, Supabase, Raycast, Sentry
- Docs/content: Mintlify, Notion, Sanity, MongoDB
- Marketing/landing: Stripe, Framer, Apple, SpaceX
- Dark mode: Linear, Cursor, ElevenLabs, Warp, Superhuman
- Light/clean: Vercel, Stripe, Notion, Cal.com, Replicate
- Playful: PostHog, Figma, Lovable, Zapier, Miro
- Premium/luxury: Apple, BMW, Stripe, Superhuman, Revolut
- Data-dense: Sentry, Kraken, Cohere, ClickHouse
- Monospace/terminal: Ollama, OpenCode, x.ai, VoltAgent

---

## Part 3: DESIGN.md — Formal Token Specs (absorbed from `design-md`)

### When to Use
- User asks for DESIGN.md file, design tokens, or design system spec
- Consistent UI/brand across multiple projects/tools
- Lint, diff, export existing DESIGN.md
- Port style guide to agent-consumable format
- WCAG accessibility validation on color palette

For visual inspiration/layout: `popular-web-designs`. For process/taste on one-off artifact: `claude-design`.

### File Anatomy
```markdown
---
version: alpha
name: Heritage
description: Architectural minimalism meets journalistic gravitas.
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  body-md:
    fontFamily: Public Sans
    fontSize: 1rem
rounded:
  sm: 4px
  md: 8px
  lg: 16px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "#FFFFFF"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.primary}"
---
## Overview
Architectural Minimalism meets Journalistic Gravitas...

## Colors
- **Primary (#1A1C1E):** Deep ink for headlines and core text.
- **Tertiary (#B8422E):** "Boston Clay" — sole driver for interaction.

## Typography
Public Sans for everything except small all-caps labels...

## Components
`button-primary` is the only high-emphasis action on a page...
```

### Token Types
| Type | Format | Example |
|------|--------|---------|
| Color | `#` + hex (sRGB) | `"#1A1C1E"` |
| Dimension | number + unit (`px`, `em`, `rem`) | `48px`, `-0.02em` |
| Token reference | `{path.to.token}` | `{colors.primary}` |
| Typography | object with `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`, `fontFeature`, `fontVariation` | see above |

Component property whitelist: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. Variants are **separate entries** (`button-primary-hover`), not nested.

### Canonical Section Order (MUST appear in this order)
1. Overview (alias: Brand & Style)
2. Colors
3. Typography
4. Layout (alias: Layout & Spacing)
5. Elevation & Depth (alias: Elevation)
6. Shapes
7. Components
8. Do's and Don'ts

Unknown sections preserved, not errored. Unknown token names accepted if type valid. Unknown component properties → warning.

### Workflow: Authoring New DESIGN.md
1. Ask/infer brand tone, accent color, typography direction
2. Write `DESIGN.md` in project root with `write_file`. Always include `name:` and `colors:`.
3. Use token references (`{colors.primary}`) in `components:` — single-source palette.
4. Lint it (see below). Fix broken references/WCAG failures before returning.
5. If user has existing project, also write Tailwind/DTCG exports (`tailwind.theme.json`, `tokens.json`).

### Workflow: Lint / Diff / Export
CLI: `npx -y @google/design.md` (Node, no global install needed).

```bash
# Validate structure + token refs + WCAG contrast
npx -y @google/design.md lint DESIGN.md

# Compare versions, fail on regression (exit 1 = regression)
npx -y @google/design.md diff DESIGN.md DESIGN-v2.md

# Export to Tailwind theme JSON
npx -y @google/design.md export --format tailwind DESIGN.md > tailwind.theme.json

# Export to W3C DTCG JSON
npx -y @google/design.md export --format dtcg DESIGN.md > tokens.json

# Print spec itself (for agent prompt injection)
npx -y @google/design.md spec --rules-only --format json
```

All commands accept `-` for stdin. `lint` returns exit 1 on errors. Use `--format json` for structural parsing.

### Lint Rules
- `broken-ref` (error): `{colors.missing}` points to non-existent token
- `duplicate-section` (error): same `## Heading` appears twice
- `invalid-color`, `invalid-dimension`, `invalid-typography` (error)
- `wcag-contrast` (warning/info): component textColor vs backgroundColor ratio vs WCAG AA (4.5:1) / AAA (7:1)
- `unknown-component-property` (warning): outside whitelist

Call out WCAG findings explicitly when user cares about accessibility.

### Pitfalls
- **Don't nest component variants:** `button-primary.hover` wrong; `button-primary-hover` sibling key right
- **Hex colors must be quoted strings** (YAML chokes on `#`)
- **Negative dimensions need quotes:** `letterSpacing: "-0.02em"`
- **Section order enforced** — reorder user prose to canonical list before saving
- **`version: alpha`** is current spec (Apr 2026), marked alpha — watch for breaking changes
- **Token references resolve by dotted path:** `{colors.primary}` works; `{primary}` does not

### Spec Source
- Repo: https://github.com/google-labs-code/design.md (Apache-2.0)
- CLI: `@google/design.md` on npm
- Generated DESIGN.md license: user's project; spec is Apache-2.0

---

## Decision Table: Which Sub-Skill to Load

| User Request | Load |
|--------------|------|
| "Design a landing page from scratch" | `claude-design` (this skill drives process) |
| "Make it look like Stripe/Linear" | `popular-web-designs` (vocabulary) + `claude-design` (process) |
| "Create a DESIGN.md spec file" | `design-md` |
| "Style a component library" | `design-md` (tokens) + `popular-web-designs` (reference) |
| "Prototype an interaction flow" | `claude-design` (prototype rules) |
| "Build a slide deck" | `claude-design` (deck rules) |