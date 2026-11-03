# Smarter dashboard signals

Use when a dense operator dashboard already has several page-level insight rails and the user asks to make it "smarter".

## Rule
Do not keep adding passive chips to every page.

When multiple tabs already summarize local state, add one cross-dashboard intelligence surface instead:
- Signals / Alerts page
- compact Home attention board

## Why
This reduces operator scan cost.
The user should not have to mentally combine eight tabs to answer:
- what is rising
- what is cooling
- what is worsening
- what needs attention now

## Preferred pattern
1. Keep page-local rails for page-specific drilldowns.
2. Add a dedicated Signals page that consolidates:
   - rising
   - cooling
   - worsening
   - attention now
3. Make every signal row clickable and route to the relevant page/drawer.
4. Add a compact Home attention board with only the few highest-signal issues.

## What counts as "smart"
Build the signal layer from real app data already present:
- recent-vs-prior window comparisons
- concentration/share thresholds
- severity counts
- spike deltas
- dominant model/source/role detection

Avoid:
- fake AI scores
- decorative labels with no drill path
- duplicating the same summary chips on every tab

## Good examples
- Cost pressure from cost delta > threshold
- Ops attention from active high-severity/recent issue counts
- Model concentration from top-model share of tokens/cost
- Tool spike from tool-call delta vs prior window
- Session surge from recent sessions vs prior sessions

## Home behavior
Home should show only the urgent shortlist, for example:
- ops signals active
- cost pressure
- session surge
- model concentration

If there is no urgent issue, show a clear calm state instead of filler.