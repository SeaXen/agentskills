# Settings toolbar density and auth-card parity

Use for dense dashboard/settings cleanup where the user is reacting to visual clutter rather than missing functionality.

## Durable lessons from this session

### 1) Destructive or risky controls do not belong in the top toolbar
If the user says restore/reset controls are easy to hit accidentally:
- remove per-tab restore icons from the top toolbar
- move restore/reset/export/import/restart controls into a safer page section such as `Access -> Settings tools`
- keep the top toolbar focused on navigation + primary save/apply only

### 2) One-line desktop toolbar means *structurally one row*
If the user says the toolbar is still two lines, do not merely make it look tighter.
- flatten the desktop layout to a single grid row
- do not keep separate top/bottom flex rows hidden behind visual styling
- reserve stacked fallback only for narrower breakpoints/mobile

### 3) Settings tools placement
When the user asks to move Settings tools to the right side in Access:
- left column should keep access/public-surface info
- right column should carry runtime and settings tools
- this balances informational cards on the left and operational cards on the right

### 4) Auth cards should visually match the rest of the dashboard
If auth cards look "different" or "premium" in a bad way:
- remove special auth-only card chrome unless explicitly requested
- use the same standard card container, spacing, border, and background as the rest of the settings/dashboard theme
- auth can still have different content structure, but not a visibly separate design language

### 5) Status-chip pruning
Users may explicitly dislike noisy chips like:
- `ready`
- `clean`
- `1 LAN · 1 TS · CF on`

If so:
- remove them from the top toolbar first
- if still useful, relocate them into a lower-risk tools card instead of deleting the functionality

### 6) Reload affordance
When the toolbar is crowded:
- make reload icon-only if the meaning remains obvious
- keep text labels for the primary save actions, not for utility actions

### 7) Verification pattern when screenshot analysis is flaky
If vision/image analysis fails, do not stop.
Use live DOM/browser verification instead:
- inspect toolbar structure (`grid` vs stacked rows)
- inspect actual active columns/cards by heading text
- inspect class parity (`settings-card` etc.)
- verify button relocation by querying elements in the new panel

This is especially important for UI-polish work where visual backend issues should not block structural verification.
