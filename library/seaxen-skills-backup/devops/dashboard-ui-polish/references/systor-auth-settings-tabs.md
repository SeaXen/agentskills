# Systor auth/settings tabs and verification

Use this when a dense Systor-style Settings page has become a long mixed wall and auth/security is no longer just a small toggle.

## Information architecture
Preferred 4-tab split:
- `Alerts` — threshold presets + threshold table
- `Notifications` — Telegram, Discord, notification history
- `Auth` — single-admin login protection and all related controls
- `Access` — access URLs, runtime, service controls, dashboard/network/apps/speed defaults

Reason: once auth and notification sections grow, visual compression alone stops helping. Group by operator task instead of by storage location in the config file.

## Auth tab field set
For single-admin Systor auth, expose the whole operator model directly:
- enable login protection
- protect mode (`admin_only` / `full_app`)
- username
- password status
- new password
- confirm new password
- clear saved password
- idle auto-logout minutes (`0 = off`)
- fail limit
- cooldown seconds

Do not rely on helper text alone for password state. Show a visible chip like `saved password set` / `no saved password`.

## Backend security model
Good lightweight default for this dashboard class:
- login throttling tracked by **IP** and by **username**
- cooldown enforced on repeated failures
- session idle timeout optional and disabled by default
- logout path clears auth/session/timestamp keys together
- public dashboard rules remain separate from private login rules

## Verification pattern
Safest verification path:
1. Keep the real live dashboard config untouched.
2. Launch a temporary second local instance on another port (for example `6688`) with auth enabled.
3. Verify:
   - `/settings` redirects to `/login`
   - valid login opens protected pages
   - repeated bad logins hit `429`
   - username lock still works when IP changes
   - idle timeout redirects back to `/login`
4. Kill the temporary instance after verification.

Important: a `SIGTERM` / `process.kill` on that temporary second instance is expected cleanup, not evidence of a product crash.

## UI verification checks
- Tab row exists and only one tab is active at a time.
- Switching to `Auth` hides Notifications controls.
- Switching to `Access` hides Auth controls but shows access/runtime blocks.
- Browser console remains at zero JS errors after tab switching.
- Save state / test buttons still work after the tab refactor.
