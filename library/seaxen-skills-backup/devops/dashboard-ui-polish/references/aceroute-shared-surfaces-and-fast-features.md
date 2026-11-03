# AceRoute dashboard polish + feature pattern

Use for dense operator dashboards where the user wants both speed and polish.

## Shared-surface rule
- Fix shared CSS/layout first when multiple pages feel too loose, dim, or inconsistent.
- Start tighter than a normal dashboard pass: compact bars, denser tables, smaller chart heights, brighter primary text.
- Prefer cross-page classes and shared components over page-local widget tweaks.

## User-specific layout bias captured here
- If a dashboard still feels 'big', tighten again.
- Favor bright text over subtle gray.
- Reduce empty space before adding decoration.
- Make stat cards, result chips, table headers, and stack rows visually consistent across pages.

## Feature-addition rule
Add high-signal operator blocks inside existing pages before creating new tabs.
Good examples from this session:
- Home: operator watchlist
- Ops: handoff/compression panel
- Messages: role breakdown chart + role stats list

Why: these add usefulness without fragmenting navigation.

## Fast feature pattern
Prefer features that reuse existing cached payloads.
Avoid introducing a new expensive endpoint when the page already has enough data to derive a compact watchlist, status strip, or drill card.

## Performance patterns that paired well with polish
- Warm heavy all-time dashboards at startup.
- Use short client caches for revisits.
- Cancel in-flight fetches on page switch.
- Downsample timelines for charts.
- Keep first table load lighter than full export size.
- Refresh the current active page only; do not churn every page in the background.

## Verification pattern when browser automation is flaky
If browser tooling crashes on the host, verify with:
- served HTML contains the new IDs / cache-busted asset version
- live API payload includes the fields the new block needs
- syntax/compile checks pass

Do not record 'browser is broken' as a lasting rule. Record the fallback verification pattern instead.
