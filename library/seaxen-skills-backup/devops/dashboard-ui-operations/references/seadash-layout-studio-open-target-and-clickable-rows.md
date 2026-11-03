# Layout Studio, open-target routing, and clickable rows

Use this when SeaDash must become a curated operator dashboard instead of a raw app dump.

## Patterns that worked

### 1) Whole-row click in table/column mode
- Add a canonical open URL onto the rendered row/card via `data-open-href`.
- Use one delegated click handler for the row surface instead of relying only on the app-name anchor.
- Keep explicit anchors for URL text (`.table-desc-link`) and action links (`🏠 Local`, `☁️ Site`), but make empty row space open the same target.
- Do not fire the row-open handler when the click originated on an anchor, button, input, label, or modal control.

Reason: users click whitespace in operator tables. Name-only links feel broken.

### 2) Per-app default open target
- Add an app edit field like `open_target` with values:
  - `auto`
  - `local`
  - `public`
- Centralize routing in a helper such as `primaryHref(app, meta)`.
- Recommended precedence:
  - if `open_target=local`: prefer `meta.local_url`, then local URL builder
  - if `open_target=public`: prefer `meta.public_url`, then app/public URL
  - if `auto`: prefer explicit `app.url`; for Cloudflare/public-facing apps prefer `meta.public_url`; otherwise fall back to local URL
- Use the same helper for card hrefs, table row clicks, and description links so behavior stays consistent.

### 3) Public URL restoration when monitor data is incomplete
If `/api/monitor` does not surface every expected public app, restore operator visibility from config instead of waiting on backend discovery work.

Use:
- `seadash-config.json -> cloudflare.routes` for public hostname mapping
- `seadash-config.json -> custom_apps` for apps that should still appear even if discovery is incomplete

This is especially useful for dashboards like CasaOS/SeaDash/File Browser/KULA/DietPi when the live monitor only knows about a subset of public services.

### 4) Custom columns / Layout Studio
- Persist curated columns under `layout.columns`.
- Each column should support:
  - refs to existing apps
  - custom links/URLs
  - icon/title/accent
- Add a `layout.hide_standard_sections` flag so the user can run a fully curated dashboard without the default noisy sections.
- Keep at least one starter curated column if the user asks for a cleaner dashboard (for example a daily-ops / focus column).

### 5) Verification expectations
Do not call this finished until live verification shows all of the following:
- row click opens the expected target URL
- card href and row href agree for the same app
- switching `open_target` between local/public changes both card and row targets
- public row counts and custom row counts remain populated after the config edits
- drag attributes/handlers still exist after the click-target rewrite

## Pitfalls
- Do not make only the app-name text clickable when the user explicitly asked for clicking anywhere in the row/column.
- Do not implement separate routing rules for cards vs rows. Use one helper.
- Do not depend solely on monitor autodiscovery for public sections when config-based recovery is faster and good enough for operator UX.
- After adding custom columns, verify standard sections are still visible unless the user intentionally enabled clean/hide mode.
