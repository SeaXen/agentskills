# AceRoute layout density and span pitfalls

Concrete lessons from a multi-pass dashboard polish session where the user repeatedly said the new pages were a "disaster": cards were different sizes, arrangement looked random, and there was too much empty space.

## Trigger phrases to take literally
- "some card are big some are small"
- "arrange not good"
- "so many empty space"
- "check all page"
- "all pages are disaster"

These are signals to stop doing local widget tweaks and audit the shared layout system.

## What actually caused the regressions
1. **Missing shared row/grid CSS for new pages**
   - New summary bars (`#homeSummary`, `#costsSummary`, etc.) existed in markup but had no grid rules, so cards stacked as giant full-width blocks.
2. **Missing shared list-row styling**
   - Reused markup like `.stack-row` had no CSS, so lists looked jammed and visually broken.
3. **Mixed layout systems on the same page**
   - Combining `sessions-charts-grid`, `two-col-grid`, one-off wide cards, and page-specific span hacks created inconsistent card widths and dead zones.
4. **Stretching short content to match tall charts**
   - Grid rows stretched small cards to the tallest neighbor, producing giant empty cards.
5. **Over-decoration amplified the broken layout**
   - Gradient podium cards, uppercase headings, hover lift, and underline bars made asymmetry feel worse instead of better.
6. **Filter/control rows forced onto one line**
   - On dense pages like Models and Requests, toolbar actions and chips needed wrapping; forcing them into one line made the page look crowded and uneven.

## Reliable fix pattern
### 1) Audit shared CSS first
Before changing markup, inspect whether new pages were added to the same selector groups as older pages:
- compact top bars
- stat-row grids
- chip rows
- mobile overflow rules
- list-row styles

### 2) Normalize the card system
For this user's dashboards:
- smaller padding beats roomy padding
- heading decoration should be minimal
- remove hover lift when the page already has many cards
- avoid gradient-heavy podium/banner cards unless the layout is already stable

### 3) Use explicit dense page grids
Good default starting point:
- overview / command center: 4-column desktop grid
- dense analytics pages: 3-column desktop grid
- full-width spans only for genuinely wide charts/tables
- avoid random one-off span classes without a documented reason

### 4) Separate chart cards from list cards intentionally
Do not let short list cards stretch just because a chart in the same row is tall.
Use `align-items:start` and explicit spans instead of relying on auto-stretch.

### 5) Treat user frustration as a system-level failure
If the user says the page still looks wrong after a prior pass, assume the previous fix was too local.
Do a full page-by-page sweep and look for repeated selector omissions.

## Concrete structural fixes that worked
- Extend compact `.sessions-bar-*` selectors to **all** new pages, not just Sessions/Requests/Messages/Models.
- Add real grid rules for new summary bars (`#homeSummary`, `#costsSummary`, `#providersSummary`, `#channelsSummary`, `#opsSummary`).
- Add `.model-insights-row` grid behavior so insight chips do not become full-width blocks.
- Add `.stack-row` styling for balanced left/right list rows.
- Add `align-items:start` to shared chart grids.
- Replace over-broad span hacks with page-level grids such as `.home-grid`, `.costs-grid`, `.requests-grid`.
- Let toolbar chip rows wrap on dense pages like Models and Requests.
- Flatten card decoration after layout is stable.

## Verification standard
For screenshot-driven dashboard polish, do not stop at one page looking better.
Check all affected page classes:
- Home
- Costs
- Providers
- Channels
- Ops
- Requests
- Messages
- Models
- Sessions

If the user said "check all page", a one-page fix is not complete.
