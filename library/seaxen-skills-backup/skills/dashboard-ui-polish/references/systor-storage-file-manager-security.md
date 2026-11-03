# Systor Storage/File Manager security pattern

Use when adding file-manager or disk-analysis features to Systor-style public/LAN dashboards.

## Core product split

Do not expose a full destructive file manager directly on a public Cloudflare Tunnel surface.

Preferred shape:
- Default safe split: Public/tunnel may get read-only Storage/Disk Analysis only, while Local/LAN/Tailscale/private IP may get file actions.
- If the user is worried that public visitors can even see Storage settings or toggles, make Storage fully LAN/Tailscale/local-only instead: hide the Storage nav tab from public/tunnel pages, return 404 for `/storage`, and return 403 JSON for `/api/storage/*` on Cloudflare/public requests.
- Password/page lock can be added later, but it is an extra lock, not the primary safety model.

## Safe first implementation

Add one `Storage` page with tabs:
1. Overview — mount usage, free space, current folder size, largest items, file-type usage.
2. Disk Analysis — largest folders/files, old large files, type usage.
3. File Manager — browse and actions, but only on local/LAN/Tailscale.
4. Settings — allowed roots, read-only public toggle, trash toggle, scan limits.
5. Operations Log — audit file actions.

## Mandatory backend guards

- Use an allowlist of roots, defaulting to a data path such as `/mnt/tb`; never allow `/`.
- Resolve paths with `Path.resolve()` and verify the resolved target stays under an allowed root.
- Block system/secret paths even if a user tries to add them: `/etc`, `/boot`, `/usr`, `/proc`, `/sys`, `/dev`, `/run`, `/var/lib/docker`, `/root/.hermes`, SSH dirs, env/token/auth files.
- Treat requests carrying Cloudflare headers such as `CF-Connecting-IP` / `Cf-Ray` as public, even if `remote_addr` is localhost from `cloudflared`.
- Allow actions only when the client is loopback, RFC1918 LAN, or Tailscale/CGNAT range (`100.64.0.0/10`), and no Cloudflare header is present.
- Delete should move to a per-root trash folder first, not permanent delete.
- Log every action with timestamp, action, path, success/error.
- Avoid following symlinks while scanning; do not let symlinks escape the root.

## Performance rules

- Do not auto-run deep disk analysis on page/tab open for large roots like `/mnt/tb`.
- Make analysis a manual `Analyze` action.
- Default analysis must be **quick/shallow**: top-level entries and capped summaries only. Deep recursive scans must be an explicit separate mode/action, never the default button path.
- For virtual root/SSD views (`/`), never call recursive folder-size helpers for root children. Render root as a shallow, read-only selector/list; root browse and root analysis should return in milliseconds, not minutes.
- Add max-scan limits and keep folder-size estimates capped for dashboard responsiveness.
- Overview can compute shallow/current-folder data, but long recursive scans must be explicit.

## UI rules learned from Systor Storage

- If the user asks for SSD/root selection, do not show only passive mount stats. Provide explicit root-selection controls near `Up` / `Refresh` / `Open`, preferably compact buttons/chips such as `Data /mnt/tb` and `Root / SSD`, not a cramped dropdown.
- Keep `/` as a shallow read-only root/SSD view. Do not allow file actions at `/`, and do not recursively size root folders.
- Root/system-ish folders should show unknown size as `—`, not `0 B`. `0 B` reads as broken/misleading; use real sizes only under managed roots where the capped folder-size helper is safe.
- If Storage is LAN-only, copy should say so plainly (`LAN/Tailscale only · public hidden`) rather than implying public read-only remains available.
- If a no-right-click option is exposed, apply it immediately on checkbox change and after settings load; verify with a real `contextmenu` event (`dispatchEvent` should return false). Still describe it as a deterrent, not security.
- A file manager needs a real custom right-click/context menu, not just a right-click blocker. Minimum row context actions: `Open`, `Download`, `Copy`, `Move`, `Rename`, `Trash`. Verify by dispatching a `contextmenu` event on an actual row and checking that the menu becomes visible.
- Hide sensitive Settings tabs/options from public surfaces by hiding the entire Storage page from public when requested; do not leave toggles visible where a public user can see or attempt to change them.

## Expected File Manager affordances

For this user, do not stop at browse/copy/move/delete if the ask was a “10/10” file page. Add the expected operator affordances early:

- Quick navigation buttons: `Up`, `/mnt/tb`, `/root`.
  - On desktop, right-align these quick nav buttons in the File Manager header.
  - On mobile, let them become a compact grid.
- Upload:
  - LAN/Tailscale/local only.
  - Use multipart upload to the current managed directory.
  - Auto-rename on conflict instead of overwriting silently.
  - Log uploads in the operation log.
- Download:
  - LAN/Tailscale/local only.
  - File download via `send_file(..., as_attachment=True)`.
  - Folder download as a temporary zip with a hard cap (for example 5000 files) and cleanup via `after_this_request`.
- Visual scan cues:
  - Use colored file-type badges and colored action buttons.
  - Good defaults: folder = cyan, video = orange, image = green, doc/text/pdf = blue, archive = purple, upload = cyan, download = green, new folder = purple, trash = red.

## Backend implementation notes

- For browsing, separate **browse resolution** from **action resolution**. Browsing can safely allow shallow LAN-only views of `/`, `/mnt`, `/root` with deny-prefix filtering; actions must remain restricted to configured allowlisted roots.
- For `/root` browse, block known secret subpaths and secret-like filenames. Do not permit writes unless `/root` is explicitly allowlisted and you are certain that is desired.
- Downloading folders should skip symlinks, trash folders, and secret-like files. Keep a max-file cap so a browser click cannot zip the whole disk for minutes.
- When adding upload/download, update both toolbar buttons and the context menu; users expect right-click download too.

## 10/10 Storage/File Manager finishers

When the user asks to make Storage/File Manager “10/10”, add these after the basic safe implementation:

- Breadcrumb chips for the current path, each chip opening that path.
- Client-side search/filter over name/path/type, with no backend scan.
- Page-size selector and Prev/Next pagination for large folders.
- Preview pane:
  - text/code/markdown/json/log files via capped text read;
  - image files via safe local download/preview URL;
  - binary/large files should say “use Download”.
- Background deep scan:
  - POST starts a daemon thread;
  - GET polls state;
  - never auto-run on tab open;
  - cap by `max_scan_files`.
- Checksum-confirmed duplicate finder:
  - manual only;
  - first group by file size;
  - hash only size-colliding candidates;
  - cap file count to prevent runaway IO.
- Action password hardening:
  - Store only a password hash; never return the hash from `/api/storage/settings`.
  - Password should be optional/configurable; if enabled but no password is set, block major actions and tell user to set one.
  - Major actions requiring password: upload, chunk upload, download, copy, move/cut, rename, trash/delete, restore, deep scan, checksum duplicate scan, ops export, ops clear.
  - For browser downloads, pass password via query or header only because `send_file` is GET-based; this is acceptable only because Storage remains LAN/Tailscale-only.
- Trash/restore:
  - Add `/api/storage/trash` and restore UI in Ops tab.
  - Restore should validate that source is inside a configured root’s `.systor-trash` and auto-rename on conflict.
- Operation log maintenance:
  - Add export and clear controls; protect both with action password when enabled.
- Auto drives:
  - Fresh installs should not be hardcoded to one user’s `/mnt/tb`; auto-detect real mountpoints with `findmnt`, while keeping `/mnt/tb` if present and avoiding plain directories like `/media` unless actually mounted.
  - Still append `/root` for this user profile, but keep public blocked and secret deny-prefixes active.
- Large upload:
  - Add chunked upload endpoint with offset checks for large files; use temp `.systor-upload-tmp` under destination and finalize only when total bytes are written.
- Verify with browser DOM: breadcrumbs visible, search/pagination controls present, preview opens a known text file, action password settings exist, trash/restore and ops export/clear controls exist, analysis buttons include Quick/Deep/Checksum, and public Cloudflare still returns 404/403.

## Verification checklist

- `/storage` returns 200 on localhost/LAN.
- `/api/storage/settings` returns roots, config, and can-write mode.
- `/api/storage/browse?path=<allowed-root>` returns entries.
- Path escape/system path probe such as `/etc` returns 403.
- Simulated Cloudflare request with `CF-Connecting-IP` blocks POST actions with 403.
- Local smoke action creates a temporary folder, then trash-deletes it; original path disappears and `.systor-trash` receives it.
- Browser check shows no JS errors, Storage nav is active, and Disk Analysis does not run automatically before the user clicks Analyze.

## User preference signal

For Dr. Sagar dashboards, choose this split over a password-only public file manager. Page/action password is useful later, but public read-only + private actions is the safer default.