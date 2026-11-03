# Google Antigravity on Linux

Session-derived reference for the `linux-desktop-app-bundles` skill.

## Vendor distribution shape observed
Two separate tracks existed:

1. **apt repo package** for `antigravity`
   - Linux repo page exposed package install instructions.
   - Installed package version found on host: `1.23.2-1776332190`.
   - Candidate version from apt repo matched installed package.

2. **direct-download bundle** from the main download page
   - Antigravity 2.0 Linux x64 tarball version: `2.0.1-6566078776737792`
   - Antigravity IDE Linux x64 tarball version: `2.0.3-6242596486512640`

Implication:
- The vendor's main download page may advertise newer desktop-bundle releases than the apt package channel.
- If the user says "update from the download page", do not assume `apt upgrade` is enough.

## Useful source URLs seen
- Linux repo install page: `https://antigravity.google/download/linux`
- Main download hub: `https://antigravity.google/download`
- Releases page: `https://antigravity.google/releases`

## Artifact shapes
### Antigravity 2.0 tarball
Top-level directory:
- `Antigravity-x64/`

Binary:
- `Antigravity-x64/antigravity`

### Antigravity IDE tarball
Top-level directory:
- `Antigravity IDE/`

Binary:
- `Antigravity IDE/antigravity-ide`

Important:
- IDE archive path contains a space. Wrapper and copy logic must quote paths carefully.

## Version extraction notes
### Antigravity 2.0
Direct `--version` from the binary was not a clean probe as root without sandbox args.
Using the wrapper with `--no-sandbox` caused the app to start and log:
- `Starting app (v2.0.1) ...`

### Antigravity IDE
Reliable metadata source inside archive:
- `resources/app/product.json` → `ideVersion: 2.0.3`
- `resources/app/package.json` → internal package version `1.107.0`

Interpretation:
- Use `product.json` for the human-facing IDE version.
- `package.json` may reflect the upstream codebase version and not the marketed IDE release number.

## Root/Electron launch quirk
Observed behavior:
- running either vendor binary directly as root aborted with Chromium/Electron sandbox fatal errors.

Working fix:
- wrapper detects root and adds:
  - `--no-sandbox`
  - `--user-data-dir=<separate root profile>`

This fix is durable for the class of Electron root-launch problems. Do not store the crash text as a persistent rule; store the wrapper pattern.

## Desktop integration pattern used
Installed under `/usr/local/share/applications`:
- `antigravity.desktop`
- `antigravity-url-handler.desktop`
- `antigravity-ide.desktop`

Installed icon for IDE from bundle asset:
- `resources/app/resources/linux/code.png`
- placed as `/usr/local/share/icons/hicolor/512x512/apps/antigravity-ide.png`

Why `/usr/local/share/applications`:
- avoids editing distro-managed files under `/usr/share/applications`
- cleanly overrides vendor/distro desktop entries

## Existing package coexistence
The older apt package was left installed underneath.
`/usr/local/bin` wrappers overrode `/usr/bin` command resolution.

Operational consequence:
- CLI resolution used the new bundle
- duplicate menu entries may still remain until the old package is removed

Good user-facing note:
- tell the user the old package still exists and offer cleanup, but do not silently purge without request

## Recommended Antigravity-specific install layout
- `/opt/antigravity/versions/2.0.1-6566078776737792/Antigravity-x64`
- `/opt/antigravity/current -> .../2.0.1-6566078776737792`
- `/opt/antigravity-ide/versions/2.0.3-6242596486512640/Antigravity IDE`
- `/opt/antigravity-ide/current -> .../2.0.3-6242596486512640`
- `/usr/local/bin/antigravity`
- `/usr/local/bin/antigravity-ide`

## Verification points that worked well
- `command -v antigravity`
- `command -v antigravity-ide`
- shell syntax check of wrappers with `sh -n`
- resolve `/opt/.../current`
- read installed IDE metadata files directly

## What not to overlearn
- Headless GUI launch warnings about X11/GPU were environment-specific and not install-failure proof.
- The temporary archive-inspection directories are not part of the reusable pattern.
