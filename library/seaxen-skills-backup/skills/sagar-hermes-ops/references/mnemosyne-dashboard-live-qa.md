# Mnemosyne dashboard live QA notes

Use this when validating a standalone/community Mnemosyne dashboard against a live Hermes + Mnemosyne setup.

## What to verify first
- Confirm Hermes is actually using Mnemosyne as the active memory provider.
- Confirm the live SQLite DB path the dashboard should read.
- Confirm whether the dashboard is bound to `127.0.0.1` or `0.0.0.0` before judging LAN reachability.
- Verify the real listening socket/process, not just config files.

## Standalone-vs-built-in distinction
- Keep the Hermes dashboard memory route and the standalone Mnemosyne dashboard conceptually separate.
- The standalone dashboard can be healthy even if the built-in `/memory` route has different scope or weaker Mnemosyne-specific views.
- Do not describe the standalone dashboard as a replacement unless the user explicitly wants that.

## Graph diagnosis
If the Knowledge Graph tab looks empty:
1. Check live dashboard diagnostics for the `triples` count.
2. Run a real triple query against Mnemosyne.
3. If triples are `0`, explain that the graph view is empty because there is no triple data, not because the renderer necessarily failed.
4. Distinguish this from other visual surfaces like Visualiser that may still render non-triple memory structures.

## Useful smoke-test order
1. Overview / landing page
2. Visualiser
3. Knowledge Graph
4. Memories browser
5. Settings / diagnostics
6. Review queue
7. History

## Known high-value failure pattern
- A page can falsely show `Password required` even when auth status reports `auth_enabled: false`, `has_password: false`, and `authenticated: true`.
- Treat this as a UI/API inconsistency worth debugging, not as proof that the user configured auth incorrectly.
- Check whether the page is hitting missing endpoints / 404s before blaming authentication.

## Reporting shape
For this class of task, report in three buckets:
- What works
- What is data-empty but not broken
- What is genuinely broken or inconsistent

This avoids calling an empty graph a bug when the real issue is lack of triples, while still surfacing actual defects like route/auth mismatches.