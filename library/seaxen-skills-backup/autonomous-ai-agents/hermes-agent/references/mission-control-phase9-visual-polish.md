# Mission Control Phase 9 — Visual Polish When the User Says It Looks Ugly or Haphazard

Use this after the operator-console redesign exists but the user still reacts negatively to the visual result with feedback like:
- "too ugly"
- "haphazard"
- "messy"
- "not premium"
- "looks bad"

## Core lesson
The failure mode is usually not information architecture anymore. It is **visual discipline**:
- inconsistent density
- noisy borders/glows
- weak typography hierarchy
- low-contrast helper text
- cramped multi-column control areas
- background texture competing with content

Do not respond by adding more features. Do a **CSS-first polish pass**.

## Default polish moves

### 1) Normalize the shell first
Prefer a Linear/Vercel-style dark premium surface:
- restrained dark panels
- soft border opacity
- subtle radius consistency
- one accent family, not many neon accents
- reduce decorative texture visibility behind content

### 2) Tighten hierarchy
- stronger main heading
- cleaner small uppercase labels
- brighter but still restrained secondary text
- session titles and section titles should be visibly more important than metadata

### 3) Fix the action dock
If the right rail feels cramped, stack controls vertically instead of making many tiny columns.
This is a common cause of the "haphazard" look.

### 4) Improve readability
- raise contrast on helper text and KPI detail lines
- use a reliable sans + mono stack
- keep transcript/meta text readable at small sizes

### 5) Reduce visual competition
- hero/header should not dominate an operational page
- background art/texture must sit behind an overlay if it competes with cards
- keep stat cards consistent and quiet

### 6) Rebalance the 3-column body
A reliable premium operator-console ratio is roughly:
- left queue: compact but readable
- center context: widest
- right controls: narrower but not cramped

If the center is too wide and the right rail too narrow, the page feels awkward even when the CSS is otherwise good.

## Good concrete CSS interventions
- add a dark pseudo-element overlay behind the plugin shell
- unify card radius and border/shadow treatment across hero, stats, rows, detail, and controls
- convert the controls grid to a single-column stack when density becomes visually noisy
- strengthen muted text from dim gray to readable cool gray
- reduce exaggerated glow/neon treatments
- standardize button radius and weight
- add subtle divider lines inside session cards instead of many separate buttons floating visually

## Verification pattern
After the polish pass:
1. run the Mission Control plugin/dashboard tests
2. hard refresh the browser route
3. visually check that the page now feels:
   - organized
   - compact
   - premium
   - less haphazard
4. note remaining weak points honestly (hero too tall, KPI cards too generic, sidebar less premium, etc.)

## Anti-patterns
- Do not add new sections when the complaint is aesthetics.
- Do not lean harder into cyberpunk styling if the user asked for premium/organized.
- Do not keep a dense multi-column control rail if it is already visually collapsing.
- Do not leave low-contrast metadata just because it looks stylish in CSS.

## When to apply
Apply this as the first follow-up move when the user explicitly dislikes the look after a prior dashboard redesign. This is not a new feature phase; it is a **presentation correction phase**.
