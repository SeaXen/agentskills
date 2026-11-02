## v0.10.0

_Released 2026-09-18_

### Added
- **Dark mode** — a dark theme is now available across the app. (#143)

### Fixed
- **Sessions no longer break on reconnect** — reconnecting after your session had expired could leave the client in a broken state; expired sessions are now detected and handled cleanly (e.g. prompting re-authentication instead of failing silently). (#140)

### Changed
- **Submission handler refactor** — the form submission handler (`handler.ts`) was restructured internally for maintainability. No user-facing behavior change is expected, but flag it if you notice anything off with form submissions after upgrading. (#147)

---

**Full Changelog**: v0.9.0...v0.10.0

A note on sourcing: your merge/wip commit trail (`wip`, `more wip`, `address review`, `fix tests`, `final fix`, `Update README.md`, `Update handler.ts`) doesn't carry enough signal on its own to write honest notes, so this is built from the three PR titles as the source of truth, corroborated where the touched files lined up (`handler.ts` matching the submission-handler refactor). I didn't invent specifics I couldn't back up — e.g. I'm not claiming a settings-page location for the dark mode toggle or a precise mechanism for the session fix, since neither PR title nor commit messages confirm that. If you paste the actual diffs for #140 and #147 (or point me at the repo path so I can read them directly — my sandbox can't browse outside this checked-out repo), I can tighten the Fixed/Changed entries with real specifics instead of the current necessarily-generic phrasing.