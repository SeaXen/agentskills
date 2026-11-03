# AceRoute compact bright operator pass

Use when polishing dense self-hosted operator dashboards for Dr. Sagar.

## Visual defaults

Start at the compact/bright end immediately:
- tighten card padding first
- make KPI values bright white and dominant
- make labels quieter, smaller, and non-shouty
- prefer shared surface changes over per-widget tweaks

## What to audit globally before page-level tweaks

1. shared `.card` surface
2. shared KPI / stat cards
3. shared stack rows / list rows
4. shared page header bars
5. shared table density / row height

If multiple tabs feel "big", "empty", or inconsistent, the problem is usually in the shared surface layer, not in one page.

## Specific polish lessons from this session

- KPI cards can still feel too tall even after numeric size reduction if labels stay uppercase, too dim, or too visually noisy.
- Shared stack/list rows benefit from a single pass: tighter padding, brighter primary text, slightly stronger borders, and a restrained hover shadow.
- For this user, premium means compact, bright, and deliberate — not glossy, oversized, or decorative.
- When the user asks for more polish after a performance pass, do not only style the new settings panel; audit the full dashboard system.

## Pair with performance work

When a dashboard is both slow and visually loose, fix both together:
- downsample long timelines
- reduce first table loads
- cache repeat opens
- then tighten shared CSS surfaces so the faster UI also feels sharper
