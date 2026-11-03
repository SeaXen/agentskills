# Rexterm header settings dropdown + vendored tmux runtime

Use with `dashboard-ui-operations` for standalone browser-terminal apps built as a single-file/monolithic UI plus Python backend.

## What changed cleanly
- Existing-user account management moved into an in-app **Settings** dropdown in the terminal header.
- Header controls became **icon-only Settings + Logout** on the far right.
- Username and password changes were split into separate actions.
- Username edit was simplified further to a **single-line row**: `new username` + `Save`.
- Password change still requires `current password`.

## Durable UX rule
For terminal-page auth controls:
- keep the login page for login / first-account creation
- put normal account management in a dropdown on the terminal page
- keep username change low-friction and visually compact
- keep password change more explicit and security-checked
- after any header polish request, live-verify the whole terminal still boots

## Failure pattern seen here
A header/auth tweak can appear visually correct while the terminal is still broken for a different reason.

Observed pattern:
1. Header/settings controls rendered.
2. Browser still showed terminal request failure / blank session area.
3. Root cause was not the new dropdown; terminal creation depended on vendored `tmux` runtime resolution.

## Better backend pattern
If the app ships a vendored runtime binary (like `vendor-rootfs-tmux/usr/bin/tmux`), do not rely on manual launcher env forever.

Make the backend itself:
- resolve the bundled binary path automatically
- inject any required library path (for example `LD_LIBRARY_PATH`) when running that binary
- use the same runtime env for both one-shot checks and long-lived attach/spawn paths

That avoids a fragile situation where the app only works when started with a special shell wrapper.

## Verification shape that caught the real state
Do all of these after auth/header changes:
1. login in a real browser
2. confirm terminal page loads
3. create or attach a real terminal session
4. open Settings dropdown
5. verify username row layout visually
6. test username change success
7. test wrong current password on password change and confirm inline error
8. confirm logout still returns to login page

## Concrete live-verification outcomes from this session
- Username changed `sagar -> sagar2` successfully, then back to `sagar`.
- Wrong current password for password change showed inline `Current password is incorrect` instead of throwing the user back to login.
- Terminal prompt rendered live after backend runtime fix.

## Pitfall
Do not stop once the header icons appear. In standalone terminal apps, a polished auth dropdown can coexist with a broken terminal spawn path. Always verify both UI affordance and actual session creation.
