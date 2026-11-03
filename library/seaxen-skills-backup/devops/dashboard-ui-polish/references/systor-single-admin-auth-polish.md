# Systor single-admin auth polish and hardening

Use this when adding or refining optional username/password login on a lightweight self-hosted dashboard.

## Product shape that fit this user best
- One dashboard, one admin user.
- Optional, disabled by default.
- Enable/disable from Settings.
- Public/tunnel read-only dashboard rules stay separate from private admin auth.
- Avoid multi-user signup, reset flows, or OAuth unless explicitly requested.

## Good default behavior
- `auth.enabled: false` by default.
- `auth.mode: admin_only | full_app`.
- `auth.username` + hashed `auth.password_hash` only.
- Signed session cookie.
- Header should show a small visible `auth on` badge when enabled.
- Settings should show a visible auth status chip too.

## Settings UX requirements
Do not make password handling implicit only through placeholder text.

Preferred Security card fields:
- enable login protection
- protect mode
- username
- password status (`saved password set` / `no saved password`)
- new password
- confirm new password
- explicit `clear saved password` checkbox

This user specifically rejected a version that had no explicit delete/change-password option.

## Login-page UX
For this user, a raw form is not enough once auth exists.
- make the login card compact and visually cleaner
- keep the page narrow and dense
- add a small auth-enabled kicker/badge
- keep copy short
- keep only the essential actions: Login / Back

## Brute-force protection
Minimum acceptable first pass:
- in-memory per-IP failed-login counter
- temporary cooldown after repeated failures
- return `429` while blocked
- show a concrete wait message like `Try again in 57s`

This is enough for a simple single-admin setup and much better than no guard.

## Verification pattern
Before claiming auth works:
1. add tests for defaults, redirect, successful login, and public-read-only preservation
2. run tests and get green
3. deploy to the live install with auth still OFF by default
4. verify the live Settings page exposes the Security controls
5. spin up a separate temporary auth-enabled instance on another port using a temp config file
6. browser-verify redirect to `/login`, successful login, logout, and cooldown behavior
7. kill the temporary test instance afterward so it does not linger

## Pitfalls
- Do not claim a placeholder like `leave blank to keep password` is enough. Add explicit change/clear controls.
- Do not let enabling auth without a password succeed.
- Do not expose the saved password hash or session secret in `/api/config`.
- Do not test auth only on the live production service if auth is still disabled there; use a temporary auth-enabled side instance for browser verification.
- If the temporary auth test instance uses a copied hash string, verify the hash/password pair is valid before trusting a failed login attempt as an app bug.
- Background-process `SIGTERM` notifications from the temporary auth instance are expected if you intentionally kill it after testing; do not confuse them with failure of the real live service.
