# Case Study: Tinybird Design Token Extraction

Real-world example of extracting design tokens from tinybird.co when user provided both a DESIGN.md spec and a reference HTML file.

## Three sources of truth (ranked by reliability)

1. **User's reference HTML file** (most reliable) - has exact Tailwind classes and inline colors
2. **Live site getComputedStyle()** - actual rendered values from browser
3. **DESIGN.md spec** (least reliable) - often outdated or aspirational

## What the DESIGN.md said (wrong)

```
bg: #1A1A2E (indigo - WRONG)
accent: #27C486 (muted green - WRONG)
card: #292942 (purple-gray - WRONG)
font: Inter (partially right)
radius: 8px (WRONG - actual is 4px or less)
```

## What the live site actually used

```
body bg: rgb(10,10,10) = #0a0a0a (near-black)
--primary: #27f795 (neon green)
font: Roboto (not Inter)
h1: 64px, weight 400
```

## What the reference HTML had (correct)

```
body bg: #000000 (pure black)
green accent: #00E67A
card surface: #111113
card borders: #27272A
body font: Inter
heading font: Space Grotesk
badges: rounded-full (pill)
cards: rounded-3xl (24px)
buttons: rounded-lg (10px)
```

## Final correct tokens

| Token | Spec | Live | Reference HTML | Final |
|-------|------|------|----------------|-------|
| BG | #1A1A2E | #0a0a0a | #000000 | #000000 |
| Card | #292942 | #151515 | #111113 | #111113 |
| Border | #40405C | #262626 | #27272A | #27272A |
| Green | #27C486 | #27f795 | #00E67A | #00E67A |
| Font | Inter | Roboto | Inter+SpaceGrotesk | Inter+SpaceGrotesk |
| Radius | 8px | 4px | mixed | 16-20px cards, 9999px pills, 10px buttons |

## Lesson

When user provides a reference HTML file, extract from THAT first. The HTML is the design they want. Spec docs and live sites are supplementary. All three disagreed - the reference HTML won.
