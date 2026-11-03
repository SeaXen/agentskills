# SeaDash alert UX patterns

Session-learned pattern for operator-facing dashboard clarity.

## When to use
- User says the dashboard text is repetitive, noisy, or hard to scan.
- Monitoring surfaces show repeated issues like `Public endpoint down · Sensitive app exposed ...`.
- Dead public apps are easy to miss in the public exposure sections.

## Concrete UI moves
- Add a `Rescan Apps` quick action beside refresh when the operator wants a direct re-check of app status.
- Summarize duplicate alerts in banner/modal using grouped counts:
  - `Public endpoint down ×3`
  - `Sensitive app exposed ×4`
- Keep alert detail messages in the modal, but group them by title first.
- Add short issue badges on cards and mini-cards:
  - `OFFLINE` for stopped/exited/dead apps
  - `PUBLIC DOWN` for failing public probes on apps with a public URL
  - `EXPOSED` for sensitive/admin apps reachable publicly

## Important distinction
Do not collapse exposure and issue state into one label.

Use both layers together:
- exposure: `PUBLIC`, `LOCAL`, `ZERO TRUST`, `SENSITIVE`
- issue state: `OFFLINE`, `PUBLIC DOWN`, `EXPOSED`

This preserves both topology and urgency.

## Verification
- Banner text should show grouped summaries, not repeated raw titles.
- Public cards for dead apps (for example N8N, Dashdot) should visibly show `OFFLINE` and, if applicable, `PUBLIC DOWN`.
- The same issue badges should appear in both main app cards and public-route mini-cards.
