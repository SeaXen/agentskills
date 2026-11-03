---
name: linux-desktop-app-bundles
description: Install or update vendor-distributed Linux desktop apps from tarballs or direct downloads, wire desktop entries/icons, and handle root-run Electron wrappers safely.
---

# Linux desktop app bundles

## When to use
- User asks to install, update, or verify a Linux desktop app that is distributed as a tarball/AppImage/standalone bundle rather than a native distro package.
- Vendor docs provide direct download links instead of a maintained apt/dnf package.
- Existing distro package is older than the vendor download and the user wants the vendor version.
- Electron/Chromium desktop app must run on a machine where the agent operates as root.

## When not to use
- A maintained distro package exists and the user explicitly wants the distro-managed path.
- The task is specifically about Flatpak/Snap/AppImage lifecycle management; use a more specific skill if one exists.

## Goal
Install or update the app in a reversible, versioned layout under `/opt`, expose stable launchers in `/usr/local/bin`, and make the desktop environment see the app via `.desktop` entries and icons.

## Standard layout
Use a versioned layout so rollback is trivial:

1. App payload: `/opt/<app>/versions/<version>/...`
2. Stable symlink: `/opt/<app>/current -> /opt/<app>/versions/<version>`
3. Launch wrapper: `/usr/local/bin/<command>`
4. Desktop entries: `/usr/local/share/applications/*.desktop`
5. Icons: `/usr/local/share/icons/hicolor/<size>/apps/<icon>.png`

Why this layout:
- Keeps vendor payload untouched.
- Makes upgrades atomic via symlink swap.
- Lets `/usr/local/bin` override older distro binaries in `/usr/bin` without deleting packages first.

## Procedure

### 1. Discover the current state
Check:
- current installed command path via `command -v`
- vendor version/candidate version from docs or metadata
- whether a distro package already exists and could conflict with wrappers or desktop entries
- desktop files already present in `/usr/share/applications` and `/usr/local/share/applications`

Important:
- Do not assume `--version` is safe on Electron apps when running as root. Many fail without `--no-sandbox`.

### 2. Inspect the vendor artifact before installing
Before writing into system paths:
- download to a temp directory
- inspect archive top-level with `tar -tzf`
- identify the real executable name
- inspect embedded metadata files (`package.json`, `product.json`, build manifests) when available
- locate icon assets and any shipped desktop files

Preferred version source order:
1. vendor release/download page
2. embedded product metadata (`product.json`, `package.json`)
3. executable `--version` output

### 3. Install into `/opt` using versioned directories
- create `/opt/<app>/versions/<version>/`
- copy or extract the payload there
- update `/opt/<app>/current` symlink
- avoid mutating the vendor directory structure more than necessary

### 4. Create a stable launcher wrapper
For wrappers in `/usr/local/bin`:
- point to `/opt/<app>/current/.../binary`
- preserve quoted paths if the app dir contains spaces
- use `exec` so process trees are clean

For Electron/Chromium apps when running as root:
- detect `id -u = 0`
- append `--no-sandbox`
- use a separate `--user-data-dir` for the root profile

Reason:
Electron/Chromium commonly aborts as root without `--no-sandbox`, even for `--version`.

Wrapper pattern:
```sh
#!/bin/sh
set -eu
APPDIR=/opt/<app>/current/<payload-dir>
BIN="$APPDIR/<binary>"
if [ "$(id -u)" -eq 0 ]; then
  exec "$BIN" --no-sandbox --user-data-dir="${HOME:-/root}/.config/<RootProfileDir>" "$@"
else
  exec "$BIN" "$@"
fi
```

### 5. Create or replace desktop integration
Provide `.desktop` files in `/usr/local/share/applications` with:
- `Type=Application`
- `Name=`
- `Exec=` using the stable wrapper in `/usr/local/bin`
- `Terminal=false`
- `Categories=`
- `Icon=` if available
- `MimeType=` for custom URL handlers if the app needs them
- `StartupWMClass=` if the window manager otherwise groups badly

Notes:
- Prefer `/usr/local/share/applications` over editing vendor or distro desktop files.
- If the vendor app has separate main app and URL-handler entries, create both.
- If the icon is embedded inside the archive, install it to the hicolor tree under `/usr/local/share/icons/...`.

### 6. Refresh desktop caches
Run if present:
- `update-desktop-database /usr/local/share/applications`
- `gtk-update-icon-cache /usr/local/share/icons/hicolor`

Ignore absence of those helpers; some minimal systems do not have them.

### 7. Verify
Minimum verification:
- `command -v <app>` resolves to `/usr/local/bin/<app>`
- wrapper passes shell syntax check (`sh -n`)
- `/opt/<app>/current` points to the intended version directory
- installed desktop entries contain the expected `Exec=` target
- embedded metadata in the installed payload matches the target version

If you must test-launch an Electron app as root:
- do it through the wrapper
- expect GPU/X11 noise on headless systems
- treat install verification separately from GUI-launch verification

## Pitfalls
- **Root + Electron:** running vendor binaries directly as root often crashes unless `--no-sandbox` is added.
- **Spaces in app paths:** quote paths aggressively; some vendor archives use names like `Antigravity IDE/`.
- **Older distro package still installed:** this is not fatal if `/usr/local/bin` wins, but it can leave duplicate menu entries. Tell the user.
- **Do not trust `--version` alone:** some Electron apps launch background processes or require GUI state. Prefer metadata files when present.
- **Do not overwrite `/usr/bin` or vendor package files:** use `/usr/local/bin` and `/usr/local/share/applications` as the override layer.
- **Headless verification is limited:** missing `$DISPLAY` or GPU warnings do not prove install failure.

## Communication pattern
Keep the handoff tight:
- what version was installed
- whether an IDE/helper app was added
- what paths were changed
- whether an older package still remains underneath
- any next cleanup step worth offering

## Support files
- `references/antigravity-google.md` — concrete example: Google Antigravity bundle install/update, version sources, wrapper quirks, and desktop-entry pattern.

## Reusable checklist
1. Discover existing commands/packages/desktop files.
2. Read vendor download page and capture target version.
3. Download to temp and inspect archive structure.
4. Extract/copy into `/opt/<app>/versions/<version>`.
5. Update `/opt/<app>/current` symlink.
6. Install `/usr/local/bin` wrapper.
7. Install `.desktop` file(s) and icon(s).
8. Refresh caches if available.
9. Verify wrapper path, symlink target, desktop `Exec=`, and metadata version.
10. Tell the user if distro package duplicates remain.
