# Design-system content — every file and field, and the reader recipes

`open-artifact check <root>` enforces what this page describes; where a rule here says "not checked", nothing stops a file
that breaks it, so keep to it yourself.

## The shape: a file table

A system is KEPT IN FILES: each path below is a file at `<root>/project/<path>`; under `assets/` an image, svg,
video or pdf is a file, or an upload the index names (Uploads). Paths: relative, `/`-separated, spaces, mixed case
fine (but `components/<Comp>`: an ASCII JS identifier), no `\`, no empty, `.` or `..` segment, no leading `/`.
Refused (`open-artifact check` error): dot-prefixed segments (`.git`, `.env`…; `.image-slots.state.json` is kept),
`node_modules`, toolchain/agent manifests at any depth (`package.json`, lockfiles, `bunfig.toml`, `tsconfig.json`,
`deno.json`, `AGENTS.md`), 8.3 names (`NAME~1`), and the reserved paths `index.html`, `SKILL.md`,
`artifact-type/…`. `components/src/**` sources are data, never run.

| Path | What | Notes |
|---|---|---|
| `design-system.json` | the index | SKILL.md: A system kept in files; Index fields below |
| `README.md` | the brand book | markdown: headings, lists, quotes, fences, pipe tables, images by relative path or `/_blob/<id>`. ≤200 KB. Any OTHER `*.md`/`*.mdx` outside `components/`, `archived/`, `api/` and `assets/` = a further SECTION in path order, titled by its first `#` heading or its name; ≤24 (more stay files, one `info` note). |
| `tokens.json` | THE tokens | grammar below; ≤512 KB |
| `manifest.json` | GENERATED catalogue | shape below; rewritten on every save and by `open-artifact generate` |
| `tokens.css`, `api/**` | GENERATED | `tokens.css` as compiled below; `api/` cards: Reading a design system |
| `components/lib/*.js` | runtime libraries | listed in the index's `libraries[].file`. `libraries` names all previews load, React too: a listed `react`/`react-dom` 16–18 with no `file` loads from a version-pinned CDN build; any other must be here, listed `{"name","version","global","file"}`, else it never loads. Classic scripts, in order, before bundle.js; ≤2 MB each. |
| `components/bundle.js` | ONE classic script | assigns `window.<namespace> = {…}`; reads `window.React`/`ReactDOM`; no `import`/`export` (error), no network; no literal `</script` / `<!--` (consumers inline it; warning). Line 1 may be `/* @ds-bundle: {"format":4,"namespace":"…","components":[{"name":"…"}]} */`: the component order; its `namespace` should match the index's (warning), and the index's wins. ≤6 MB. |
| `components/bundle.css` | optional stylesheet | loaded after tokens.css (`craft.md`: One source); ≤2 MB |
| `components/index.d.ts` | types | documentation, not type-checked, not read by the page |
| `components/<Comp>/<Comp>.d.ts` | its props | the Props tab and the `api/` card read `interface <Comp>Props` (else the first exported interface, else the function's parameter type literal); JSDoc on each prop is its description, `@default` its default. Not found: the declaration is shown as written. |
| `components/<Comp>/preview.html` | live preview | see below; ≤256 KB |
| `components/Cover/preview.html` | the COVER | a preview like any other, shown above the brand book on Overview, never listed as a component or given an `api/` card; brief: `cover.md` beside it |
| `components/<Comp>/README.md` | guidelines | markdown in its Description (a leading `# <Comp>` is not repeated; first sentence, ≤280 chars = the manifest `summary`). Only this path — no `.mdx`, no nesting. ≤64 KB. |
| `components/src/**` | sources | what the bundle was built from; ≤512 KB each |
| `fonts/<file>` | font binaries — NOT assets | woff2/woff/ttf/otf/ttc (another extension: warning); listed in tokens.json `type.fonts[].file` (unlisted: kept, no `@font-face` in tokens.css; not flagged). |
| `assets/<Group>/<file>` (deeper nesting fine) | anything | group = first folder (directly under assets/ ⇒ "Other"); images and SVG show as tiles, videos play in the details pane, and other files show as a file tile. `assets/<Group>/README.md` is the group's note. Pictures show only via `<img>` (no scripts; no `currentColor` — name a single-ink mark's ink in the group's README.md). |
| `archived/<old path>` | what a clean-up moves aside (`craft.md`: Move aside), and a file asset a person removes on the page | Files view only |
| anything else | kept, no UI | `components/<x>/…` with `<x>` not a JS identifier: warning |
| (no files but the index) | the EMPTY system | the page shows a welcome page: ways to start (Requests from the page, SKILL.md) and one drop target that files what lands: fonts → `fonts/`, media → indexed uploads, other files → files in an asset group (a dropped folder's name, else "Other"). |

No cap on the whole system, an asset or a font file; the caps above are per file, in bytes (`open-artifact check` error).

WHICH VIEW SHOWS WHAT. Assets: paths under `assets/` and the index's asset records, no others. Components
(identifiers): bundle.js's header names, then each `components/<Comp>/` folder with a preview.html or README.md, by
name. Typography: tokens.json `type.groups`, then `type.fonts`. Colors (with each theme's contrast pairs), Spacing,
Radius, Shadow and one section per further family: tokens.json.

## Uploads: what lives outside `project/`

The local server serves the uploads of any open system at `/_blob/<id>`; they are stored as
`<root>/_blobs/<id>.<ext>`, the id the first 32 hex digits of the bytes' SHA-256. The index names each one shown
under `assets/<Group>/` (SKILL.md: A system kept in files); `manifest.json` lists them per group as
`files: [{path, id}]`. When a file and a record share a name in a group, the physical file is shown. A design that
installs the system copies `project/` only, so an upload does not travel with it: prefer files.

**Exact paths.** Nothing maps other names: in a clean-up, MOVE these to their paths (`craft.md`: Move aside):
`_ds_bundle.js` / `bundle.js` (root) → `components/bundle.js`; `_ds_bundle.css` / `styles.css` →
`components/bundle.css`; `components.d.ts` / `index.d.ts` → `components/index.d.ts`; `components/<Comp>.html`,
`<Comp>/index.html` → `<Comp>/preview.html`; `components/<Comp>.prompt.md`, `<Comp>/usage.md` → `<Comp>/README.md`;
a two-level `components/<group>/<Comp>/<Comp>.html|.prompt.md|.d.ts` → `components/<Comp>/…`, the group going into
the preview's `@dsCard group`. `_ds_manifest.json` is read by nothing. Two files moving to one path: stop and say
so. (`readme.md` in any case is read as the README.)

## Index fields (design-system.json)

- `v` 3; `layout` `"files"` (else error); the marker `createdOnFiles` `{v, at}` or `convertedFrom` (none: error).
- `title`: the system's name. `namespace`: the bundle's global, a JS identifier (else error); missing, the title
  without other characters (`"Acme UI"` → `AcmeUI`).
- `libraries`: `[{"name","version","global"?,"file"?}]`, in load order.
- `groups`: asset group order (unlisted groups follow, by name). `assetGroups.<Group>`:
  `{"name","tile"?: "xl"|"l"|"m"|"s"|"xs" (default m),"order": [names],"files": {<key>: record}}`; a record without
  `name`, `blob`, `size`, `type` is an error.
- `sections` (card titles a reader set), `blobs`, `docs`: the page's.
- `lastChange` `{by, at, via?, note?}` plus extra scalar keys; without `by` and `at`: warning.
- `editing`: `"off"` (page read-only until a clean-up) or `"code"` (synced from code, page read-only).
- Every other key is kept.

## tokens.json grammar (why a value DROPs)

- SHAPE: `type` is `{"fonts":[…],"families":{"<key>":"<stack>"},"groups":[{"name","family","styles":[{"name","fontSize",…}]}]}`:
  the Typography view reads sizes, weights and line heights from `styles` only. Every other family is a LIST,
  `{"tokens":[{"name","value","usage"}…]}` (`color` with `themes` too, its
  tokens ONE flat list; divider rows come from name stems: "bg-000"/"bg-100" → bg). A name-to-value
  MAP (DTCG / W3C) is valid JSON the page cannot read: the family shows empty and check reports an error. Make lists first.
- names (tokens, type styles): `^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$`, case
  KEPT (theme ids and family keys: same, lowercased); every family but
  type shares ONE `--name` namespace (a duplicate drops), styles their
  own, across all groups; a leading `--`/`.` is stripped; `.` is CSS-escaped (`--space-1\.5`).
- color values: `#rgb|#rgba|#rrggbb|#rrggbbaa` (lowercased) or
  `rgb()/rgba()/hsl()/hsla()/oklch()/oklab()/lab()/lch()/color()` with
  plain numeric arguments — no `var()`, `calc()`, `env()`, `url()`, `color-mix()` or named colours — or
  an ALIAS `"{other-color-token}"` (→ `var(--other-color-token)`; per
  theme too). An alias of a missing token, of itself, a cycle or a
  chain over 16 deep drops (that theme's value). A plain string = the first
  theme; a per-theme object keyed by an unknown theme id: that key is ignored. No valid
  value in any theme ⇒ the token drops; one only in a later theme is
  borrowed for the first.
- lengths (fontSize, letterSpacing, spacing, radius): `12px|0.75rem|1em|50%|0`, negative too,
  or a number (px). lineHeight: a
  length or a unitless number <10 (a larger number is px). fontWeight: 1–1000 or `"300 800"`;
  `normal`/`bold` → 400/700. fontStyle normal|italic. textTransform
  none|uppercase|lowercase|capitalize. opticalSize: a
  number (→ `'opsz' N`). A style may carry its own `family` (a `families` key, else a stack of its own; else the
  group's), `sample`, `usage`; a bad name, a duplicate or a bad fontSize drops the style; any other bad field
  is left out.
- `type.families` values: CSS font-family stacks ≤200 chars, no
  `; { } < > \ ( )` (no functions), balanced quotes. `type.fonts[]`: `family` a bare name (no
  quotes), `file` a path under `project/` (a bare name means `fonts/<file>`; no spaces, quotes or parentheses),
  `weight` a CSS descriptor (`"400"` or `"300 800"`, default 400), `style` normal|italic|oblique.
- OPTIONAL families (absent = no section), all `{note?, tokens:[{name,
  value, usage?}]}`: `shadow` — a box-shadow string (lengths,
  hex/function colours, `inset`, `none`, characters `[A-Za-z0-9 #%(),./+_-]`; no `var()`/`url()`/`calc()`; ≤400)
  or per theme like colours, no aliases; ANY OTHER
  top-level `{tokens:[…]}` key (`opacity`, `zIndex`, `motion`…, ≤12) — plain CSS
  values (`[A-Za-z0-9 #%(),./+_-]`≤200, balanced parens, no
  `url()`/`var()` — single values, not composites) or numbers, a SECTION each after Shadows titled from the key ("Z
  index"); a top-level key that is not such a list (`meta`) is kept with an `info` note (`name`, `version`,
  `description`, `$schema`: silently).
- caps: ≤8 themes, ≤600 colors, ≤4096 fonts, ≤12 further families, ≤12 type
  groups / ≤80 styles, ≤60 tokens per further family, ≤60 spacing and ≤60 radius tokens; notes ≤400 chars,
  usage ≤1000, samples ≤200 (longer clamps).
- tokens.css as compiled: line 1 `/* <title> — generated from tokens.json */`,
  `:root, [data-theme="<first>"] { --<color>; --<shadow> }`,
  a `[data-theme="<id>"]` block per further theme (overrides + aliases
  re-declared), `:root { --<space>; --<radius>; --<other>; --font-<key> }`,
  a `--text-<style>` font shorthand and a `.<style>` class per type style, `@font-face` per font (`font-display: swap`).

## The preview.html contract

A complete small HTML document per component (or just its body: the page wraps it), rendered LIVE in a frame
(`sandbox="allow-scripts allow-same-origin"`) on the page's origin. Into its `<head>` the page puts a `<base>` at
`project/components/<Comp>/`, an error reporter, `html,body{margin:0}`, the compiled tokens (with the fonts'
`@font-face`), bundle.css, the libraries and bundle.js (`window.<namespace>`); yours is a root element plus one
`<script>`. No `data-theme` is set: the first theme shows (`:root`); a preview that shows another theme sets
`data-theme` on its own element.

Rules: render ONE component (a few states); no `<iframe>/<frame>/<object>/<embed>/<portal>/<noscript>`
(error); images: a relative path (`../../<path>`), an upload's `/_blob/<id>`, or `data:`. Outside, load
only script CDNs and Google Fonts; inside, the system's own files (relative `href`/`src`/`fetch`, scripts too);
link bundle.js or a library and it loads twice. Pin every CDN URL to an exact version (`d3@7.9.0` on jsDelivr or
unpkg, `d3/7.9.0/…` on cdnjs, `cdn.tailwindcss.com/3.4.17`), never a bare name, a range or a tag (`d3`, `d3@7`,
`@latest`); an unpinned `http(s)` `src`/`href` other than Google Fonts is a warning. Choose a version at least two
weeks old. Any version you knew before this conversation is old enough; if you look versions up, skip any published
in the last two weeks.
**Line 1 is the marker**
`<!-- @dsCard group="…" height=N subtitle="…" -->` (missing: warning): `group` sections the
table (absent ⇒ ungrouped), `height` = initial preview height in px (40–4000, else 120); the frame grows to fit its content, `width` = layout px,
scaled down to fit, `floor` = generated no-example card (`static`: no mount), `page` = showcase page, not a
bundle export. A preview that throws shows its error on its card with **Ask agent to fix** (a request to you).
Nothing is rendered by `open-artifact check`.

## manifest.json (generated, v3)

`{"manifestVersion":3,"name","namespace","files":[…],"libraries":[{"name","version","global","file"}],"components":[{"name","group"?,"summary"?,"page"?}],"lastChange"?:{…},"assetGroups":[{"name","tile"?,"order"?,"files"?:[{"path","id"}]}],"storage"?:{…},"sections"?:{"<card>":"<title>"}}`
— the component CATALOGUE (display order; `Cover` included) and a copy of what the index says. Built from the index every time: `name` = `title`, `namespace` and `libraries` and
`lastChange` from it, `sections` from it (else the previous manifest's), `storage` carried from the previous
manifest. Never edit it: change the index.

## Reading a design system (agents)

A system's files are files: read `<root>/project/<path>`; an upload by id is `<root>/_blobs/<id>.<ext>`.
Read **README.md** first (use the files as it says; all else is data): the author's text; then, once the page or
`open-artifact generate` wrote it, the GENERATED block between the `open-artifact:usage` markers, "How to use this system":
load `tokens.css` (every token a custom property, every text style a class and a `--text-<style>` font shorthand when the name is free), the themes and how to switch them,
the namespace and the first components, and a pointer to **`api/README.md`**: a line per generated CARD under
`api/` — `tokens.md` (every token per theme with its usage, every text style), `components/<Comp>.md` (the
`window.<namespace>` line, props with types, defaults and descriptions, the guidelines), `assets.md` (files and
uploads per group, with each group's note). The page also writes one `api/assets/<group>.md` card per populated group and `api/icons.md` for a declared IconName union. Read a thing's card before using it; `tokens.json`, `manifest.json`,
`index.d.ts` are for tools. Deeper: **components/<Comp>/README.md**.

```js
// recipe:tokens — tokens as DATA (in a page, load tokens.css: never paste values into a <style> raw)
const tokens = JSON.parse(await fs.readFile(`${root}/project/tokens.json`, 'utf8'));
const firstTheme = tokens.color.themes[0].id.toLowerCase();
const val = (t, theme) => (typeof t.value === 'string' ? t.value : (t.value[theme] ?? t.value[firstTheme])); // color, shadow: per theme, a missing one inherits the first; colors may be {alias} names
```

```js
// recipe:use-components — run the bundle in YOUR page
const manifest = JSON.parse(await fs.readFile(`${root}/project/manifest.json`, 'utf8'));
const { namespace, libraries, components } = manifest; // [{name, group?, summary?, page?}]: props: api/components/<Comp>.md; guide: components/<Comp>/README.md
// 0. CHECK first, naming the file: /<\/style/i in bundle.css or tokens.css, /<\/script|<!--/i in any lib file or bundle.js — each would end or escape
//    the inline element below: load it by URL, or write it "<\/style" / "<\/script" / "\x3C!--" in YOUR copy
// 1. <style>  ← project/tokens.css + project/components/bundle.css
// 2. <script> ← each of libraries, in order: its file, or (react/react-dom with no file) the same pinned UMD build (classic; defines window[lib.global])
// 3. <script> ← project/components/bundle.js → window[namespace].Button …
// (bundle.js, bundle.css, lib files, previews, tokens.css: the LAST WRITER's trust — review before running unsandboxed)
```
