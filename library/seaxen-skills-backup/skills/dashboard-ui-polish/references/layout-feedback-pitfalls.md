# Layout feedback pitfalls

Session lessons for screenshot-driven dashboard polish.

## Exact placement beats nearby placement
- If the user says tabs/page names belong in a toolbar or system-control bar, move them into that bar.
- Leaving the same controls as a second row underneath is not 'basically done' — it is still wrong.

## Scroll complaints usually need structure changes
- When the complaint is wasted space, too much scroll, or bad first-screen composition, do not only reduce padding/font size.
- Rebalance the card stack across columns.
- Move medium-height cards to fill dead space under shorter cards.
- Merge related controls into one surface when the user wants a tighter control area.

## Verify spatial composition, not just presence
- The fact that all cards exist is not enough.
- Check whether the first screen is balanced and whether one column is visibly emptier/heavier than the other.
- Treat screenshot complaints about gaps as layout bugs, not cosmetic opinions.

## Compact status chips
- For dense toolbars, shorten state chips aggressively.
- Prefer compact labels like `net`, `svc`, `auth on/off` and icon+state for Telegram/Discord when horizontal space is tight.

## User preference reinforced
- For this user, dashboard fixes are only done when the live visible arrangement matches the requested screenshot-driven placement and density.
