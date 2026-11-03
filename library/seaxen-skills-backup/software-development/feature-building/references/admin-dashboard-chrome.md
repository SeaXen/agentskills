# Admin Dashboard Chrome Matching Checklist

Use this when a user wants an app to look like a provided admin dashboard reference.

## Source-of-truth order
1. User-provided HTML/CSS mockup or extracted page source
2. User screenshots
3. Live reference site
4. Existing app theme system

Do not improvise a "close enough" palette before checking the reference tokens.

## What to extract from the reference
- body background color/layering
- top header background
- sidebar background
- panel/card background
- border color
- primary / secondary / faint text colors
- accent colors and where they are actually used
- radius style (sharp / soft / pill)
- whether the layout relies on:
  - top search bar
  - ticker strip
  - left utility rail
  - nested expandable sidebar groups
  - widget/card action chrome

## Common failure mode
User says "theme not matching" but the real gap is structural chrome, not just colors.

Typical missing pieces:
- sidebar too wide or too plain
- no collapse/expand affordance
- no search bar
- no ticker strip
- no utility icon rail
- groups are flat instead of expandable
- shell/background layers still use the old theme even after card colors changed

## Implementation pattern that worked
- Keep theme work additive (`data-theme` / CSS vars).
- Create shared chrome components instead of page-local hacks:
  - `TopSearchBar`
  - `TickerStrip`
  - `UtilityRail`
  - `SidebarNav` with expandable groups
- Default sidebar mode when the user explicitly prefers the reference admin layout.
- Make collapse state persistent in settings.

## Live verification checklist
Do not stop at code review or a build.

Verify in the live app that:
- search input exists and returns dropdown results
- utility rail renders the expected quick links
- ticker strip shows live symbols/prices in DOM
- expandable nav groups open and close
- expanded vs collapsed sidebar widths actually change
- computed body/sidebar/card colors match the intended reference family

## Concrete values from the TradingX admin pass
Reference HTML used these core tokens:
- body bg: `#0C1B32`
- nav/ticker bg: `#0A1628`
- panel bg: `#1D2F43`
- border: `#2A3F5A`
- primary text: `#E2E8F0`
- secondary text: `#94A3B8`

Those values produced a closer match than the earlier freehand dark-blue theme.
